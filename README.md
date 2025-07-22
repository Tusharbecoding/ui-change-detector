# Web UI Change Detector & Impact Assessor

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

> **Proactively detect UI changes and assess their impact on browser automation.**

---

## 🚀 Overview

**Web UI Change Detector & Impact Assessor** is a multi-agent, LLM-powered system that scans web pages, detects UI changes, and predicts their impact on browser automation scripts. It empowers QA engineers, SDETs, and developers to maintain robust automation in the face of ever-changing web UIs.

- **Detects breaking changes before they hit production**
- **Provides actionable, detailed impact reports**
- **Designed for reliability, extensibility, and developer experience**

---

## 🏗️ Architecture

```
Page Scanner (Agent) → Change Detector (Agent) → Impact Analyzer (Agent)
        |                    |                        |
   [scraper_tool]      [file_tool]                [LLM]
```

- **Sequential multi-agent pipeline** using [CrewAI](https://github.com/joaomdmoura/crewAI)
- **LLM-powered analysis** (Google Gemini)
- **Snapshot-based change detection**
- **Modular tools** for scraping and file management

---

## 🤖 Agents & Tasks

### 1. **Page Scanner**

- **Role:** Captures and analyzes the full structure of a target web page
- **Goal:** Extract all automation-relevant elements (buttons, forms, links, IDs, classes, etc.)
- **Tools:** `scraper_tool`, `file_tool`
- **Task:** Save a detailed snapshot for future comparison

### 2. **Change Detector**

- **Role:** Compares the latest snapshot with a previous version
- **Goal:** Identify all structural and content changes (moved, added, deleted, or modified elements)
- **Tools:** `file_tool`
- **Task:** Generate a comprehensive change report

### 3. **Impact Analyzer**

- **Role:** Assesses the automation impact of detected changes
- **Goal:** Predict which changes will break scripts, cause selector failures, or require updates
- **Tools:** LLM only
- **Task:** Output a professional impact report (`ui_change_impact_report.md`)

---

## 🛠️ Tools

- **scraper_tool:** Scrapes a web page and extracts its structure (buttons, forms, links, inputs, headings, etc.)
- **file_tool:** Manages snapshot storage and retrieval (save/load/list)

---

## ✨ Features

- 🔍 **Deep Structure Analysis**: Extracts all automation-critical elements
- 📊 **Change Detection**: Identifies moved, added, deleted, or modified elements
- ⚠️ **Impact Assessment**: Predicts which changes break web agents/scripts
- 📝 **Detailed Reports**: Actionable, human-readable Markdown reports
- 🧩 **Modular & Extensible**: Add new agents, tools, or LLMs easily
- 🚀 **Simple CLI**: Analyze any website in minutes

---

## ⚡ Quick Start

### 1. **Clone & Install**

```bash
# Clone the repo
$ git clone https://github.com/Tusharbecoding/ui-change-detector/tree/main
$ cd ui-change-detector

# Create and activate a virtual environment (recommended)
$ python3 -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt
```

### 2. **Environment Setup**

- Add your Google API key to a `.env` file:

```
GOOGLE_API_KEY=your-google-api-key
```

### 3. **Run Analysis**

```bash
python crew.py
```

- Select a test URL or enter your own when prompted.
- The system will scan, compare, and generate a detailed impact report.
- Output: `ui_change_impact_report.md`

---

## 📝 Example Output

Below is a sample excerpt from a generated impact report:

```
# 🔍 UI Change Impact Assessment Report

**Website:** California Secretary of State - UCC Search
**URL:** https://bizfileonline.sos.ca.gov/search/ucc
**Analysis Date:** January 22, 2025

## 📊 Executive Summary

**Overall Impact Level:** 🔴 HIGH IMPACT
**Total Changes Detected:** 8 significant modifications
**Automation Scripts Affected:** Estimated 85% of scripts require updates

---

## 🎯 Critical Changes Detected

- **Search Button Selector Changed:** BREAKS ALL AUTOMATION
- **Debtor Name Input Field Restructured:** HIGH FAILURE RISK
- ...

## 🛠️ Immediate Fix Recommendations

- Update selectors in automation scripts
- Remove dependencies on deleted elements
- Implement fallback selector strategies

---
```

See [`ui_change_impact_report.md`](ui_change_impact_report.md) for a full example.

---

## 🧑‍💻 Developer Notes

- **Agents:** Defined in [`agents.py`](agents.py) with clear roles and LLM configuration
- **Tasks:** Modular, described in [`tasks.py`](tasks.py)
- **Tools:** Extend or customize in [`tools.py`](tools.py)
- **Main entrypoint:** [`crew.py`](crew.py) (CLI interface)
- **Dependencies:** See [`requirements.txt`](requirements.txt)
- **Virtual environment:** Recommended for isolation (`venv/`)
- **Snapshots:** Saved in `snapshots/` (auto-created, gitignored)

---

## 🙏 Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI) for multi-agent orchestration
- [Google Gemini](https://ai.google.dev/gemini-api/docs) for LLM-powered analysis
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing
- [Requests](https://docs.python-requests.org/) for HTTP requests

---

## 💡 Best Practices & Tips

- **Run regularly:** Integrate into your CI/CD to catch breaking UI changes early
- **Use robust selectors:** Prefer IDs, fallback to classes/XPath as needed
- **Review reports:** Address high-severity changes before deploying automation
- **Extend agents/tools:** Adapt the system for your unique automation stack
