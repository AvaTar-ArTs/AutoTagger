#!/usr/bin/env python3
"""
AutoTagger Core - V4 Optimized
Unified Intelligent File Indexer with Semantic Awareness and Code Intelligence
(Maturity Check Removed)
"""

import os
import sys
import json
import csv
import re
import ast
import sqlite3
import subprocess
import argparse
from datetime import datetime
from pathlib import Path

class AutoTagger:
    SEMANTIC_CATEGORIES = {
        "AI/ML": {
            "keywords": {
                "openai": 10, "anthropic": 10, "claude": 10, "gpt": 10, "llm": 9, "ai": 7, "gemini": 9
            },
            "code_patterns": ["Model", "Trainer", "LLM"],
            "imports": ["openai", "anthropic", "transformers", "torch"]
        },
        "Web Development": {
            "keywords": {
                "flask": 10, "django": 10, "fastapi": 9, "html": 8, "css": 8, "javascript": 8, "api": 8
            },
            "code_patterns": ["Router", "View", "API"],
            "imports": ["flask", "django", "fastapi", "requests"]
        },
        "Automation Scripts": {
            "keywords": {
                "automation": 10, "script": 9, "bot": 9, "automate": 9, "pipeline": 7
            },
            "code_patterns": ["Bot", "Automation", "Pipeline"],
            "imports": ["schedule", "celery"]
        },
        "Data Analysis": {
            "keywords": {
                "pandas": 10, "numpy": 10, "dataframe": 10, "analysis": 8, "csv": 8
            },
            "code_patterns": ["DataFrame", "Processor"],
            "imports": ["pandas", "numpy", "matplotlib"]
        }
    }

    def __init__(self, output_dir=None, db_path=None):
        self.output_dir = Path(output_dir or "~/AutoTagger/output").expanduser()
        self.db_path = Path(db_path or "~/AutoTagger/output/autotagger.db").expanduser()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS knowledge_entries (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, category TEXT, tags TEXT, source TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
        conn.commit()
        conn.close()

    def run(self, target_dir, prefix="scan", formats=["json", "csv", "md", "html"]):
        target_path = Path(target_dir).expanduser().resolve()
        if not target_path.is_dir(): return False

        print(f"🚀 Starting AutoTagger on: {target_path}")
        data = self._phase_discovery(target_path)
        data = self._phase_analysis(data)
        self._save_outputs(data, prefix, formats)
        print(f"✅ AutoTagger complete for {prefix}")
        return True

    def _phase_discovery(self, target_path):
        data = {'scan_time': datetime.now().isoformat(), 'target': str(target_path), 'items': []}
        for root, dirs, files in os.walk(target_path):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                if file.startswith('.'): continue
                file_path = Path(root) / file
                try:
                    stats = file_path.stat()
                    content = ""
                    if stats.st_size < 1024 * 1024:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f: content = f.read()
                    
                    item = {
                        'name': file,
                        'path': str(file_path),
                        'size_mb': round(stats.st_size / (1024*1024), 3),
                        'ext': file_path.suffix.lower(),
                        'content_preview': content[:1000]
                    }
                    if item['ext'] == '.py': item['code_intelligence'] = self._analyze_python(content)
                    data['items'].append(item)
                except: continue
        return data

    def _analyze_python(self, content):
        metrics = {'functions': 0, 'classes': 0, 'imports': [], 'complexity': 'low'}
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef): metrics['functions'] += 1
                elif isinstance(node, ast.ClassDef): metrics['classes'] += 1
                elif isinstance(node, ast.Import): [metrics['imports'].append(n.name) for n in node.names]
            if metrics['functions'] > 10: metrics['complexity'] = 'high'
        except: pass
        return metrics

    def _phase_analysis(self, data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for item in data['items']:
            all_text = f"{item['name']} {item['content_preview']}".lower()
            scores = {cat: sum(all_text.count(k) * w for k, w in config["keywords"].items()) for cat, config in self.SEMANTIC_CATEGORIES.items()}
            item['category'] = max(scores.items(), key=lambda x: x[1])[0] if any(scores.values()) else "General"
            biz_score = sum(2 for k in ['revenue', 'profit', 'ai', 'scale'] if k in all_text)
            item['business_value'] = min(biz_score / 2.0, 10.0)
            cursor.execute('INSERT INTO knowledge_entries (title, content, category, source) VALUES (?,?,?,?)', (item['name'], item['content_preview'][:500], item['category'], "autotagger_v4"))
        conn.commit()
        conn.close()
        return data

    def _save_outputs(self, data, prefix, formats):
        base_name = f"{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        if 'csv' in formats:
            path = self.output_dir / f"{base_name}.csv"
            with open(path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['name', 'category', 'value', 'complexity', 'size_mb', 'path'])
                writer.writeheader()
                for item in data['items']:
                    writer.writerow({'name': item['name'], 'category': item['category'], 'value': f"{item['business_value']:.2f}", 'complexity': item.get('code_intelligence', {}).get('complexity', 'N/A'), 'size_mb': item['size_mb'], 'path': item['path']})
            if sys.platform == 'darwin': subprocess.run(["open", str(path)], stderr=subprocess.DEVNULL)

        if 'md' in formats:
            path = self.output_dir / f"{base_name}.md"
            with open(path, 'w') as f:
                f.write(f"# AutoTagger Index: {prefix}\n\n| Name | Category | Value | Description |\n| :--- | :--- | :--- | :--- |\n")
                for item in data['items'][:100]:
                    f.write(f"| {item['name']} | {item['category']} | {item['business_value']:.1f} | {item['content_preview'][:100].strip()}... |\n")
            if sys.platform == 'darwin': subprocess.run(["open", str(path)], stderr=subprocess.DEVNULL)

        if 'html' in formats:
            path = self.output_dir / f"{base_name}.html"
            with open(path, 'w') as f:
                f.write(f"<html><body><h1>{prefix}</h1><table border=1><tr><th>Name</th><th>Category</th><th>Value</th></tr>")
                for item in data['items'][:100]:
                    f.write(f"<tr><td>{item['name']}</td><td>{item['category']}</td><td>{item['business_value']:.1f}</td></tr>")
                f.write("</table></body></html>")
            if sys.platform == 'darwin': subprocess.run(["open", str(path)], stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")
    parser.add_argument("--prefix", default="scan")
    parser.add_argument("--formats", default="csv,md,html")
    args = parser.parse_args()
    AutoTagger().run(args.dir, args.prefix, args.formats.split(','))
