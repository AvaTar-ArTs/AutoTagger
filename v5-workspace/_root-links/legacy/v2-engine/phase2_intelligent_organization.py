#!/usr/bin/env python3
"""
Tiered Indexing System for AVATARARTS Automations Directory
Phase 2: Intelligent Organization
"""

import json
import os
from datetime import datetime
import argparse
import sqlite3

def load_index(input_path):
    """Load the index from Phase 1"""
    with open(input_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_content_for_category(description):
    """Analyze content to determine the most appropriate category"""
    if not description:
        return 'General', 0
    
    content_lower = description.lower()
    
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
            matches = len(content_lower.split(keyword)) - 1
            weight += matches
        
        categories[category]['weight'] = weight
    
    # Find category with highest weight
    best_category = max(categories.keys(), key=lambda k: categories[k]['weight'])
    
    # If no significant matches found, default to General
    if categories[best_category]['weight'] == 0:
        best_category = 'General'
    
    return best_category, categories[best_category]['weight']

def analyze_content_for_tags(description):
    """Analyze content to generate relevant tags"""
    if not description:
        return []
    
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
    content_lower = description.lower()
    for term in tech_terms:
        if term.lower() in content_lower:
            tags.add(term.lower())
    
    # Extract any hashtags if present
    hashtag_pattern = r'#(\w+)'
    import re
    hashtags = re.findall(hashtag_pattern, description)
    for tag in hashtags:
        tags.add(tag.lower())
    
    # Extract capitalized words/phrases that might be important
    caps_pattern = r'\b[A-Z]{2,}\b'  # Standalone uppercase words
    caps_words = re.findall(caps_pattern, description)
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

def process_index_with_intelligence(index_data, db_path):
    """Process the index with intelligent categorization and tagging"""
    print(f"Processing {len(index_data['automation_tools'])} tools with intelligent organization...")
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    processed_count = 0
    for tool in index_data['automation_tools']:
        # Analyze description for category and tags
        category, confidence_score = analyze_content_for_category(tool.get('description', ''))
        tags = analyze_content_for_tags(tool.get('description', ''))
        
        # Update tool with analysis results
        tool['intelligent_category'] = category
        tool['confidence_score'] = min(confidence_score / 10.0, 1.0)  # Normalize confidence
        tool['auto_generated_tags'] = tags
        tool['processed_by_phase2'] = datetime.now().isoformat()
        
        # Also save to database for cross-referencing
        cursor.execute('''
            INSERT INTO knowledge_entries (title, content, category, tags, source)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            tool['name'], 
            tool['description'][:500],  # Limit content length
            category, 
            json.dumps(tags), 
            f"phase2_intelligent_organization_{tool['name']}"
        ))
        
        processed_count += 1
        if processed_count % 50 == 0:
            print(f"  Processed {processed_count}/{len(index_data['automation_tools'])} tools...")
    
    conn.commit()
    conn.close()
    
    print(f"Phase 2 complete. Processed {processed_count} tools with intelligent organization.")
    return index_data

def save_enhanced_index(index_data, output_path):
    """Save the enhanced index to a JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    print(f"Enhanced index saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Process automation index with intelligent organization')
    parser.add_argument('--input', default='~/AutoTagger/v2-engine/automations_index_phase1.json',
                        help='Input file from Phase 1')
    parser.add_argument('--output', default='~/AutoTagger/v2-engine/automations_index_phase2.json',
                        help='Output file for Phase 2')
    parser.add_argument('--db-path', default='~/AutoTagger/v2-engine/knowledge_base.db',
                        help='Path to the SQLite database')
    
    args = parser.parse_args()
    
    # Expand user paths
    input_path = os.path.expanduser(args.input)
    output_path = os.path.expanduser(args.output)
    db_path = os.path.expanduser(args.db_path)
    
    # Load index from Phase 1
    print(f"Loading index from: {input_path}")
    index_data = load_index(input_path)
    
    # Process with intelligent organization
    enhanced_index = process_index_with_intelligence(index_data, db_path)
    
    # Save enhanced index
    save_enhanced_index(enhanced_index, output_path)
    
    print(f"\nPhase 2 complete. Enhanced index saved to {output_path}")
    print("Ready for Phase 3: Advanced Intelligence & Prediction")

if __name__ == "__main__":
    main()