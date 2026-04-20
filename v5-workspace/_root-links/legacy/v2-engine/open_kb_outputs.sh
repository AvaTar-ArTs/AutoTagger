#!/bin/bash
# Script to automatically open the most recent CSV files from the AVATARARTS Knowledge Base system

# Define the tagger directory
TAGGER_DIR="$HOME/.tagger"

# Function to open CSV files
open_csv_files() {
    local search_term="${1:-index}"  # Default to searching for "index" CSVs
    
    echo "Looking for CSV files in $TAGGER_DIR containing '$search_term'..."
    
    # Find the most recent CSV files containing the search term
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS version
        recent_csvs=$(find "$TAGGER_DIR" -name "*${search_term}*.csv" -type f -exec stat -f '%m %N' {} \; 2>/dev/null | sort -nr | head -5 | awk '{print $2}')
    else
        # Linux version
        recent_csvs=$(find "$TAGGER_DIR" -name "*${search_term}*.csv" -type f -exec stat -c '%Y %n' {} \; 2>/dev/null | sort -nr | head -5 | awk '{print $2}')
    fi
    
    if [ -z "$recent_csvs" ]; then
        echo "No CSV files found containing '$search_term' in $TAGGER_DIR"
        echo "Available CSV files in the directory:"
        find "$TAGGER_DIR" -name "*.csv" -type f | head -10
        return 1
    fi
    
    echo "Found recent CSV files:"
    echo "$recent_csvs"
    echo ""
    
    # Try to open with different applications in order of preference
    for csv_file in $recent_csvs; do
        echo "Attempting to open: $csv_file"
        
        # Try opening with different applications based on OS
        if command -v open >/dev/null 2>&1 && [[ "$OSTYPE" == "darwin"* ]]; then
            # macOS
            open "$csv_file"
            echo "Opened with default application"
        elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
            # Linux
            if command -v libreoffice >/dev/null 2>&1; then
                libreoffice "$csv_file" &
                echo "Opened with LibreOffice"
            elif command -v google-chrome >/dev/null 2>&1; then
                google-chrome "$csv_file" &
                echo "Opened with Chrome"
            elif command -v firefox >/dev/null 2>&1; then
                firefox "$csv_file" &
                echo "Opened with Firefox"
            elif command -v xdg-open >/dev/null 2>&1; then
                xdg-open "$csv_file" &
                echo "Opened with default application"
            else
                echo "No suitable application found to open $csv_file"
                echo "You can manually open it with a spreadsheet application"
            fi
        else
            # Other OS
            echo "Unsupported OS for automatic opening: $OSTYPE"
            echo "Please manually open $csv_file with a spreadsheet application"
        fi
        
        echo ""
    done
}

# Function to open the knowledge base database
open_knowledge_db() {
    DB_PATH="$TAGGER_DIR/knowledge_base.db"
    
    if [ ! -f "$DB_PATH" ]; then
        echo "Knowledge base database not found at: $DB_PATH"
        return 1
    fi
    
    echo "Opening knowledge base database: $DB_PATH"
    
    # Try to open with different applications in order of preference
    if command -v open >/dev/null 2>&1 && [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if open -a "DB Browser for SQLite" "$DB_PATH" 2>/dev/null; then
            echo "Opened with DB Browser for SQLite"
        elif open -a "SQLite Database Browser" "$DB_PATH" 2>/dev/null; then
            echo "Opened with SQLite Database Browser"
        elif open -a "Numbers" "$DB_PATH" 2>/dev/null; then
            echo "Opened with Numbers"
        elif open -a "TextEdit" "$DB_PATH" 2>/dev/null; then
            echo "Opened with TextEdit"
        else
            open "$DB_PATH"
            echo "Opened with default application"
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        if command -v sqlitebrowser >/dev/null 2>&1; then
            sqlitebrowser "$DB_PATH" &
            echo "Opened with SQLite Browser"
        elif command -v libreoffice >/dev/null 2>&1; then
            libreoffice "$DB_PATH" &
            echo "Opened with LibreOffice"
        elif command -v xdg-open >/dev/null 2>&1; then
            xdg-open "$DB_PATH" &
            echo "Opened with default application"
        else
            echo "No suitable application found to open $DB_PATH"
            echo "You can install sqlitebrowser or use command line: sqlite3 $DB_PATH"
        fi
    else
        # Other OS
        echo "Unsupported OS for automatic opening: $OSTYPE"
        echo "Please manually open $DB_PATH with a database application"
    fi
}

# Main function
main() {
    if [ $# -eq 0 ]; then
        echo "Usage: $0 [option] [search_term]"
        echo "Options:"
        echo "  csv [search_term]  - Open recent CSV files (default search term: 'index')"
        echo "  db                 - Open the knowledge base SQLite database"
        echo "  all                - Open both recent CSVs and the database"
        echo ""
        echo "Examples:"
        echo "  $0 csv                    # Opens recent index CSVs"
        echo "  $0 csv automation        # Opens recent automation CSVs"
        echo "  $0 db                    # Opens the knowledge base database"
        echo "  $0 all                   # Opens both CSVs and database"
        return 1
    fi
    
    case "$1" in
        "csv")
            search_term="${2:-index}"
            open_csv_files "$search_term"
            ;;
        "db")
            open_knowledge_db
            ;;
        "all")
            echo "Opening recent CSV files..."
            open_csv_files "index"
            echo ""
            echo "Opening knowledge base database..."
            open_knowledge_db
            ;;
        *)
            echo "Invalid option: $1"
            echo "Use 'csv', 'db', or 'all'"
            return 1
            ;;
    esac
}

# Call main function with all arguments
main "$@"