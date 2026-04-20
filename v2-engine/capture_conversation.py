#!/usr/bin/env python3
"""
Conversation Capture and Knowledge Base Integration Tool
This script captures conversation data and saves it to the AVATARARTS knowledge database
"""

import sqlite3
import json
import os
import sys
from datetime import datetime
import argparse
import re

def create_database(db_path):
    """Create the knowledge base database with appropriate tables"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table for knowledge entries
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT,
            tags TEXT,
            source TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create table for analysis results
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_id INTEGER,
            analysis_type TEXT,
            analysis_data TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (entry_id) REFERENCES knowledge_entries (id)
        )
    ''')
    
    # Create table for conversation logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            role TEXT,
            content TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create table for extracted insights
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_id INTEGER,
            insight_type TEXT,
            insight_data TEXT,
            confidence_score REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (entry_id) REFERENCES knowledge_entries (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def extract_title_from_content(content):
    """Extract a title from content if none is provided"""
    # Look for the first heading or first sentence
    lines = content.split('\n')
    for line in lines:
        # Check for markdown heading
        if line.strip().startswith('#'):
            title = line.strip('# ')
            return title[:100]  # Limit title length
    
    # If no heading found, use first sentence
    sentences = re.split(r'[.!?]+', content.strip())
    if sentences and sentences[0]:
        title = sentences[0].strip()
        return title[:100]  # Limit title length
    
    # Fallback to first 50 characters
    return content[:50].strip() + "..."

def save_knowledge_entry(db_path, title, content, category=None, tags=None, source="manual"):
    """Save a knowledge entry to the database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Convert tags to JSON string if provided
    tags_json = json.dumps(tags) if tags else None
    
    cursor.execute('''
        INSERT INTO knowledge_entries (title, content, category, tags, source)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, content, category, tags_json, source))
    
    entry_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return entry_id

def extract_insights(content):
    """Extract key insights from the content"""
    insights = []
    
    # Look for key sections in the content
    sections = {
        'Executive Summary': re.search(r'##?\s*Executive Summary(.*?)##?', content, re.DOTALL | re.IGNORECASE),
        'Analysis': re.search(r'##?\s*(AEO|SEO|GEO).*?Analysis(.*?)##?', content, re.DOTALL | re.IGNORECASE),
        'Recommendations': re.search(r'##?\s*Recommendations(.*?)##?', content, re.DOTALL | re.IGNORECASE),
        'Key Metrics': re.search(r'##?\s*Success Metrics|KPIs(.*?)##?', content, re.DOTALL | re.IGNORECASE),
        'Implementation': re.search(r'##?\s*Implementation(.*?)##?', content, re.DOTALL | re.IGNORECASE),
    }
    
    for insight_type, match in sections.items():
        if match:
            insight_text = match.group(1).strip()[:500]  # Limit length
            insights.append({
                'type': insight_type,
                'data': insight_text,
                'confidence': 0.8
            })
    
    return insights

def save_insights(db_path, entry_id, insights):
    """Save extracted insights to the database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    for insight in insights:
        cursor.execute('''
            INSERT INTO insights (entry_id, insight_type, insight_data, confidence_score)
            VALUES (?, ?, ?, ?)
        ''', (entry_id, insight['type'], json.dumps(insight['data']), insight['confidence']))
    
    conn.commit()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Capture and save conversation data to knowledge base')
    parser.add_argument('--db-path', default=os.path.expanduser('~/AutoTagger/v2-engine/knowledge_base.db'),
                        help='Path to the SQLite database')
    parser.add_argument('--title', help='Title of the knowledge entry (will be auto-generated if not provided)')
    parser.add_argument('--content', help='Content of the knowledge entry (reads from stdin if not provided)')
    parser.add_argument('--category', default='conversation', help='Category of the knowledge entry')
    parser.add_argument('--tags', nargs='+', help='Tags for the knowledge entry')
    parser.add_argument('--source', default='conversation_capture', help='Source identifier')
    parser.add_argument('--action', choices=['save', 'search', 'capture'], default='save', 
                        help='Action to perform')
    parser.add_argument('--query', help='Search query (used with search action)')
    
    args = parser.parse_args()
    
    # Ensure the database directory exists
    db_dir = os.path.dirname(args.db_path)
    os.makedirs(db_dir, exist_ok=True)
    
    # Create database if it doesn't exist
    create_database(args.db_path)
    
    if args.action == 'save' or args.action == 'capture':
        # Get content from stdin if not provided
        if not args.content:
            print("Enter content (press Ctrl+D when finished):")
            content = sys.stdin.read()
        else:
            content = args.content
        
        # Generate title if not provided
        if not args.title:
            title = extract_title_from_content(content)
        else:
            title = args.title
        
        # Save the knowledge entry
        entry_id = save_knowledge_entry(
            args.db_path, 
            title, 
            content, 
            args.category, 
            args.tags,
            args.source
        )
        
        # Extract and save insights
        insights = extract_insights(content)
        if insights:
            save_insights(args.db_path, entry_id, insights)
        
        print(f"Knowledge entry saved with ID: {entry_id}")
        print(f"Title: {title}")
        print(f"Category: {args.category}")
        print(f"Insights extracted: {len(insights)}")
        
    elif args.action == 'search':
        if not args.query:
            print("Error: --query is required for search action")
            return
            
        conn = sqlite3.connect(args.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, content, category, tags, created_at
            FROM knowledge_entries
            WHERE title LIKE ? OR content LIKE ?
            ORDER BY created_at DESC
        ''', (f'%{args.query}%', f'%{args.query}%'))
        
        results = cursor.fetchall()
        conn.close()
        
        print(f"Found {len(results)} results:")
        for result in results:
            print(f"\nID: {result[0]}")
            print(f"Title: {result[1]}")
            print(f"Category: {result[3]}")
            print(f"Created: {result[5]}")
            print(f"Content preview: {result[2][:200]}...")
            print("-" * 50)

if __name__ == "__main__":
    main()