#!/usr/bin/env python3
"""
Tiered Indexing System for AVATARARTS Knowledge Base
Phase 3: LLM-Powered Advanced Intelligence
"""

import json
import os
import argparse
import sqlite3
from datetime import datetime
from openai import OpenAI
import time

def load_enhanced_index(input_path):
    """Load the enhanced index from Phase 2"""
    with open(input_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_tool_with_llm(client, tool, model, all_tool_names):
    """Use LLM to analyze a single tool"""
    prompt = f"""
    Analyze the following tool/script for a technical knowledge base.
    
    Name: {tool.get('name')}
    Path: {tool.get('path')}
    Description: {tool.get('description')}
    
    Provide a detailed analysis in JSON format with the following structure:
    {{
        "technical_terms": ["List of core technologies, languages, or protocols used"],
        "metrics": ["Any quantifiable data points mentioned"],
        "platforms": ["Target platforms like YouTube, AWS, macOS, etc."],
        "tools": ["Specific tools or libraries mentioned"],
        "business_value": 0-10,
        "business_value_justification": "Why this score?",
        "insights": [
            {{
                "type": "capability|purpose|technology|compatibility|features",
                "content": "The actual insight",
                "confidence": 0.0-1.0
            }}
        ],
        "integration_potential": ["Names of related tools from this list that might integrate well: {', '.join(all_tool_names[:50])}"]
    }}
    
    Ensure the response is ONLY the JSON object.
    """
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a senior systems architect and business analyst for AVATARARTS, an AI automation company."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"  Error analyzing {tool.get('name')}: {e}")
        return None

def process_with_llm_intelligence(index_data, db_path, api_key, model, limit=None):
    """Process the index with LLM-powered intelligence"""
    client = OpenAI(api_key=api_key)
    tools = index_data.get('automation_tools', [])
    if limit:
        tools = tools[:limit]
        print(f"Limiting processing to first {limit} tools.")
    
    if not tools:
        print("No tools found to process.")
        return index_data

    print(f"Processing {len(tools)} tools with {model} intelligence...")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    all_tool_names = [t.get('name') for t in index_data.get('automation_tools', [])]
    
    processed_count = 0
    for tool in tools:
        print(f"  Analyzing {tool.get('name')} ({processed_count + 1}/{len(tools)})...")
        
        analysis = analyze_tool_with_llm(client, tool, model, all_tool_names)
        
        if analysis:
            # Update tool with LLM results
            tool['llm_analysis'] = analysis
            tool['advanced_entities'] = {
                'technical_terms': analysis.get('technical_terms', []),
                'metrics': analysis.get('metrics', []),
                'platforms': analysis.get('platforms', []),
                'tools': analysis.get('tools', [])
            }
            tool['predicted_business_value'] = analysis.get('business_value', 0)
            tool['business_value_justification'] = analysis.get('business_value_justification', '')
            tool['integration_potential'] = {
                'has_potential': len(analysis.get('integration_potential', [])) > 0,
                'related_tools': analysis.get('integration_potential', [])
            }
            tool['extracted_insights'] = analysis.get('insights', [])
            tool['processed_by_phase3_llm'] = datetime.now().isoformat()
            
            # Save to database
            cursor.execute('''
                INSERT INTO analysis_results (entry_id, analysis_type, analysis_data)
                VALUES (?, ?, ?)
            ''', (
                tool.get('id', 1),
                'phase3_llm_intelligence',
                json.dumps(analysis)
            ))
            
            for insight in analysis.get('insights', []):
                cursor.execute('''
                    INSERT INTO insights (entry_id, insight_type, insight_data, confidence_score)
                    VALUES (?, ?, ?, ?)
                ''', (
                    tool.get('id', 1),
                    insight['type'],
                    insight['content'],
                    insight['confidence']
                ))
            
            processed_count += 1
            # Rate limiting / polite delay
            time.sleep(0.5)
        
        if processed_count % 10 == 0:
            conn.commit()
    
    conn.commit()
    conn.close()
    
    print(f"Phase 3 (LLM) complete. Processed {processed_count} tools.")
    return index_data

def save_final_index(index_data, output_path):
    """Save the final index to a JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    print(f"Final index saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Process automation index with LLM-powered intelligence')
    parser.add_argument('--input', default='~/avatararts-kb/automations_index_phase2.json',
                        help='Input file from Phase 2')
    parser.add_argument('--output', default='~/avatararts-kb/automations_index_phase3_llm.json',
                        help='Output file for Phase 3')
    parser.add_argument('--db-path', default='~/avatararts-kb/knowledge_base.db',
                        help='Path to the SQLite database')
    parser.add_argument('--model', default='gpt-4o-mini',
                        help='OpenAI model to use')
    parser.add_argument('--limit', type=int, default=None,
                        help='Limit the number of tools processed')
    
    args = parser.parse_args()
    
    # Expand user paths
    input_path = os.path.expanduser(args.input)
    output_path = os.path.expanduser(args.output)
    db_path = os.path.expanduser(args.db_path)
    
    # Get API key from environment
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        return
    
    # Load enhanced index from Phase 2
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} not found.")
        return
        
    print(f"Loading enhanced index from: {input_path}")
    index_data = load_enhanced_index(input_path)
    
    # Process with LLM intelligence
    final_index = process_with_llm_intelligence(index_data, db_path, api_key, args.model, args.limit)
    
    # Save final index
    save_final_index(final_index, output_path)
    
    print(f"\nPhase 3 (LLM) complete. Results saved to {output_path}")

if __name__ == "__main__":
    main()
