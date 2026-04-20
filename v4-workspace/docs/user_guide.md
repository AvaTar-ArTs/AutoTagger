# AutoTag User Guide

## Overview

AutoTag is an intelligent tagging and categorization system for AVATARARTS automation tools. It helps organize, categorize, and assess the business value of automation scripts and tools, with automatic CSV export and file opening for easy analysis.

## Quick Start

1. **Setup AutoTag**:
   ```bash
   cd /Users/steven/AutoTag
   ./setup_autotag.sh
   ```

2. **Run AutoTag on a directory**:
   ```bash
   ./autotag.sh /path/to/your/automation/directory [optional_output_name]
   ```

3. **View Results**:
   - The CSV results file will automatically open in your default application
   - Additional detailed results will be in `/Users/steven/AutoTag/output/[output_name]/`

## Understanding the Output

AutoTag produces four main outputs:

### Phase 1: Rapid Scan
- Basic catalog of all directories and files
- Identification of potential automation tools
- Basic metadata extraction

### Phase 2: Intelligent Organization
- Categorization of tools (e.g., "AI/Automation", "Content Creation", "Code/Scripts")
- Auto-generated tags based on content
- Confidence scores for categorizations

### Phase 3: Advanced Intelligence
- Predicted business value scores (0-10 scale)
- Integration potential identification
- Relationship mapping between tools
- Extracted insights

### Phase 4: CSV Export & Auto-Open
- **Automatic CSV conversion** of key metrics for spreadsheet analysis
- **Automatic file opening** of the CSV results in your default application
- **Easy access** to the most important metrics without parsing JSON

## CSV Output Columns

The automatically generated CSV file includes these key columns:
- `name`: Tool name
- `path`: Full path to the tool
- `size_mb`: Size in megabytes
- `created`: Creation timestamp
- `modified`: Last modification timestamp
- `primary_type`: Primary type classification
- `description`: Tool description (truncated to 200 characters)
- `intelligent_category`: AI-assigned category
- `confidence_score`: Confidence in categorization (0-1 scale)
- `predicted_business_value`: Predicted business value (0-10 scale)
- `integration_potential_has_potential`: Boolean for integration potential

## Use Cases

### 1. Inventory Management
Use AutoTag to catalog your entire automation library:
```bash
./autotag.sh /Users/steven/pythons python_scripts_inventory
```

### 2. Value Assessment
Identify high-value automation tools:
```bash
./autotag.sh /Users/steven/AVATARARTS/Automations high_value_assessment
# The CSV will automatically open showing business value scores
```

### 3. Organization Planning
Understand how your automation tools are categorized:
```bash
./autotag.sh /Users/steven/AVATARARTS/Automations organization_plan
```

### 4. Portfolio Analysis
Analyze your automation portfolio with spreadsheet tools:
```bash
./autotag.sh /Users/steven/AVATARARTS/Automations portfolio_analysis
# The CSV will open automatically in Excel, Numbers, or your preferred app
```

## Advanced Usage

### Skip Auto-Opening
If you don't want the CSV file to automatically open:
```bash
./autotag.sh /Users/steven/pythons my_analysis --no-open
```

### Custom Output Names
Use descriptive names for your analysis runs:
```bash
./autotag.sh /Users/steven/AVATARARTS/Automations marketing_automation_audit
./autotag.sh /Users/steven/pythons ai_tools_inventory
```

## Configuration

The system can be configured via `/Users/steven/AutoTag/config/autotag_config.json`.

## Troubleshooting

### Common Issues

1. **Virtual Environment Not Found**
   - Run `./setup_autotag.sh` to create the virtual environment

2. **Permission Errors**
   - Ensure the runner script is executable: `chmod +x autotag.sh`

3. **Large Directory Processing**
   - For very large directories, consider running on subsets first

4. **CSV Auto-Opening Fails**
   - The system will display the file path for manual access
   - Check that you have a default application for CSV files

5. **No Results in CSV**
   - If no automation tools are detected, the CSV may be empty
   - Ensure your target directory contains recognizable automation tools

## Best Practices

1. **Start Small**: Test on a small directory before running on large collections
2. **Use Descriptive Names**: Give meaningful names to your analysis runs
3. **Regular Analysis**: Periodically re-analyze growing automation libraries
4. **Review Results**: Check the categorization accuracy and adjust as needed
5. **Leverage CSV**: Use the automatically opened CSV for further analysis in spreadsheets
6. **Track Changes**: Run periodic analyses to track evolution of your automation library

## Integration with AVATARARTS

AutoTag integrates with the broader AVATARARTS ecosystem by:
- Providing structured data about automation tools
- Supporting the content-awareness intelligence system
- Enabling better organization and discovery of automation capabilities
- Facilitating the activation of the 95% built AVATARARTS system
- Making results easily accessible through CSV export for business analysis
