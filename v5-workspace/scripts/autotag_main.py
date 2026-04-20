#!/usr/bin/env python3
"""
AutoTag - AVATARARTS Automation Tagging System
Main entry point for the AutoTag system
"""

import os
import sys
import argparse
import subprocess
from datetime import datetime
import json
import csv

def run_autotag_phase(phase_script, description, input_path=None, output_path=None):
    """Run a single phase of the AutoTag process"""
    print(f"\n{'='*60}")
    print(f"RUNNING: {description}")
    print(f"{'='*60}")

    cmd = [sys.executable, phase_script]
    if input_path:
        cmd.extend(["--input", input_path])
    if output_path:
        cmd.extend(["--output", output_path])

    start_time = datetime.now()
    print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        end_time = datetime.now()
        duration = end_time - start_time

        print(f"Completed successfully in {duration}")
        print(f"Ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Print any important output
        if result.stdout:
            print(f"Output:\n{result.stdout}")

        return True

    except subprocess.CalledProcessError as e:
        print(f"ERROR in {description}:")
        print(f"Return code: {e.returncode}")
        print(f"Error output: {e.stderr}")
        return False

def convert_json_to_csv(json_file_path, csv_file_path):
    """Convert the JSON output to CSV format for easier viewing"""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if 'automation_tools' in data and data['automation_tools']:
            tools = data['automation_tools']

            # Define the CSV headers based on the fields in the JSON
            headers = [
                'name', 'path', 'size_mb', 'created', 'modified', 'primary_type',
                'description', 'intelligent_category', 'confidence_score',
                'predicted_business_value', 'integration_potential_has_potential'
            ]

            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()

                for tool in tools:
                    row = {
                        'name': tool.get('name', ''),
                        'path': tool.get('path', ''),
                        'size_mb': tool.get('size_mb', 0),
                        'created': tool.get('created', ''),
                        'modified': tool.get('modified', ''),
                        'primary_type': tool.get('primary_type', ''),
                        'description': tool.get('description', '')[:200],  # Limit description length
                        'intelligent_category': tool.get('intelligent_category', ''),
                        'confidence_score': tool.get('confidence_score', 0),
                        'predicted_business_value': tool.get('predicted_business_value', 0),
                        'integration_potential_has_potential': tool.get('integration_potential', {}).get('has_potential', False)
                    }
                    writer.writerow(row)

            print(f"CSV file created: {csv_file_path}")
            return True
        else:
            print("No automation tools found in JSON to convert to CSV")
            return False

    except Exception as e:
        print(f"Error converting JSON to CSV: {str(e)}")
        return False

def open_file(file_path):
    """Open the file using the default application"""
    try:
        if sys.platform.startswith('darwin'):  # macOS
            subprocess.run(['open', file_path], check=True)
        elif sys.platform.startswith('win'):   # Windows
            os.startfile(file_path)
        elif sys.platform.startswith('linux'):  # Linux
            subprocess.run(['xdg-open', file_path], check=True)
        print(f"Opened file: {file_path}")
    except Exception as e:
        print(f"Could not open file automatically: {str(e)}")
        print(f"You can manually open the file: {file_path}")

def main():
    parser = argparse.ArgumentParser(description='AutoTag - AVATARARTS Automation Tagging System')
    parser.add_argument('--target', required=True, help='Path to directory to index')
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument('--output-dir', default=os.path.join(repo_root, 'output'), help='Output directory for results')
    parser.add_argument('--name', default='autotag_run', help='Name for this indexing run')
    parser.add_argument('--no-open', action='store_true', help='Skip opening the output file after completion')

    args = parser.parse_args()

    print("🚀 AutoTag - AVATARARTS Automation Tagging System")
    print("="*60)
    print(f"Target directory: {args.target}")
    print(f"Output directory: {args.output_dir}")
    print(f"Run name: {args.name}")
    print("="*60)

    # Create output directory for this run
    run_output_dir = os.path.join(args.output_dir, args.name)
    os.makedirs(run_output_dir, exist_ok=True)

    # Define the phase scripts
    base_script_dir = os.path.dirname(os.path.abspath(__file__))
    phases = [
        (os.path.join(base_script_dir, "phase1_rapid_scan.py"),
         "Phase 1: Rapid Initial Scan",
         {"--path": args.target}),
        (os.path.join(base_script_dir, "phase2_intelligent_organization.py"),
         "Phase 2: Intelligent Organization",
         {}),
        (os.path.join(base_script_dir, "phase3_advanced_intelligence.py"),
         "Phase 3: Advanced Intelligence",
         {})
    ]

    # Run each phase
    all_successful = True
    phase_outputs = []

    for i, (script, description, extra_args) in enumerate(phases):
        if i == 0:
            # Phase 1: input is target path, output is first phase result
            input_path = None  # Will be specified by --path
            output_filename = f"{args.name}_phase1.json"
        else:
            # Phases 2 and 3: input is previous phase output
            input_path = phase_outputs[-1]
            output_filename = f"{args.name}_phase{i+1}.json"

        output_path = os.path.join(run_output_dir, output_filename)

        # Build command with extra args for phase 1
        cmd = [sys.executable, script]
        if input_path:
            cmd.extend(["--input", input_path])
        cmd.extend(["--output", output_path])

        # Add extra args for phase 1 (like --path)
        for arg_name, arg_value in extra_args.items():
            cmd.extend([arg_name, arg_value])

        print(f"\n{'='*60}")
        print(f"RUNNING: {description}")
        print(f"{'='*60}")

        start_time = datetime.now()
        print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            end_time = datetime.now()
            duration = end_time - start_time

            print(f"Completed successfully in {duration}")
            print(f"Ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

            phase_outputs.append(output_path)
            print(f"Output saved to: {output_path}")

        except subprocess.CalledProcessError as e:
            print(f"ERROR in {description}:")
            print(f"Return code: {e.returncode}")
            print(f"Error output: {e.stderr}")
            all_successful = False
            break

    # Final summary
    print(f"\n{'='*60}")
    if all_successful:
        print("🎉 AUTOtag PROCESS COMPLETED SUCCESSFULLY!")
        print(f"The {args.target} directory has been fully indexed:")
        print("  - Phase 1: Rapid cataloging of all tools")
        print("  - Phase 2: Intelligent categorization and tagging")
        print("  - Phase 3: Advanced analysis and predictions")

        # Convert final output to CSV
        final_json_path = phase_outputs[-1]  # Last phase output (Phase 3)
        csv_output_path = os.path.join(run_output_dir, f"{args.name}_results.csv")

        print(f"\nConverting results to CSV format...")
        if convert_json_to_csv(final_json_path, csv_output_path):
            print(f"CSV results saved to: {csv_output_path}")

            # Open the CSV file if not disabled
            if not args.no_open:
                print("Opening CSV results file...")
                open_file(csv_output_path)
        else:
            print("Could not convert results to CSV format")

        print(f"\nDetailed results saved to: {run_output_dir}")
        print("The knowledge base now contains comprehensive intelligence")
        print("about all automation tools with predictive insights.")
    else:
        print("❌ Some phases failed. Please check the error messages above.")
    print("="*60)

if __name__ == "__main__":
    main()
