# Automated Report Pipeline

A serverless automated reporting system using GitHub Actions.

## What it does
- Runs on a weekly schedule (every Monday at 08:00 UTC)
- Processes raw data and calculates KPIs (Orders, Revenue, AOV)
- Generates a Markdown report and commits it back to the repository automatically
- Zero manual intervention and zero server cost

## Tech Stack
- **Python** (Pandas) for data processing
- **GitHub Actions** for scheduled workflow automation
- **Git** for automated commits

## How to test
1. Go to the **Actions** tab
2. Select "Weekly Report Generator"
3. Click "Run workflow"
