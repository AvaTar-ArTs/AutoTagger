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

def run_tiered_indexing_on_directory(target_directory, output_prefix="custom_index"):
    """Run the complete tiered indexing on a specified directory"""
    print(f"Starting tiered indexing on: {target_directory}")
    print(f"Output prefix: {output_prefix}")
    
    # Validate directory exists
    if not os.path.isdir(target_directory):
        print(f"Error: Directory {target_directory} does not exist")
        return False
    
    # Define the base path for the avatararts-kb directory
    base_path = os.path.expanduser("~/avatararts-kb")
    
    # Phase 1: Rapid Initial Scan
    print("\nPhase 1: Rapid Initial Scan")
    print("-" * 40)
    phase1_script = os.path.join(base_path, "phase1_rapid_scan.py")
    phase1_output = os.path.join(base_path, f"{output_prefix}_phase1.json")
    
    cmd1 = [sys.executable, phase1_script, "--path", target_directory, "--output", phase1_output]
    result1 = subprocess.run(cmd1, capture_output=True, text=True)
    
    if result1.returncode != 0:
        print(f"Error in Phase 1: {result1.stderr}")
        return False
    
    print("Phase 1 completed successfully")
    
    # Phase 2: Intelligent Organization
    print("\nPhase 2: Intelligent Organization")
    print("-" * 40)
    phase2_script = os.path.join(base_path, "phase2_intelligent_organization.py")
    phase2_output = os.path.join(base_path, f"{output_prefix}_phase2.json")
    
    cmd2 = [sys.executable, phase2_script, "--input", phase1_output, "--output", phase2_output]
    result2 = subprocess.run(cmd2, capture_output=True, text=True)
    
    if result2.returncode != 0:
        print(f"Error in Phase 2: {result2.stderr}")
        return False
    
    print("Phase 2 completed successfully")
    
    # Phase 3: Advanced Intelligence
    print("\nPhase 3: Advanced Intelligence")
    print("-" * 40)
    phase3_script = os.path.join(base_path, "phase3_advanced_intelligence.py")
    phase3_output = os.path.join(base_path, f"{output_prefix}_phase3.json")
    
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
    print(f"  - Output files: {output_prefix}_phase*.json")
    print("="*60)
    
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 universal_directory_indexer.py <directory> [output_prefix]")
        print("Example: python3 universal_directory_indexer.py ~/Pictures pictures_scan")
        return

    directory = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else "custom_index"

    success = run_tiered_indexing_on_directory(directory, prefix)

    if success:
        print(f"\nIndexing complete! Results saved with prefix: {prefix}")
        print("The knowledge base has been updated with new entries.")
    else:
        print("\nIndexing failed. Please check the error messages above.")

if __name__ == "__main__":
    main()