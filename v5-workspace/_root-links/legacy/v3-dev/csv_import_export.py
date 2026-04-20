#!/usr/bin/env python3
"""
CSV Import/Export Module for AVATARARTS Knowledge Base
Allows importing from scan functions and exporting to CSV for AirTable/Sheets
"""

import csv
import json
import sqlite3
import os
import argparse
from datetime import datetime

def import_from_csv(csv_path, db_path):
    """Import data from CSV into the knowledge base"""
    print(f"Importing data from CSV: {csv_path}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    imported_count = 0
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Map CSV columns to knowledge base fields
            title = row.get('name', row.get('title', 'Unknown'))
            content = row.get('description', row.get('content', ''))
            category = row.get('category', row.get('type', 'General'))
            tags_str = row.get('tags', row.get('keywords', ''))
            tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()] if tags_str else []
            
            # Convert tags to JSON string
            tags_json = json.dumps(tags) if tags else '[]'
            
            # Insert into knowledge base
            cursor.execute('''
                INSERT INTO knowledge_entries (title, content, category, tags, source)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, content, category, tags_json, 'csv_import'))
            
            imported_count += 1
    
    conn.commit()
    conn.close()
    
    print(f"Successfully imported {imported_count} entries from CSV")
    return imported_count

def export_to_csv(db_path, csv_path, category_filter=None):
    """Export knowledge base data to CSV for AirTable/Sheets"""
    print(f"Exporting data to CSV: {csv_path}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Build query based on category filter
    if category_filter:
        cursor.execute('''
            SELECT id, title, content, category, tags, source, created_at
            FROM knowledge_entries
            WHERE category = ?
            ORDER BY created_at DESC
        ''', (category_filter,))
    else:
        cursor.execute('''
            SELECT id, title, content, category, tags, source, created_at
            FROM knowledge_entries
            ORDER BY created_at DESC
        ''')
    
    rows = cursor.fetchall()
    conn.close()
    
    # Write to CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'content', 'category', 'tags', 'source', 'created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in rows:
            # Parse tags from JSON
            try:
                tags_list = json.loads(row[4]) if row[4] else []
                tags_str = ', '.join(tags_list) if tags_list else ''
            except:
                tags_str = row[4] if row[4] else ''
            
            writer.writerow({
                'id': row[0],
                'title': row[1],
                'content': row[2],
                'category': row[3],
                'tags': tags_str,
                'source': row[5],
                'created_at': row[6]
            })
    
    print(f"Successfully exported {len(rows)} entries to CSV")
    return len(rows)

def create_sample_scan_csv():
    """Create a sample CSV that matches the expected format from scan functions"""
    sample_data = [
        {
            'name': 'notebooklm-categorizer-main',
            'path': '/Users/steven/AVATARARTS/Automations/notebooklm-categorizer-main',
            'type': 'browser-extension',
            'size_mb': '2.5',
            'description': 'Browser extension that adds smart category filter buttons to NotebookLM',
            'tags': 'notebooklm, categorization, browser-extension, automation',
            'created': '2024-01-15',
            'modified': '2024-01-15'
        },
        {
            'name': 'tiny-openai-whisper-api-main',
            'path': '/Users/steven/AVATARARTS/Automations/tiny-openai-whisper-api-main',
            'type': 'api-server',
            'size_mb': '3.2',
            'description': 'OpenAI Whisper API-style local server running on FastAPI',
            'tags': 'whisper, api, fastapi, speech-to-text, openai',
            'created': '2024-01-10',
            'modified': '2024-01-12'
        },
        {
            'name': 'ComicBook-AI-main',
            'path': '/Users/steven/AVATARARTS/Automations/ComicBook-AI-main',
            'type': 'web-application',
            'size_mb': '15.7',
            'description': 'React-Vite app to generate custom images for comic book strips using OpenAI DALL-E',
            'tags': 'comic, ai, image-generation, react, openai, dalle',
            'created': '2024-01-08',
            'modified': '2024-01-09'
        }
    ]
    
    csv_path = os.path.expanduser('~/AutoTagger/v3-dev/sample_scan_data.csv')
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'path', 'type', 'size_mb', 'description', 'tags', 'created', 'modified']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in sample_data:
            writer.writerow(row)
    
    print(f"Sample scan CSV created: {csv_path}")
    print("This format matches what a scan function would typically output")
    return csv_path

def main():
    parser = argparse.ArgumentParser(description='CSV Import/Export for AVATARARTS Knowledge Base')
    parser.add_argument('action', choices=['import', 'export', 'sample'], 
                        help='Action to perform: import from CSV, export to CSV, or create sample')
    parser.add_argument('--csv-path', help='Path to the CSV file')
    parser.add_argument('--db-path', default='~/AutoTagger/v3-dev/knowledge_base.db', 
                        help='Path to the SQLite database')
    parser.add_argument('--category', help='Filter by category when exporting')
    
    args = parser.parse_args()
    
    # Expand user paths
    db_path = os.path.expanduser(args.db_path)
    
    if args.action == 'import':
        if not args.csv_path:
            print("Error: --csv-path is required for import action")
            return
        csv_path = os.path.expanduser(args.csv_path)
        import_from_csv(csv_path, db_path)
        
    elif args.action == 'export':
        if not args.csv_path:
            print("Error: --csv-path is required for export action")
            return
        csv_path = os.path.expanduser(args.csv_path)
        export_to_csv(db_path, csv_path, args.category)
        
    elif args.action == 'sample':
        create_sample_scan_csv()

if __name__ == "__main__":
    main()