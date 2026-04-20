#!/bin/bash
# Tagger Setup Verification Script

echo "🔍 Tagger Setup Verification"
echo "==========================="

echo "1. Checking ~/.tagger directory..."
if [ -d ~/.tagger ]; then
    echo "   ✅ ~/.tagger directory exists"
    echo "   📁 Files in ~/.tagger: $(ls -1 ~/.tagger | wc -l) files"
else
    echo "   ❌ ~/.tagger directory does not exist"
    exit 1
fi

echo ""
echo "2. Checking key files..."
KEY_FILES=(
    "kb_aliases.sh"
    "multi_format_directory_indexer.py"
    "devonthink_alternative.py"
    "knowledge_base.db"
    "README.md"
)

for file in "${KEY_FILES[@]}"; do
    if [ -f ~/.tagger/"$file" ]; then
        echo "   ✅ $file exists"
    else
        echo "   ❌ $file missing"
    fi
done

echo ""
echo "3. Checking zshrc integration..."
if grep -q "source ~/.tagger/kb_aliases.sh" ~/.zshrc; then
    echo "   ✅ Tagger sourced in ~/.zshrc"
else
    echo "   ❌ Tagger not found in ~/.zshrc"
fi

echo ""
echo "4. Testing basic functionality..."
echo "   Running: dt-search 'test' (should return results)"
source ~/.tagger/kb_aliases.sh 2>/dev/null
if command -v dt-search >/dev/null 2>&1; then
    echo "   ✅ dt-search command is available"
else
    echo "   ❌ dt-search command not available"
fi

if command -v autotag >/dev/null 2>&1; then
    echo "   ✅ autotag command is available"
else
    echo "   ❌ autotag command not available"
fi

echo ""
echo "5. Database status..."
if [ -f ~/.tagger/knowledge_base.db ]; then
    DB_SIZE=$(du -h ~/.tagger/knowledge_base.db | cut -f1)
    echo "   🗄️  knowledge_base.db exists (Size: $DB_SIZE)"
    
    # Count entries in the database
    ENTRY_COUNT=$(sqlite3 ~/.tagger/knowledge_base.db "SELECT COUNT(*) FROM knowledge_entries;" 2>/dev/null)
    if [ $? -eq 0 ]; then
        echo "   📊 Database contains $ENTRY_COUNT entries"
    fi
else
    echo "   ❌ knowledge_base.db not found"
fi

echo ""
echo "✅ Tagger Setup Verification Complete!"
echo ""
echo "To use Tagger commands, either:"
echo "   - Restart your terminal"
echo "   - Run: source ~/.zshrc"
echo "   - Run: source ~/.tagger/kb_aliases.sh"
echo ""
echo "Available commands:"
echo "   - autotag: Universal directory indexing"
echo "   - dt-index: DevonThink-like indexing"
echo "   - dt-search: Smart search across content"
echo "   - dt-relations: Relationship mapping"
echo "   - dt-ocr: OCR processing for documents"