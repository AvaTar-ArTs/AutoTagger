#!/usr/bin/env python3
"""
Phase 1: Rapid Initial Scan
This script performs a rapid scan of the target directory to catalog all files.
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
            "total_size": 0
        },
        "files": []
    }

    total_files = 0
    total_size = 0

    for root, dirs, files in os.walk(path):
        # Skip hidden directories and common system directories
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ["__pycache__", ".git", "node_modules", "venv", ".venv"]]
        
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
                    "created": datetime.fromtimestamp(stat.st_ctime).isoformat() if hasattr(stat, "st_birthtime") else datetime.fromtimestamp(stat.st_ctime).isoformat(),
                    "mime_type": mime_type or "unknown",
                    "extension": os.path.splitext(file)[1],
                    "directory": root
                }
                
                results["files"].append(file_info)
                total_files += 1
                total_size += stat.st_size
                
            except (OSError, IOError) as e:
                print(f"Error accessing file {file_path}: {str(e)}", file=sys.stderr)
                continue

    results["scan_info"]["total_files"] = total_files
    results["scan_info"]["total_size"] = total_size
    results["scan_info"]["scan_completed"] = datetime.now().isoformat()

    return results

def main():
    parser = argparse.ArgumentParser(description="Phase 1: Rapid Initial Scan")
    parser.add_argument("--path", required=True, help="Path to scan")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    
    args = parser.parse_args()
    
    print(f"Starting rapid scan of: {args.path}")
    
    results = scan_directory(args.path)
    
    # Write results to output file
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"Scan completed. Results saved to: {args.output}")
    print(
        f"Found {results['scan_info']['total_files']} files, total size: {results['scan_info']['total_size']} bytes"
    )

if __name__ == "__main__":
    main()
