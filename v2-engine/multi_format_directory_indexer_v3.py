#!/usr/bin/env python3
"""
Multi-Format Directory Indexer v3 for AVATARARTS Knowledge Base
Can process any directory with the tiered indexing system and output in multiple formats
Also includes import functionality for clean directory scan CSVs
"""

import sys
import os
import json
import csv
import sqlite3
import argparse
from datetime import datetime
import subprocess
from pathlib import Path
import re

def run_tiered_indexing_on_directory(target_directory, output_prefix="custom_index", output_formats=["json"]):
    """Run the complete tiered indexing on a specified directory with multiple output formats"""
    print(f"Starting tiered indexing on: {target_directory}")
    print(f"Output prefix: {output_prefix}")
    print(f"Output formats: {', '.join(output_formats)}")

    # Validate directory exists
    if not os.path.isdir(target_directory):
        print(f"Error: Directory {target_directory} does not exist")
        return False

    # Define the base path for the tagger directory
    base_path = os.path.expanduser("~/.tagger")

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

    # Convert JSON output to other formats if requested
    for fmt in output_formats:
        if fmt != "json":
            convert_json_to_format(phase3_output, output_prefix, fmt)

    # Summary
    print(f"\n{'='*60}")
    print("🎉 ALL PHASES COMPLETED SUCCESSFULLY!")
    print(f"Directory {target_directory} has been fully indexed:")
    print(f"  - Phase 1: Rapid cataloging")
    print(f"  - Phase 2: Intelligent categorization and tagging")
    print(f"  - Phase 3: Advanced analysis and predictions")
    print(f"  - Output files: {output_prefix}_phase*.{{json,csv,md,html}}")
    print("="*60)

    return True

def convert_json_to_format(json_file, output_prefix, format_type):
    """Convert JSON output to specified format"""
    base_path = os.path.expanduser("~/.tagger")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    tools = data.get('automation_tools', [])
    
    if format_type == 'csv':
        csv_file = os.path.join(base_path, f"{output_prefix}_index.csv")
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['name', 'path', 'primary_type', 'size_mb', 'description', 'intelligent_category', 'confidence_score', 'predicted_business_value']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for tool in tools:
                writer.writerow({
                    'name': tool.get('name', ''),
                    'path': tool.get('path', ''),
                    'primary_type': tool.get('primary_type', ''),
                    'size_mb': tool.get('size_mb', 0),
                    'description': tool.get('description', '')[:200],  # Limit description length
                    'intelligent_category': tool.get('intelligent_category', ''),
                    'confidence_score': tool.get('confidence_score', 0),
                    'predicted_business_value': tool.get('predicted_business_value', 0)
                })
        print(f"  - CSV output created: {output_prefix}_index.csv")
    
    elif format_type == 'md':
        md_file = os.path.join(base_path, f"{output_prefix}_index.md")
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f"# Directory Index: {output_prefix}\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Total tools found: {len(tools)}\n\n")
            
            f.write("| Name | Type | Category | Business Value | Description |\n")
            f.write("|------|------|----------|----------------|-------------|\n")
            
            for tool in tools[:50]:  # Limit to first 50 for readability
                name = tool.get('name', '')
                ptype = tool.get('primary_type', '')
                category = tool.get('intelligent_category', '')
                biz_value = f"{tool.get('predicted_business_value', 0):.2f}" if tool.get('predicted_business_value') else "N/A"
                desc = tool.get('description', '')[:100] + "..." if len(tool.get('description', '')) > 100 else tool.get('description', '')
                
                f.write(f"| {name} | {ptype} | {category} | {biz_value}/10 | {desc} |\n")
        print(f"  - Markdown output created: {output_prefix}_index.md")
    
    elif format_type == 'html':
        html_file = os.path.join(base_path, f"{output_prefix}_index.html")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n")
            f.write(f"<title>Directory Index: {output_prefix}</title>\n")
            f.write("<style>\n")
            f.write("body { font-family: Arial, sans-serif; margin: 20px; }\n")
            f.write("table { border-collapse: collapse; width: 100%; }\n")
            f.write("th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }\n")
            f.write("th { background-color: #f2f2f2; }\n")
            f.write("</style>\n")
            f.write("</head>\n<body>\n")
            f.write(f"<h1>Directory Index: {output_prefix}</h1>\n")
            f.write(f"<p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>\n")
            f.write(f"<p>Total tools found: {len(tools)}</p>\n")
            
            f.write("<table>\n")
            f.write("<thead>\n<tr><th>Name</th><th>Type</th><th>Category</th><th>Business Value</th><th>Description</th></tr>\n</thead>\n")
            f.write("<tbody>\n")
            
            for tool in tools[:50]:  # Limit to first 50 for readability
                name = tool.get('name', '')
                ptype = tool.get('primary_type', '')
                category = tool.get('intelligent_category', '')
                biz_value = f"{tool.get('predicted_business_value', 0):.2f}" if tool.get('predicted_business_value') else "N/A"
                desc = tool.get('description', '')[:100] + "..." if len(tool.get('description', '')) > 100 else tool.get('description', '')
                
                f.write(f"<tr><td>{name}</td><td>{ptype}</td><td>{category}</td><td>{biz_value}/10</td><td>{desc}</td></tr>\n")
            
            f.write("</tbody>\n</table>\n")
            f.write("</body>\n</html>")
        print(f"  - HTML output created: {output_prefix}_index.html")

def import_clean_scan_csv(csv_path, db_path=None):
    """Import CSV from clean directory scans into the knowledge base"""
    if db_path is None:
        db_path = os.path.expanduser("~/.tagger/knowledge_base.db")
    
    print(f"Importing CSV data from: {csv_path}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    imported_count = 0
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Determine the type of CSV based on headers
            if 'Duration' in row and 'File Size' in row:
                # Audio CSV
                title = row.get('Filename', 'Unknown')
                content = f"Audio file: {row.get('Duration', 'Unknown duration')}, {row.get('File Size', 'Unknown size')}"
                category = 'Audio/Media'
                tags = ['audio', 'media', 'music', 'mp3', 'wav']
            elif 'Width' in row and 'Height' in row:
                # Image CSV
                title = row.get('Filename', 'Unknown')
                content = f"Image file: {row.get('Width', 'Unknown')}x{row.get('Height', 'Unknown')}, {row.get('File Size', 'Unknown size')}"
                category = 'Images/Media'
                tags = ['image', 'media', 'jpg', 'png', 'graphics']
            elif 'Filename' in row and 'File Size' in row and 'Creation Date' in row:
                # Document CSV
                title = row.get('Filename', 'Unknown')
                content = f"Document file: {row.get('File Size', 'Unknown size')}, {row.get('Creation Date', 'Unknown date')}"
                category = 'Documents'
                tags = ['document', 'file', 'data', 'pdf', 'txt']
            else:
                # General CSV - try to infer from available fields
                title = row.get('Filename', row.get(list(row.keys())[0], 'Unknown')) if row.keys() else 'Unknown'
                content = f"File data: {dict(row)}"
                category = 'General/Media'
                tags = ['file', 'data', 'media']
            
            # Add original path to content
            original_path = row.get('Original Path', row.get('original_path', ''))
            if original_path:
                content += f"\nOriginal path: {original_path}"
            
            # Convert tags to JSON string
            tags_json = json.dumps(tags)
            
            # Insert into knowledge base
            cursor.execute('''
                INSERT INTO knowledge_entries (title, content, category, tags, source)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, content, category, tags_json, f'clean_scan_import_{os.path.basename(csv_path)}'))
            
            imported_count += 1
    
    conn.commit()
    conn.close()
    
    print(f"Successfully imported {imported_count} entries from CSV")
    return imported_count

def import_clean_config_exclusions(config_path, db_path=None):
    """Import exclusion patterns from clean config to enhance filtering"""
    if db_path is None:
        db_path = os.path.expanduser("~/.tagger/knowledge_base.db")
    
    print(f"Importing exclusion patterns from: {config_path}")
    
    # Read the config file to extract exclusion patterns
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract exclusion patterns using regex
    pattern = r'EXCLUDED_PATTERNS\s*=\s*\[(.*?)\]', re.DOTALL
    match = re.search(r'EXCLUDED_PATTERNS\s*=\s*\[(.*?)\]', content, re.DOTALL)
    
    if match:
        patterns_str = match.group(1)
        # Extract individual patterns (lines between brackets)
        lines = patterns_str.split('\n')
        patterns = []
        for line in lines:
            line = line.strip()
            if line.startswith(r"r'") or line.startswith(r'r"') or line.startswith('"') or line.startswith("'"):
                # Extract the pattern from the line
                pattern_match = re.search(r'[rR]?[\'"](.+?)[\'"]', line)
                if pattern_match:
                    pattern = pattern_match.group(1)
                    patterns.append(pattern)
        
        print(f"Found {len(patterns)} exclusion patterns")
        # Could store these in the database for future reference
        return patterns
    else:
        print("Could not find EXCLUDED_PATTERNS in config file")
        return []

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 multi_format_directory_indexer_v3.py <directory> [output_prefix] [formats]")
        print("   OR: python3 multi_format_directory_indexer_v3.py --import-csv <csv_file>")
        print("   OR: python3 multi_format_directory_indexer_v3.py --import-config <config_file>")
        print("Formats: json (default), csv, md, html, or combinations like 'json,csv,md'")
        print("Example: python3 multi_format_directory_indexer_v3.py ~/Pictures pictures_scan json,csv,md")
        print("Example: python3 multi_format_directory_indexer_v3.py --import-csv ~/clean/audio-07-24-15:56.csv")
        print("Example: python3 multi_format_directory_indexer_v3.py --import-config ~/clean/config.py")
        return
    
    if sys.argv[1] == '--import-csv':
        if len(sys.argv) < 3:
            print("Error: CSV file path required for import-csv action")
            return
        
        csv_path = sys.argv[2]
        import_clean_scan_csv(csv_path)
        return
    
    if sys.argv[1] == '--import-config':
        if len(sys.argv) < 3:
            print("Error: Config file path required for import-config action")
            return
        
        config_path = sys.argv[2]
        import_clean_config_exclusions(config_path)
        return
    
    directory = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else "custom_index"
    
    # Parse formats
    if len(sys.argv) > 3:
        formats = sys.argv[3].split(',')
        # Validate formats
        valid_formats = {'json', 'csv', 'md', 'html'}
        formats = [fmt.strip() for fmt in formats if fmt.strip() in valid_formats]
        if not formats:
            formats = ['json']  # Default to json if no valid formats
    else:
        formats = ['json']  # Default to json
    
    success = run_tiered_indexing_on_directory(directory, prefix, formats)
    
    if success:
        print(f"\nIndexing complete! Results saved with prefix: {prefix}")
        print(f"Output formats: {', '.join(formats)}")
        print("The knowledge base has been updated with new entries.")
    else:
        print("\nIndexing failed. Please check the error messages above.")

if __name__ == "__main__":
    main()