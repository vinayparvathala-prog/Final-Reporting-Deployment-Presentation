# Apex Planet Data Analytics Internship — Task 5
## Final Reporting, Deployment & Presentation

This starter project helps prepare the final submission from your completed Tasks 1–4.

### Includes
- `src/generate_report.py`: summarizes CSV outputs and generates Markdown + JSON reports.
- `src/run_pipeline.py`: configurable pipeline runner with logging.
- `reports/FINAL_REPORT_TEMPLATE.md`: final report outline.
- `reports/PRESENTATION_CHECKLIST.md`: slide and demo checklist.

> This is a starter template. Add your real Task 1–4 scripts and outputs, then verify every finding and metric. It does not claim that a dashboard is already deployed.

## Setup (Windows 11 / VS Code)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`.

## Run the report generator
Copy your real CSV outputs into `outputs/`, then run:
```powershell
python src/generate_report.py
```
This creates `outputs/final_summary.json` and `outputs/final_report.md`.

## Run the pipeline
Edit `PIPELINE_STEPS` in `src/run_pipeline.py` to point to your actual Task 1–4 scripts, then run:
```powershell
python src/run_pipeline.py
```
The log is saved at `logs/pipeline.log`. Missing scripts are reported rather than silently treated as successful.

## Optional Windows Task Scheduler
1. Open Task Scheduler → Create Basic Task.
2. Choose a daily or weekly trigger.
3. Choose **Start a program**.
4. Program: the full path to `.venv\Scripts\python.exe`.
5. Arguments: the full path to `src\run_pipeline.py`.
6. Start in: the project folder.
7. Test it and inspect `logs/pipeline.log`.

For cloud deployment, publish your actual dashboard using your chosen service and add its verified URL here. No cloud hosting is preconfigured.
