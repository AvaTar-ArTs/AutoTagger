#!/bin/bash
# AutoTag Compat Runner Script (add-only wrapper)

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ $# -eq 0 ]; then
    echo "Usage: $0 <target_directory> [output_name] [--no-open]"
    echo "Example: $0 /Users/steven/pythons my_python_analysis"
    echo "Example: $0 /Users/steven/pythons my_python_analysis --no-open"
    exit 1
fi

TARGET_DIR="$1"
OUTPUT_NAME="${2:-autotag_run_$(date +%Y%m%d_%H%M%S)}"
NO_OPEN_FLAG=""

if [ "$3" == "--no-open" ]; then
    NO_OPEN_FLAG="--no-open"
fi

echo "Running AutoTag Compat on: $TARGET_DIR"
echo "Run name: $OUTPUT_NAME"

python3 "$REPO_ROOT/scripts/autotag_main_compat.py" --target "$TARGET_DIR" --name "$OUTPUT_NAME" $NO_OPEN_FLAG

