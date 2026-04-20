#!/usr/bin/env python3
"""
Quick Action Script to Save Knowledge Base Information to Database
This script captures conversation data and saves it to a SQLite database
"""

import sqlite3
import json
import os
from datetime import datetime
import argparse

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
    
    conn.commit()
    conn.close()

def save_knowledge_entry(db_path, title, content, category=None, tags=None):
    """Save a knowledge entry to the database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Convert tags to JSON string if provided
    tags_json = json.dumps(tags) if tags else None
    
    cursor.execute('''
        INSERT INTO knowledge_entries (title, content, category, tags)
        VALUES (?, ?, ?, ?)
    ''', (title, content, category, tags_json))
    
    entry_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return entry_id

def save_analysis_result(db_path, entry_id, analysis_type, analysis_data):
    """Save an analysis result linked to a knowledge entry"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO analysis_results (entry_id, analysis_type, analysis_data)
        VALUES (?, ?, ?)
    ''', (entry_id, analysis_type, json.dumps(analysis_data)))
    
    result_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return result_id

def save_conversation_log(db_path, session_id, role, content):
    """Save a conversation log entry"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO conversation_logs (session_id, role, content)
        VALUES (?, ?, ?)
    ''', (session_id, role, content))
    
    log_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return log_id

def search_knowledge(db_path, query, category=None):
    """Search for knowledge entries"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    if category:
        cursor.execute('''
            SELECT id, title, content, category, tags, created_at
            FROM knowledge_entries
            WHERE (title LIKE ? OR content LIKE ?) AND category = ?
            ORDER BY created_at DESC
        ''', (f'%{query}%', f'%{query}%', category))
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

def main():
    parser = argparse.ArgumentParser(description='Save knowledge base information to database')
    parser.add_argument('--db-path', default=os.path.expanduser('~/avatararts-kb/knowledge_base.db'),
                        help='Path to the SQLite database')
    parser.add_argument('--action', choices=['save', 'search'], default='save',
                        help='Action to perform')
    parser.add_argument('--title', help='Title of the knowledge entry (required for save action)')
    parser.add_argument('--content', help='Content of the knowledge entry (required for save action)')
    parser.add_argument('--category', help='Category of the knowledge entry')
    parser.add_argument('--tags', nargs='+', help='Tags for the knowledge entry')
    parser.add_argument('--query', help='Search query (used with search action)')
    
    args = parser.parse_args()

    # Validate required arguments based on action
    if args.action == 'save':
        if not args.title or not args.content:
            print("Error: --title and --content are required for save action")
            return

    if args.action == 'search':
        if not args.query:
            print("Error: --query is required for search action")
            return

    # Ensure the database directory exists
    db_dir = os.path.dirname(args.db_path)
    os.makedirs(db_dir, exist_ok=True)

    # Create database if it doesn't exist
    create_database(args.db_path)

    if args.action == 'save':
        entry_id = save_knowledge_entry(
            args.db_path,
            args.title,
            args.content,
            args.category,
            args.tags
        )
        print(f"Knowledge entry saved with ID: {entry_id}")

    elif args.action == 'search':
        results = search_knowledge(args.db_path, args.query, args.category)
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