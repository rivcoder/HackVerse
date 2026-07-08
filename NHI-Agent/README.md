# 🛡️ NHI Governance Agent

> **AI-powered Non-Human Identity detection, risk scoring, and drift tracking for GitLab repositories.**

Built with **Gemini 2.0 Flash** · **Google Cloud Agent Builder** · **MongoDB Atlas** · **HTML5/CSS3/JS**

---

## 🎯 Problem Statement

Non-Human Identities (NHIs) — API keys, service account tokens, database passwords, and other machine credentials hardcoded in source code — are the **#1 cause of data breaches** in modern software. Most organizations have **17x more NHIs than human identities**, yet lack any governance tooling to detect, score, and track them over time.

## 💡 Solution

The **NHI Governance Agent** is an autonomous AI agent that:

1. **🔍 Scans** GitLab repositories for hardcoded credentials using pattern matching
2. **🤖 Scores** each finding's risk level (CRITICAL/HIGH/MEDIUM/LOW) using Gemini AI
3. **📊 Tracks** permission drift — detects when an NHI's risk level changes over time
4. **📈 Dashboards** everything in a premium, glassmorphic security console with export capabilities

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    NHI Governance Agent                         │
│                                                                 │
│  ┌──────────────┐   ┌──────────────┐   ┌────────────────────┐  │
│  │  scanner.py   │──▶│  Gemini AI   │──▶│   MongoDB Atlas    │  │
│  │  GitLab API   │   │  Risk Scorer │   │   (Persistence)    │  │
│  └──────────────┘   └──────────────┘   └────────────────────┘  │
│         │                                        │              │
│         ▼                                        ▼              │
│  ┌────────────────────────┐              ┌────────────────────┐  │
│  │  frontend/              │◀─────────────│   db.py            │  │
│  │  (HTML/CSS/JS SPA)     │              │   Drift Tracking   │  │
│  └────────────────────────┘              └────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Google Cloud Platform                        │  │
│  │  Cloud Run  ·  Pub/Sub  ·  Scheduler  ·  Secret Manager  │  │
│  │  Agent Builder  ·  GitLab MCP                             │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [Gemini API key](https://aistudio.google.com/apikey)
- MongoDB Atlas cluster (free M0 tier works)
- GitLab personal access token (optional, for private repos)

### Installation

```bash
# Clone and setup
git clone <repo-url>
cd nhi-agent
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### Configuration

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/?retryWrites=true&w=majority
MONGO_DB=nhi_governance
GITLAB_TOKEN=glpat-xxxxxxxxxxxxxxxxxxxx
```

### Run

```bash
# Option 1: Run the Unified Backend & Dashboard Server
python backend/server.py

# Option 2: CLI Scanner (legacy)
python backend/scanner.py
```

---

## 📁 Project Structure

```
nhi-agent/
├── backend/             # Consolidated Python API & database layers
│   ├── server.py        # Unified Flask API & static frontend server
│   ├── scanner.py       # Core NHI scanner + Gemini risk scoring engine
│   └── db.py            # MongoDB persistence layer (scans, NHI index, drift)
├── frontend/            # Single-page premium dashboard assets (HTML/CSS/JS)
│   ├── index.html       # Dashboard HTML structure
│   ├── css/style.css    # Premium CSS design system (neon accents, glassmorphic layout)
│   └── js/app.js        # Core dashboard logic, tab switching, and chart draws
├── agent.yaml           # Google Cloud Agent Builder configuration
├── deploy.sh            # One-shot GCP infrastructure setup script
├── Dockerfile           # Container config for Cloud Run deployment
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
└── README.md            # This file
```

---

## 🔑 Key Features

### Gemini-Powered Risk Scoring
Each detected NHI is analyzed by Gemini 2.0 Flash, which evaluates:
- **Risk level** — CRITICAL / HIGH / MEDIUM / LOW
- **Credential type** — API key, password, service token, etc.
- **Blast radius** — what could be compromised if leaked
- **Remediation action** — specific steps to fix

If Gemini is unavailable, the system falls back to **heuristic scoring** using pattern-based rules — ensuring zero downtime.

### Permission Drift Detection
The agent tracks every NHI across scans. When a credential's risk level changes (e.g., LOW → CRITICAL), it flags it as **risk drift** — a key signal that an identity's permissions are escalating without oversight.

### Automated Scanning Pipeline
- **Cloud Scheduler** triggers hourly scans via Cloud Run
- **Pub/Sub** publishes CRITICAL alerts to subscribed services
- **Slack integration** for real-time team notifications
- **MongoDB Atlas** persists all findings for historical analysis

---

## 🔌 Model Context Protocol (MCP) Integration

This project is fully designed for the **Google Cloud Rapid Agent Hackathon**. It features deep integration with the official partner MCP servers:
- **GitLab MCP**: Gives Gemini standardized tools to fetch file structures, read code, and inspect repository trees.
- **MongoDB MCP**: Allows Gemini to query, write, and track historical drift logs directly inside the database.

For step-by-step instructions on deploying these servers on Cloud Run and connecting them to Google Cloud Agent Builder, see [MCP_SETUP.md](file:///c:/Users/Asus/OneDrive/Desktop/hackathon/nhi-agent/MCP_SETUP.md).

---

## 🖥️ Dashboard Tabs

| Tab | Description |
|-----|-------------|
| **Live Scan** | Scan any GitLab repo on-demand, view findings with risk scores, export CSV |
| **History & Drift** | Risk trend charts over time, drift alerts, scan history table |
| **NHI Index** | Centralized inventory of all tracked NHIs with per-identity drift charts |

---

## ☁️ GCP Deployment

```bash
# Edit the 3 config variables at the top of deploy.sh
# Then run:
bash deploy.sh
```

This sets up:
- Cloud Run service for automated scanning
- Pub/Sub topic for CRITICAL alerts
- Cloud Scheduler for hourly scan triggers
- Secret Manager for credential storage
- Service account with least-privilege IAM roles

---

## 🔒 Security Considerations

- API keys and tokens stored in **GCP Secret Manager** (production) or `.env` (local)
- GitLab tokens use **read-only** repository access
- MongoDB connections use **TLS/SSL** via Atlas
- Cloud Run service account follows **least-privilege** principle
- No credentials are logged or exposed in the dashboard

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| AI Engine | Google Gemini 2.0 Flash |
| Agent Framework | Google Cloud Agent Builder |
| Source Control Integration | GitLab API + MCP |
| Database | MongoDB Atlas |
| Dashboard | HTML5 / CSS3 (Vanilla JS) |
| Cloud Infrastructure | GCP Cloud Run, Pub/Sub, Scheduler |
| Alerting | Pub/Sub + Slack webhooks |
| Language | Python 3.11 |

---

## 📊 Demo

Click **🎭 Demo** in the dashboard sidebar to see a simulated scan of `acme-payments` — 5 findings across Kubernetes secrets, environment files, CI pipelines, AWS integrations, and Terraform configs.

Click **Seed demo data** to generate 7 days of historical scans showing Agent #3 (AWS access key) escalating from LOW → CRITICAL over a week — demonstrating the drift detection capability.

---

## 👥 Team

Built for the **Google Cloud AI Hackathon 2025**

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
