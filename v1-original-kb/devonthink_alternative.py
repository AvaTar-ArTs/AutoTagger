#!/usr/bin/env python3
"""
DevonThink Alternative - Enhanced Multi-Format Directory Indexer
Adds DevonThink-like features for non-Mac users
"""

import sys
import os
import json
import csv
import sqlite3
import argparse
from datetime import datetime
from pathlib import Path
import subprocess

def add_devonthink_features_to_index(json_file, db_path):
    """Add DevonThink-like features to the indexed data"""
    print("Adding DevonThink-like features to indexed data...")
    
    # Load the indexed data
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    tools = data.get('automation_tools', [])
    
    # Connect to knowledge base
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Enhance each tool with DevonThink-like features
    for tool in tools:
        name = tool.get('name', '')
        description = tool.get('description', '')
        path = tool.get('path', '')
        
        # Add to knowledge base if not already there
        cursor.execute('''
            SELECT id FROM knowledge_entries WHERE title = ? AND content LIKE ?
        ''', (name, f'%{description[:50]}%'))
        
        existing = cursor.fetchone()
        
        if not existing:
            # Add with enhanced DevonThink-like metadata
            tags = tool.get('auto_generated_tags', [])
            category = tool.get('intelligent_category', 'General')
            
            cursor.execute('''
                INSERT INTO knowledge_entries (title, content, category, tags, source)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                name,
                description,
                category,
                json.dumps(tags),
                f'devonthink_import_{name}'
            ))
    
    conn.commit()
    conn.close()
    print("DevonThink-like features added to knowledge base")

def search_devonthink_style(query, db_path, category_filter=None):
    """Perform DevonThink-style search across indexed content"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    if category_filter:
        cursor.execute('''
            SELECT id, title, content, category, tags, created_at
            FROM knowledge_entries
            WHERE (title LIKE ? OR content LIKE ?)
            AND category = ?
            ORDER BY created_at DESC
        ''', (f'%{query}%', f'%{query}%', category_filter))
    else:
        cursor.execute('''
            SELECT id, title, content, category, tags, created_at
            FROM knowledge_entries
            WHERE title LIKE ? OR content LIKE ?
            ORDER BY created_at DESC
        ''', (f'%{query}%', f'%{query}%'))
    
    results = cursor.fetchall()
    conn.close()
    
    return results

def create_relationship_graph(db_path):
    """Create relationships between indexed items (DevonThink-style)"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Find items with similar tags or categories
    cursor.execute('''
        SELECT id, title, tags, category
        FROM knowledge_entries
        WHERE tags IS NOT NULL AND tags != '[]'
    ''')
    
    items = cursor.fetchall()
    
    relationships = []
    for i, item1 in enumerate(items):
        for j, item2 in enumerate(items[i+1:], i+1):
            # Check for tag overlap
            tags1 = set(json.loads(item1[2]) if item1[2] else [])
            tags2 = set(json.loads(item2[2]) if item2[2] else [])
            common_tags = tags1.intersection(tags2)
            
            # Check for category match
            same_category = item1[3] == item2[3]
            
            if common_tags or same_category:
                relationships.append({
                    'item1_id': item1[0],
                    'item1_title': item1[1],
                    'item2_id': item2[0],
                    'item2_title': item2[1],
                    'common_tags': list(common_tags),
                    'same_category': same_category,
                    'strength': len(common_tags) + (1 if same_category else 0)
                })
    
    conn.close()
    return relationships

def export_relationships_to_csv(relationships, output_file):
    """Export relationships to CSV for visualization"""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['item1_id', 'item1_title', 'item2_id', 'item2_title', 'common_tags', 'same_category', 'strength']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rel in relationships:
            rel['common_tags'] = ', '.join(rel['common_tags'])
            writer.writerow(rel)

def main():
    parser = argparse.ArgumentParser(description='DevonThink Alternative - Enhanced Directory Indexer')
    parser.add_argument('action', choices=['index', 'search', 'relationships', 'annotate'], 
                        help='Action to perform')
    parser.add_argument('--directory', help='Directory to index')
    parser.add_argument('--query', help='Search query')
    parser.add_argument('--output', help='Output file for relationships')
    parser.add_argument('--category', help='Filter by category when searching')
    parser.add_argument('--prefix', default='devonthink_index', help='Output prefix')
    
    args = parser.parse_args()
    
    db_path = os.path.expanduser("~/avatararts-kb/knowledge_base.db")
    
    if args.action == 'index':
        if not args.directory:
            print("Error: --directory is required for index action")
            return
        
        # Run the multi-format indexer
        indexer_script = os.path.expanduser("~/avatararts-kb/multi_format_directory_indexer.py")
        cmd = [sys.executable, indexer_script, args.directory, args.prefix, "json,csv,md"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Add DevonThink-like features
            json_file = os.path.expanduser(f"~/avatararts-kb/{args.prefix}_phase3.json")
            add_devonthink_features_to_index(json_file, db_path)
            print("Directory indexed with DevonThink-like features!")
        else:
            print(f"Indexing failed: {result.stderr}")
    
    elif args.action == 'search':
        if not args.query:
            print("Error: --query is required for search action")
            return
        
        results = search_devonthink_style(args.query, db_path, args.category)
        
        print(f"Found {len(results)} results for query: '{args.query}'")
        if args.category:
            print(f"Category filter: {args.category}")
        
        for result in results[:10]:  # Show top 10
            print(f"\nID: {result[0]}")
            print(f"Title: {result[1]}")
            print(f"Category: {result[3]}")
            print(f"Content preview: {result[2][:200]}...")
            print("-" * 50)
    
    elif args.action == 'relationships':
        relationships = create_relationship_graph(db_path)
        if args.output:
            export_relationships_to_csv(relationships, args.output)
            print(f"Relationships exported to {args.output}")
        else:
            print(f"Found {len(relationships)} relationships between items")
            for rel in relationships[:10]:  # Show top 10
                print(f"{rel['item1_title']} <-> {rel['item2_title']} (strength: {rel['strength']})")
    
    elif args.action == 'annotate':
        print("Annotation feature coming soon - allows adding notes to indexed items")

if __name__ == "__main__":
    main()