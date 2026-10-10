#!/usr/bin/env python3
"""Render self-hosted GitHub profile SVGs using the GitHub APIs (stdlib only)."""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

USER = os.environ.get('PROFILE_USERNAME', 'tjallemann01')
TOKEN = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN', '')
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)

BG = '#0d1117'; PANEL = '#161b22'; TEXT = '#e6edf3'; MUTED = '#8b949e'; ACCENT = '#58a6ff'; TEAL = '#2dd4bf'; LINE = '#30363d'


def api(url: str, payload: dict | None = None):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'GitHub-profile-dashboard'}
    if TOKEN:
        headers['Authorization'] = f'Bearer {TOKEN}'
    if payload is not None:
        headers['Content-Type'] = 'application/json'
    request = Request(url, data=json.dumps(payload).encode() if payload is not None else None, headers=headers)
    with urlopen(request, timeout=35) as response:
        data = json.load(response)
    if isinstance(data, dict) and data.get('errors'):
        raise RuntimeError(f'GitHub API errors: {data["errors"]}')
    return data


def public_repos():
    result = []
    for page in range(1, 11):
        batch = api(f'https://api.github.com/users/{USER}/repos?type=owner&per_page=100&page={page}')
        if not isinstance(batch, list):
            raise RuntimeError(f'Unexpected repositories response: {batch}')
        result.extend(batch)
        if len(batch) < 100:
            break
    return result


def contributions():
    if not TOKEN:
        raise RuntimeError('GH_TOKEN / GITHUB_TOKEN is required for the contribution calendar.')
    query = '''query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks { contributionDays { contributionCount date } }
          }
        }
      }
    }'''
    data = api('https://api.github.com/graphql', {'query': query, 'variables': {'login': USER}})
    if not data.get('data', {}).get('user'):
        raise RuntimeError('GitHub GraphQL did not return this user.')
    return data['data']['user']['contributionsCollection']['contributionCalendar']


def svg_save(filename, body, width, height):
    full = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">'
            '<style>text{font-family:Arial,Helvetica,sans-serif} .label{font-size:15px;fill:#8b949e} .value{font-size:32px;fill:#e6edf3;font-weight:700} .small{font-size:12px;fill:#8b949e}</style>'
            + body + '</svg>')
    (ASSETS / filename).write_text(full, encoding='utf-8')


def text(x, y, string, size=14, color=TEXT, bold=False, anchor=None):
    attrs = f'font-size="{size}" fill="{color}"' + (' font-weight="700"' if bold else '') + (f' text-anchor="{anchor}"' if anchor else '')
    return f'<text x="{x}" y="{y}" {attrs}>{escape(str(string))}</text>'


def card_base(width, height):
    return f'<rect width="{width}" height="{height}" rx="16" fill="{PANEL}" stroke="{LINE}"/>'


def make_stats(repos, calendar):
    owned = [r for r in repos if not r.get('fork')]
    stars = sum(int(r.get('stargazers_count', 0)) for r in owned)
    forks = sum(int(r.get('forks_count', 0)) for r in owned)
    total = int(calendar['totalContributions'])
    w, h = 960, 208
    parts = [card_base(w,h), text(30,42,'GitHub activity · live repository data',21,ACCENT,True)]
    metrics = [('PUBLIC REPOS',len(owned)), ('TOTAL STARS',stars), ('FORKS',forks), ('CONTRIBUTIONS / YEAR',total)]
    for i, (label, value) in enumerate(metrics):
        x = 30 + i*235
        parts += [text(x,90,label,12,MUTED,True), text(x,146,f'{value:,}',33,TEAL,True)]
        if i != 3:
            parts.append(f'<path d="M{x+208} 74 V160" stroke="{LINE}"/>')
    parts.append(text(30,187,'Public repositories only · contributions as reported by GitHub · refreshed daily',11,MUTED))
    svg_save('github-stats.svg',''.join(parts),w,h)


def make_calendar(cal):
    weeks = cal['weeks'][-53:]
    days = [d for week in weeks for d in week['contributionDays']]
    max_count = max([d['contributionCount'] for d in days] or [0])
    colors = ['#161b22','#0e4429','#006d32','#26a641','#39d353']
    def color(n):
        if not n: return colors[0]
        if max_count <= 1: return colors[2]
        return colors[min(4,max(1, round(n/max_count*4)))]
    w,h = 970,260
    cell=12; gap=4; startx=42; starty=75
    parts=[card_base(w,h),text(30,39,'Contribution calendar · last 12 months',21,ACCENT,True)]
    for yi, day in enumerate(['Mon','Wed','Fri']):
        parts.append(text(8, starty+cell*(1+yi*2)+gap*(1+yi*2)+10,day,10,MUTED))
    for wi,week in enumerate(weeks):
        for d in week['contributionDays']:
            weekday=datetime.fromisoformat(d['date']).weekday()
            yday=(weekday+1)%7  # Sunday first
            x=startx+wi*(cell+gap);y=starty+yday*(cell+gap)
            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{color(d["contributionCount"])}"><title>{d["date"]}: {d["contributionCount"]} contributions</title></rect>')
    parts.append(text(42,225,f'{int(cal["totalContributions"]):,} contributions recorded by GitHub',13,TEAL,True))
    parts.append(text(42,244,'Private activity is included only if GitHub makes it visible to this workflow.',11,MUTED))
    svg_save('contributions.svg',''.join(parts),w,h)


def make_languages(repos):
    # Languages reflect each public, non-fork repository's primary language, not lines of code.
    counts = Counter(r['language'] for r in repos if not r.get('fork') and r.get('language'))
    top = counts.most_common(5)
    if not top: top=[('No data yet',0)]
    total=sum(counts.values())
    w,h=960,230
    parts=[card_base(w,h),text(30,42,'Languages · public repositories',21,ACCENT,True)]
    palette=['#58a6ff','#2dd4bf','#bc8cff','#ffa657','#f778ba']
    offset=30
    for i,(name,count) in enumerate(top):
        length=900*(count/total) if total else 0
        if length:
            parts.append(f'<rect x="{offset:.1f}" y="65" width="{length:.1f}" height="17" fill="{palette[i]}"/>')
        offset+=length
    for i,(name,count) in enumerate(top):
        col=i%3; row=i//3
        x=30+col*305;y=120+row*42
        parts.append(f'<circle cx="{x+6}" cy="{y-4}" r="6" fill="{palette[i]}"/>')
        pct=round(100*count/total) if total else 0
        parts.append(text(x+20,y,f'{name}  {pct}% ({count})',15,TEXT))
    parts.append(text(30,215,'Primary language per public repository · not a measure of expertise or code volume.',11,MUTED))
    svg_save('languages.svg',''.join(parts),w,h)


def main():
    repos = public_repos()
    calendar = contributions()
    make_stats(repos,calendar)
    make_calendar(calendar)
    make_languages(repos)
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    (ASSETS/'last-updated.txt').write_text(now+'\n', encoding='utf-8')
    print(f'Updated three SVGs for {USER}: {len(repos)} public repos, {calendar["totalContributions"]} contributions; {now}')

if __name__ == '__main__':
    main()
