"""
NGO Research Automation Pipeline
================================
Automates research data organization into Excel + Word deliverables.

Usage:
    python src/main.py                          # Use default data, generate outputs
    python src/main.py --data path/to/data.json # Custom NGO data file
    python src/main.py --config path/to/config  # Custom task configuration
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))

from excel_exporter import export_to_excel
from word_exporter import export_to_word
from analysis import generate_all_analysis


def load_config(config_path: Path) -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_ngos(data_path: Path) -> list[dict]:
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_pipeline(
    data_path: Path,
    config_path: Path,
    output_dir: Path,
) -> dict[str, Path]:
    config = load_config(config_path)
    ngos = load_ngos(data_path)

    min_required = config.get("task", {}).get("min_entities", 20)
    if len(ngos) < min_required:
        print(f"WARNING: Only {len(ngos)} NGOs found; minimum required is {min_required}")

    output_config = config.get("output", {})
    excel_name = output_config.get("excel_filename", "NGO_Research_Database.xlsx")
    word_name = output_config.get("word_filename", "NGO_Analysis_Report.docx")

    excel_path = output_dir / excel_name
    word_path = output_dir / word_name

    print(f"Loaded {len(ngos)} NGOs from {data_path}")
    print("Generating Excel spreadsheet...")
    export_to_excel(ngos, excel_path)
    print(f"  -> {excel_path}")

    print("Generating analytical insights...")
    analysis = generate_all_analysis(ngos)

    print("Generating Word analysis report...")
    task_title = config.get("task", {}).get("title", "NGO Research Analysis")
    export_to_word(ngos, analysis, word_path, task_title=task_title)
    print(f"  -> {word_path}")

    return {"excel": excel_path, "word": word_path}


def main():
    parser = argparse.ArgumentParser(description="NGO Research Automation Pipeline")
    parser.add_argument(
        "--data",
        type=Path,
        default=Path(__file__).parent.parent / "data" / "ngos_database.json",
        help="Path to NGO JSON data file",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).parent.parent / "config" / "task_config.yaml",
        help="Path to task configuration YAML",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent.parent / "output",
        help="Output directory for generated files",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  NGO Research Automation Pipeline")
    print("  Persona: AI Agent Developer")
    print("=" * 60)

    results = run_pipeline(args.data, args.config, args.output)

    print("\n" + "=" * 60)
    print("  DELIVERABLES READY")
    print("=" * 60)
    print(f"  Excel: {results['excel']}")
    print(f"  Word:  {results['word']}")
    print("\nUpload these files to Google Drive before the deadline.")
    print("=" * 60)


if __name__ == "__main__":
    main()
