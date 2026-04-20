#!/usr/bin/env python3
"""
Universal Directory Indexer for AVATARARTS Knowledge Base
Can process any directory with the tiered indexing system
"""

import sys
import os
import argparse
from datetime import datetime
import subprocess

def run_tiered_indexing_on_directory(target_directory, output_prefix="custom_index", output_dir=None):
    """Run the complete tiered indexing on a specified directory"""
    # Define unified output directory
    if output_dir:
        output_path = os.path.abspath(os.path.expanduser(output_dir))
    else:
        output_path = os.path.expanduser("~/AutoTag/output")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    print(f"Starting tiered indexing on: {target_directory}")
    print(f"Output prefix: {output_prefix}")
    print(f"Output directory: {output_path}")

    # Validate directory exists
    if not os.path.isdir(target_directory):
        print(f"Error: Directory {target_directory} does not exist")
        return False

    # Define the base path for the scripts
    script_base_path = os.path.expanduser("~/.tagger")
    
    # Phase 1: Rapid Initial Scan
    print("\nPhase 1: Rapid Initial Scan")
    print("-" * 40)
    phase1_script = os.path.join(script_base_path, "phase1_rapid_scan.py")
    phase1_output = os.path.join(output_path, f"{output_prefix}_phase1.json")
    
    cmd1 = [sys.executable, phase1_script, "--path", target_directory, "--output", phase1_output]
    result1 = subprocess.run(cmd1, capture_output=True, text=True)
    
    if result1.returncode != 0:
        print(f"Error in Phase 1: {result1.stderr}")
        return False
    
    print("Phase 1 completed successfully")
    
    # Phase 2: Intelligent Organization
    print("\nPhase 2: Intelligent Organization")
    print("-" * 40)
    phase2_script = os.path.join(script_base_path, "phase2_intelligent_organization.py")
    phase2_output = os.path.join(output_path, f"{output_prefix}_phase2.json")
    
    cmd2 = [sys.executable, phase2_script, "--input", phase1_output, "--output", phase2_output]
    result2 = subprocess.run(cmd2, capture_output=True, text=True)
    
    if result2.returncode != 0:
        print(f"Error in Phase 2: {result2.stderr}")
        return False
    
    print("Phase 2 completed successfully")
    
    # Phase 3: Advanced Intelligence
    print("\nPhase 3: Advanced Intelligence")
    print("-" * 40)
    phase3_script = os.path.join(script_base_path, "phase3_advanced_intelligence.py")
    phase3_output = os.path.join(output_path, f"{output_prefix}_phase3.json")
    
    cmd3 = [sys.executable, phase3_script, "--input", phase2_output, "--output", phase3_output]
    result3 = subprocess.run(cmd3, capture_output=True, text=True)
    
    if result3.returncode != 0:
        print(f"Error in Phase 3: {result3.stderr}")
        return False
    
    print("Phase 3 completed successfully")
    
    # Summary
    print(f"\n{'='*60}")
    print("🎉 ALL PHASES COMPLETED SUCCESSFULLY!")
    print(f"Directory {target_directory} has been fully indexed:")
    print(f"  - Phase 1: Rapid cataloging")
    print(f"  - Phase 2: Intelligent categorization and tagging")
    print(f"  - Phase 3: Advanced analysis and predictions")
    print(f"  - Output directory: {output_path}")
    print(f"  - Output files: {output_prefix}_phase*.json")
    print("="*60)
    
    return True

def main():
    parser = argparse.ArgumentParser(description="Universal Directory Indexer for AVATARARTS Knowledge Base")
    parser.add_argument("directory", help="Target directory to index")
    parser.add_argument("prefix", nargs="?", default="custom_index", help="Output file prefix")
    parser.add_argument("--output-dir", help="Directory to save output files")
    
    args = parser.parse_args()
    
    directory = args.directory
    prefix = args.prefix

    success = run_tiered_indexing_on_directory(directory, prefix, args.output_dir)

    if success:
        print(f"\nIndexing complete! Results saved with prefix: {prefix}")
        print("The knowledge base has been updated with new entries.")
    else:
        print("\nIndexing failed. Please check the error messages above.")

if __name__ == "__main__":
    main()