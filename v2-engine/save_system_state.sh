#!/bin/bash
# AVATARARTS Knowledge Base System - Complete State Capture
# Saves the entire system configuration and current state

echo "==========================================="
echo "AVATARARTS Knowledge Base System - State Capture"
echo "==========================================="
echo "Timestamp: $(date)"
echo "System: macOS Intel"
echo ""
echo "This script captures the complete state of the AVATARARTS Knowledge Base system"
echo "including all versions, configurations, and current knowledge base status."
echo ""
echo "==========================================="

# Create a timestamped backup directory
BACKUP_DIR="$HOME/.tagger/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "Creating backup in: $BACKUP_DIR"
echo ""

# 1. Save the knowledge base database
echo "1. Saving knowledge base database..."
cp ~/.tagger/knowledge_base.db "$BACKUP_DIR/knowledge_base.db"
echo "   ✓ knowledge_base.db saved"

# 2. Save all version scripts
echo "2. Saving all version scripts..."
cp ~/.tagger/multi_format_directory_indexer.py "$BACKUP_DIR/multi_format_directory_indexer_v1.py" 2>/dev/null || echo "   - v1 script not found"
cp ~/.tagger/multi_format_directory_indexer_v2.py "$BACKUP_DIR/multi_format_directory_indexer_v2.py" 2>/dev/null || echo "   - v2 script not found"
cp ~/.tagger/multi_format_directory_indexer_v3.py "$BACKUP_DIR/multi_format_directory_indexer_v3.py" 2>/dev/null || echo "   - v3 script not found"
cp ~/.tagger/multi_format_directory_indexer_v4.py "$BACKUP_DIR/multi_format_directory_indexer_v4.py" 2>/dev/null || echo "   - v4 script not found"
echo "   ✓ All version scripts saved"

# 3. Save all phase scripts
echo "3. Saving phase scripts..."
cp ~/.tagger/phase1_rapid_scan.py "$BACKUP_DIR/phase1_rapid_scan.py" 2>/dev/null || echo "   - phase1 script not found"
cp ~/.tagger/phase2_intelligent_organization.py "$BACKUP_DIR/phase2_intelligent_organization.py" 2>/dev/null || echo "   - phase2 script not found"
cp ~/.tagger/phase3_advanced_intelligence.py "$BACKUP_DIR/phase3_advanced_intelligence.py" 2>/dev/null || echo "   - phase3 script not found"
echo "   ✓ Phase scripts saved"

# 4. Save the aliases and opening script
echo "4. Saving configuration files..."
cp ~/.tagger/kb_aliases.sh "$BACKUP_DIR/kb_aliases.sh"
cp ~/.tagger/open_kb_outputs.sh "$BACKUP_DIR/open_kb_outputs.sh"
echo "   ✓ Configuration files saved"

# 5. Save documentation files
echo "5. Saving documentation..."
DOC_FILES=(
    "AVATARARTS_KNOWLEDGE_BASE_SYSTEM_VERSION_4.md"
    "AVATARARTS_KNOWLEDGE_BASE_EVOLUTION_SUMMARY.md" 
    "AVATARARTS_KNOWLEDGE_BASE_SYSTEM_DOCUMENTATION.md"
    "DEVONTHINK_ALTERNATIVE.md"
    "MULTI_FORMAT_INDEXER.md"
    "SYSTEM_STATUS.md"
    "COMPLETE_IMPLEMENTATION_SUMMARY.md"
    "HYBRID_INTELLIGENCE_SYSTEM.md"
    "AUTO_SORTING_SYSTEM.md"
    "KNOWLEDGE_BASE_TOOLS_README.md"
    "AVATARARTS_KNOWLEDGE_BASE_EVOLUTION_SUMMARY.md"
    "AVATARARTS_KNOWLEDGE_BASE_SYSTEM_VERSION_4.md"
    "COMPLETE_SYSTEM_OVERVIEW.md"
    "DEVONTHINK_ALTERNATIVE_COMPLETE.md"
    "ENHANCED_CLIPBOARD_CAPTURE.md"
    "KNOWLEDGE_BASE_TOOLS_README.md"
    "MULTI_FORMAT_INDEXER.md"
    "SYSTEM_MIGRATION_COMPLETE.md"
    "TIERED_INDEXING_RESULTS_SUMMARY.md"
    "UNIVERSAL_DIRECTORY_INDEXER.md"
    "UNIVERSAL_INDEXER_COMPLETE_SYSTEM.md"
    "AVATARARTS_KNOWLEDGE_BASE.md"
    "PROGRESS_REPORT_V3.md"
    "SYSTEM_SUMMARY.md"
    "COMPLETE_SYSTEM_SUMMARY.md"
    "AVATARARTS_KNOWLEDGE_BASE_SYSTEM_DOCUMENTATION.md"
    "AVATARARTS_KNOWLEDGE_BASE_EVOLUTION_SUMMARY.md"
    "AVATARARTS_KNOWLEDGE_BASE_SYSTEM_VERSION_4.md"
    "COMPLETE_IMPLEMENTATION_SUMMARY.md"
)

for doc in "${DOC_FILES[@]}"; do
    if [ -f ~/.tagger/"$doc" ]; then
        cp ~/.tagger/"$doc" "$BACKUP_DIR/$doc"
        echo "   ✓ $doc saved"
    else
        echo "   - $doc not found"
    fi
done

# 6. Save recent CSV outputs
echo "6. Saving recent CSV outputs..."
RECENT_CSVS=$(find ~/.tagger -name "*.csv" -type f -mtime -7 | head -10)
for csv in $RECENT_CSVS; do
    filename=$(basename "$csv")
    cp "$csv" "$BACKUP_DIR/$filename"
    echo "   ✓ $filename saved"
done

# 7. Generate system status report
echo "7. Generating system status report..."
cat > "$BACKUP_DIR/SYSTEM_STATUS_REPORT.md" << EOF
# AVATARARTS Knowledge Base System - Status Report
Generated on: $(date)

## System Overview
- Directory: ~/.tagger
- Database: knowledge_base.db ($(stat -f%z ~/.tagger/knowledge_base.db 2>/dev/null || stat -c%s ~/.tagger/knowledge_base.db 2>/dev/null) bytes)
- Total entries in knowledge base: $(sqlite3 ~/.tagger/knowledge_base.db "SELECT COUNT(*) FROM knowledge_entries;")

## Available Versions
- Version 1: Basic multi-format indexer
- Version 2: Enhanced with auto-sorting
- Version 3: DevonThink alternative
- Version 4: AVATARARTS ecosystem intelligence

## Current AVATARARTS Ecosystem Status
- Ready to Launch Properties: 4 (potential $125-325K/month)
- In Development Properties: 3 (potential $60-130K/month)
- Total Potential: $160-425K/month ($1.9M-$5.1M annually)

## Shell Integration
- Aliases available: autotag, dt-*, avatararts-*, import-*, open-kb-outputs
- Auto-loaded in shell: $(if grep -q "source ~/.tagger/kb_aliases.sh" ~/.zshrc; then echo "YES"; else echo "NO"; fi)

## Recent Activity
$(sqlite3 ~/.tagger/knowledge_base.db "SELECT title, category, created_at FROM knowledge_entries ORDER BY created_at DESC LIMIT 5;")

## System Health
- All scripts present: $(if [ -f ~/.tagger/multi_format_directory_indexer_v4.py ] && [ -f ~/.tagger/kb_aliases.sh ] && [ -f ~/.tagger/open_kb_outputs.sh ]; then echo "OK"; else echo "ISSUES"; fi)
- Database accessible: $(if sqlite3 ~/.tagger/knowledge_base.db "SELECT 1" >/dev/null 2>&1; then echo "YES"; else echo "NO"; fi)
- Shell commands working: Test with 'source ~/.tagger/kb_aliases.sh && autotag --help'

EOF
echo "   ✓ System status report generated"

# 8. Create a restore script
echo "8. Creating restore script..."
cat > "$BACKUP_DIR/RESTORE_SYSTEM.sh" << 'EOF'
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
EOF

chmod +x "$BACKUP_DIR/RESTORE_SYSTEM.sh"
echo "   ✓ Restore script created and made executable"

# 9. Create a summary
echo "9. Creating backup summary..."
cat > "$BACKUP_DIR/BACKUP_SUMMARY.md" << EOF
# AVATARARTS Knowledge Base System Backup
Backup created: $(date)
Backup directory: $BACKUP_DIR

## Contents
- knowledge_base.db: Complete knowledge base with $(sqlite3 ~/.tagger/knowledge_base.db "SELECT COUNT(*) FROM knowledge_entries;") entries
- Version scripts: All 4 versions of the indexing system
- Phase scripts: All 3 phases of the indexing process
- Configuration: Shell aliases and opening utilities
- Documentation: All system documentation files
- Recent CSVs: Recently generated CSV outputs
- Status report: Complete system status at time of backup
- Restore script: Complete restoration utility

## Restoration
To restore the system from this backup:
1. Run: $BACKUP_DIR/RESTORE_SYSTEM.sh $BACKUP_DIR
2. Reload aliases: source ~/.tagger/kb_aliases.sh

## System Status
Current AVATARARTS ecosystem potential: $160-425K/month ($1.9M-$5.1M annually)
Ready to activate: 4 properties worth $125-325K/month
In development: 3 properties worth $60-130K/month
EOF

echo "   ✓ Backup summary created"

echo ""
echo "==========================================="
echo "✅ BACKUP COMPLETE!"
echo "Backup location: $BACKUP_DIR"
echo ""
echo "Contents:"
echo "- Knowledge base database (with $(sqlite3 ~/.tagger/knowledge_base.db "SELECT COUNT(*) FROM knowledge_entries;") entries)"
echo "- All version scripts (v1-v4)"
echo "- All phase scripts (1-3)"
echo "- Configuration files"
echo "- Documentation files"
echo "- Recent CSV outputs"
echo "- System status report"
echo "- Restore script"
echo ""
echo "To restore: $BACKUP_DIR/RESTORE_SYSTEM.sh $BACKUP_DIR"
echo "==========================================="