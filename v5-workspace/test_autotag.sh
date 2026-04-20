#!/bin/bash
# AutoTag Test Script

echo "🧪 Testing AutoTag installation..."

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$REPO_ROOT/venv"

# Check if virtual environment exists
if [ ! -d "$VENV_PATH" ]; then
    echo "❌ Virtual environment not found. Run setup first."
    exit 1
fi

# Check if main script exists
if [ ! -f "$REPO_ROOT/scripts/autotag_main.py" ]; then
    echo "❌ Main script not found."
    exit 1
fi

# Check if runner script exists
if [ ! -f "$REPO_ROOT/autotag.sh" ]; then
    echo "❌ Runner script not found."
    exit 1
fi

echo "✅ All AutoTag components are present"
echo "✅ AutoTag installation test passed!"
