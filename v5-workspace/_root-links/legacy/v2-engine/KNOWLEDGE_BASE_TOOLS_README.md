# AVATARARTS Knowledge Base Tools

This directory contains tools for saving and managing knowledge base information in a SQLite database.

## Files

- `save_knowledge_to_db.py`: Python script for saving knowledge entries
- `save_knowledge.sh`: Shell wrapper for easy command-line usage
- `capture_conversation.py`: Advanced script for capturing conversation data
- `kb_aliases.sh`: Shell aliases for quick access
- `README.md`: This file

## Setup

To use these tools, you can either:

1. Source the aliases in your shell:
   ```bash
   source ~/AutoTagger/v2-engine/kb_aliases.sh
   ```

2. Or add the aliases to your `.zshrc` or `.bashrc`:
   ```bash
   echo "source ~/AutoTagger/v2-engine/kb_aliases.sh" >> ~/.zshrc
   source ~/.zshrc
   ```

## Usage

### Basic Saving

Using the shell script:
```bash
# Save information
~/AutoTagger/v2-engine/save_knowledge.sh save "My Title" "Content goes here..." "category" "tag1" "tag2"

# Search for information
~/AutoTagger/v2-engine/save_knowledge.sh search "query" "optional_category"
```

### Using Aliases

After setting up the aliases:

```bash
# Save information
save-kb save "My Title" "Content goes here..." "category" "tag1" "tag2"

# Capture conversation with interactive input
capture-kb "Conversation Title" "category" "tag1" "tag2"

# Quick save from clipboard (macOS)
quick-save-kb "Title" "category"
```

### Direct Python Usage

```bash
# Save information
python3 ~/AutoTagger/v2-engine/capture_conversation.py --title "Title" --content "Content here" --category "category" --tags "tag1" "tag2"

# Search information
python3 ~/AutoTagger/v2-engine/capture_conversation.py --action search --query "search term"
```

### Enhanced Clipboard Capture (NEW!)

The system now includes enhanced clipboard capture with auto-formatting preservation and auto-tagging:

```bash
# Capture clipboard content with auto-analysis (no title needed)
enhanced-clip-capture

# Capture clipboard content with custom title
quick-clip-capture "My Title"

# Capture clipboard content with custom title and category
quick-clip-capture "My Title" "category"
```

The enhanced capture automatically:
- Retrieves content from clipboard
- Preserves formatting (Markdown, HTML, etc.)
- Analyzes content to generate relevant tags
- Auto-detects category based on content
- Extracts key insights

### Auto-Sorting and Content Analysis (NEW!)

The system now includes advanced auto-sorting capabilities:

```bash
# Auto-sort clipboard content with analysis
auto-sort-clip

# Auto-sort with custom title
auto-sort-clip "My Title"

# Force a specific category
force-category "Code/Scripts" "Title for code entry"

# Force category with clipboard content
force-category "Business/Revenue"
```

The auto-sorter automatically:
- Analyzes content to determine best category
- Calculates confidence scores for categorization
- Extracts key entities (technical terms, platforms, tools)
- Finds related entries in the database
- Provides detailed analysis report

### Hybrid Intelligence System (ADVANCED!)

The system now includes a hybrid intelligence system that combines original automation capabilities with new knowledge base features:

```bash
# Capture content with full hybrid analysis
hybrid-capture

# Capture with custom title
hybrid-capture "My Title"

# Search the knowledge base
kb-search "query"

# Search within a specific category
kb-search "query" "Code/Scripts"
```

The hybrid system combines:
- Original content analysis and categorization
- Advanced entity extraction
- Insight generation from content
- Knowledge base search capabilities
- Confidence scoring for all analyses

### Universal Directory Indexer (autotag)

The system now includes a universal directory indexer that can process any directory with the tiered indexing system and output in multiple formats:

```bash
# Index any directory with automatic prefix (JSON output by default)
autotag ~/Pictures

# Index with custom prefix
autotag ~/Documents docs_scan

# Index with custom prefix and specific format
autotag ~/Pictures pictures_scan csv

# Index with multiple output formats
autotag ~/Documents docs_scan "csv,md,html"

# Index with custom prefix (for better organization)
autotag ~/AVATARARTS/Automations automations_scan "json,csv,md,html"
```

The autotag command will:
- Scan the directory and identify all files/subdirectories
- Apply intelligent categorization and tagging
- Perform advanced analysis with predictive intelligence
- Add all results to the knowledge base
- Generate indexed data files in specified formats (JSON, CSV, Markdown, HTML)
- Create user-friendly outputs for different use cases

## Database Location

The knowledge base is stored in: `~/AutoTagger/v2-engine/knowledge_base.db`

## Features

- **Knowledge Entries**: Store titles, content, categories, and tags
- **Conversation Logs**: Track conversation history
- **Analysis Results**: Store analytical insights
- **Insights Extraction**: Automatically extract key points from content
- **Search Functionality**: Find information by content or category
- **Flexible Tagging**: Organize information with custom tags