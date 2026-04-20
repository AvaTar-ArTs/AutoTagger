#!/usr/bin/env python3
"""
Hybrid AVATARARTS Intelligence System
Combines original automation capabilities with new knowledge base features
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
from collections import Counter

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

def analyze_content_for_category(content):
    """Analyze content to determine the most appropriate category"""
    content_lower = content.lower()
    
    # Define category keywords and their weights
    categories = {
        'Code/Scripts': {
            'keywords': ['python', 'script', 'function', 'def ', 'import', 'class', 'api', 'database', 'sql', 'json', 'xml'],
            'weight': 0
        },
        'Business/Revenue': {
            'keywords': ['revenue', 'profit', 'income', 'sales', 'marketing', 'monetization', 'business', 'client', 'customer', 'roi', 'conversion'],
            'weight': 0
        },
        'Analytics/Optimization': {
            'keywords': ['seo', 'aeo', 'geo', 'analytics', 'metrics', 'kpi', 'tracking', 'performance', 'optimization', 'ranking', 'traffic'],
            'weight': 0
        },
        'AI/Automation': {
            'keywords': ['ai', 'automation', 'automate', 'bot', 'chatgpt', 'claude', 'gpt', 'ml', 'machine learning', 'neural', 'algorithm'],
            'weight': 0
        },
        'Content Creation': {
            'keywords': ['content', 'video', 'youtube', 'instagram', 'social media', 'podcast', 'blog', 'article', 'writing', 'publishing'],
            'weight': 0
        },
        'Technical Documentation': {
            'keywords': ['documentation', 'readme', 'setup', 'install', 'configuration', 'settings', 'tutorial', 'guide', 'how-to', 'instructions'],
            'weight': 0
        },
        'Research/Analysis': {
            'keywords': ['research', 'analysis', 'study', 'data', 'report', 'findings', 'results', 'methodology', 'conclusion', 'insight'],
            'weight': 0
        },
        'Strategy/Planning': {
            'keywords': ['strategy', 'plan', 'planning', 'roadmap', 'timeline', 'goals', 'objectives', 'vision', 'mission', 'priorities'],
            'weight': 0
        },
        'Marketing/Sales': {
            'keywords': ['marketing', 'sales', 'leads', 'prospects', 'campaign', 'advertising', 'promotion', 'outreach', 'engagement'],
            'weight': 0
        },
        'General': {
            'keywords': [],
            'weight': 0
        }
    }
    
    # Calculate weight for each category based on keyword matches
    for category, data in categories.items():
        weight = 0
        for keyword in data['keywords']:
            # Count occurrences of keyword in content
            matches = len(re.findall(r'\b' + re.escape(keyword) + r'\b', content_lower))
            weight += matches
        
        categories[category]['weight'] = weight
    
    # Find category with highest weight
    best_category = max(categories.keys(), key=lambda k: categories[k]['weight'])
    
    # If no significant matches found, default to General
    if categories[best_category]['weight'] == 0:
        best_category = 'General'
    
    return best_category, categories[best_category]['weight']

def analyze_content_for_tags(content):
    """Analyze content to generate relevant tags"""
    tags = set()
    
    # Common technical terms that could become tags
    tech_terms = [
        'AEO', 'SEO', 'GEO', 'analytics', 'optimization', 'automation', 
        'AI', 'machine learning', 'python', 'database', 'API', 'framework',
        'content-awareness', 'intelligence', 'trend', 'strategy', 'revenue',
        'marketing', 'digital', 'platform', 'script', 'tool', 'system',
        'automation', 'content', 'generation', 'analysis', 'research'
    ]
    
    # Look for technical terms in content
    content_lower = content.lower()
    for term in tech_terms:
        if term.lower() in content_lower:
            tags.add(term.lower())
    
    # Extract any hashtags if present
    hashtag_pattern = r'#(\w+)'
    hashtags = re.findall(hashtag_pattern, content)
    for tag in hashtags:
        tags.add(tag.lower())
    
    # Extract capitalized words/phrases that might be important
    caps_pattern = r'\b[A-Z]{2,}\b'  # Standalone uppercase words
    caps_words = re.findall(caps_pattern, content)
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
    if any(word in content_lower for word in ['ai', 'automation', 'bot']):
        tags.add('ai')
    if any(word in content_lower for word in ['seo', 'aeo', 'geo', 'optimization']):
        tags.add('seo')
    
    return list(tags)[:10]  # Limit to 10 tags

def extract_key_entities(content):
    """Extract key entities from content"""
    # This is a simplified entity extraction - in a real system you might use NLP libraries
    entities = {
        'technical_terms': [],
        'metrics': [],
        'platforms': [],
        'tools': []
    }
    
    # Extract technical terms
    tech_pattern = r'\b(?:AI|ML|API|JSON|XML|SQL|HTML|CSS|JS|Python|JavaScript|React|Node\.js|Docker|Kubernetes)\b'
    entities['technical_terms'] = list(set(re.findall(tech_pattern, content, re.IGNORECASE)))
    
    # Extract metrics (numbers followed by common metric terms)
    metric_pattern = r'(\d+(?:\.\d+)?)\s*(?:%|million|thousand|k|%|hours?|days?|weeks?|months?|years?|mb|gb|kb)'
    entities['metrics'] = re.findall(metric_pattern, content, re.IGNORECASE)
    
    # Extract platforms
    platform_pattern = r'\b(?:YouTube|Instagram|TikTok|Twitter|Facebook|LinkedIn|Spotify|Apple|Google|Microsoft|Amazon|Netflix)\b'
    entities['platforms'] = list(set(re.findall(platform_pattern, content, re.IGNORECASE)))
    
    # Extract tools
    tool_pattern = r'\b(?:ChatGPT|Claude|GPT|Midjourney|Figma|VSCode|Terminal|iTerm|QuickLook|SQLite|PostgreSQL|MongoDB)\b'
    entities['tools'] = list(set(re.findall(tool_pattern, content, re.IGNORECASE)))
    
    return entities

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
    
    # Create table for insights
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

def save_knowledge_entry(db_path, title, content, category=None, tags=None, source="hybrid_capture"):
    """Save a knowledge entry to the database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Convert tags to JSON string if provided
    tags_json = json.dumps(tags) if tags else json.dumps([])
    
    # Determine category if not provided
    if not category:
        category, _ = analyze_content_for_category(content)
    
    cursor.execute('''
        INSERT INTO knowledge_entries (title, content, category, tags, source)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, content, category, tags_json, source))
    
    entry_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return entry_id

def save_analysis_results(db_path, entry_id, analysis_data):
    """Save analysis results to the database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO analysis_results (entry_id, analysis_type, analysis_data)
        VALUES (?, ?, ?)
    ''', (entry_id, 'hybrid_classification', json.dumps(analysis_data)))
    
    conn.commit()
    conn.close()

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
    parser = argparse.ArgumentParser(description='Hybrid AVATARARTS Intelligence System - Combines original automation with new knowledge base features')
    parser.add_argument('--db-path', default=os.path.expanduser('~/AutoTagger/v2-engine/knowledge_base.db'), 
                        help='Path to the SQLite database')
    parser.add_argument('--title', help='Title of the knowledge entry (will be auto-generated if not provided)')
    parser.add_argument('--content', help='Content to analyze and sort (reads from clipboard if not provided)')
    parser.add_argument('--category', help='Category of the knowledge entry (auto-detected if not provided)')
    parser.add_argument('--tags', nargs='+', help='Tags for the knowledge entry (auto-generated if not provided)')
    parser.add_argument('--source', default='hybrid_intelligence_system', help='Source identifier')
    parser.add_argument('--action', choices=['save', 'search', 'analyze'], default='save', 
                        help='Action to perform')
    parser.add_argument('--query', help='Search query (used with search action)')
    parser.add_argument('--force-category', help='Force a specific category instead of auto-detection')
    parser.add_argument('--verbose', action='store_true', help='Show detailed analysis')
    
    args = parser.parse_args()
    
    # Ensure the database directory exists
    db_dir = os.path.dirname(args.db_path)
    os.makedirs(db_dir, exist_ok=True)
    
    # Create database if it doesn't exist
    create_database(args.db_path)
    
    if args.action == 'search':
        if not args.query:
            print("Error: --query is required for search action")
            return
            
        results = search_knowledge(args.db_path, args.query, args.category)
        print(f"Found {len(results)} results:")
        for result in results:
            print(f"\nID: {result[0]}")
            print(f"Title: {result[1]}")
            print(f"Category: {result[3]}")
            print(f"Created: {result[5]}")
            print(f"Content preview: {result[2][:200]}...")
            print("-" * 50)
    
    elif args.action == 'save' or args.action == 'analyze':
        # Get content from clipboard if not provided
        if not args.content:
            clipboard_content = get_clipboard_content()
            if clipboard_content:
                content = clipboard_content
                if args.verbose:
                    print(f"Retrieved {len(clipboard_content)} characters from clipboard")
            else:
                print("Enter content to analyze and sort (press Ctrl+D when finished):")
                content = sys.stdin.read()
        else:
            content = args.content
        
        # Exit if no content
        if not content.strip():
            print("No content to analyze and sort")
            return
        
        # Generate title if not provided
        if not args.title:
            title = extract_title_from_content(content)
        else:
            title = args.title
        
        # Analyze content for category if not forced
        if args.force_category:
            category = args.force_category
            confidence = 1.0  # Perfect confidence since it's forced
        else:
            category, confidence_score = analyze_content_for_category(content)
            confidence = min(confidence_score / 10.0, 1.0)  # Normalize confidence to 0-1 range
        
        # Generate tags if not provided
        if not args.tags:
            tags = analyze_content_for_tags(content)
        else:
            tags = args.tags
        
        # Extract entities
        entities = extract_key_entities(content)
        
        # Extract insights
        insights = extract_insights(content)
        
        # Create analysis report
        analysis_report = {
            'category': category,
            'confidence': confidence,
            'tags': tags,
            'entities': entities,
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        if args.verbose:
            print(f"Analysis Results:")
            print(f"  Category: {category} (confidence: {confidence:.2f})")
            print(f"  Tags: {', '.join(tags)}")
            print(f"  Technical Terms: {entities['technical_terms']}")
            print(f"  Platforms: {entities['platforms']}")
            print(f"  Tools: {entities['tools']}")
            print()
        
        # Save the knowledge entry
        entry_id = save_knowledge_entry(
            args.db_path, 
            title, 
            content, 
            category,
            tags,
            args.source
        )
        
        # Save analysis results
        save_analysis_results(args.db_path, entry_id, analysis_report)
        
        # Save insights
        if insights:
            save_insights(args.db_path, entry_id, insights)
        
        print(f"Content analyzed and sorted into category '{category}'")
        print(f"Knowledge entry saved with ID: {entry_id}")
        print(f"Title: {title}")
        print(f"Category: {category}")
        print(f"Tags: {', '.join(tags) if tags else 'Auto-generated'}")
        print(f"Insights extracted: {len(insights)}")
        
        # Suggest related entries
        conn = sqlite3.connect(args.db_path)
        cursor = conn.cursor()
        
        # Find entries with similar tags
        if tags:
            cursor.execute(f'''
                SELECT id, title, category 
                FROM knowledge_entries 
                WHERE id != ? AND tags LIKE ?
                ORDER BY created_at DESC
                LIMIT 3
            ''', (entry_id, f'%{tags[0]}%'))  # Using first tag to find similar entries
            
            similar_entries = cursor.fetchall()
            if similar_entries:
                print(f"\nSimilar entries you might find relevant:")
                for entry in similar_entries:
                    print(f"  - ID {entry[0]}: {entry[1]} [{entry[2]}]")
        
        conn.close()

if __name__ == "__main__":
    main()