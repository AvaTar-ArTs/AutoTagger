#!/bin/bash
# Script to add Tagger to shell profile

SHELL_PROFILE="$HOME/.zshrc"

echo "Adding Tagger to $SHELL_PROFILE..."

# Check if the source line already exists
if grep -q "source ~/.tagger/kb_aliases.sh" "$SHELL_PROFILE"; then
    echo "Tagger already sourced in $SHELL_PROFILE"
else
    # Add the source line to the shell profile
    echo "" >> "$SHELL_PROFILE"
    echo "# Tagger - AVATARARTS Universal Directory Indexer" >> "$SHELL_PROFILE"
    echo "source ~/.tagger/kb_aliases.sh" >> "$SHELL_PROFILE"
    echo "Added Tagger to $SHELL_PROFILE"
fi

echo "Setup complete! Please run 'source $SHELL_PROFILE' or restart your terminal to use the commands."