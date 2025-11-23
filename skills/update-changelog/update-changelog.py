#!/usr/bin/env python3
"""
Update CHANGELOG.md with git commit message and timestamp.

Prepends new entries to the top of CHANGELOG.md (most recent first).

Usage:
    python update-changelog.py <commit_message> [timestamp]

Example:
    python update-changelog.py "feat: add new feature" "2025-11-23 14:30:00"
"""

import sys
from pathlib import Path
from datetime import datetime


def update_changelog(commit_message, timestamp=None):
    """
    Update CHANGELOG.md by prepending new commit entry at the top.

    Args:
        commit_message: The git commit message
        timestamp: Optional timestamp string. If not provided, uses current time.

    Returns:
        Path to the updated CHANGELOG.md
    """
    # Use current working directory (where the git repo is)
    changelog_path = Path.cwd() / "CHANGELOG.md"

    # Get timestamp
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Read existing content if file exists
    existing_content = ""
    if changelog_path.exists():
        with open(changelog_path, 'r', encoding='utf-8') as f:
            existing_content = f.read()

    # Create new entry
    new_entry = f"## {timestamp}\n\n{commit_message}\n\n---\n\n"

    # Prepend new entry to existing content
    new_content = new_entry + existing_content

    # Write back to file
    with open(changelog_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return changelog_path


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python update-changelog.py <commit_message> [timestamp]")
        print("\nExamples:")
        print('  python update-changelog.py "feat: add new feature"')
        print('  python update-changelog.py "fix: bug fix" "2025-11-23 14:30:00"')
        sys.exit(1)

    commit_message = sys.argv[1]
    timestamp = sys.argv[2] if len(sys.argv) >= 3 else None

    changelog_path = update_changelog(commit_message, timestamp)

    print(f"✓ CHANGELOG.md updated: {changelog_path}")


if __name__ == "__main__":
    main()
