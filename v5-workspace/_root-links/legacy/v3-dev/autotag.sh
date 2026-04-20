#!/bin/bash

# Universal Directory Indexer for AVATARARTS Knowledge Base
# Can be used as an alias to index any directory

if [ $# -eq 0 ]; then
    echo "Usage: autotag <directory> [output_prefix]"
    echo "Example: autotag ~/Pictures pictures_scan"
    echo "Example: autotag ~/Documents docs_scan"
    echo "Example: autotag ~/AVATARARTS/Automations automations_scan"
    exit 1
fi

DIRECTORY="$1"
PREFIX="${2:-$(basename "$DIRECTORY" | sed 's/[^a-zA-Z0-9]/_/g')_scan}"

echo "Running tiered indexing on: $DIRECTORY"
echo "Output prefix: $PREFIX"

python3 ~/AutoTagger/v3-dev/universal_directory_indexer.py "$DIRECTORY" --prefix "$PREFIX"