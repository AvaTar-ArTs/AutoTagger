#!/usr/bin/env python3
"""
autotagger-lite: File scanner with history tracking
- Scans directories and stores file metadata + content hashes
- Tracks changes over time in SQLite database
- Detects file moves by matching content hashes

Usage:
  python3 scan.py /path/to/directory           # Scan and store
  python3 scan.py --history /path/to/file.txt  # Show file history
  python3 scan.py --changes                    # Show recent changes
  python3 scan.py --moved                      # Detect moved files
"""

import argparse
import hashlib
import json
import os
import sqlite3
import sys
import time
from datetime import datetime
from pathlib import Path

# Config
DB_PATH = Path.home() / ".autotagger-lite" / "files.db"
IGNORE_PATTERNS = {".git", ".venv", "node_modules", "__pycache__", ".DS_Store", ".cache"}
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB max for hashing


def ensure_db():
    """Create database and tables if needed."""
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY,
            scan_time REAL,
            directory TEXT,
            file_count INTEGER
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY,
            scan_id INTEGER,
            path TEXT,
            name TEXT,
            extension TEXT,
            size INTEGER,
            modified REAL,
            content_hash TEXT,
            category TEXT,
            FOREIGN KEY (scan_id) REFERENCES scans(id)
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_path ON files(path)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_hash ON files(content_hash)")
    conn.commit()
    return conn


def file_hash(path: Path) -> str:
    """Compute MD5 hash of file content."""
    try:
        if path.stat().st_size > MAX_FILE_SIZE:
            return "too_large"
        return hashlib.md5(path.read_bytes()).hexdigest()
    except Exception as e:
        return f"error:{type(e).__name__}"


def categorize(path: Path) -> str:
    """Simple file categorization by extension."""
    ext = path.suffix.lower()
    categories = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".sh": "shell",
        ".md": "markdown",
        ".txt": "text",
        ".json": "data",
        ".csv": "data",
        ".yaml": "config",
        ".yml": "config",
        ".html": "web",
        ".css": "web",
        ".sql": "database",
        ".db": "database",
        ".png": "image",
        ".jpg": "image",
        ".gif": "image",
        ".mp3": "audio",
        ".wav": "audio",
        ".mp4": "video",
        ".mov": "video",
        ".pdf": "document",
        ".docx": "document",
        ".zip": "archive",
        ".tar": "archive",
        ".gz": "archive",
    }
    return categories.get(ext, "other")


def should_ignore(path: Path) -> bool:
    """Check if path should be ignored."""
    for part in path.parts:
        if part in IGNORE_PATTERNS:
            return True
    return False


def scan_directory(directory: str, conn: sqlite3.Connection) -> dict:
    """Scan directory and store file metadata."""
    dir_path = Path(directory).expanduser().resolve()
    if not dir_path.exists():
        print(f"Error: {directory} does not exist")
        return {}

    scan_time = time.time()
    cursor = conn.cursor()

    # Create scan record
    cursor.execute(
        "INSERT INTO scans (scan_time, directory, file_count) VALUES (?, ?, 0)",
        (scan_time, str(dir_path))
    )
    scan_id = cursor.lastrowid

    file_count = 0
    categories = {}

    print(f"Scanning {dir_path}...")

    for root, dirs, files in os.walk(dir_path):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_PATTERNS]

        for fname in files:
            fpath = Path(root) / fname
            if should_ignore(fpath):
                continue

            try:
                stat = fpath.stat()
                ext = fpath.suffix.lower()
                cat = categorize(fpath)
                h = file_hash(fpath)

                cursor.execute("""
                    INSERT INTO files (scan_id, path, name, extension, size, modified, content_hash, category)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    scan_id,
                    str(fpath),
                    fname,
                    ext,
                    stat.st_size,
                    stat.st_mtime,
                    h,
                    cat
                ))

                file_count += 1
                categories[cat] = categories.get(cat, 0) + 1

                if file_count % 100 == 0:
                    print(f"  Scanned {file_count} files...")

            except Exception as e:
                print(f"  Error scanning {fpath}: {e}")

    # Update scan record with file count
    cursor.execute("UPDATE scans SET file_count = ? WHERE id = ?", (file_count, scan_id))
    conn.commit()

    print(f"\n✅ Scan complete: {file_count} files")
    print(f"   Categories: {json.dumps(categories, indent=2)}")

    return {"scan_id": scan_id, "file_count": file_count, "categories": categories}


def show_file_history(file_path: str, conn: sqlite3.Connection):
    """Show history of a specific file across scans."""
    path = Path(file_path).expanduser().resolve()
    cursor = conn.cursor()

    # Find by exact path
    cursor.execute("""
        SELECT s.scan_time, f.path, f.size, f.content_hash, f.modified
        FROM files f
        JOIN scans s ON f.scan_id = s.id
        WHERE f.path = ?
        ORDER BY s.scan_time DESC
    """, (str(path),))

    rows = cursor.fetchall()

    if not rows:
        # Try to find by hash (file may have moved)
        current_hash = file_hash(path) if path.exists() else None
        if current_hash and not current_hash.startswith("error"):
            cursor.execute("""
                SELECT s.scan_time, f.path, f.size, f.content_hash, f.modified
                FROM files f
                JOIN scans s ON f.scan_id = s.id
                WHERE f.content_hash = ?
                ORDER BY s.scan_time DESC
            """, (current_hash,))
            rows = cursor.fetchall()

    if not rows:
        print(f"No history found for {file_path}")
        return

    print(f"\n📜 History for: {file_path}")
    print("-" * 80)

    prev_hash = None
    for scan_time, fpath, size, content_hash, modified in rows:
        dt = datetime.fromtimestamp(scan_time).strftime("%Y-%m-%d %H:%M")
        mod_dt = datetime.fromtimestamp(modified).strftime("%Y-%m-%d %H:%M")
        changed = "📝 CHANGED" if prev_hash and prev_hash != content_hash else ""
        moved = "📦 MOVED" if str(path) != fpath else ""

        print(f"  {dt} | {size:>10,} bytes | hash:{content_hash[:8]} | mod:{mod_dt} {changed} {moved}")
        if moved:
            print(f"           └── was at: {fpath}")

        prev_hash = content_hash

    print()


def show_recent_changes(conn: sqlite3.Connection, limit: int = 20):
    """Show files that changed between recent scans."""
    cursor = conn.cursor()

    # Get last two scans
    cursor.execute("SELECT id, scan_time, directory FROM scans ORDER BY scan_time DESC LIMIT 2")
    scans = cursor.fetchall()

    if len(scans) < 2:
        print("Need at least 2 scans to detect changes. Run more scans first.")
        return

    new_scan_id, new_time, _ = scans[0]
    old_scan_id, old_time, _ = scans[1]

    print(f"\n🔄 Changes between scans:")
    print(f"   Old: {datetime.fromtimestamp(old_time).strftime('%Y-%m-%d %H:%M')}")
    print(f"   New: {datetime.fromtimestamp(new_time).strftime('%Y-%m-%d %H:%M')}")
    print("-" * 80)

    # Find changed files (same path, different hash)
    cursor.execute("""
        SELECT n.path, o.content_hash as old_hash, n.content_hash as new_hash, n.size
        FROM files n
        JOIN files o ON n.path = o.path
        WHERE n.scan_id = ? AND o.scan_id = ?
          AND n.content_hash != o.content_hash
        LIMIT ?
    """, (new_scan_id, old_scan_id, limit))

    changed = cursor.fetchall()
    if changed:
        print(f"\n📝 Modified files ({len(changed)}):")
        for path, old_hash, new_hash, size in changed:
            print(f"  {path}")
            print(f"     {old_hash[:8]} → {new_hash[:8]}")

    # Find new files
    cursor.execute("""
        SELECT n.path, n.size, n.category
        FROM files n
        WHERE n.scan_id = ?
          AND n.path NOT IN (SELECT path FROM files WHERE scan_id = ?)
        LIMIT ?
    """, (new_scan_id, old_scan_id, limit))

    new_files = cursor.fetchall()
    if new_files:
        print(f"\n✨ New files ({len(new_files)}):")
        for path, size, cat in new_files:
            print(f"  [{cat}] {path}")

    # Find deleted files
    cursor.execute("""
        SELECT o.path, o.size, o.category
        FROM files o
        WHERE o.scan_id = ?
          AND o.path NOT IN (SELECT path FROM files WHERE scan_id = ?)
        LIMIT ?
    """, (old_scan_id, new_scan_id, limit))

    deleted = cursor.fetchall()
    if deleted:
        print(f"\n🗑️ Deleted files ({len(deleted)}):")
        for path, size, cat in deleted:
            print(f"  [{cat}] {path}")

    print()


def detect_moved_files(conn: sqlite3.Connection, limit: int = 20):
    """Detect files that were moved (same hash, different path)."""
    cursor = conn.cursor()

    # Get last two scans
    cursor.execute("SELECT id FROM scans ORDER BY scan_time DESC LIMIT 2")
    scans = cursor.fetchall()

    if len(scans) < 2:
        print("Need at least 2 scans to detect moves.")
        return

    new_scan_id = scans[0][0]
    old_scan_id = scans[1][0]

    # Find files with same hash but different path
    cursor.execute("""
        SELECT o.path as old_path, n.path as new_path, n.content_hash, n.size
        FROM files o
        JOIN files n ON o.content_hash = n.content_hash
        WHERE o.scan_id = ? AND n.scan_id = ?
          AND o.path != n.path
          AND o.content_hash NOT LIKE 'error%'
          AND o.content_hash != 'too_large'
        LIMIT ?
    """, (old_scan_id, new_scan_id, limit))

    moved = cursor.fetchall()

    if not moved:
        print("No moved files detected between recent scans.")
        return

    print(f"\n📦 Detected moved files ({len(moved)}):")
    print("-" * 80)
    for old_path, new_path, content_hash, size in moved:
        print(f"  {old_path}")
        print(f"  └── moved to: {new_path}")
        print(f"      (hash: {content_hash[:12]}, size: {size:,} bytes)")
        print()


def main():
    parser = argparse.ArgumentParser(description="autotagger-lite: File scanner with history")
    parser.add_argument("directory", nargs="?", help="Directory to scan")
    parser.add_argument("--history", metavar="FILE", help="Show history of specific file")
    parser.add_argument("--changes", action="store_true", help="Show recent changes")
    parser.add_argument("--moved", action="store_true", help="Detect moved files")
    parser.add_argument("--stats", action="store_true", help="Show database stats")

    args = parser.parse_args()
    conn = ensure_db()

    if args.history:
        show_file_history(args.history, conn)
    elif args.changes:
        show_recent_changes(conn)
    elif args.moved:
        detect_moved_files(conn)
    elif args.stats:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM scans")
        scan_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM files")
        file_count = cursor.fetchone()[0]
        print(f"Database: {DB_PATH}")
        print(f"Total scans: {scan_count}")
        print(f"Total file records: {file_count}")
    elif args.directory:
        scan_directory(args.directory, conn)
    else:
        parser.print_help()

    conn.close()


if __name__ == "__main__":
    main()
