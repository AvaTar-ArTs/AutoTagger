#!/usr/bin/env python3
"""
Enhanced Knowledge Base Capture Tool
This script captures formatted content from clipboard, analyzes it, and saves to the database
with auto-generated tags and formatting preserved.
"""

import sqlite3
import json
import os
import re
import sys
from datetime import datetime
import argparse
import subprocess
import markdown
from bs4 import BeautifulSoup

def get_clipboard_content():
    """Get content from clipboard (macOS specific)"""
    try:
        # On macOS, use pbpaste to get clipboard content
        result = subprocess.run(['pbpaste'], capture_output=True, text=True)
        return result.stdout
    except FileNotFoundError:
        print("Clipboard access not available on this system")
        return None

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

def analyze_content_for_tags(content):
    """Analyze content to generate relevant tags"""
    tags = set()
    
    # Convert markdown/html to plain text for analysis
    try:
        # Try to parse as HTML first
        soup = BeautifulSoup(content, 'html.parser')
        plain_text = soup.get_text()
    except:
        plain_text = content
    
    # Common technical terms that could become tags
    tech_terms = [
        'AEO', 'SEO', 'GEO', 'analytics', 'optimization', 'automation', 
        'AI', 'machine learning', 'python', 'database', 'API', 'framework',
        'content-awareness', 'intelligence', 'trend', 'strategy', 'revenue',
        'marketing', 'digital', 'platform', 'script', 'tool', 'system'
    ]
    
    # Look for technical terms in content
    content_lower = plain_text.lower()
    for term in tech_terms:
        if term.lower() in content_lower:
            tags.add(term.lower())
    
    # Extract any hashtags if present
    hashtag_pattern = r'#(\w+)'
    hashtags = re.findall(hashtag_pattern, plain_text)
    for tag in hashtags:
        tags.add(tag.lower())
    
    # Extract capitalized words/phrases that might be important
    caps_pattern = r'\b[A-Z]{2,}\b'  # Standalone uppercase words
    caps_words = re.findall(caps_pattern, plain_text)
    for word in caps_words:
        if len(word) > 2:  # Avoid short acronyms
            tags.add(word.lower())
    
    # Extract potential categories based on content
    if any(word in content_lower for word in ['analysis', 'research', 'study']):
        tags.add('analysis')
    if any(word in content_lower for word in ['tutorial', 'guide', 'how-to', 'instructions']):
        tags.add('tutorial')
    if any(word in content_lower for word in ['code', 'script', 'programming', 'development']):
        tags.add('code')
    if any(word in content_lower for word in ['revenue', 'business', 'monetization', 'sales']):
        tags.add('revenue')
    
    return list(tags)[:10]  # Limit to 10 tags

def save_knowledge_entry(db_path, title, content, category=None, tags=None, source="clipboard_capture"):
    """Save a knowledge entry to the database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Convert tags to JSON string if provided
    tags_json = json.dumps(tags) if tags else json.dumps([])
    
    # Determine category if not provided
    if not category:
        content_lower = content.lower()
        if 'seo' in content_lower or 'search' in content_lower:
            category = 'SEO/AEO'
        elif 'code' in content_lower or 'script' in content_lower or 'python' in content_lower:
            category = 'Code/Scripts'
        elif 'revenue' in content_lower or 'business' in content_lower:
            category = 'Business/Revenue'
        elif 'analysis' in content_lower or 'research' in content_lower:
            category = 'Analysis/Research'
        else:
            category = 'General'
    
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
    parser = argparse.ArgumentParser(description='Capture and save formatted clipboard content to knowledge base')
    parser.add_argument('--db-path', default=os.path.expanduser('~/avatararts-kb/knowledge_base.db'), 
                        help='Path to the SQLite database')
    parser.add_argument('--title', help='Title of the knowledge entry (will be auto-generated if not provided)')
    parser.add_argument('--content', help='Content of the knowledge entry (reads from clipboard if not provided)')
    parser.add_argument('--category', help='Category of the knowledge entry (auto-detected if not provided)')
    parser.add_argument('--tags', nargs='+', help='Tags for the knowledge entry (auto-generated if not provided)')
    parser.add_argument('--source', default='enhanced_clipboard_capture', help='Source identifier')
    parser.add_argument('--no-auto-tags', action='store_true', help='Skip auto-tag generation')
    
    args = parser.parse_args()
    
    # Ensure the database directory exists
    db_dir = os.path.dirname(args.db_path)
    os.makedirs(db_dir, exist_ok=True)
    
    # Get content from clipboard if not provided
    if not args.content:
        clipboard_content = get_clipboard_content()
        if clipboard_content:
            content = clipboard_content
            print(f"Retrieved content from clipboard ({len(clipboard_content)} characters)")
        else:
            print("Enter content to save (press Ctrl+D when finished):")
            content = sys.stdin.read()
    else:
        content = args.content
    
    # Exit if no content
    if not content.strip():
        print("No content to save")
        return
    
    # Generate title if not provided
    if not args.title:
        title = extract_title_from_content(content)
    else:
        title = args.title
    
    # Generate tags if not provided
    if not args.tags and not args.no_auto_tags:
        tags = analyze_content_for_tags(content)
        print(f"Auto-generated tags: {', '.join(tags)}")
    else:
        tags = args.tags or []
    
    # Save the knowledge entry
    entry_id = save_knowledge_entry(
        args.db_path, 
        title, 
        content, 
        args.category, 
        tags,
        args.source
    )
    
    # Extract and save insights
    insights = extract_insights(content)
    if insights:
        save_insights(args.db_path, entry_id, insights)
    
    print(f"Knowledge entry saved with ID: {entry_id}")
    print(f"Title: {title}")
    print(f"Category: {args.category or 'Auto-detected'}")
    print(f"Tags: {', '.join(tags) if tags else 'Auto-generated'}")
    print(f"Insights extracted: {len(insights)}")

if __name__ == "__main__":
    main()