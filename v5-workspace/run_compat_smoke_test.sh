#!/bin/bash
# Compat smoke test (add-only)

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$REPO_ROOT/docs"
RUN_NAME="compat_smoke_$(date +%Y%m%d_%H%M%S)"

"$REPO_ROOT/autotag_compat.sh" "$TARGET_DIR" "$RUN_NAME" --no-open
