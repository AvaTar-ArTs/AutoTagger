#!/usr/bin/env python3
"""
Multi-Format Directory Indexer v4 for AVATARARTS Knowledge Base
Enhanced with AVATARARTS ecosystem awareness and intelligent activation capabilities
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
import hashlib

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

def import_avatararts_ecosystem_data(db_path=None):
    """Import AVATARARTS ecosystem data for intelligent activation"""
    if db_path is None:
        db_path = os.path.expanduser("~/.tagger/knowledge_base.db")
    
    print("Importing AVATARARTS ecosystem data for intelligent activation...")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Import AVATARARTS ecosystem status information
    avatararts_status = {
        'properties': [
            {
                'name': 'HeavenlyHands Cleaning Service',
                'status': '70-80% complete',
                'revenue': '$0 (in development)',
                'category': 'In Development',
                'potential': '$20-40K/month when launched'
            },
            {
                'name': 'AvatarArts.org Ecosystem',
                'status': '75-85% complete',
                'revenue': '$0 (ready to activate)',
                'category': 'Ready to Launch',
                'potential': '$20-50K/month'
            },
            {
                'name': 'Creative AI Marketplace',
                'status': '60-70% complete',
                'revenue': '$0 (ready to activate)',
                'category': 'Ready to Launch',
                'potential': '$30-75K/month'
            },
            {
                'name': 'Creative AI Education Platform',
                'status': '60-70% complete',
                'revenue': '$0 (ready to activate)',
                'category': 'Ready to Launch',
                'potential': '$25-50K/month'
            },
            {
                'name': 'Retention & Return Visit Suite',
                'status': '50-60% complete',
                'revenue': '$0 (ready to activate)',
                'category': 'Ready to Launch',
                'potential': '$50-150K/month'
            },
            {
                'name': 'Automation Empire',
                'status': '60-70% complete',
                'revenue': '$10-25K/month (partial)',
                'category': 'In Development',
                'potential': '$15-40K/month'
            },
            {
                'name': 'Passive Income Empire',
                'status': '50-60% complete',
                'revenue': '$15-30K/month (partial)',
                'category': 'In Development',
                'potential': '$25-50K/month'
            }
        ],
        'total_potential': '$160-425K/month ($1.9M-$5.1M annually)',
        'activation_strategy': 'Hybrid approach: Activate properties while building social presence',
        'priority_order': [
            'Quick wins (AvatarArts payments)',
            'Medium effort (Marketplace + Education)',
            'Scaling (Retention Suite)'
        ]
    }
    
    # Add ecosystem status to knowledge base
    for prop in avatararts_status['properties']:
        title = f"AVATARARTS Property: {prop['name']}"
        content = f"Status: {prop['status']}\nRevenue: {prop['revenue']}\nPotential: {prop['potential']}\nCategory: {prop['category']}"
        category = prop['category']
        tags = ['avatararts', 'ecosystem', 'revenue', 'automation', 'business']
        
        tags_json = json.dumps(tags)
        
        cursor.execute('''
            INSERT OR REPLACE INTO knowledge_entries (title, content, category, tags, source)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, content, category, tags_json, 'avatararts_ecosystem_import'))
    
    # Add overall ecosystem summary
    cursor.execute('''
        INSERT OR REPLACE INTO knowledge_entries (title, content, category, tags, source)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        'AVATARARTS Ecosystem Summary',
        f"Total potential: {avatararts_status['total_potential']}\nActivation strategy: {avatararts_status['activation_strategy']}",
        'Business Strategy',
        json.dumps(['avatararts', 'ecosystem', 'strategy', 'revenue', 'activation']),
        'avatararts_ecosystem_import'
    ))
    
    conn.commit()
    conn.close()
    
    print(f"Successfully imported AVATARARTS ecosystem data with {len(avatararts_status['properties']) + 1} entries")
    return len(avatararts_status['properties']) + 1

def analyze_avatararts_activation_opportunities(db_path=None):
    """Analyze AVATARARTS ecosystem for activation opportunities"""
    if db_path is None:
        db_path = os.path.expanduser("~/.tagger/knowledge_base.db")
    
    print("Analyzing AVATARARTS ecosystem for activation opportunities...")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Find all AVATARARTS related entries
    cursor.execute('''
        SELECT title, content, category
        FROM knowledge_entries
        WHERE title LIKE '%AVATARARTS%' OR content LIKE '%AVATARARTS%'
        OR title LIKE '%HeavenlyHands%' OR content LIKE '%HeavenlyHands%'
        OR title LIKE '%AvatarArts%' OR content LIKE '%AvatarArts%'
    ''')
    
    results = cursor.fetchall()
    conn.close()
    
    print(f"Found {len(results)} AVATARARTS-related entries in knowledge base")
    
    # Analyze for activation opportunities
    activation_opportunities = []
    for result in results:
        title, content, category = result
        if 'ready to activate' in content.lower() or 'ready to launch' in content.lower():
            activation_opportunities.append({
                'title': title,
                'content': content,
                'category': category
            })
    
    if activation_opportunities:
        print(f"\n🔍 IDENTIFIED ACTIVATION OPPORTUNITIES ({len(activation_opportunities)}):")
        for opp in activation_opportunities:
            print(f"  • {opp['title']}")
            print(f"    Category: {opp['category']}")
            # Extract potential revenue from content
            revenue_match = re.search(r'\$[\d,]+K/month', opp['content'])
            if revenue_match:
                print(f"    Potential: {revenue_match.group()}")
            print()
    
    return activation_opportunities

def generate_avatararts_activation_plan(db_path=None):
    """Generate an activation plan based on AVATARARTS ecosystem analysis"""
    if db_path is None:
        db_path = os.path.expanduser("~/.tagger/knowledge_base.db")
    
    print("Generating AVATARARTS activation plan...")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all entries related to activation opportunities
    cursor.execute('''
        SELECT title, content, category
        FROM knowledge_entries
        WHERE (title LIKE '%AVATARARTS%' OR content LIKE '%AVATARARTS%')
        AND (content LIKE '%ready to activate%' OR content LIKE '%ready to launch%' OR content LIKE '%activate payments%')
    ''')
    
    results = cursor.fetchall()
    conn.close()
    
    # Generate activation plan
    activation_plan = {
        'executive_summary': 'AVATARARTS Ecosystem Activation Plan',
        'total_properties': len(results),
        'total_potential_revenue': '$180-465K/month',
        'priority_actions': [],
        'timeline': {
            'week_1': 'Quick wins - enable payments on ready properties',
            'week_2_3': 'Launch marketplace and education platforms',
            'week_4_6': 'Complete retention suite and scale automation',
            'month_2_plus': 'Optimize and scale all properties'
        }
    }
    
    for result in results:
        title, content, category = result
        if 'ready to activate' in content.lower() or 'ready to launch' in content.lower():
            # Extract potential revenue
            revenue_match = re.search(r'\$[\d,]+K/month', content)
            revenue = revenue_match.group() if revenue_match else 'Unknown'
            
            activation_plan['priority_actions'].append({
                'property': title,
                'category': category,
                'potential_revenue': revenue,
                'estimated_effort': '1-3 weeks' if 'activate' in content.lower() else '2-4 weeks'
            })
    
    # Save activation plan to knowledge base
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO knowledge_entries (title, content, category, tags, source)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        'AVATARARTS Activation Plan',
        json.dumps(activation_plan, indent=2),
        'Business Strategy',
        json.dumps(['avatararts', 'activation', 'plan', 'revenue', 'strategy']),
        'avatararts_activation_plan'
    ))
    
    conn.commit()
    conn.close()
    
    print(f"Activation plan generated with {len(activation_plan['priority_actions'])} priority actions")
    print("Plan saved to knowledge base")
    
    return activation_plan

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 multi_format_directory_indexer_v4.py <directory> [output_prefix] [formats]")
        print("   OR: python3 multi_format_directory_indexer_v4.py --import-csv <csv_file>")
        print("   OR: python3 multi_format_directory_indexer_v4.py --import-ecosystem")
        print("   OR: python3 multi_format_directory_indexer_v4.py --analyze-opportunities")
        print("   OR: python3 multi_format_directory_indexer_v4.py --generate-plan")
        print("Formats: json (default), csv, md, html, or combinations like 'json,csv,md'")
        print("Example: python3 multi_format_directory_indexer_v4.py ~/Pictures pictures_scan json,csv,md")
        print("Example: python3 multi_format_directory_indexer_v4.py --import-csv ~/clean/audio-07-24-15:56.csv")
        print("Example: python3 multi_format_directory_indexer_v4.py --import-ecosystem")
        print("Example: python3 multi_format_directory_indexer_v4.py --analyze-opportunities")
        print("Example: python3 multi_format_directory_indexer_v4.py --generate-plan")
        return
    
    if sys.argv[1] == '--import-csv':
        if len(sys.argv) < 3:
            print("Error: CSV file path required for import-csv action")
            return
        
        csv_path = sys.argv[2]
        import_clean_scan_csv(csv_path)
        return
    
    if sys.argv[1] == '--import-ecosystem':
        import_avatararts_ecosystem_data()
        return
    
    if sys.argv[1] == '--analyze-opportunities':
        analyze_avatararts_activation_opportunities()
        return
    
    if sys.argv[1] == '--generate-plan':
        generate_avatararts_activation_plan()
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
        
        # Check if this is an AVATARARTS directory and suggest analysis
        if 'avatararts' in directory.lower():
            print("\n💡 TIP: This appears to be an AVATARARTS directory!")
            print("   Consider running: python3 multi_format_directory_indexer_v4.py --analyze-opportunities")
            print("   Or: python3 multi_format_directory_indexer_v4.py --generate-plan")
    else:
        print("\nIndexing failed. Please check the error messages above.")

if __name__ == "__main__":
    main()