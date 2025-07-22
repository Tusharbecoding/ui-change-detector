# Web UI Change Detector & Impact Assessor

A multi-agent system that detects webpage changes and predicts their impact on browser automation

## Why This Matters for Web Automation

**The Problem:** Web UIs constantly change - new buttons, moved elements, updated IDs. These changes break browser automation scripts and AI agents.

**The Solution:** Proactive change detection that predicts automation failures before they happen.

## Agents

1. **Page Scanner** - Captures detailed webpage structure and automation-relevant elements
2. **Change Detector** - Compares snapshots to identify all structural differences
3. **Impact Analyzer** - Assesses which changes would break browser automation

## Features

- 🔍 **Deep Structure Analysis** - Extracts buttons, forms, links, IDs, classes
- 📊 **Change Detection** - Identifies moved, added, deleted, or modified elements
- ⚠️ **Automation Impact Assessment** - Predicts which changes break web agents
- 📝 **Detailed Reports** - Provides actionable insights for maintaining robust automation
- 🚀 **Simple Interface** - Test any website in minutes

## Quick Start

1. **Setup**

   ```bash
   pip install -r requirements.txt
   # Add your Google API key to .env file
   ```

2. **Run Analysis**

   ```bash
   python crew.py
   ```
