#!/usr/bin/env python3
"""
Legacy compatibility script for run_tiered_indexing.py
This is a thin wrapper that calls the new autotag_main.py for backward compatibility.
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = "/Users/steven/pythons"  # default for tests

    print("Running legacy tiered indexing via new AutoTag system...")
    print(f"Target: {target_dir}")

    # Call the main AutoTag script
    repo_root = Path(__file__).parent.parent
    main_script = repo_root / "scripts" / "autotag_main.py"

    cmd = [sys.executable, str(main_script), "--target", target_dir, "--name", "legacy_compat_test"]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        print("✅ Legacy compatibility test completed successfully via new pipeline.")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(e.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
