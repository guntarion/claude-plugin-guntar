#!/usr/bin/env python3
"""
Chapter Files Analyzer
Analyzes chapter markdown files and creates work manifest for content composition.

Usage:
    python python_scripts/16-analyze-chapter-files.py <folder_path>

Example:
    python python_scripts/16-analyze-chapter-files.py ./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/markdown-composed
"""

from pathlib import Path
import json
import re
import sys
from collections import defaultdict


def parse_filename(filename: str) -> dict:
    """
    Parse filename to extract metadata

    Pattern: 0X-ABC-X.Y.Z-Seq-Type-Description.md (with sequence)
          or 0X-ABC-X.Y.Z-Type-Description.md (without sequence)
    Example: 02-HK-2.3.1-A-IK-Pembersihan_Kamar.md
          or 02-HK-2.1.0-PNGTR-Housekeeping.md

    Returns:
        dict with keys: chapter_num, chapter_abbrev, hierarchy, sequence, doc_type, description
        or None if pattern doesn't match
    """
    # First try pattern with sequence letter: 02-HK-2.3.1-A-IK-Pembersihan_Kamar.md
    pattern_with_seq = r'^(\d{2})-([A-Z]+)-(\d+\.\d+\.?\d*)-([A-Z])-([A-Z]+)-(.+)\.md$'
    match = re.match(pattern_with_seq, filename)

    if match:
        return {
            'chapter_num': match.group(1),
            'chapter_abbrev': match.group(2),
            'hierarchy': match.group(3),
            'sequence': match.group(4),
            'doc_type': match.group(5),
            'description': match.group(6)
        }

    # Try pattern without sequence letter: 02-HK-2.1.0-PNGTR-Housekeeping.md
    pattern_no_seq = r'^(\d{2})-([A-Z]+)-(\d+\.\d+\.?\d*)-([A-Z]+)-(.+)\.md$'
    match = re.match(pattern_no_seq, filename)

    if match:
        return {
            'chapter_num': match.group(1),
            'chapter_abbrev': match.group(2),
            'hierarchy': match.group(3),
            'sequence': '',  # No sequence
            'doc_type': match.group(4),
            'description': match.group(5)
        }

    return None


def get_two_digit_hierarchy(hierarchy: str) -> str:
    """
    Extract two-digit sub-chapter from hierarchy
    Example: "2.3.1" -> "2.3", "2.4.2" -> "2.4"
    """
    parts = hierarchy.split('.')
    if len(parts) >= 2:
        return f"{parts[0]}.{parts[1]}"
    return hierarchy


def get_sub_chapter_title(hierarchy: str, existing_files: list) -> str:
    """
    Infer sub-chapter title from existing file descriptions

    This is a simple heuristic - user can manually adjust if needed
    """
    two_digit = get_two_digit_hierarchy(hierarchy)

    # Common patterns for sub-chapter titles
    title_map = {
        "2.1": "Pengantar Pembahasan",
        "2.2": "Prosedur Induk dan Kerangka Umum",
        "2.3": "Layanan Akomodasi (Wisma)",
        "2.4": "Area Pembelajaran",
        "2.5": "Area Kerja dan Khusus",
        "2.6": "Area Makanan dan Minuman (F&B)",
        "2.7": "Area Publik, Fasilitas Pendukung, dan Outdoor",
        "2.8": "Sistem Pengelolaan Mutu dan Dokumentasi"
    }

    # Try to get from predefined map first
    if two_digit in title_map:
        return title_map[two_digit]

    # Otherwise, use generic title
    return f"Sub-Bab {two_digit}"


def analyze_chapter_files(folder_path: Path) -> dict:
    """
    Analyze chapter folder and create work manifest

    Returns:
        dict with keys:
        - chapter_info: metadata about the chapter
        - introduction_files_to_create: list of x.x.0 files to create
        - content_files_to_edit: list of existing files to edit
        - sub_chapters: grouping by sub-chapter
    """
    # Get all markdown files
    md_files = sorted([f for f in folder_path.glob("*.md") if f.is_file()])

    if not md_files:
        print(f"Warning: No markdown files found in {folder_path}")
        return None

    # Parse all filenames
    parsed_files = []
    for f in md_files:
        parsed = parse_filename(f.name)
        if parsed:
            parsed['filename'] = f.name
            parsed_files.append(parsed)
        else:
            print(f"Warning: Could not parse filename: {f.name}")

    if not parsed_files:
        print("Error: No files matched expected naming pattern")
        return None

    # Extract chapter info from first file
    first_file = parsed_files[0]
    chapter_num = first_file['chapter_num']
    chapter_abbrev = first_file['chapter_abbrev']

    # Group files by two-digit sub-chapter
    sub_chapter_groups = defaultdict(list)
    for f in parsed_files:
        two_digit = get_two_digit_hierarchy(f['hierarchy'])
        sub_chapter_groups[two_digit].append(f)

    # Identify which x.x.0 introduction files need to be created
    introduction_files_to_create = []

    for two_digit, files in sorted(sub_chapter_groups.items()):
        # Check if x.x.0 file exists
        has_intro = any(f['hierarchy'] == f"{two_digit}.0" for f in files)

        if not has_intro:
            # Need to create introduction file
            title = get_sub_chapter_title(two_digit, files)

            # Generate filename for x.x.0
            intro_filename = f"{chapter_num}-{chapter_abbrev}-{two_digit}.0-PNGTR-{title.split()[0]}.md"

            # Get source files (all files in this sub-chapter)
            source_files = [f['filename'] for f in files]

            introduction_files_to_create.append({
                'file_to_create': intro_filename,
                'sub_chapter': two_digit,
                'title': title,
                'source_files': source_files
            })

    # List all content files to edit (all existing files)
    content_files_to_edit = [f['filename'] for f in parsed_files]

    # Create sub-chapters summary
    sub_chapters = {}
    for two_digit, files in sorted(sub_chapter_groups.items()):
        sub_chapters[two_digit] = {
            'title': get_sub_chapter_title(two_digit, files),
            'file_count': len(files)
        }

    # Build manifest
    manifest = {
        'chapter_info': {
            'folder': str(folder_path),
            'chapter_number': chapter_num,
            'chapter_abbrev': chapter_abbrev,
            'total_files': len(parsed_files)
        },
        'introduction_files_to_create': introduction_files_to_create,
        'content_files_to_edit': content_files_to_edit,
        'sub_chapters': sub_chapters
    }

    return manifest


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("ERROR: Invalid number of arguments")
        print("\nUsage:")
        print("  python python_scripts/16-analyze-chapter-files.py <folder_path>")
        print("\nExample:")
        print("  python python_scripts/16-analyze-chapter-files.py ./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/markdown-composed")
        sys.exit(1)

    folder_arg = sys.argv[1]
    folder_path = Path(folder_arg)

    # Validate folder exists
    if not folder_path.exists():
        print(f"ERROR: Folder does not exist: {folder_path}")
        sys.exit(1)

    if not folder_path.is_dir():
        print(f"ERROR: Not a directory: {folder_path}")
        sys.exit(1)

    print(f"Analyzing chapter files in: {folder_path}")

    # Analyze files
    manifest = analyze_chapter_files(folder_path)

    if not manifest:
        print("ERROR: Failed to analyze files")
        sys.exit(1)

    # Write manifest
    output_path = folder_path / "chapter-work-manifest.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # Print summary
    print("\n" + "=" * 60)
    print("CHAPTER ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"Chapter: {manifest['chapter_info']['chapter_number']} ({manifest['chapter_info']['chapter_abbrev']})")
    print(f"Total files found: {manifest['chapter_info']['total_files']}")
    print(f"Introduction files to create: {len(manifest['introduction_files_to_create'])}")
    print(f"Content files to edit: {len(manifest['content_files_to_edit'])}")
    print(f"Sub-chapters: {len(manifest['sub_chapters'])}")
    print("=" * 60)

    if manifest['introduction_files_to_create']:
        print("\nIntroduction files to create:")
        for intro in manifest['introduction_files_to_create']:
            print(f"  - {intro['file_to_create']} ({intro['sub_chapter']}: {intro['title']})")

    print(f"\nManifest saved to: {output_path}")
    print("\nReady for content composition workflow!")


if __name__ == "__main__":
    main()
