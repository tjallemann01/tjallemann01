from __future__ import annotations
import os, json, html, urllib.request, urllib.parse, datetime as dt
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "live"
OUT.mkdir(parents=True, exist_ok=True)

USERNAME = os.environ.get("PROFILE_USERNAME", "tjallemann01")
TOKEN = os.environ.get("GH_TOKEN", "")

BG = "#0d1117"
BORDER = "#30363d"
TITLE = "#58a6ff"
TEXT = "#c9d1d9"
MUTED = "#8b949e"
GREEN = "#39d353"

def esc(value):
    return html.escape(str(value), quote=True)

def request_json(url, method="GET", payload=None):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "tjallemann01-profile-readme",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, headers=headers, data=data, method=method)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))

def get_repos():
    repos = []
    page = 1
    while True:
        query = urllib.parse.urlencode({
            "per_page": 100,
            "page": page,
            "sort": "updated",
            "type": "owner",
        })
        batch = request_json(f"https://api.github.com/users/{USERNAME}/repos?{query}")
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return [repo for repo in repos if not repo.get("fork")]

def contribution_days():
    now = dt.datetime.now(dt.timezone.utc)
    start = now - dt.timedelta(days=29)

    if TOKEN:
        query = '''
        query($login:String!, $from:DateTime!, $to:DateTime!) {
          user(login:$login) {
            contributionsCollection(from:$from, to:$to) {
              contributionCalendar {
                weeks {
                  contributionDays {
                    date
                    contributionCount
                  }
                }
              }
            }
          }
        }
        '''
        payload = {
            "query": query,
            "variables": {
                "login": USERNAME,
                "from": start.isoformat(),
                "to": now.isoformat(),
            },
        }
        try:
            result = request_json("https://api.github.com/graphql", method="POST", payload=payload)
            weeks = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
            data = {}
            for week in weeks:
                for day in week["contributionDays"]:
                    data[day["date"]] = int(day["contributionCount"])
            return data
        except Exception:
            pass

    data = defaultdict(int)
    try:
        events = request_json(f"https://api.github.com/users/{USERNAME}/events/public?per_page=100")
        for event in events:
            created = dt.datetime.fromisoformat(event["created_at"].replace("Z", "+00:00"))
            if created >= start:
                data[created.date().isoformat()] += 1
    except Exception:
        pass
    return dict(data)

def write_svg(name, content):
    (OUT / name).write_text(content, encoding="utf-8", newline="\n")

def make_stats(user, repos, contributions):
    stars = sum(int(repo.get("stargazers_count", 0)) for repo in repos)
    forks = sum(int(repo.get("forks_count", 0)) for repo in repos)
    total_30 = sum(contributions.values())
    updated = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="495" height="165" viewBox="0 0 495 165">
<style>
text{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif}}
.t{{font-size:18px;font-weight:700;fill:{TITLE}}}.l{{font-size:11px;fill:{MUTED};letter-spacing:.5px}}
.v{{font-size:20px;font-weight:700;fill:{TEXT}}}.s{{font-size:10px;fill:#6e7681}}
</style>
<rect width="495" height="165" rx="8" fill="{BG}"/>
<rect x=".5" y=".5" width="494" height="164" rx="8" fill="none" stroke="{BORDER}"/>
<text x="22" y="34" class="t">{esc(USERNAME)}'s GitHub Stats</text>
<text x="22" y="69" class="l">PUBLIC REPOS</text><text x="22" y="94" class="v">{user.get("public_repos", 0)}</text>
<text x="139" y="69" class="l">FOLLOWERS</text><text x="139" y="94" class="v">{user.get("followers", 0)}</text>
<text x="253" y="69" class="l">STARS</text><text x="253" y="94" class="v">{stars}</text>
<text x="337" y="69" class="l">FORKS</text><text x="337" y="94" class="v">{forks}</text>
<text x="414" y="69" class="l">30D</text><text x="414" y="94" class="v">{total_30}</text>
<text x="22" y="139" class="s">Generated locally from GitHub API · {updated}</text>
</svg>'''
    write_svg("live-github-stats.svg", svg)

def make_languages(repos):
    language_bytes = Counter()
    for repo in repos:
        try:
            values = request_json(repo["languages_url"])
            for language, size in values.items():
                language_bytes[language] += int(size)
        except Exception:
            continue

    top = language_bytes.most_common(5)
    total = sum(language_bytes.values()) or 1
    palette = ["#3572A5", "#f1e05a", "#555555", "#b07219", "#178600"]

    bars = []
    x = 22.0
    bar_width = 451.0
    if top:
        for i, (_, size) in enumerate(top):
            fraction = size / total
            width = bar_width * fraction
            bars.append(f'<rect x="{x:.1f}" y="57" width="{max(width, 2):.1f}" height="11" fill="{palette[i % len(palette)]}"/>')
            x += width

    labels = []
    positions = [(22, 99), (180, 99), (338, 99), (22, 126), (180, 126)]
    for i, (language, size) in enumerate(top):
        pct = size / total * 100
        px, py = positions[i]
        color = palette[i % len(palette)]
        labels.append(f'<circle cx="{px+5}" cy="{py-4}" r="5" fill="{color}"/>')
        labels.append(f'<text x="{px+16}" y="{py}" class="l">{esc(language)} {pct:.1f}%</text>')

    if not top:
        labels.append('<text x="22" y="100" class="l">No public language data available.</text>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="495" height="165" viewBox="0 0 495 165">
<style>
text{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif}}
.t{{font-size:18px;font-weight:700;fill:{TITLE}}}.l{{font-size:11px;fill:{TEXT}}}.s{{font-size:10px;fill:#6e7681}}
</style>
<rect width="495" height="165" rx="8" fill="{BG}"/>
<rect x=".5" y=".5" width="494" height="164" rx="8" fill="none" stroke="{BORDER}"/>
<text x="22" y="34" class="t">Most Used Languages</text>
<clipPath id="bar"><rect x="22" y="57" width="451" height="11" rx="5.5"/></clipPath>
<g clip-path="url(#bar)">{''.join(bars) if bars else '<rect x="22" y="57" width="451" height="11" fill="#21262d"/>'}</g>
{''.join(labels)}
<text x="338" y="145" class="s">Public repositories</text>
</svg>'''
    write_svg("live-top-languages.svg", svg)

def make_graph(contributions):
    now = dt.datetime.now(dt.timezone.utc).date()
    days = [now - dt.timedelta(days=i) for i in range(29, -1, -1)]
    values = [int(contributions.get(day.isoformat(), 0)) for day in days]
    peak = max(max(values, default=0), 1)

    x0, y0 = 58.0, 190.0
    width, height = 908.0, 115.0
    points = []
    area_points = [f"{x0:.1f},{y0:.1f}"]

    for i, value in enumerate(values):
        x = x0 + width * i / 29
        y = y0 - height * value / peak
        points.append(f"{x:.1f},{y:.1f}")
        area_points.append(f"{x:.1f},{y:.1f}")

    area_points.append(f"{x0+width:.1f},{y0:.1f}")

    grid = []
    for j in range(4):
        y = y0 - height * j / 3
        grid.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0+width}" y2="{y:.1f}" stroke="#21262d"/>')

    total = sum(values)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="250" viewBox="0 0 1000 250">
<style>
text{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif}}
.t{{font-size:18px;font-weight:700;fill:{TITLE}}}.l{{font-size:11px;fill:{MUTED}}}.v{{font-size:11px;fill:{TEXT}}}
</style>
<defs>
  <linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{GREEN}" stop-opacity=".35"/>
    <stop offset="1" stop-color="{GREEN}" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect width="1000" height="250" rx="8" fill="{BG}"/>
<rect x=".5" y=".5" width="999" height="249" rx="8" fill="none" stroke="{BORDER}"/>
<text x="24" y="35" class="t">GitHub Activity — Last 30 Days</text>
<text x="800" y="35" class="v">{total} contributions / public events</text>
{''.join(grid)}
<polygon points="{' '.join(area_points)}" fill="url(#area)"/>
<polyline points="{' '.join(points)}" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<text x="{x0}" y="220" class="l">{days[0].strftime("%b %d")}</text>
<text x="{x0+width-37}" y="220" class="l">{days[-1].strftime("%b %d")}</text>
</svg>'''
    write_svg("live-activity-graph.svg", svg)

def main():
    user = request_json(f"https://api.github.com/users/{USERNAME}")
    repos = get_repos()
    contributions = contribution_days()
    make_stats(user, repos, contributions)
    make_languages(repos)
    make_graph(contributions)

if __name__ == "__main__":
    main()
