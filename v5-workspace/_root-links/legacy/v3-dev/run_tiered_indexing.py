#!/usr/bin/env python3
"""
Master Script for Tiered Indexing System
Runs all three phases of the AVATARARTS Automations Directory indexing
"""

import subprocess
import sys
import os
from datetime import datetime

def run_phase(phase_script, description):
    """Run a single phase of the indexing process"""
    print(f"\n{'='*60}")
    print(f"RUNNING: {description}")
    print(f"{'='*60}")
    
    start_time = datetime.now()
    print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        result = subprocess.run([sys.executable, phase_script], 
                              capture_output=True, text=True, check=True)
        
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

def main():
    print("🚀 AVATARARTS Tiered Indexing System")
    print("="*60)
    print("This system will process the Automations directory in 3 phases:")
    print("  Phase 1: Rapid Initial Scan (simple data points)")
    print("  Phase 2: Intelligent Organization (auto-classification)")
    print("  Phase 3: Advanced Intelligence (predictions & insights)")
    print("="*60)
    
    # Define the phase scripts
    phases = [
        ("phase1_rapid_scan.py", "Phase 1: Rapid Initial Scan"),
        ("phase2_intelligent_organization.py", "Phase 2: Intelligent Organization"),
        ("phase3_advanced_intelligence.py", "Phase 3: Advanced Intelligence")
    ]
    
    # Check if all scripts exist
    base_path = "/Users/steven/AutoTagger/v3-dev/"
    for script, description in phases:
        script_path = os.path.join(base_path, script)
        if not os.path.exists(script_path):
            print(f"❌ Error: Script {script_path} does not exist!")
            return
    
    # Run each phase
    all_successful = True
    for script, description in phases:
        script_path = os.path.join(base_path, script)
        success = run_phase(script_path, description)
        
        if not success:
            print(f"\n❌ {description} failed. Stopping execution.")
            all_successful = False
            break
        else:
            print(f"\n✅ {description} completed successfully.")
    
    # Final summary
    print(f"\n{'='*60}")
    if all_successful:
        print("🎉 ALL PHASES COMPLETED SUCCESSFULLY!")
        print("The AVATARARTS Automations directory has been fully indexed:")
        print("  - Phase 1: Rapid cataloging of all tools")
        print("  - Phase 2: Intelligent categorization and tagging")
        print("  - Phase 3: Advanced analysis and predictions")
        print("\nThe knowledge base now contains comprehensive intelligence")
        print("about all automation tools with predictive insights.")
    else:
        print("❌ Some phases failed. Please check the error messages above.")
    print("="*60)

if __name__ == "__main__":
    main()