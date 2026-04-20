#!/usr/bin/env python3
"""
Phase 1: Rapid Initial Scan (Compat)
Add-only wrapper to fix syntax error and keep original intact.
"""

import os
import sys
import json
import argparse
from datetime import datetime
import mimetypes


def scan_directory(path):
    """Scan directory and collect basic file information"""
    results = {
        "scan_info": {
            "target_path": path,
            "scan_started": datetime.now().isoformat(),
            "total_files": 0,
            "total_size": 0,
        },
        "files": [],
    }

    total_files = 0
    total_size = 0

    for root, dirs, files in os.walk(path):
        # Skip hidden directories and common system directories
        dirs[:] = [
            d
            for d in dirs
            if not d.startswith(".")
            and d not in ["__pycache__", ".git", "node_modules", "venv", ".venv"]
        ]

        for file in files:
            file_path = os.path.join(root, file)

            try:
                stat = os.stat(file_path)
                mime_type, _ = mimetypes.guess_type(file_path)

                file_info = {
                    "name": file,
                    "path": file_path,
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "created": datetime.fromtimestamp(stat.st_ctime).isoformat()
                    if hasattr(stat, "st_birthtime")
                    else datetime.fromtimestamp(stat.st_ctime).isoformat(),
                    "mime_type": mime_type or "unknown",
                    "extension": os.path.splitext(file)[1],
                    "directory": root,
                }

                results["files"].append(file_info)
                total_files += 1
                total_size += stat.st_size

            except (OSError, IOError) as e:
                print("Error accessing file {0}: {1}".format(file_path, str(e)), file=sys.stderr)
                continue

    results["scan_info"]["total_files"] = total_files
    results["scan_info"]["total_size"] = total_size
    results["scan_info"]["scan_completed"] = datetime.now().isoformat()

    return results


def main():
    parser = argparse.ArgumentParser(description="Phase 1: Rapid Initial Scan (Compat)")
    parser.add_argument("--path", required=True, help="Path to scan")
    parser.add_argument("--output", required=True, help="Output JSON file path")

    args = parser.parse_args()

    print("Starting rapid scan of: {0}".format(args.path))

    results = scan_directory(args.path)

    # Write results to output file
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("Scan completed. Results saved to: {0}".format(args.output))
    print(
        "Found {0} files, total size: {1} bytes".format(
            results["scan_info"]["total_files"], results["scan_info"]["total_size"]
        )
    )


if __name__ == "__main__":
    main()
