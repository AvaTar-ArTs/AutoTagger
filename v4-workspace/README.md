# AutoTag - AVATARARTS Automation Tagging System

AutoTag is an intelligent tagging and categorization system for AVATARARTS automation tools. It uses a three-phase approach to analyze, categorize, and assign business value to automation tools, with automatic CSV export and file opening.

## Features

- **Three-Phase Analysis**: Rapid scan → Intelligent organization → Advanced intelligence
- **Smart Categorization**: Automatically categorizes tools based on functionality
- **Business Value Prediction**: Assigns predicted business value scores
- **Integration Potential**: Identifies potential tool integrations
- **Scalable Processing**: Efficiently handles large automation libraries
- **CSV Export**: Automatically converts results to CSV format for easy analysis
- **Auto-Open**: Automatically opens the CSV results file after completion
- **Flexible Output**: Customizable output names and locations

## Prerequisites

- Python 3.8+
- Unix-like environment (macOS, Linux)

## Setup

1. Run the setup script:
   ```bash
   ./setup_autotag.sh
   ```

## Usage

1. Run AutoTag on a directory:
   ```bash
   ./autotag.sh /path/to/target/directory [output_name]
   ```

2. Examples:
   ```bash
   # Analyze the pythons directory
   ./autotag.sh /Users/steven/pythons my_python_analysis

   # Analyze with default timestamped output name
   ./autotag.sh /Users/steven/AVATARARTS/Automations

   # Run without auto-opening the results file
   ./autotag.sh /Users/steven/pythons my_analysis --no-open
   ```

## Output

Results are stored in `/Users/steven/AutoTag/output/[run_name]/` with:
- Phase 1: Basic cataloging and metadata
- Phase 2: Intelligent categorization and tagging
- Phase 3: Advanced analysis and predictions
- **NEW**: `[run_name]_results.csv`: Automatically generated CSV with key metrics

CSV columns include:
- `name`: Tool name
- `path`: Full path to the tool
- `size_mb`: Size in megabytes
- `created`: Creation timestamp
- `modified`: Last modification timestamp
- `primary_type`: Primary type classification
- `description`: Tool description
- `intelligent_category`: AI-assigned category
- `confidence_score`: Confidence in categorization
- `predicted_business_value`: Predicted business value (0-10)
- `integration_potential_has_potential`: Boolean for integration potential

## Architecture

The system follows a three-phase approach:

1. **Phase 1: Rapid Initial Scan**
   - Catalogs all directories and files
   - Identifies potential automation tools
   - Extracts basic metadata

2. **Phase 2: Intelligent Organization**
   - Categorizes tools based on content
   - Generates relevant tags
   - Assigns confidence scores

3. **Phase 3: Advanced Intelligence**
   - Predicts business value
   - Identifies integration potential
   - Extracts insights and relationships

4. **Phase 4: CSV Export & Auto-Open**
   - Converts JSON results to CSV format
   - Automatically opens the CSV file in your default application
   - Makes results easily accessible for analysis

## Directory Structure

```
AutoTag/
├── scripts/                 # Core Python scripts
├── config/                  # Configuration files
├── data/                    # Data files and database
├── output/                  # Analysis results (including CSV files)
├── logs/                    # Log files
├── docs/                    # Documentation
├── autotag.sh              # Main runner script (with auto-open feature)
├── setup_autotag.sh        # Setup script
└── README.md               # This file
```

## Integration with AVATARARTS

AutoTag is designed to work seamlessly with the AVATARARTS ecosystem, providing intelligent analysis of automation tools to support the content-awareness intelligence system. The CSV export functionality makes it easy to integrate results with spreadsheet applications and business intelligence tools.

## Documentation

Complete documentation is available in the `/docs/` directory:
- `user_guide.md`: Basic usage instructions
- `autotag_comprehensive_guide.md`: Advanced usage, code snippets, and integration strategies
- `autotag_csv_enhancement_summary.md`: Details about CSV functionality
- `autotag_implementation_summary.md`: Implementation overview
- `avatararts_noi_knowledge_base.html`: Noi app integration knowledge base

## Reports & Research

Analysis reports and research documents are in the `/reports/` directory:
- `tiered_indexing_analysis.md`: Performance and capability analysis
- `pythons_directory_scan_report.md`: Detailed scan of pythons directory
- `avatararts_noi_handoff_document.md`: Noi app handoff documentation
- `devonthink_alternatives_research.md`: DevonThink alternatives research
- `avatars_knowledge_management_integration.md`: Knowledge management strategies
- `devonthink_alternatives_complete_summary.md`: DevonThink alternatives summary

## System Organization

For a complete overview of the system structure, see: `ORGANIZATION_INDEX.md`

## Auto-Open Feature

After completion, AutoTag automatically opens the CSV results file using your system's default application:
- **macOS**: Uses `open` command
- **Windows**: Uses `os.startfile` function
- **Linux**: Uses `xdg-open` command

If auto-opening fails, the system will display the file path for manual access.
