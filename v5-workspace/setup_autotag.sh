#!/bin/bash
# AutoTag Setup Script

set -e  # Exit on any error

echo "🚀 Setting up AutoTag - AVATARARTS Automation Tagging System"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$REPO_ROOT/venv"

# Check if already set up
if [ -d "$VENV_PATH" ]; then
    echo "⚠️  AutoTag virtual environment already exists. Skipping setup."
    echo "To reinstall, remove the venv directory first: rm -rf $VENV_PATH"
    exit 0
fi

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv "$VENV_PATH"

# Activate virtual environment
source "$VENV_PATH/bin/activate"

# Upgrade pip
pip install --upgrade pip

echo "✅ Virtual environment created and packages installed"

# Make scripts executable
chmod +x "$REPO_ROOT/autotag.sh"
chmod +x "$REPO_ROOT/setup_autotag.sh"

# Create initial database
echo "Creating initial knowledge base database..."
touch "$REPO_ROOT/data/knowledge_base.db"

# Create initial data files
echo '{"runs": []}' > "$REPO_ROOT/data/runs.json"

echo "✅ AutoTag setup completed successfully!"

echo ""
echo "To use AutoTag:"
echo "1. Run: source $VENV_PATH/bin/activate"
echo "2. Or use the runner: $REPO_ROOT/autotag.sh /path/to/target"
echo ""
echo "For more information, see: $REPO_ROOT/README.md"
