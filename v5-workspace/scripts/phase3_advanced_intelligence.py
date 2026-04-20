#!/usr/bin/env python3
"""
Phase 3: Advanced Intelligence (Compat)
Adds lightweight business value and integration potential.
"""

import json
import argparse
from datetime import datetime


CATEGORY_VALUE = {
    "python": 7.0,
    "javascript": 6.0,
    "typescript": 6.5,
    "shell": 5.5,
    "data": 6.5,
    "web": 5.0,
    "documentation": 4.0,
    "text": 3.5,
    "other": 3.0,
}


def score_tool(tool):
    category = tool.get("intelligent_category", "other")
    base = CATEGORY_VALUE.get(category, 3.0)
    size_mb = float(tool.get("size_mb", 0) or 0)
    bonus = 0.5 if size_mb > 1 else 0.0
    return round(base + bonus, 2)


def main():
    parser = argparse.ArgumentParser(description="Phase 3: Advanced Intelligence (Compat)")
    parser.add_argument("--input", required=True, help="Input JSON from Phase 2")
    parser.add_argument("--output", required=True, help="Output JSON file path")

    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    tools = data.get("automation_tools", [])
    enriched = []

    for tool in tools:
        score = score_tool(tool)
        tool["predicted_business_value"] = score
        tool["integration_potential"] = {
            "has_potential": score >= 6.0,
            "reason": "score_threshold",
        }
        enriched.append(tool)

    phase3 = {
        "phase": "phase3_advanced_intelligence",
        "generated_at": datetime.now().isoformat(),
        "automation_tools": enriched,
        "source_phase2": data.get("phase", "phase2_intelligent_organization"),
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(phase3, f, indent=2, ensure_ascii=False)

    print("Phase 3 complete. Output saved to: {0}".format(args.output))


if __name__ == "__main__":
    main()
