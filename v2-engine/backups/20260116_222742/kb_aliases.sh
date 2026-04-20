# AVATARARTS Knowledge Base Tools
# Add these aliases to your .zshrc or .bashrc to easily save knowledge to the database

# Save knowledge to database
alias save-kb='~/AutoTagger/v2-engine/save_knowledge.sh'

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
        python3 ~/AutoTagger/v2-engine/capture_conversation.py --title "$TITLE" --content "$CONTENT" --category "$CATEGORY" --tags "${TAGS[@]}"
    else
        python3 ~/AutoTagger/v2-engine/capture_conversation.py --title "$TITLE" --content "$CONTENT" --category "$CATEGORY"
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

    python3 ~/AutoTagger/v2-engine/capture_conversation.py --title "$TITLE" --content "$CONTENT" --category "$CATEGORY"
}

# Enhanced clipboard capture with auto-tagging
enhanced-clip-capture() {
    echo "Capturing clipboard content with auto-analysis..."
    python3 ~/AutoTagger/v2-engine/enhanced_clipboard_capture.py
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
        python3 ~/AutoTagger/v2-engine/enhanced_clipboard_capture.py --title "$TITLE" --category "$CATEGORY"
    else
        python3 ~/AutoTagger/v2-engine/enhanced_clipboard_capture.py --title "$TITLE"
    fi
}

# Auto-sort clipboard content
auto-sort-clip() {
    if [ $# -gt 0 ]; then
        python3 ~/AutoTagger/v2-engine/auto_sorter.py --title "$1" --verbose
    else
        python3 ~/AutoTagger/v2-engine/auto_sorter.py --verbose
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

    python3 ~/AutoTagger/v2-engine/auto_sorter.py --force-category "$CATEGORY" --title "$TITLE" --verbose
}

# Hybrid intelligence system
hybrid-capture() {
    if [ $# -gt 0 ]; then
        python3 ~/AutoTagger/v2-engine/hybrid_intelligence_system.py --title "$1" --verbose
    else
        python3 ~/AutoTagger/v2-engine/hybrid_intelligence_system.py --verbose
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
        python3 ~/AutoTagger/v2-engine/hybrid_intelligence_system.py --action search --query "$QUERY" --category "$CATEGORY"
    else
        python3 ~/AutoTagger/v2-engine/hybrid_intelligence_system.py --action search --query "$QUERY"
    fi
}

# Universal directory indexer (autotag)
autotag() {
    if [ $# -eq 0 ]; then
        echo "Usage: autotag <directory> [output_prefix] [formats]"
        echo "Formats: json (default), csv, md, html, or combinations like 'json,csv,md'"
        echo "Example: autotag ~/Pictures pictures_scan"
        echo "Example: autotag ~/Documents docs_scan json,csv"
        echo "Example: autotag ~/AVATARARTS/Automations automations_scan json,csv,md,html"
        return 1
    fi

    DIRECTORY="$1"
    if [ $# -ge 2 ]; then
        PREFIX="$2"
    else
        PREFIX="$(basename "$DIRECTORY" | sed 's/[^a-zA-Z0-9]/_/g')_scan"
    fi

    if [ $# -eq 3 ]; then
        FORMAT="$3"
        python3 ~/.tagger/multi_format_directory_indexer_v3.py "$DIRECTORY" "$PREFIX" "$FORMAT"
    else
        python3 ~/.tagger/multi_format_directory_indexer_v3.py "$DIRECTORY" "$PREFIX"
    fi
}

# Import clean directory scan CSV
import-clean-csv() {
    if [ $# -ne 1 ]; then
        echo "Usage: import-clean-csv <csv_file_path>"
        echo "Imports CSV from clean directory scans into the knowledge base"
        echo "Example: import-clean-csv ~/clean/audio-07-24-15:56.csv"
        return 1
    fi

    CSV_FILE="$1"
    python3 ~/.tagger/multi_format_directory_indexer_v3.py --import-csv "$CSV_FILE"
}

# Import clean directory config
import-clean-config() {
    if [ $# -ne 1 ]; then
        echo "Usage: import-clean-config <config_file_path>"
        echo "Imports exclusion patterns from clean directory config"
        echo "Example: import-clean-config ~/clean/config.py"
        return 1
    fi

    CONFIG_FILE="$1"
    python3 ~/.tagger/multi_format_directory_indexer_v3.py --import-config "$CONFIG_FILE"
}

# Open knowledge base outputs
open-kb-outputs() {
    if [ $# -lt 1 ]; then
        echo "Usage: open-kb-outputs <option> [search_term]"
        echo "Options:"
        echo "  csv [search_term]  - Open recent CSV files (default: 'index')"
        echo "  db                 - Open the knowledge base SQLite database"
        echo "  all                - Open both recent CSVs and the database"
        echo "Examples:"
        echo "  open-kb-outputs csv"
        echo "  open-kb-outputs csv automation"
        echo "  open-kb-outputs db"
        echo "  open-kb-outputs all"
        return 1
    fi

    ~/.tagger/open_kb_outputs.sh "$@"
}

# Import AVATARARTS ecosystem data
import-avatararts-ecosystem() {
    echo "Importing AVATARARTS ecosystem data for intelligent activation..."
    python3 ~/.tagger/multi_format_directory_indexer_v4.py --import-ecosystem
}

# Analyze AVATARARTS activation opportunities
analyze-avatararts-opportunities() {
    echo "Analyzing AVATARARTS ecosystem for activation opportunities..."
    python3 ~/.tagger/multi_format_directory_indexer_v4.py --analyze-opportunities
}

# Generate AVATARARTS activation plan
generate-avatararts-plan() {
    echo "Generating AVATARARTS activation plan..."
    python3 ~/.tagger/multi_format_directory_indexer_v4.py --generate-plan
}

# Enhanced AVATARARTS commands
avatararts-activate() {
    if [ $# -lt 1 ]; then
        echo "Usage: avatararts-activate <directory> [prefix] [formats]"
        echo "Activates AVATARARTS ecosystem analysis on a directory"
        echo "Example: avatararts-activate ~/AVATARARTS"
        echo "Example: avatararts-activate ~/AVATARARTS/01_TOOLS tools_scan json,csv"
        return 1
    fi

    DIRECTORY="$1"
    PREFIX="${2:-$(basename "$DIRECTORY" | sed 's/[^a-zA-Z0-9]/_/g')_avatararts}"

    if [ $# -eq 3 ]; then
        FORMATS="$3"
        python3 ~/.tagger/multi_format_directory_indexer_v4.py "$DIRECTORY" "$PREFIX" "$FORMATS"
    else
        python3 ~/.tagger/multi_format_directory_indexer_v4.py "$DIRECTORY" "$PREFIX"
    fi

    # Automatically suggest next steps for AVATARARTS activation
    echo ""
    echo "💡 Next steps for AVATARARTS activation:"
    echo "   - analyze-avatararts-opportunities"
    echo "   - generate-avatararts-plan"
    echo "   - dt-search 'activation opportunity'"
}

# AVATARARTS ecosystem status
avatararts-status() {
    echo "Checking AVATARARTS ecosystem status..."
    dt-search "AVATARARTS" "Business Strategy"
    dt-search "activation" "Ready to Launch"
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

    python3 ~/.tagger/devonthink_alternative.py index --directory "$DIRECTORY" --prefix "$PREFIX"
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
        python3 ~/.tagger/devonthink_alternative.py search --query "$QUERY" --category "$CATEGORY"
    else
        python3 ~/.tagger/devonthink_alternative.py search --query "$QUERY"
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
        python3 ~/.tagger/devonthink_alternative.py relationships --output "$1"
    else
        python3 ~/.tagger/devonthink_alternative.py relationships
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

    ~/.tagger/devonthink_ocr_enhancement.sh "$DIRECTORY" "$PREFIX"
}