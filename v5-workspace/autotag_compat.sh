#!/bin/bash
# AutoTag Compat Runner Script (add-only wrapper)

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ $# -eq 0 ]; then
    echo "ℹ️  No target directory provided. Using base workspace as source: $REPO_ROOT"
    TARGET_DIR="$REPO_ROOT"
    OUTPUT_NAME="autotag_run_$(date +%Y%m%d_%H%M%S)"
    NO_OPEN_FLAG=""
else
    TARGET_DIR="$1"
    OUTPUT_NAME="${2:-autotag_run_$(date +%Y%m%d_%H%M%S)}"
    NO_OPEN_FLAG=""

    if [ "$3" == "--no-open" ]; then
        NO_OPEN_FLAG="--no-open"
    fi
fi

echo "Running AutoTag Compat on: $TARGET_DIR"
echo "Run name: $OUTPUT_NAME"

python3 "$REPO_ROOT/scripts/autotag_main_compat.py" --target "$TARGET_DIR" --name "$OUTPUT_NAME" $NO_OPEN_FLAG

