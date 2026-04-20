#!/usr/bin/env python3
"""
AutoTag - Compat Main Runner
Add-only wrapper that fixes paths and missing phase scripts without editing originals.
"""

import os
import sys
import argparse
import subprocess
from datetime import datetime
import json
import csv


def _repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_phase(cmd, description):
    print("\n{0}".format("=" * 60))
    print("RUNNING: {0}".format(description))
    print("{0}".format("=" * 60))

    start_time = datetime.now()
    print("Started at: {0}".format(start_time.strftime("%Y-%m-%d %H:%M:%S")))

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        end_time = datetime.now()
        duration = end_time - start_time

        print("Completed successfully in {0}".format(duration))
        print("Ended at: {0}".format(end_time.strftime("%Y-%m-%d %H:%M:%S")))

        if result.stdout:
            print("Output:\n{0}".format(result.stdout))

        return True

    except subprocess.CalledProcessError as e:
        print("ERROR in {0}:".format(description))
        print("Return code: {0}".format(e.returncode))
        print("Error output: {0}".format(e.stderr))
        return False


def convert_json_to_csv(json_file_path, csv_file_path):
    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "automation_tools" in data and data["automation_tools"]:
            tools = data["automation_tools"]

            headers = [
                "name",
                "path",
                "size_mb",
                "created",
                "modified",
                "primary_type",
                "description",
                "intelligent_category",
                "confidence_score",
                "predicted_business_value",
                "integration_potential_has_potential",
            ]

            with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()

                for tool in tools:
                    row = {
                        "name": tool.get("name", ""),
                        "path": tool.get("path", ""),
                        "size_mb": tool.get("size_mb", 0),
                        "created": tool.get("created", ""),
                        "modified": tool.get("modified", ""),
                        "primary_type": tool.get("primary_type", ""),
                        "description": (tool.get("description", "") or "")[:200],
                        "intelligent_category": tool.get("intelligent_category", ""),
                        "confidence_score": tool.get("confidence_score", 0),
                        "predicted_business_value": tool.get("predicted_business_value", 0),
                        "integration_potential_has_potential": tool.get("integration_potential", {}).get(
                            "has_potential", False
                        ),
                    }
                    writer.writerow(row)

            print("CSV file created: {0}".format(csv_file_path))
            return True
        else:
            print("No automation tools found in JSON to convert to CSV")
            return False

    except Exception as e:
        print("Error converting JSON to CSV: {0}".format(str(e)))
        return False


def open_file(file_path):
    try:
        if sys.platform.startswith("darwin"):
            subprocess.run(["open", file_path], check=True)
        elif sys.platform.startswith("win"):
            os.startfile(file_path)
        elif sys.platform.startswith("linux"):
            subprocess.run(["xdg-open", file_path], check=True)
        print("Opened file: {0}".format(file_path))
    except Exception as e:
        print("Could not open file automatically: {0}".format(str(e)))
        print("You can manually open the file: {0}".format(file_path))


def main():
    parser = argparse.ArgumentParser(description="AutoTag - Compat Runner")
    parser.add_argument("--target", required=True, help="Path to directory to index")
    parser.add_argument(
        "--output-dir",
        default=os.path.join(_repo_root(), "output"),
        help="Output directory for results",
    )
    parser.add_argument("--name", default="autotag_run", help="Name for this indexing run")
    parser.add_argument("--no-open", action="store_true", help="Skip opening the output file after completion")

    args = parser.parse_args()

    print("AutoTag - Compat Runner")
    print("=" * 60)
    print("Target directory: {0}".format(args.target))
    print("Output directory: {0}".format(args.output_dir))
    print("Run name: {0}".format(args.name))
    print("=" * 60)

    run_output_dir = os.path.join(args.output_dir, args.name)
    os.makedirs(run_output_dir, exist_ok=True)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    phase1 = os.path.join(script_dir, "phase1_rapid_scan_compat.py")
    phase2 = os.path.join(script_dir, "phase2_intelligent_organization.py")
    phase3 = os.path.join(script_dir, "phase3_advanced_intelligence.py")

    phase_outputs = []

    # Phase 1
    output_path = os.path.join(run_output_dir, "{0}_phase1.json".format(args.name))
    cmd = [sys.executable, phase1, "--path", args.target, "--output", output_path]
    if not run_phase(cmd, "Phase 1: Rapid Initial Scan (Compat)"):
        print("Phase 1 failed. Aborting.")
        sys.exit(1)
    phase_outputs.append(output_path)

    # Phase 2
    output_path = os.path.join(run_output_dir, "{0}_phase2.json".format(args.name))
    cmd = [sys.executable, phase2, "--input", phase_outputs[-1], "--output", output_path]
    if not run_phase(cmd, "Phase 2: Intelligent Organization (Compat)"):
        print("Phase 2 failed. Aborting.")
        sys.exit(1)
    phase_outputs.append(output_path)

    # Phase 3
    output_path = os.path.join(run_output_dir, "{0}_phase3.json".format(args.name))
    cmd = [sys.executable, phase3, "--input", phase_outputs[-1], "--output", output_path]
    if not run_phase(cmd, "Phase 3: Advanced Intelligence (Compat)"):
        print("Phase 3 failed. Aborting.")
        sys.exit(1)
    phase_outputs.append(output_path)

    final_json_path = phase_outputs[-1]
    csv_output_path = os.path.join(run_output_dir, "{0}_results.csv".format(args.name))

    print("\nConverting results to CSV format...")
    if convert_json_to_csv(final_json_path, csv_output_path):
        print("CSV results saved to: {0}".format(csv_output_path))
        if not args.no_open:
            print("Opening CSV results file...")
            open_file(csv_output_path)
    else:
        print("Could not convert results to CSV format")

    print("\nDetailed results saved to: {0}".format(run_output_dir))
    print("Process complete.")


if __name__ == "__main__":
    main()
