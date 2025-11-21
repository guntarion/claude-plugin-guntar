#!/usr/bin/env python3
"""
Modify Chapter Numbering Script

This script changes chapter numbering in both filenames and file contents.

Usage:
    python 22-modify-chapter-numbering.py <folder_path> <old_chapter> <new_chapter>

Examples:
    python 22-modify-chapter-numbering.py ./folder 14 8
    python 22-modify-chapter-numbering.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop" 14 8

What it does:
    1. Renames files with chapter numbers:
       14-LIB-14.1.0-PNGTR-File.md → 08-LIB-08.1.0-PNGTR-File.md
       (Note: Leading zeros for chapters < 10 in filename)

    2. Replaces chapter numbers in content:
       - Bab 14 → Bab 8
       - BAB 14 → BAB 8
       - 14.1. → 8.1.
       - 14.1.1. → 8.1.1.
       (Note: NO leading zeros in content)
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Dict


def rename_file_with_chapter(file_path: Path, old_chapter: int, new_chapter: int) -> Tuple[Path, bool]:
    """
    Rename a file by replacing chapter numbers.

    Args:
        file_path: Path to the file
        old_chapter: Old chapter number (e.g., 14)
        new_chapter: New chapter number (e.g., 8)

    Returns:
        Tuple of (new_path, was_renamed)
    """
    filename = file_path.name
    old_chapter_str = str(old_chapter)
    new_chapter_str = str(new_chapter)

    # Format with leading zero for chapters < 10
    old_chapter_padded = f"{old_chapter:02d}"
    new_chapter_padded = f"{new_chapter:02d}"

    # Pattern: XX-ABBREV-XX.Y.Z-TYPE-Description.md
    # We need to replace:
    # 1. The leading chapter number (14- → 08-)
    # 2. The chapter in hierarchy (14.Y.Z → 8.Y.Z)

    new_filename = filename

    # Replace leading chapter number with padded version
    # Pattern: ^14-ABBREV → 08-ABBREV
    if filename.startswith(f"{old_chapter_padded}-"):
        new_filename = new_filename.replace(f"{old_chapter_padded}-", f"{new_chapter_padded}-", 1)

    # Replace chapter in hierarchy (XX.Y.Z → YY.Y.Z)
    # Pattern: -14.Y.Z- → -8.Y.Z-
    # Use regex to match the pattern after the first dash
    pattern = f"-{old_chapter_str}\\.(\\d+\\.\\d+)-"
    replacement = f"-{new_chapter_str}.\\1-"
    new_filename = re.sub(pattern, replacement, new_filename)

    if new_filename == filename:
        return file_path, False

    new_path = file_path.parent / new_filename
    return new_path, True


def replace_chapter_in_content(content: str, old_chapter: int, new_chapter: int) -> Tuple[str, int]:
    """
    Replace chapter numbers in file content.

    Args:
        content: File content string
        old_chapter: Old chapter number (e.g., 14)
        new_chapter: New chapter number (e.g., 8)

    Returns:
        Tuple of (new_content, replacement_count)
    """
    old_str = str(old_chapter)
    new_str = str(new_chapter)

    replacements = 0
    new_content = content

    # Patterns to replace (case-insensitive where appropriate)
    patterns = [
        # "Bab 14" or "BAB 14"
        (rf'\b[Bb][Aa][Bb]\s+{old_str}\b', f'Bab {new_str}'),
        (rf'\bBAB\s+{old_str}\b', f'BAB {new_str}'),

        # Chapter headings: "## 14." or "### 14.1" etc.
        (rf'^(#+\s*){old_str}\.', rf'\g<1>{new_str}.'),

        # Section references: "14.1." "14.1.1." "14.2." etc.
        # Pattern: word boundary, chapter number, dot, digit(s), dot
        (rf'\b{old_str}\.(\d+)\.',  f'{new_str}.\\1.'),

        # Section references in lists: "**14.1.1.**" or "- **14.2.1.**"
        (rf'\*\*{old_str}\.(\d+)\.(\d+)\.\*\*', f'**{new_str}.\\1.\\2.**'),

        # "Daftar Isi Bab 14" or similar
        (rf'\b[Dd]aftar\s+[Ii]si\s+[Bb]ab\s+{old_str}\b', f'Daftar Isi Bab {new_str}'),
    ]

    for pattern, replacement in patterns:
        new_content, count = re.subn(pattern, replacement, new_content, flags=re.MULTILINE)
        replacements += count

    return new_content, replacements


def process_markdown_file(file_path: Path, old_chapter: int, new_chapter: int, dry_run: bool = False) -> Dict:
    """
    Process a single markdown file: rename and replace content.

    Args:
        file_path: Path to the markdown file
        old_chapter: Old chapter number
        new_chapter: New chapter number
        dry_run: If True, don't actually modify anything

    Returns:
        Dictionary with processing results
    """
    result = {
        'original_name': file_path.name,
        'new_name': None,
        'renamed': False,
        'content_changes': 0,
        'error': None
    }

    try:
        # Check if file needs renaming
        new_path, needs_rename = rename_file_with_chapter(file_path, old_chapter, new_chapter)
        result['new_name'] = new_path.name
        result['renamed'] = needs_rename

        # Read file content
        content = file_path.read_text(encoding='utf-8')

        # Replace chapter numbers in content
        new_content, replacements = replace_chapter_in_content(content, old_chapter, new_chapter)
        result['content_changes'] = replacements

        if not dry_run:
            # Write updated content
            if replacements > 0:
                file_path.write_text(new_content, encoding='utf-8')

            # Rename file if needed
            if needs_rename:
                file_path.rename(new_path)

    except Exception as e:
        result['error'] = str(e)

    return result


def main():
    """Main execution function."""

    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)

    folder_path = Path(sys.argv[1])
    try:
        old_chapter = int(sys.argv[2])
        new_chapter = int(sys.argv[3])
    except ValueError:
        print("Error: Chapter numbers must be integers")
        sys.exit(1)

    if not folder_path.exists():
        print(f"Error: Folder not found: {folder_path}")
        sys.exit(1)

    if not folder_path.is_dir():
        print(f"Error: Not a directory: {folder_path}")
        sys.exit(1)

    print("=" * 70)
    print("Modify Chapter Numbering")
    print("=" * 70)
    print(f"Folder: {folder_path}")
    print(f"Change: Bab {old_chapter} → Bab {new_chapter}")
    print()

    # Get all markdown files
    md_files = sorted(folder_path.glob('*.md'))

    if not md_files:
        print("No markdown files found in the folder.")
        sys.exit(0)

    print(f"Found {len(md_files)} markdown file(s)")
    print()

    # Ask for confirmation
    print("This will:")
    print(f"  1. Rename files: {old_chapter:02d}-XXX-{old_chapter}.Y.Z-... → {new_chapter:02d}-XXX-{new_chapter}.Y.Z-...")
    print(f"  2. Replace in content: Bab {old_chapter} → Bab {new_chapter}, {old_chapter}.Y.Z → {new_chapter}.Y.Z")
    print()

    response = input("Continue? (y/n): ").strip().lower()
    if response != 'y':
        print("Cancelled.")
        sys.exit(0)

    print()
    print("Processing files...")
    print()

    # Process all files
    results = []
    for md_file in md_files:
        result = process_markdown_file(md_file, old_chapter, new_chapter, dry_run=False)
        results.append(result)

        # Print progress
        status = "✓" if not result['error'] else "✗"

        if result['renamed']:
            print(f"{status} {result['original_name']}")
            print(f"  → {result['new_name']}")
        else:
            print(f"{status} {result['original_name']}")

        if result['content_changes'] > 0:
            print(f"    Content changes: {result['content_changes']}")

        if result['error']:
            print(f"    Error: {result['error']}")

        print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)

    total_files = len(results)
    renamed_files = sum(1 for r in results if r['renamed'])
    content_changed = sum(1 for r in results if r['content_changes'] > 0)
    total_changes = sum(r['content_changes'] for r in results)
    errors = sum(1 for r in results if r['error'])

    print(f"Total files processed: {total_files}")
    print(f"Files renamed: {renamed_files}")
    print(f"Files with content changes: {content_changed}")
    print(f"Total content replacements: {total_changes}")

    if errors > 0:
        print(f"Errors: {errors}")
    else:
        print()
        print("✓ All files processed successfully!")

    print()
    print(f"Chapter numbering changed from Bab {old_chapter} to Bab {new_chapter}")
    print()


if __name__ == "__main__":
    main()
