# Tagger - AVATARARTS Universal Directory Indexer

## Overview

Tagger is a comprehensive directory indexing and organization system that provides intelligent analysis, categorization, and management of any collection of files. This system replicates and enhances DevonThink functionality for cross-platform use.

## Features

### Tiered Indexing System
- **Phase 1**: Rapid Initial Scan (simple data points)
- **Phase 2**: Intelligent Organization (auto-classification and tagging)
- **Phase 3**: Advanced Intelligence (predictions and insights)

### Multi-Format Output
- **JSON**: Full structured data for programmatic use
- **CSV**: Spreadsheet-compatible format for AirTable, Excel, Google Sheets
- **Markdown**: Human-readable format for documentation
- **HTML**: Web-viewable format for presentations

### DevonThink Alternative
- **dt-index**: DevonThink-like directory indexing
- **dt-search**: Smart search across indexed content
- **dt-relations**: Relationship mapping between items
- **dt-ocr**: OCR processing for images/PDFs

### Universal Compatibility
- Works with any directory structure
- Handles various file types (images, documents, code, etc.)
- Adapts categorization based on directory content
- Maintains consistent indexing approach

## Installation

1. **Clone or copy** the Tagger directory to your system
2. **Add to shell profile** (optional but recommended):
   ```bash
   echo "source ~/Tagger/kb_aliases.sh" >> ~/.zshrc
   source ~/.zshrc
   ```

## Usage

### Basic Directory Indexing
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

### DevonThink Alternative Commands
```bash
# Index a directory with DevonThink-like intelligence
dt-index ~/Documents

# Search across all indexed content
dt-search "project report"

# Search within specific category
dt-search "financial data" "Business/Revenue"

# Find relationships between indexed items
dt-relations

# Export relationships to CSV for analysis
dt-relations ~/Desktop/relationships.csv

# Process images/PDFs with OCR for text extraction
dt-ocr ~/Scans
```

### Direct Script Usage
```bash
# Multi-format indexing
python3 ~/Tagger/multi_format_directory_indexer.py ~/Pictures pictures_scan "csv,md,html"

# OCR enhancement
~/Tagger/devonthink_ocr_enhancement.sh ~/Documents docs_ocr

# Tiered indexing
python3 ~/Tagger/run_tiered_indexing.py
```

## Key Components

### Core Scripts
- `multi_format_directory_indexer.py`: Main indexing system with multi-format output
- `devonthink_alternative.py`: DevonThink-like functionality
- `devonthink_ocr_enhancement.sh`: OCR processing for documents
- `run_tiered_indexing.py`: Complete tiered indexing system

### Knowledge Base
- `knowledge_base.db`: SQLite database storing all indexed information
- `kb_aliases.sh`: Shell aliases for easy access to functionality

### Output Files
- `*_phase1.json`: Raw scan data and basic metadata
- `*_phase2.json`: Categorized and tagged data
- `*_phase3.json`: Fully analyzed and enriched data
- `*_index.csv`: CSV format for spreadsheet applications
- `*_index.md`: Markdown format for documentation
- `*_index.html`: HTML format for web viewing

## Integration Capabilities

### With AirTable/Google Sheets
- Export to CSV format for direct import
- Compatible with spreadsheet applications
- Structured data for easy analysis

### With Shell Workflows
- Works with existing .zshrc/.bashrc functions
- Integrates with scan functions
- Compatible with existing automation workflows

### With Development Tools
- JSON output for programmatic access
- API-ready for custom integrations
- Structured data for development workflows

## Performance

The system is optimized for efficiency:
- Large directories processed in seconds
- Memory-efficient processing
- Incremental updates to knowledge base
- Preserves system resources during operation

## Use Cases

### Personal Organization
- Photo collections with intelligent tagging
- Document libraries with automatic organization
- Media files with metadata extraction

### Business Applications
- Automation tools inventory with business value assessment
- Content assets organization with usage predictions
- Code repositories with dependency analysis

### Development Workflows
- Project directory analysis with code structure mapping
- Asset library organization with usage patterns
- API collections with endpoint cataloging

## Troubleshooting

### Common Issues
- **Permission errors**: Ensure read access to target directory
- **Large directories**: System handles thousands of files efficiently
- **Special characters**: System handles Unicode and special characters

### Performance Tips
- **Sequential processing**: Large directories are handled efficiently
- **Memory usage**: Optimized for standard system resources
- **Format selection**: Choose only needed formats to save time

## Future Enhancements

- **TSV format**: Tab-separated values for better CSV compatibility
- **PDF reports**: Professional report generation
- **Direct integrations**: Direct export to AirTable, Google Sheets APIs
- **Custom templates**: User-defined HTML/markdown templates

## License

This system is provided as part of the AVATARARTS ecosystem for intelligent automation and digital marketing operations.

---

The Tagger system provides a powerful way to bring intelligent analysis to any collection of files while delivering results in the format that best suits your workflow and use case.