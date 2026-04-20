# AVATARARTS Knowledge Base Tools
# Add these aliases to your .zshrc or .bashrc to easily save knowledge to the database

# Save knowledge to database
alias save-kb='~/AutoTagger/v3-dev/save_knowledge.sh'

# Capture current conversation to knowledge base
capture-kb() {
    if [ $# -lt 1 ]; then
        echo "Usage: capture-kb \"<title>\" [category] [tag1 tag2 ...]"
        return 1
    fi
    
    TITLE="$1"
    CATEGORY="${2:-conversation}"
    shift 2
    TAGS=("$@")
    
    echo "Enter content to save (press Ctrl+D when finished):"
    CONTENT=$(cat)
    
    if [ ${#TAGS[@]} -gt 0 ]; then
        python3 ~/AutoTagger/v3-dev/capture_conversation.py --title "$TITLE" --content "$CONTENT" --category "$CATEGORY" --tags "${TAGS[@]}"
    else
        python3 ~/AutoTagger/v3-dev/capture_conversation.py --title "$TITLE" --content "$CONTENT" --category "$CATEGORY"
    fi
}

# Quick save function for clipboard content
quick-save-kb() {
    if [ $# -lt 1 ]; then
        echo "Usage: quick-save-kb \"<title>\" [category]"
        return 1
    fi

    TITLE="$1"
    CATEGORY="${2:-general}"

    # On macOS, use pbpaste to get clipboard content
    if command -v pbpaste >/dev/null 2>&1; then
        CONTENT=$(pbpaste)
    else
        echo "Clipboard reading not supported on this system"
        echo "Enter content to save (press Ctrl+D when finished):"
        CONTENT=$(cat)
    fi

    python3 ~/AutoTagger/v3-dev/capture_conversation.py --title "$TITLE" --content "$CONTENT" --category "$CATEGORY"
}

# Enhanced clipboard capture with auto-tagging
enhanced-clip-capture() {
    echo "Capturing clipboard content with auto-analysis..."
    python3 ~/AutoTagger/v3-dev/enhanced_clipboard_capture.py
}

# Quick clipboard capture with custom title
quick-clip-capture() {
    if [ $# -lt 1 ]; then
        echo "Usage: quick-clip-capture \"<title>\" [category]"
        return 1
    fi

    TITLE="$1"
    CATEGORY="$2"

    if [ -n "$CATEGORY" ]; then
        python3 ~/AutoTagger/v3-dev/enhanced_clipboard_capture.py --title "$TITLE" --category "$CATEGORY"
    else
        python3 ~/AutoTagger/v3-dev/enhanced_clipboard_capture.py --title "$TITLE"
    fi
}

# Auto-sort clipboard content
auto-sort-clip() {
    if [ $# -gt 0 ]; then
        python3 ~/AutoTagger/v3-dev/auto_sorter.py --title "$1" --verbose
    else
        python3 ~/AutoTagger/v3-dev/auto_sorter.py --verbose
    fi
}

# Force category for clipboard content
force-category() {
    if [ $# -lt 2 ]; then
        echo "Usage: force-category \"<category>\" \"<title>\""
        return 1
    fi

    CATEGORY="$1"
    TITLE="$2"

    python3 ~/AutoTagger/v3-dev/auto_sorter.py --force-category "$CATEGORY" --title "$TITLE" --verbose
}

# Hybrid intelligence system
hybrid-capture() {
    if [ $# -gt 0 ]; then
        python3 ~/AutoTagger/v3-dev/hybrid_intelligence_system.py --title "$1" --verbose
    else
        python3 ~/AutoTagger/v3-dev/hybrid_intelligence_system.py --verbose
    fi
}

# Search the knowledge base
kb-search() {
    if [ $# -lt 1 ]; then
        echo "Usage: kb-search \"<query>\" [category]"
        return 1
    fi

    QUERY="$1"
    CATEGORY="$2"

    if [ -n "$CATEGORY" ]; then
        python3 ~/AutoTagger/v3-dev/hybrid_intelligence_system.py --action search --query "$QUERY" --category "$CATEGORY"
    else
        python3 ~/AutoTagger/v3-dev/hybrid_intelligence_system.py --action search --query "$QUERY"
    fi
}

# Universal directory indexer (autotag)
autotag() {
    if [ $# -eq 0 ]; then
        echo "Usage: autotag <directory> [prefix]"
        return 1
    fi
    python3 ~/AutoTagger/current/autotagger.py "$1" --prefix "${2:-$(basename "$1")_scan}"
}
# DevonThink-like functionality
dt-index() {
    if [ $# -eq 0 ]; then
        echo "Usage: dt-index <directory> [prefix]"
        echo "DevonThink-like indexing with intelligent categorization"
        echo "Example: dt-index ~/Documents"
        echo "Example: dt-index ~/Scans scans_dt"
        return 1
    fi

    DIRECTORY="$1"
    PREFIX="${2:-$(basename "$DIRECTORY" | sed 's/[^a-zA-Z0-9]/_/g')_dt}"

    python3 ~/AutoTagger/v3-dev/devonthink_alternative.py index --directory "$DIRECTORY" --prefix "$PREFIX"
}

dt-search() {
    if [ $# -eq 0 ]; then
        echo "Usage: dt-search <query> [category]"
        echo "DevonThink-like search across indexed content"
        echo "Example: dt-search 'project report'"
        echo "Example: dt-search 'financial data' 'Business/Revenue'"
        return 1
    fi

    QUERY="$1"
    CATEGORY="$2"

    if [ -n "$CATEGORY" ]; then
        python3 ~/AutoTagger/v3-dev/devonthink_alternative.py search --query "$QUERY" --category "$CATEGORY"
    else
        python3 ~/AutoTagger/v3-dev/devonthink_alternative.py search --query "$QUERY"
    fi
}

dt-relations() {
    if [ $# -eq 0 ]; then
        echo "Usage: dt-relations [output_file]"
        echo "Find relationships between indexed items (DevonThink-style)"
        echo "Example: dt-relations"
        echo "Example: dt-relations ~/Desktop/relationships.csv"
        return 1
    fi

    if [ $# -eq 1 ]; then
        python3 ~/AutoTagger/v3-dev/devonthink_alternative.py relationships --output "$1"
    else
        python3 ~/AutoTagger/v3-dev/devonthink_alternative.py relationships
    fi
}

dt-ocr() {
    if [ $# -eq 0 ]; then
        echo "Usage: dt-ocr <directory> [prefix]"
        echo "DevonThink-like OCR processing for images/PDFs"
        echo "Example: dt-ocr ~/Scans"
        echo "Example: dt-ocr ~/Documents docs_ocr"
        return 1
    fi

    DIRECTORY="$1"
    PREFIX="${2:-$(basename "$DIRECTORY" | sed 's/[^a-zA-Z0-9]/_/g')_ocr}"

    ~/AutoTagger/v3-dev/devonthink_ocr_enhancement.sh "$DIRECTORY" "$PREFIX"
}