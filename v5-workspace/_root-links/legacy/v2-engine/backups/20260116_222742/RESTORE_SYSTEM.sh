#!/bin/bash
# Restore script for AVATARARTS Knowledge Base System

if [ $# -ne 1 ]; then
    echo "Usage: $0 <backup_directory>"
    echo "Example: $0 /Users/steven/.tagger/backups/20260117_120000"
    exit 1
fi

BACKUP_DIR="$1"

if [ ! -d "$BACKUP_DIR" ]; then
    echo "Error: Backup directory does not exist: $BACKUP_DIR"
    exit 1
fi

echo "Restoring AVATARARTS Knowledge Base System from: $BACKUP_DIR"

# Restore the knowledge base
echo "Restoring knowledge base..."
cp "$BACKUP_DIR/knowledge_base.db" ~/.tagger/knowledge_base.db

# Restore all version scripts
echo "Restoring version scripts..."
cp "$BACKUP_DIR/multi_format_directory_indexer_v1.py" ~/.tagger/ 2>/dev/null || echo "v1 script not in backup"
cp "$BACKUP_DIR/multi_format_directory_indexer_v2.py" ~/.tagger/ 2>/dev/null || echo "v2 script not in backup"
cp "$BACKUP_DIR/multi_format_directory_indexer_v3.py" ~/.tagger/ 2>/dev/null || echo "v3 script not in backup"
cp "$BACKUP_DIR/multi_format_directory_indexer_v4.py" ~/.tagger/ 2>/dev/null || echo "v4 script not in backup"

# Restore phase scripts
echo "Restoring phase scripts..."
cp "$BACKUP_DIR/phase1_rapid_scan.py" ~/.tagger/ 2>/dev/null || echo "phase1 script not in backup"
cp "$BACKUP_DIR/phase2_intelligent_organization.py" ~/.tagger/ 2>/dev/null || echo "phase2 script not in backup"
cp "$BACKUP_DIR/phase3_advanced_intelligence.py" ~/.tagger/ 2>/dev/null || echo "phase3 script not in backup"

# Restore configuration files
echo "Restoring configuration files..."
cp "$BACKUP_DIR/kb_aliases.sh" ~/.tagger/
cp "$BACKUP_DIR/open_kb_outputs.sh" ~/.tagger/

echo "Restore complete!"
echo "To reload the system, run: source ~/.tagger/kb_aliases.sh"
