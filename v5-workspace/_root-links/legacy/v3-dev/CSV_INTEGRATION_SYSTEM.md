# AVATARARTS Knowledge Base - CSV Integration System

## Overview

The CSV Integration System provides bidirectional data flow between the AVATARARTS Knowledge Base and external tools like AirTable, Google Sheets, and scan functions. This system enables:

1. **Import**: Bring data from scan functions and other sources into the knowledge base
2. **Export**: Send indexed data to CSV for use in spreadsheets and external tools
3. **Integration**: Connect with your existing workflows and tools

## System Components

### 1. CSV Import Module
- Imports data from scan functions (like `scan(python ~/clean)`)
- Converts CSV format to knowledge base entries
- Preserves metadata and relationships
- Supports bulk import operations

### 2. CSV Export Module
- Exports knowledge base data to CSV format
- Compatible with AirTable, Google Sheets, Excel
- Preserves all metadata and relationships
- Supports filtered exports by category

### 3. Scan Function Integration
- Simulates the output format of your `.zshrc` scan functions
- Converts directory metadata to structured CSV
- Integrates with existing automation workflows

## Usage Examples

### Import Data from .zshrc Scan Functions
```bash
# Use your existing scan functions from ~/.zshrc
# Examples of common scan functions:
scan-all      # Scan all file types
scan-img      # Scan image files
scan-docs     # Scan document files
scan-audio    # Scan audio files
scan-video    # Scan video files
scan-code     # Scan code files

# Redirect output to CSV for import
scan-all > scan_output.csv

# Import into knowledge base
python3 ~/AutoTagger/v3-dev/csv_import_export.py import --csv-path scan_output.csv
```

### Export Data for External Tools
```bash
# Export all data to CSV
python3 ~/AutoTagger/v3-dev/csv_import_export.py export --csv-path all_data.csv

# Export specific category
python3 ~/AutoTagger/v3-dev/csv_import_export.py export --csv-path ai_tools.csv --category "AI/Automation"
```

### Create Sample Data
```bash
# Generate sample CSV in the expected format
python3 ~/AutoTagger/v3-dev/csv_import_export.py sample
```

## CSV Format Specification

### Import Format
The system expects CSV files with these columns:
- `name` or `title`: Name of the entry/tool
- `description` or `content`: Description of the entry
- `category` or `type`: Category for classification
- `tags` or `keywords`: Comma-separated tags
- `path`: File path (optional)
- `size_mb`: Size in MB (optional)
- `created`: Creation date (optional)
- `modified`: Modification date (optional)

### Export Format
The system exports CSV files with these columns:
- `id`: Unique identifier
- `title`: Entry title
- `content`: Entry content/description
- `category`: Classification category
- `tags`: Comma-separated tags
- `source`: Source of the entry
- `created_at`: Creation timestamp

## Integration with .zshrc Scan Functions

To integrate with your existing scan functions in `.zshrc`:

1. **Use your existing scan functions** that output structured data:
```bash
# Typical scan functions in ~/.zshrc might look like:
scan-all() {
    echo "name,path,type,size_mb,description,tags,created,modified"
    # Your existing scan logic that outputs structured data
    # This could be adapted to output CSV format
}

scan-img() {
    echo "name,path,type,size_mb,description,tags,created,modified"
    # Image-specific scanning logic
}

scan-docs() {
    echo "name,path,type,size_mb,description,tags,created,modified"
    # Document-specific scanning logic
}
```

2. **Import the results** into the knowledge base:
```bash
scan ~/AVATARARTS/Automations
python3 ~/AutoTagger/v3-dev/csv_import_export.py import --csv-path /tmp/scan_output.csv
```

## AirTable/Google Sheets Integration

### For AirTable:
1. Export data: `python3 csv_import_export.py export --csv-path data.csv`
2. Import into AirTable via the "Import" feature
3. Use AirTable's automation features to sync back to CSV if needed

### For Google Sheets:
1. Export data: `python3 csv_import_export.py export --csv-path data.csv`
2. Upload to Google Drive and open with Google Sheets
3. Use Google Sheets' import features or Google Apps Script for automation

## Benefits

### Workflow Integration
- Seamlessly integrates with existing scan functions
- Preserves your current automation workflows
- Adds intelligence layer without disruption

### Data Portability
- Export to any CSV-compatible tool
- Import from various data sources
- Maintain data integrity across systems

### Scalability
- Handle large datasets efficiently
- Batch processing capabilities
- Support for filtered operations

## Advanced Usage

### Custom Field Mapping
For non-standard CSV formats, you can extend the import function to map custom fields to knowledge base properties.

### Scheduled Sync
Set up cron jobs to regularly sync between your scan functions and the knowledge base:
```bash
# Sync every hour
0 * * * * scan ~/AVATARARTS/Automations && python3 ~/AutoTagger/v3-dev/csv_import_export.py import --csv-path /tmp/scan_output.csv
```

### Filtered Operations
Use category filters for targeted imports/exports:
```bash
# Export only AI tools
python3 ~/AutoTagger/v3-dev/csv_import_export.py export --csv-path ai_tools.csv --category "AI/Automation"

# Import with specific source tagging
# (Modify the import function to add custom source tags)
```

## Best Practices

1. **Consistent Naming**: Use consistent column names in your scan output
2. **Data Validation**: Validate CSV data before import
3. **Incremental Updates**: Use timestamps to identify new/updated entries
4. **Backup**: Regularly backup the knowledge base before bulk operations
5. **Testing**: Test import/export with small datasets first

## Error Handling

The system includes:
- Input validation for CSV format
- Graceful handling of malformed data
- Progress reporting for large operations
- Transaction-based database operations

## Future Enhancements

1. **Direct API Integration**: Connect directly to AirTable/Google Sheets APIs
2. **Real-time Sync**: WebSocket-based live synchronization
3. **Advanced Filtering**: Complex query-based imports/exports
4. **Data Transformation**: Custom transformation rules for field mapping

The CSV Integration System provides a robust bridge between your existing automation workflows and the intelligent knowledge management capabilities of the AVATARARTS system, enabling seamless data flow and enhanced productivity.