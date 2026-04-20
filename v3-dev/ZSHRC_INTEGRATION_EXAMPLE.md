# Integration Example for ~/.zshrc Scan Functions

If you have scan functions in your ~/.zshrc file, here's how to integrate them with the AVATARARTS Knowledge Base:

## Example .zshrc Scan Functions

Add these functions to your ~/.zshrc file to output in CSV format:

```bash
# Enhanced scan-all function that outputs CSV
scan-all-csv() {
    local target_dir="${1:-.}"
    echo "name,path,type,size_mb,description,tags,created,modified"
    
    find "$target_dir" -maxdepth 2 -type d | while read dir; do
        [ "$dir" = "." ] && continue
        [ "$(basename "$dir")" = "." ] && continue
        
        dirname=$(basename "$dir")
        size=$(du -sm "$dir" 2>/dev/null | cut -f1)
        [ -z "$size" ] && size="0.1"
        
        # Try to get description from README or main file
        if [ -f "$dir/README.md" ]; then
            description=$(head -10 "$dir/README.md" | grep -v "^#" | grep -v "^$" | head -1 | cut -c1-100)
        elif [ -f "$dir/main.py" ]; then
            description="Python script with main function"
        elif [ -f "$dir/index.js" ]; then
            description="JavaScript application"
        else
            description="Directory with $(ls -1 "$dir" | wc -l) items"
        fi
        
        # Clean up description for CSV
        description=$(echo "$description" | tr '\n\r,' '   ')
        
        # Determine type
        if [ -f "$dir/main.py" ] || [ -f "$dir/app.py" ]; then
            type="python-script"
        elif [ -f "$dir/index.js" ] || [ -f "$dir/package.json" ]; then
            type="javascript-app"
        elif [ -f "$dir/README.md" ]; then
            type="documentation"
        else
            type="directory"
        fi
        
        # Generate tags based on content
        tags="automation,tool"
        if [[ $dirname =~ .*ai.* ]] || [[ $dirname =~ .*AI.* ]]; then
            tags="$tags,ai,artificial-intelligence"
        fi
        if [[ $dirname =~ .*notebook.* ]]; then
            tags="$tags,notebooklm,google"
        fi
        
        date=$(stat -f "%Sm" -t "%Y-%m-%d" "$dir" 2>/dev/null || date +%Y-%m-%d)
        
        echo "\"$dirname\",\"$dir\",\"$type\",\"$size\",\"$description\",\"$tags\",\"$date\",\"$date\""
    done
}

# Enhanced scan specific file types to CSV
scan-img-csv() {
    local target_dir="${1:-.}"
    echo "name,path,type,size_mb,description,tags,created,modified"
    
    find "$target_dir" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.svg" -o -iname "*.webp" \) | while read file; do
        filename=$(basename "$file")
        dirpath=$(dirname "$file")
        size=$(du -sm "$file" 2>/dev/null | cut -f1)
        [ -z "$size" ] && size="0.01"
        
        echo "\"$filename\",\"$file\",\"image\",\"$size\",\"Image file\",\"images,media\",\"$(date +%Y-%m-%d)\",\"$(date +%Y-%m-%d)\""
    done
}

# Function to scan and import directly to knowledge base
scan-and-import() {
    local scan_type="${1:-all}"
    local temp_csv="/tmp/scan_output_$(date +%s).csv"
    
    case $scan_type in
        "all")
            scan-all-csv > "$temp_csv"
            ;;
        "img")
            scan-img-csv > "$temp_csv"
            ;;
        "docs")
            scan-docs-csv > "$temp_csv"
            ;;
        *)
            echo "Usage: scan-and-import [all|img|docs|audio|video|code]"
            return 1
            ;;
    esac
    
    if [ -f "$temp_csv" ]; then
        python3 ~/AutoTagger/v3-dev/csv_import_export.py import --csv-path "$temp_csv"
        rm "$temp_csv"
        echo "Scan results imported to knowledge base"
    else
        echo "No scan results to import"
    fi
}
```

## Usage Examples

After adding these functions to your ~/.zshrc and sourcing it:

```bash
# Scan all and import directly
scan-and-import all

# Scan images and import
scan-and-import img

# Scan and export to CSV for external tools
scan-all-csv > ~/Desktop/scan_results.csv

# Use with the knowledge base system
scan-all-csv ~/AVATARARTS/Automations > automations_scan.csv
python3 ~/AutoTagger/v3-dev/csv_import_export.py import --csv-path automations_scan.csv
```

This approach maintains compatibility with your existing workflow while adding intelligent knowledge management capabilities.