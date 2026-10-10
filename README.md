<p align="center">
  <img src="assets/cover-dynamic.svg" alt="Animated engineering profile banner" width="100%">
</p>

<h1 align="center">Jacobo Allemann Castro</h1>
<h3 align="center">Mechatronics Engineer · Robotics · Artificial Intelligence · Automation · Systems Integration</h3>

<p align="center">
  <a href="https://github.com/tjallemann01"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-Portfolio-111827?style=for-the-badge&logo=github"></a>
  <a href="https://www.linkedin.com/in/jacoboallemanncastro"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin"></a>
  <a href="https://www.linkedin.com/in/jacoboallemanncastro/"><img alt="Harvard CS50AI on LinkedIn" src="https://img.shields.io/badge/Harvard-CS50AI%20Certificate-A51C30?style=for-the-badge"></a>
</p>

<p align="center"><strong>PERCEIVE → DECIDE → CONTROL → ACTUATE → VALIDATE</strong></p>

<p align="center">
  <a href="#engineering-profile">Profile</a> · <a href="#featured-engineering-systems">Engineering Systems</a> · <a href="#harvard-cs50ai--12-completed-projects">Harvard AI</a> · <a href="#technologies--engineering-stack">Tech Logos</a> · <a href="#technical-toolbox">Toolbox</a> · <a href="#education--professional-practice">Education & Practice</a>
</p>

---

## Engineering Profile

**B.S. in Mechatronics Engineering — Tecnológico de Monterrey (2026).** I design, build and integrate intelligent electromechanical systems connecting **mechanical design, sensing, computer vision, embedded computing, control, actuators, safety and testing**.

My work emphasizes the entire engineering cycle—from subsystem selection and CAD to implementation, troubleshooting and physical validation.

<p align="center"><img src="assets/engineering-loop.svg" alt="Animated mechatronics systems engineering workflow" width="100%"></p>

| Discipline | Engineering focus |
| :-- | :-- |
| **Autonomous Systems** | Mobile robotics, perception, tracking, motion control and safety supervision |
| **Intelligent Perception** | YOLO, OpenCV, Intel RealSense and Cognex VisionPro |
| **Embedded Control** | NVIDIA Jetson, STM32, ESP32, sensors, BLDC/VESC and PID |
| **Industrial Robotics** | Siemens PLC/TIA Portal, robotic kinematics, manufacturing and systems integration |
| **Design & Validation** | SolidWorks, prototyping, integration testing, troubleshooting and documentation |

---

## Featured Engineering Systems

### 01 — Autonomous Mobile Robot + AI

<a href="https://github.com/tjallemann01/AMR-AI-Autonomous-Mobile-Robot"><img src="assets/amr-card.svg" alt="Animated Autonomous Mobile Robot project card" width="100%"></a>

**Role:** Primary Developer / Systems Integrator. NVIDIA Jetson Orin NX, Intel RealSense, YOLO perception, target tracking, VESC motor control and safety supervision.

**Documented observations:** approximately 20–25 FPS in perception tests; 68/75 valid system tests; 26–28/30 successful real-environment trials under the reported test conditions.

<details><summary><strong>View perception-to-motion architecture</strong></summary>

```mermaid
flowchart LR
    A[RealSense and Sensors] --> B[YOLO Detection]
    B --> C[Target Tracking]
    C --> D[Motion Decision]
    D --> E[VESC Motor Control]
    E --> F[Tracked Drive]
    F -. Physical Feedback .-> A
    G[Watchdog and Emergency Stop] --> D
```

</details>

**[Explore AMR project →](https://github.com/tjallemann01/AMR-AI-Autonomous-Mobile-Robot)**

### 02 — 3-DOF Delta Robot with Computer Vision

<a href="https://github.com/tjallemann01/3DOF-Delta-Robot-Vision-Control"><img src="assets/delta-card.svg" alt="Animated Delta Robot project card" width="100%"></a>

Parallel robotic mechanisms, Siemens PLC/TIA Portal, Cognex VisionPro, Python integration, forward/inverse kinematics and vision-guided manipulation.

<details><summary><strong>View robot system flow</strong></summary>

```mermaid
flowchart LR
    CAM[Cognex Camera] --> VP[VisionPro]
    VP --> PY[Python Supervisor]
    PY --> KIN[Robot Kinematics]
    KIN --> PLC[Siemens PLC]
    PLC --> ROBOT[3-DOF Delta Robot]
    ROBOT -. Feedback .-> CAM
```

</details>

**[Explore Delta Robot →](https://github.com/tjallemann01/3DOF-Delta-Robot-Vision-Control)**

### 03 — BattleBot P_5

<a href="https://github.com/tjallemann01/BattleBot"><img src="assets/battlebot-card.svg" alt="Animated BattleBot project card" width="100%"></a>

FlySky iBUS RC, onboard NVIDIA Jetson vision, YOLO target detection, differential BLDC drive, dual Makerbase MINI VESC controllers and safety-oriented mode arbitration.

**Control priority:** `E-STOP > MANUAL > AI`

<details><summary><strong>View control-priority logic</strong></summary>

```mermaid
flowchart TD
    INPUT[RC Receiver] --> VALID{Signal Valid?}
    VALID -- No --> STOP[Safe Stop]
    VALID -- Yes --> ESTOP{E-STOP?}
    ESTOP -- Yes --> STOP
    ESTOP -- No --> MODE{Control Mode}
    MODE --> MAN[Manual Control]
    MODE --> AI[AI Assistance]
    MAN --> DRIVE[Dual VESC Drive]
    AI --> DRIVE
```

</details>

**[Explore BattleBot →](https://github.com/tjallemann01/BattleBot)**

### 04 — Industrial Drying-Line Automation

<a href="https://github.com/tjallemann01/Industrial-Drying-Line-Automation"><img src="assets/drying-card.svg" alt="Animated industrial automation project card" width="100%"></a>

Thermal and airflow design, STM32 firmware, temperature control, conveyor synchronization, custom electronics and ESP32 monitoring.

<details><summary><strong>View process-control architecture</strong></summary>

```mermaid
flowchart LR
    SENSOR[Temperature Sensors] --> MCU[STM32]
    MCU --> PID[PID Control]
    PID --> HEATER[Heating System]
    MCU --> CONVEYOR[Conveyor]
    MCU --> ESP[ESP32 Monitoring]
    HEATER -. Feedback .-> SENSOR
```

</details>

**[Explore Drying-Line Automation →](https://github.com/tjallemann01/Industrial-Drying-Line-Automation)**

---

## Harvard CS50AI — 12 Completed Projects

<p align="center"><a href="https://www.linkedin.com/in/jacoboallemanncastro/"><img alt="Harvard CS50AI on LinkedIn" src="https://img.shields.io/badge/Certificate-Verify%20Harvard%20CS50AI-A51C30?style=for-the-badge"></a></p>

**CS50's Introduction to Artificial Intelligence with Python.** Projects span fundamental search algorithms through probabilistic inference, machine learning, reinforcement learning, computer vision and Transformer-based NLP.

| Project | AI topic | Repository |
| :-- | :-- | :-- |
| Degrees | Breadth-first search | [CS50AI-Degrees](https://github.com/tjallemann01/CS50AI-Degrees) |
| Tic-Tac-Toe | Minimax, adversarial search | [CS50AI-TicTacToe](https://github.com/tjallemann01/CS50AI-TicTacToe) |
| Knights | Propositional logic, model checking | [CS50AI-Knights](https://github.com/tjallemann01/CS50AI-Knights) |
| Minesweeper | Knowledge-based agents | [CS50AI-Minesweeper](https://github.com/tjallemann01/CS50AI-Minesweeper) |
| PageRank | Probabilistic ranking | [CS50AI-PageRank](https://github.com/tjallemann01/CS50AI-PageRank) |
| Heredity | Bayesian inference | [CS50AI-Heredity](https://github.com/tjallemann01/CS50AI-Heredity) |
| Crossword | Constraint satisfaction | [CS50AI-Crossword](https://github.com/tjallemann01/CS50AI-Crossword) |
| Shopping | Supervised learning, KNN | [CS50AI-Shopping](https://github.com/tjallemann01/CS50AI-Shopping) |
| Nim | Reinforcement learning, Q-learning | [CS50AI-Nim](https://github.com/tjallemann01/CS50AI-Nim) |
| Traffic | CNN, TensorFlow, computer vision | [CS50AI-Traffic](https://github.com/tjallemann01/CS50AI-Traffic) |
| Parser | Natural language parsing, NLTK | [CS50AI-Parser](https://github.com/tjallemann01/CS50AI-Parser) |
| Attention | BERT, Transformer self-attention | [CS50AI-Attention](https://github.com/tjallemann01/CS50AI-Attention) |

> **Academic integrity:** Repositories containing graded CS50AI solutions should remain private under course sharing restrictions. Links to private repositories are visible only to authorized viewers.

---

## Technologies & Engineering Stack

<p align="center"><strong>AI · Machine Learning · Computer Vision</strong></p>
<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
  <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
  <img alt="Scikit Learn" src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
  <img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=111827">
  <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img alt="YOLO" src="https://img.shields.io/badge/YOLO-Computer%20Vision-00FFFF?style=for-the-badge&logoColor=111827">
  <img alt="BERT" src="https://img.shields.io/badge/BERT-Transformers-7C3AED?style=for-the-badge">
  <img alt="NLTK" src="https://img.shields.io/badge/NLTK-NLP-2D6A4F?style=for-the-badge">
</p>

<p align="center"><strong>Embedded · Robotics · Industrial Control</strong></p>
<p align="center">
  <img alt="NVIDIA" src="https://img.shields.io/badge/NVIDIA%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white">
  <img alt="Arduino" src="https://img.shields.io/badge/Arduino-00878F?style=for-the-badge&logo=arduino&logoColor=white">
  <img alt="ESP32" src="https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white">
  <img alt="STM32" src="https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white">
  <img alt="C" src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=111827">
  <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white">
  <img alt="Siemens" src="https://img.shields.io/badge/Siemens%20PLC-009999?style=for-the-badge&logo=siemens&logoColor=white">
  <img alt="Industrial Automation" src="https://img.shields.io/badge/TIA%20Portal-Industrial%20Control-007E87?style=for-the-badge">
  <img alt="ROS" src="https://img.shields.io/badge/ROS-Robotics-22314E?style=for-the-badge&logo=ros&logoColor=white">
  <img alt="RealSense" src="https://img.shields.io/badge/Intel%20RealSense-Camera-0071C5?style=for-the-badge&logo=intel&logoColor=white">
  <img alt="VESC" src="https://img.shields.io/badge/VESC-BLDC%20Control-0E7490?style=for-the-badge">
</p>

<p align="center"><strong>Mechanical Design · Software · Development Tools</strong></p>
<p align="center">
  <img alt="SolidWorks" src="https://img.shields.io/badge/SolidWorks-CB333B?style=for-the-badge">
  <img alt="Fusion 360" src="https://img.shields.io/badge/Autodesk%20Fusion-000000?style=for-the-badge&logo=autodesk&logoColor=white">
  <img alt="MATLAB" src="https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge">
  <img alt="Git" src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  <img alt="Visual Studio Code" src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
  <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=111827">
  <img alt="Windows" src="https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white">
  <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white">
  <img alt="Markdown" src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white">
</p>

<sub>Logos represent tools, libraries and technology areas featured in my engineering projects and technical learning; they do not imply vendor endorsements or equal proficiency in every tool.</sub>

---

## Technical Toolbox

| AI & Perception | Control & Embedded | Mechanical & Industrial |
| :-- | :-- | :-- |
| Python / TensorFlow | NVIDIA Jetson | SolidWorks / CAD |
| YOLO / OpenCV | STM32 / ESP32 | Siemens PLC / TIA Portal |
| RealSense / Cognex | VESC / BLDC motors | Robot kinematics |
| BERT / NLTK | PID / Watchdogs | CNC / Prototyping |
| Tracking / Kalman filtering | UART / I²C / PWM | Integration & Validation |

---

## Education & Professional Practice

- **B.S. Mechatronics Engineering — Tecnológico de Monterrey (2026).**
- **Harvard CS50AI — certificate earned and twelve programming projects completed.** [See credentials on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/) · [Verify Harvard certificate](https://cs50.harvard.edu/certificates/4d1848b5-b7cc-4b37-8155-819e19e6054d).
- **Lean Six Sigma Black Belt coursework** — organization, team management and process-improvement methodology. [See training and credentials on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/).
- **Claude Academy — AI developer training** — AI Fluency for Builders, Claude Code in Action, Introduction to MCP, MCP Advanced Topics and Subagents. [See credentials on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/).

### Certifications & Learning Credentials

<p align="center">
  <a href="https://www.linkedin.com/in/jacoboallemanncastro/"><img alt="Harvard CS50AI on LinkedIn" src="https://img.shields.io/badge/Harvard-CS50AI%20Certificate-A51C30?style=for-the-badge"></a>
  <a href="https://www.linkedin.com/in/jacoboallemanncastro/"><img alt="Tecnológico de Monterrey education on LinkedIn" src="https://img.shields.io/badge/Tec%20de%20Monterrey-Mechatronics-00457C?style=for-the-badge"></a>
  <a href="https://www.linkedin.com/in/jacoboallemanncastro/"><img alt="Lean Six Sigma Black Belt training on LinkedIn" src="https://img.shields.io/badge/Lean%20Six%20Sigma-Black%20Belt%20Training-111827?style=for-the-badge"></a>
  <a href="https://www.linkedin.com/in/jacoboallemanncastro/"><img alt="Claude Academy on LinkedIn" src="https://img.shields.io/badge/Claude%20Academy-AI%20Training-D97757?style=for-the-badge"></a>
</p>

| Credential / learning track | Focus | LinkedIn |
| :-- | :-- | :-- |
| **Harvard CS50AI** | AI algorithms, ML, neural networks, NLP | [See on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/) |
| **Lean Six Sigma — Black Belt coursework** | Quality management, process improvement and project teams | [See on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/) |
| **Claude Academy — AI Fluency for Builders** | Building responsibly with AI | [See on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/) |
| **Claude Academy — Claude Code in Action** | AI-assisted development workflows | [See on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/) |
| **Claude Academy — Model Context Protocol** | MCP clients, servers, tools and resources | [See on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/) |
| **Claude Academy — MCP Advanced Topics** | Transport, notifications, sampling and state | [See on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/) |
| **Claude Academy — Subagents** | Designing and using specialized AI agents | [See on LinkedIn](https://www.linkedin.com/in/jacoboallemanncastro/) |

<sub>All links above open my LinkedIn profile; availability of individual credential entries depends on what is published there. Coursework is identified as training rather than claiming an independently verified Black Belt certification.</sub>

### Robotics & Industrial Automation Practice

<a href="https://github.com/tjallemann01"><img src="assets/laser-card.svg" alt="Animated industrial robotic integration card" width="100%"></a>

**G.A. Systems, Inc.** — Industrial equipment and robotic automation experience involving robot programming, technical integration, manufacturing and functional testing. Proprietary details are intentionally omitted.

---

## Design Philosophy

> **Build systems that can perceive, reason, act safely and be tested in the physical world.**

I prioritize controlled experimentation, technical documentation, safety interlocks, measurable validation and responsible engineering practice.

<p align="center"><img src="assets/footer-dynamic.svg" alt="Animated engineering footer" width="100%"></p>

<p align="center"><strong>Explore the work. Understand the system. Build what comes next.</strong></p>
