#!/usr/bin/env python3
"""
Phase 2: Intelligent Organization (Compat)
Lightweight categorization to keep pipeline functional.
"""

import json
import argparse
from datetime import datetime


EXTENSION_CATEGORIES = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".sh": "shell",
    ".zsh": "shell",
    ".md": "documentation",
    ".txt": "text",
    ".json": "data",
    ".yaml": "data",
    ".yml": "data",
    ".csv": "data",
    ".html": "web",
    ".css": "web",
}


def categorize_file(file_info):
    ext = (file_info.get("extension") or "").lower()
    category = EXTENSION_CATEGORIES.get(ext, "other")
    return category


def main():
    parser = argparse.ArgumentParser(description="Phase 2: Intelligent Organization (Compat)")
    parser.add_argument("--input", required=True, help="Input JSON from Phase 1")
    parser.add_argument("--output", required=True, help="Output JSON file path")

    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    files = data.get("files", [])
    automation_tools = []

    for item in files:
        category = categorize_file(item)
        tool_entry = {
            "name": item.get("name", ""),
            "path": item.get("path", ""),
            "size_mb": round(float(item.get("size", 0)) / (1024 * 1024), 4),
            "created": item.get("created", ""),
            "modified": item.get("modified", ""),
            "primary_type": item.get("mime_type", "unknown"),
            "description": "Auto-categorized by file extension",
            "intelligent_category": category,
            "confidence_score": 0.4 if category == "other" else 0.7,
        }
        automation_tools.append(tool_entry)

    phase2 = {
        "phase": "phase2_intelligent_organization",
        "generated_at": datetime.now().isoformat(),
        "automation_tools": automation_tools,
        "source_scan": data.get("scan_info", {}),
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(phase2, f, indent=2, ensure_ascii=False)

    print("Phase 2 complete. Output saved to: {0}".format(args.output))


if __name__ == "__main__":
    main()
