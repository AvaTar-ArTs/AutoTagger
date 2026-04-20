#!/bin/bash
# AutoTag System Verification Script
# Verifies that all components of the AutoTag system are properly installed

echo "🔍 Verifying AutoTag System Installation"
echo "======================================="

# Check main directory
echo ""
echo "📁 Checking main AutoTag directory..."
if [ -d "/Users/steven/AutoTag" ]; then
    echo "✅ /Users/steven/AutoTag directory exists"
else
    echo "❌ /Users/steven/AutoTag directory does not exist"
    exit 1
fi

# Check essential files
echo ""
echo "📄 Checking essential files..."
essential_files=(
    "/Users/steven/AutoTag/autotag.sh"
    "/Users/steven/AutoTag/setup_autotag.sh"
    "/Users/steven/AutoTag/test_autotag.sh"
    "/Users/steven/AutoTag/README.md"
)

for file in "${essential_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists"
    else
        echo "❌ $file does not exist"
        exit 1
    fi
done

# Check directories
echo ""
echo "📂 Checking essential directories..."
directories=(
    "/Users/steven/AutoTag/scripts"
    "/Users/steven/AutoTag/config"
    "/Users/steven/AutoTag/data"
    "/Users/steven/AutoTag/output"
    "/Users/steven/AutoTag/logs"
    "/Users/steven/AutoTag/docs"
    "/Users/steven/AutoTag/venv"
)

for dir in "${directories[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir directory exists"
    else
        echo "❌ $dir directory does not exist"
        exit 1
    fi
done

# Check scripts directory contents
echo ""
echo "⚙️  Checking scripts directory contents..."
script_files=(
    "/Users/steven/AutoTag/scripts/autotag_main.py"
    "/Users/steven/AutoTag/scripts/phase1_rapid_scan.py"
    "/Users/steven/AutoTag/scripts/phase2_intelligent_organization.py"
    "/Users/steven/AutoTag/scripts/phase3_advanced_intelligence.py"
    "/Users/steven/AutoTag/scripts/run_tiered_indexing.py"
)

for file in "${script_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists"
    else
        echo "❌ $file does not exist"
        exit 1
    fi
done

# Check documentation
echo ""
echo "📚 Checking documentation..."
doc_files=(
    "/Users/steven/AutoTag/docs/user_guide.md"
    "/Users/steven/AutoTag/config/autotag_config.json"
)

for file in "${doc_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists"
    else
        echo "❌ $file does not exist"
        exit 1
    fi
done

# Check permissions
echo ""
echo "🔒 Checking file permissions..."
executable_files=(
    "/Users/steven/AutoTag/autotag.sh"
    "/Users/steven/AutoTag/setup_autotag.sh"
    "/Users/steven/AutoTag/test_autotag.sh"
)

for file in "${executable_files[@]}"; do
    if [ -x "$file" ]; then
        echo "✅ $file is executable"
    else
        echo "❌ $file is not executable"
        chmod +x "$file"
        echo "   Fixed: Made $file executable"
    fi
done

# Test functionality
echo ""
echo "🧪 Testing basic functionality..."
cd /Users/steven/AutoTag

# Test if virtual environment is working
if [ -d "/Users/steven/AutoTag/venv" ]; then
    echo "✅ Virtual environment exists"
else
    echo "❌ Virtual environment does not exist"
    exit 1
fi

# Test if test script runs successfully
echo "Running test script..."
./test_autotag.sh
if [ $? -eq 0 ]; then
    echo "✅ Test script ran successfully"
else
    echo "❌ Test script failed"
    exit 1
fi

# Check if CSV functionality is working
echo ""
echo "📊 Checking CSV functionality..."
if [ -f "/Users/steven/AutoTag/output/csv_test/csv_test_results.csv" ]; then
    echo "✅ CSV output file exists"
    csv_columns=$(head -1 "/Users/steven/AutoTag/output/csv_test/csv_test_results.csv")
    echo "   CSV columns: $csv_columns"
else
    echo "❌ CSV output file does not exist"
    exit 1
fi

echo ""
echo "🎉 AutoTag System Verification Complete!"
echo "========================================"
echo ""
echo "All components are properly installed and functional:"
echo "- Core scripts with CSV export functionality ✓"
echo "- Configuration files ✓"
echo "- Documentation ✓"
echo "- Virtual environment ✓"
echo "- Test functionality ✓"
echo "- CSV export functionality ✓"
echo ""
echo "AutoTag is ready for use!"
echo ""
echo "To run AutoTag:"
echo "  cd /Users/steven/AutoTag"
echo "  ./autotag.sh /path/to/target/directory [optional_name]"
echo ""