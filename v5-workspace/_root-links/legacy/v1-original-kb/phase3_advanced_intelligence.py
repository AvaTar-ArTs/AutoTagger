#!/usr/bin/env python3
"""
Tiered Indexing System for AVATARARTS Automations Directory
Phase 3: Advanced Intelligence & Prediction
"""

import json
import os
import re
from datetime import datetime
import argparse
import sqlite3
from collections import Counter

def load_enhanced_index(input_path):
    """Load the enhanced index from Phase 2"""
    with open(input_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_key_entities(description):
    """Extract key entities from description"""
    if not description:
        return {
            'technical_terms': [],
            'metrics': [],
            'platforms': [],
            'tools': []
        }
    
    entities = {
        'technical_terms': [],
        'metrics': [],
        'platforms': [],
        'tools': []
    }
    
    # Extract technical terms
    tech_pattern = r'\b(?:AI|ML|API|JSON|XML|SQL|HTML|CSS|JS|Python|JavaScript|React|Node\.js|Docker|Kubernetes|FastAPI|OpenAI|Claude|GPT|NotebookLM|SQLite|PostgreSQL|MongoDB|AWS|GCP|Azure)\b'
    entities['technical_terms'] = list(set(re.findall(tech_pattern, description, re.IGNORECASE)))
    
    # Extract metrics (numbers followed by common metric terms)
    metric_pattern = r'(\d+(?:\.\d+)?)\s*(?:%|million|thousand|k|%|hours?|days?|weeks?|months?|years?|mb|gb|kb)'
    entities['metrics'] = re.findall(metric_pattern, description, re.IGNORECASE)
    
    # Extract platforms
    platform_pattern = r'\b(?:YouTube|Instagram|TikTok|Twitter|Facebook|LinkedIn|Spotify|Apple|Google|Microsoft|Amazon|Netflix|NotebookLM|Chrome|Firefox|Safari)\b'
    entities['platforms'] = list(set(re.findall(platform_pattern, description, re.IGNORECASE)))
    
    # Extract tools
    tool_pattern = r'\b(?:ChatGPT|Claude|GPT|Midjourney|Figma|VSCode|Terminal|iTerm|QuickLook|SQLite|PostgreSQL|MongoDB|Docker|Kubernetes|Git|GitHub|GitLab|Jira|Slack|Discord|Zoom|Trello|Asana)\b'
    entities['tools'] = list(set(re.findall(tool_pattern, description, re.IGNORECASE)))
    
    return entities

def predict_business_value(tool):
    """Predict potential business value of the tool"""
    description = tool.get('description', '').lower()
    
    # Factors that increase business value
    business_factors = {
        'revenue': 3,
        'profit': 3,
        'sales': 2,
        'marketing': 2,
        'monetization': 3,
        'customer': 2,
        'roi': 3,
        'conversion': 2,
        'growth': 2,
        'scale': 2,
        'automate': 2,
        'efficiency': 2,
        'productivity': 2,
        'ai': 2,
        'automation': 3,
        'content': 1,
        'creation': 1,
        'optimization': 1
    }
    
    score = 0
    for factor, weight in business_factors.items():
        if factor in description:
            # Count occurrences and multiply by weight
            count = description.count(factor)
            score += count * weight
    
    # Normalize score to 0-10 scale
    normalized_score = min(score / 5.0, 10.0)  # Assuming max possible score would be around 50
    
    return normalized_score

def identify_integration_potential(tool, all_tools):
    """Identify potential integrations with other tools"""
    description = tool.get('description', '').lower()
    
    # Look for common integration patterns
    integration_indicators = [
        'api', 'integration', 'connect', 'sync', 'import', 'export', 
        'webhook', 'plugin', 'extension', 'connector', 'bridge'
    ]
    
    has_integration_potential = any(indicator in description for indicator in integration_indicators)
    
    # Find related tools based on shared keywords
    related_tools = []
    for other_tool in all_tools:
        if other_tool['name'] != tool['name']:
            other_desc = other_tool.get('description', '').lower()
            # Simple keyword overlap check
            tool_keywords = set(description.split())
            other_keywords = set(other_desc.split())
            overlap = len(tool_keywords.intersection(other_keywords))
            
            if overlap > 3:  # At least 3 common words
                related_tools.append({
                    'name': other_tool['name'],
                    'overlap_count': overlap,
                    'path': other_tool['path']
                })
    
    # Sort by overlap count
    related_tools.sort(key=lambda x: x['overlap_count'], reverse=True)
    
    return {
        'has_potential': has_integration_potential,
        'related_tools': related_tools[:5]  # Top 5 related tools
    }

def extract_insights(description):
    """Extract key insights from description"""
    if not description:
        return []
    
    insights = []
    
    # Look for key phrases that indicate insights
    insight_patterns = [
        (r'(?:can|enable|allows|provides|offers) ([^\.]*?)(?:automation|tool|solution)', 'capability'),
        (r'(?:built|designed|created) for ([^\.]*?)(?:\.)', 'purpose'),
        (r'(?:uses|leverages|integrates) ([^\.]*?)(?:\.)', 'technology'),
        (r'(?:supports|compatible|works with) ([^\.]*?)(?:\.)', 'compatibility'),
        (r'(?:features|includes|contains) ([^\.]*?)(?:\.)', 'features')
    ]
    
    for pattern, insight_type in insight_patterns:
        matches = re.findall(pattern, description, re.IGNORECASE)
        for match in matches:
            if len(match.strip()) > 5:  # Avoid very short matches
                insights.append({
                    'type': insight_type,
                    'content': match.strip(),
                    'confidence': 0.8
                })
    
    return insights

def process_with_advanced_intelligence(index_data, db_path):
    """Process the index with advanced intelligence and predictive analytics"""
    print(f"Processing {len(index_data['automation_tools'])} tools with advanced intelligence...")
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    processed_count = 0
    for tool in index_data['automation_tools']:
        # Extract key entities
        entities = extract_key_entities(tool.get('description', ''))
        
        # Predict business value
        business_value = predict_business_value(tool)
        
        # Identify integration potential
        integration_info = identify_integration_potential(tool, index_data['automation_tools'])
        
        # Extract insights
        insights = extract_insights(tool.get('description', ''))
        
        # Update tool with advanced intelligence results
        tool['advanced_entities'] = entities
        tool['predicted_business_value'] = business_value
        tool['integration_potential'] = integration_info
        tool['extracted_insights'] = insights
        tool['processed_by_phase3'] = datetime.now().isoformat()
        
        # Save analysis results to database
        analysis_data = {
            'entities': entities,
            'business_value': business_value,
            'integration_info': integration_info,
            'insights': insights,
            'processing_timestamp': datetime.now().isoformat()
        }
        
        cursor.execute('''
            INSERT INTO analysis_results (entry_id, analysis_type, analysis_data)
            VALUES (?, ?, ?)
        ''', (
            cursor.lastrowid or 1,  # Use last inserted ID or default to 1
            'phase3_advanced_intelligence',
            json.dumps(analysis_data)
        ))
        
        # Save insights to insights table
        for insight in insights:
            cursor.execute('''
                INSERT INTO insights (entry_id, insight_type, insight_data, confidence_score)
                VALUES (?, ?, ?, ?)
            ''', (
                cursor.lastrowid or 1,
                insight['type'],
                json.dumps(insight['content']),
                insight['confidence']
            ))
        
        processed_count += 1
        if processed_count % 50 == 0:
            print(f"  Processed {processed_count}/{len(index_data['automation_tools'])} tools with advanced intelligence...")
    
    conn.commit()
    conn.close()
    
    print(f"Phase 3 complete. Processed {processed_count} tools with advanced intelligence and predictions.")
    return index_data

def save_final_index(index_data, output_path):
    """Save the final index to a JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    print(f"Final index saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Process automation index with advanced intelligence and predictions')
    parser.add_argument('--input', default='~/avatararts-kb/automations_index_phase2.json',
                        help='Input file from Phase 2')
    parser.add_argument('--output', default='~/avatararts-kb/automations_index_phase3.json',
                        help='Output file for Phase 3')
    parser.add_argument('--db-path', default='~/avatararts-kb/knowledge_base.db',
                        help='Path to the SQLite database')
    
    args = parser.parse_args()
    
    # Expand user paths
    input_path = os.path.expanduser(args.input)
    output_path = os.path.expanduser(args.output)
    db_path = os.path.expanduser(args.db_path)
    
    # Load enhanced index from Phase 2
    print(f"Loading enhanced index from: {input_path}")
    index_data = load_enhanced_index(input_path)
    
    # Process with advanced intelligence
    final_index = process_with_advanced_intelligence(index_data, db_path)
    
    # Save final index
    save_final_index(final_index, output_path)
    
    print(f"\nPhase 3 complete. Final index saved to {output_path}")
    print("Tiered indexing process complete!")
    
    # Print summary
    print("\nSummary:")
    print(f"  Total tools processed: {len(final_index['automation_tools'])}")
    print(f"  Total directories scanned: {final_index['total_directories']}")
    print(f"  Total files found: {final_index['total_files']}")
    print(f"  Scan completed: {final_index['scan_end_time']}")
    
    # Calculate average business value
    total_business_value = sum(tool.get('predicted_business_value', 0) for tool in final_index['automation_tools'])
    avg_business_value = total_business_value / len(final_index['automation_tools']) if final_index['automation_tools'] else 0
    print(f"  Average predicted business value: {avg_business_value:.2f}/10")

if __name__ == "__main__":
    main()