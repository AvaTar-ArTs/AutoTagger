#!/bin/bash
# AutoTag System Verification Script
# Verifies that all components of the AutoTag system are properly installed

echo "🔍 Verifying AutoTag System Installation"
echo "======================================="

# Resolve workspace root from this script location so verification is portable.
AUTOTAG_ROOT="$(cd "$(dirname "$0")" && pwd)"

# Check main directory
echo ""
echo "📁 Checking main AutoTag directory..."
if [ -d "$AUTOTAG_ROOT" ]; then
    echo "✅ $AUTOTAG_ROOT directory exists"
else
    echo "❌ $AUTOTAG_ROOT directory does not exist"
    exit 1
fi

# Check essential files
echo ""
echo "📄 Checking essential files..."
essential_files=(
    "$AUTOTAG_ROOT/autotag.sh"
    "$AUTOTAG_ROOT/setup_autotag.sh"
    "$AUTOTAG_ROOT/test_autotag.sh"
    "$AUTOTAG_ROOT/README.md"
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
    "$AUTOTAG_ROOT/scripts"
    "$AUTOTAG_ROOT/config"
    "$AUTOTAG_ROOT/data"
    "$AUTOTAG_ROOT/output"
    "$AUTOTAG_ROOT/logs"
    "$AUTOTAG_ROOT/docs"
    "$AUTOTAG_ROOT/venv"
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
    "$AUTOTAG_ROOT/scripts/autotag_main.py"
    "$AUTOTAG_ROOT/scripts/phase1_rapid_scan.py"
    "$AUTOTAG_ROOT/scripts/phase2_intelligent_organization.py"
    "$AUTOTAG_ROOT/scripts/phase3_advanced_intelligence.py"
    "$AUTOTAG_ROOT/scripts/run_tiered_indexing.py"
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
    "$AUTOTAG_ROOT/docs/user_guide.md"
    "$AUTOTAG_ROOT/config/autotag_config.json"
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
    "$AUTOTAG_ROOT/autotag.sh"
    "$AUTOTAG_ROOT/setup_autotag.sh"
    "$AUTOTAG_ROOT/test_autotag.sh"
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
cd "$AUTOTAG_ROOT"

# Test if virtual environment is working
if [ -d "$AUTOTAG_ROOT/venv" ]; then
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
if [ -f "$AUTOTAG_ROOT/output/csv_test/csv_test_results.csv" ]; then
    echo "✅ CSV output file exists"
    csv_columns=$(head -1 "$AUTOTAG_ROOT/output/csv_test/csv_test_results.csv")
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
echo "  cd $AUTOTAG_ROOT"
echo "  ./autotag.sh /path/to/target/directory [optional_name]"
echo ""