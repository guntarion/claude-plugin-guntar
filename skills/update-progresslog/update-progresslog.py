#!/usr/bin/env python3
"""
Update PROGRESS.md with progress notes and timestamp.

Prepends new entries to the top of PROGRESS.md (most recent first).

Usage:
    python update-progresslog.py <progress_note> [timestamp]

Example:
    python update-progresslog.py "Currently working on LDAP auth" "2025-11-23 14:30:00"
"""

import sys
from pathlib import Path
from datetime import datetime


def update_progresslog(progress_note, timestamp=None):
    """
    Update PROGRESS.md by prepending new progress entry at the top.

    Args:
        progress_note: The progress note to add
        timestamp: Optional timestamp string. If not provided, uses current time.

    Returns:
        Path to the updated PROGRESS.md
    """
    # Use current working directory (where the project is)
    progress_path = Path.cwd() / "PROGRESS.md"

    # Get timestamp
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Read existing content if file exists
    existing_content = ""
    if progress_path.exists():
        with open(progress_path, 'r', encoding='utf-8') as f:
            existing_content = f.read()

    # Create new entry
    new_entry = f"## {timestamp}\n\n{progress_note}\n\n---\n\n"

    # Prepend new entry to existing content
    new_content = new_entry + existing_content

    # Write back to file
    with open(progress_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return progress_path


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python update-progresslog.py <progress_note> [timestamp]")
        print("\nExamples:")
        print('  python update-progresslog.py "Currently working on LDAP auth"')
        print('  python update-progresslog.py "Completed API integration" "2025-11-23 14:30:00"')
        sys.exit(1)

    progress_note = sys.argv[1]
    timestamp = sys.argv[2] if len(sys.argv) >= 3 else None

    progress_path = update_progresslog(progress_note, timestamp)

    print(f"✓ PROGRESS.md updated: {progress_path}")


if __name__ == "__main__":
    main()
