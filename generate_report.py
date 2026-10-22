from pathlib import Path
from datetime import datetime, timezone
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

def summarize_csv(path: Path) -> dict:
    item = {"file": str(path.relative_to(ROOT)), "rows": None, "columns": [], "numeric_summary": {}}
    try:
        df = pd.read_csv(path)
        item["rows"] = int(len(df))
        item["columns"] = [str(c) for c in df.columns]
        numeric = df.select_dtypes(include="number")
        for col in numeric.columns:
            series = numeric[col].dropna()
            item["numeric_summary"][str(col)] = {
                "mean": round(float(series.mean()), 3) if not series.empty else None,
                "min": round(float(series.min()), 3) if not series.empty else None,
                "max": round(float(series.max()), 3) if not series.empty else None,
                "sum": round(float(series.sum()), 3) if not series.empty else None,
            }
    except Exception as exc:
        item["error"] = str(exc)
    return item

def main():
    csv_files = sorted(OUTPUTS.glob("*.csv"))
    summaries = [summarize_csv(p) for p in csv_files]
    data = {
        "project": "Apex Planet Data Analytics Internship — Task 5",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "csv_outputs_found": len(csv_files),
        "outputs": summaries,
        "note": "Automatically generated summary. Verify results and add interpretation before submission."
    }
    (OUTPUTS / "final_summary.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    lines = [
        "# Final Data Analytics Report", "",
        f"Generated (UTC): {data['generated_at_utc']}", "",
        "## Project overview",
        "Describe the business problem, datasets, and questions addressed in Tasks 1–4.", "",
        "## Output inventory", f"CSV output files found: **{len(csv_files)}**", ""
    ]
    if not summaries:
        lines += ["No CSV outputs found. Copy your verified Task 1–4 CSV results into `outputs/` and rerun this script.", ""]
    for item in summaries:
        lines += [f"### `{item['file']}`", f"- Rows: {item.get('rows', 'unknown')}",
                  f"- Columns: {', '.join(item.get('columns', [])) or 'not available'}"]
        if item.get("error"):
            lines.append(f"- Read error: {item['error']}")
        for col, stats in item.get("numeric_summary", {}).items():
            lines.append(f"- **{col}** — mean: {stats['mean']}, min: {stats['min']}, max: {stats['max']}, sum: {stats['sum']}")
        lines.append("")
    lines += [
        "## Key findings", "- Add 3–7 findings supported by your actual charts and metrics.", "",
        "## Recommendations", "- Link each recommendation to a verified finding.", "",
        "## Limitations", "- Document data quality, assumptions, and model limitations.", "",
        "## Reproducibility", "- Record Python/package versions, data sources, and run commands.", ""
    ]
    (OUTPUTS / "final_report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated: {OUTPUTS / 'final_report.md'}")
    print(f"Generated: {OUTPUTS / 'final_summary.json'}")
    print(f"CSV files summarized: {len(csv_files)}")

if __name__ == "__main__":
    main()
