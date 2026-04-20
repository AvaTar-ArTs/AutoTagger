#!/bin/bash

# Quick Action Script to Save Knowledge Base Information to Database
# This script provides a convenient way to save information to the AVATARARTS knowledge database

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/save_knowledge_to_db.py"
DB_PATH="$HOME/avatararts-kb/knowledge_base.db"

# Create the database directory if it doesn't exist
mkdir -p "$HOME/.avatararts"

case "$1" in
    save)
        if [ $# -lt 3 ]; then
            echo "Usage: $0 save \"<title>\" \"<content>\" [category] [tag1 tag2 ...]"
            exit 1
        fi
        
        TITLE="$2"
        CONTENT="$3"
        CATEGORY="$4"
        
        # Collect remaining arguments as tags
        shift 4
        TAGS=("$@")
        
        # Build the command with tags if any
        if [ ${#TAGS[@]} -gt 0 ]; then
            python3 "$PYTHON_SCRIPT" --db-path "$DB_PATH" --title "$TITLE" --content "$CONTENT" --category "$CATEGORY" --tags "${TAGS[@]}"
        else
            python3 "$PYTHON_SCRIPT" --db-path "$DB_PATH" --title "$TITLE" --content "$CONTENT" --category "$CATEGORY"
        fi
        ;;
    search)
        if [ $# -lt 2 ]; then
            echo "Usage: $0 search \"<query>\" [category]"
            exit 1
        fi
        
        QUERY="$2"
        CATEGORY="$3"
        
        if [ -n "$CATEGORY" ]; then
            python3 "$PYTHON_SCRIPT" --db-path "$DB_PATH" --action search --query "$QUERY" --category "$CATEGORY"
        else
            python3 "$PYTHON_SCRIPT" --db-path "$DB_PATH" --action search --query "$QUERY"
        fi
        ;;
    *)
        echo "Usage:"
        echo "  $0 save \"<title>\" \"<content>\" [category] [tag1 tag2 ...]"
        echo "  $0 search \"<query>\" [category]"
        echo ""
        echo "Examples:"
        echo "  $0 save \"AEO/SEO/GEO Analysis\" \"Detailed analysis of optimization strategies\" \"analytics\" \"AEO\" \"SEO\" \"GEO\""
        echo "  $0 search \"content-awareness\""
        ;;
esac