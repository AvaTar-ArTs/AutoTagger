#!/bin/bash
# Quick Setup Script for AVATARARTS Knowledge Base

echo "Setting up AVATARARTS Knowledge Base system..."

# Check if the aliases are already in .zshrc
if grep -q "avatararts-kb/kb_aliases.sh" ~/.zshrc; then
    echo "✓ Aliases already present in .zshrc"
else
    # Add the source command to .zshrc
    echo "source ~/AutoTagger/v3-dev/kb_aliases.sh" >> ~/.zshrc
    echo "✓ Added aliases to .zshrc"
fi

# Check if the aliases are already in .bashrc (for compatibility)
if [ -f ~/.bashrc ]; then
    if grep -q "avatararts-kb/kb_aliases.sh" ~/.bashrc; then
        echo "✓ Aliases already present in .bashrc"
    else
        echo "source ~/AutoTagger/v3-dev/kb_aliases.sh" >> ~/.bashrc
        echo "✓ Added aliases to .bashrc"
    fi
fi

echo ""
echo "Setup complete! To start using the system immediately:"
echo ""
echo "1. Restart your shell: source ~/.zshrc"
echo "2. Or open a new terminal window"
echo ""
echo "Then you can use:"
echo "- save-kb : Save/search knowledge entries"
echo "- capture-kb : Capture conversation data"
echo "- quick-save-kb : Save clipboard content"
echo ""
echo "The AVATARARTS Knowledge Base system is now ready to use!"