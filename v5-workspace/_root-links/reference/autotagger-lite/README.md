# autotagger-lite

**Standalone file scanner with history tracking** — know what changed, when, and if files moved.

## What It Does

- Scans directories and stores file metadata + content hashes
- Tracks changes over time in SQLite
- Detects file moves by matching content hashes
- Simple CLI interface

## Quick Start

```bash
# Scan a directory
python3 scan.py ~/Documents

# Run again later to track changes
python3 scan.py ~/Documents

# See what changed
python3 scan.py --changes

# Check specific file history
python3 scan.py --history ~/Documents/file.txt

# Detect moved files
python3 scan.py --moved

# Database stats
python3 scan.py --stats
```

## Database Location

```
~/.autotagger-lite/files.db
```

## How Change Detection Works

1. **First scan**: Records path, size, modified time, content hash
2. **Second scan**: Compares to previous scan
3. **Changed files**: Same path, different hash
4. **Moved files**: Different path, same hash
5. **New files**: Path exists in new scan only
6. **Deleted files**: Path exists in old scan only

## Example Output

```
🔄 Changes between scans:
   Old: 2026-02-08 10:00
   New: 2026-02-09 14:00
--------------------------------------------------------------------------------

📝 Modified files (3):
  /Users/steven/project/config.py
     a1b2c3d4 → e5f6g7h8

✨ New files (2):
  [python] /Users/steven/project/new_feature.py

🗑️ Deleted files (1):
  [text] /Users/steven/project/old_notes.txt

📦 Detected moved files (1):
  /Users/steven/old/file.txt
  └── moved to: /Users/steven/new/file.txt
      (hash: abc123def456, size: 1,234 bytes)
```

## Categories

Files are auto-categorized:
- `python`, `javascript`, `typescript`, `shell`
- `markdown`, `text`, `data`, `config`
- `web`, `database`, `image`, `audio`, `video`
- `document`, `archive`, `other`

## No Dependencies

- Python 3.7+ (standard library only)
- Uses SQLite (built into Python)
- Single file, no pip install needed
