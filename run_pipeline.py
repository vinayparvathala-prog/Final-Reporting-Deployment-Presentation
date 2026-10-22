from pathlib import Path
import subprocess
import sys
import logging

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(filename=LOG_DIR / "pipeline.log", level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(message)s")

# Add your real Task 1–4 script paths here in execution order.
PIPELINE_STEPS = [
    # "src/data_cleaning.py",
    # "src/exploratory_analysis.py",
    # "src/time_series_analysis.py",
    # "src/customer_segmentation.py",
    # "src/predictive_modeling.py",
    "src/generate_report.py",
]

def main():
    failed = []
    print("Apex Planet Task 5 pipeline")
    print("Update PIPELINE_STEPS with your actual Task 1–4 scripts.")
    for relative in PIPELINE_STEPS:
        script = ROOT / relative
        if not script.exists():
            message = f"SKIPPED (not found): {relative}"
            print(message)
            logging.warning(message)
            failed.append(relative)
            continue
        print(f"Running: {relative}")
        logging.info("START %s", relative)
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT)
        if result.returncode != 0:
            message = f"FAILED (exit {result.returncode}): {relative}"
            print(message)
            logging.error(message)
            failed.append(relative)
            break
        logging.info("SUCCESS %s", relative)
    if failed:
        print("Pipeline finished with skipped/failed steps. Check logs/pipeline.log.")
        raise SystemExit(1)
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
