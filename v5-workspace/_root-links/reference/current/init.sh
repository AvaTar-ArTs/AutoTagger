#!/bin/bash

# AutoTagger Initialization Script
echo "🔧 Initializing AutoTagger Ecosystem..."

AUTOTAGGER_ROOT="$HOME/AutoTagger"
CURRENT_DIR="$AUTOTAGGER_ROOT/current"
OUTPUT_DIR="$AUTOTAGGER_ROOT/output"

# Ensure permissions
chmod +x "$CURRENT_DIR/autotagger.py"
chmod +x "$CURRENT_DIR/main.py"

# Create symbolic link to the main script for easier access
mkdir -p "$HOME/.local/bin"
ln -sf "$CURRENT_DIR/main.py" "$HOME/.local/bin/autotag-v4"

echo "✅ Environment Ready."
echo "💡 To use the new system, run: autotag <directory>"
