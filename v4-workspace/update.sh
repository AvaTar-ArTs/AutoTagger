#!/bin/bash

# Auto-generated update script for AutoTagger
# Generated as part of the Ecosystem Evolution Enhancer

echo "🔄 Updating AutoTagger..."

# Navigate to the component directory
cd "$(dirname "$0")"

# If there's a Git repository, pull the latest changes
if [ -d .git ]; then
    echo "🔍 Detected Git repository, pulling latest changes..."
    git fetch origin
    git pull origin $(git branch --show-current)
    if [ $? -eq 0 ]; then
        echo "✅ Git repository updated successfully"
    else
        echo "⚠️  Git update failed or no changes to pull"
    fi
else
    echo "ℹ️  No Git repository detected, skipping Git update"
fi

# If there are Python dependencies, update them
if [ -f "requirements.txt" ]; then
    echo "🐍 Updating Python dependencies..."
    if command -v pip &> /dev/null; then
        pip install -r requirements.txt --upgrade
        echo "✅ Python dependencies updated"
    else
        echo "⚠️  pip not found, skipping Python dependency update"
    fi
elif [ -f "pyproject.toml" ]; then
    echo "🐍 Updating Python dependencies from pyproject.toml..."
    if command -v pip &> /dev/null; then
        pip install . --upgrade
        echo "✅ Python dependencies updated"
    else
        echo "⚠️  pip not found, skipping Python dependency update"
    fi
else
    echo "ℹ️  No Python requirements detected, skipping dependency update"
fi

# If there are Node.js dependencies, update them
if [ -f "package.json" ]; then
    echo "📦 Updating Node.js dependencies..."
    if command -v npm &> /dev/null; then
        npm update
        echo "✅ Node.js dependencies updated"
    elif command -v yarn &> /dev/null; then
        yarn upgrade
        echo "✅ Node.js dependencies updated with Yarn"
    else
        echo "⚠️  npm or yarn not found, skipping Node.js dependency update"
    fi
else
    echo "ℹ️  No Node.js package.json detected, skipping dependency update"
fi

# Run any custom update commands if they exist
if [ -f "custom-update.sh" ]; then
    echo "⚙️  Running custom update commands..."
    source custom-update.sh
    echo "✅ Custom update commands completed"
fi

echo "✅ AutoTagger update process completed"
