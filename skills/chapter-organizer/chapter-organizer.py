#!/usr/bin/env python3
"""
Generic Chapter Organizer Script
Renames markdown files according to hierarchical structure based on CSV mapping

Usage:
    python python_scripts/15-chapter-organizer.py <mapping_csv> <folder>

    mapping_csv: Path to CSV file with columns: old_name,new_name
    folder: Target folder containing markdown files to rename

Example:
    python python_scripts/15-chapter-organizer.py ./mapping-bab-3.csv ./BUKU-3/03-SECURITY/markdown-ordered
"""

from pathlib import Path
import sys
import csv
from datetime import datetime


def load_mapping_from_csv(csv_path: str) -> dict:
    """
    Load file mapping from CSV file

    CSV format:
        old_name,new_name
        oldfile1.md,newfile1.md
        oldfile2.md,newfile2.md

    Args:
        csv_path: Path to CSV mapping file

    Returns:
        dict: Mapping dictionary {old_name: new_name}
    """
    mapping = {}

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            # Validate headers
            if 'old_name' not in reader.fieldnames or 'new_name' not in reader.fieldnames:
                print(f"ERROR: CSV must have 'old_name' and 'new_name' columns")
                print(f"Found columns: {reader.fieldnames}")
                sys.exit(1)

            for row in reader:
                old_name = row['old_name'].strip()
                new_name = row['new_name'].strip()

                if old_name and new_name:
                    mapping[old_name] = new_name

        return mapping

    except FileNotFoundError:
        print(f"ERROR: Mapping CSV not found: {csv_path}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR reading CSV: {e}")
        sys.exit(1)


def generate_rename_log(folder_path: Path) -> str:
    """Generate rename log file path"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_name = f"rename-log-{timestamp}.txt"
    return str(folder_path / log_name)


def validate_files(folder_path: Path, mapping: dict) -> tuple[list, list]:
    """
    Validate that all source files exist

    Args:
        folder_path: Target folder
        mapping: File mapping dictionary

    Returns:
        tuple: (existing_files, missing_files)
    """
    existing = []
    missing = []

    for old_name in mapping.keys():
        file_path = folder_path / old_name
        if file_path.exists():
            existing.append(old_name)
        else:
            missing.append(old_name)

    return existing, missing


def rename_files(folder_path: Path, mapping: dict) -> dict:
    """
    Rename files according to mapping

    Args:
        folder_path: Target folder
        mapping: File mapping dictionary

    Returns:
        dict: Statistics and results
    """
    stats = {
        'success': 0,
        'failed': 0,
        'skipped': 0,
        'details': []
    }

    # Validate files first
    existing, missing = validate_files(folder_path, mapping)

    if missing:
        stats['details'].append(f"WARNING: {len(missing)} files not found:")
        for fname in missing:
            stats['details'].append(f"  - {fname}")
        stats['details'].append("")

    # Process existing files
    for old_name in existing:
        new_name = mapping[old_name]
        old_path = folder_path / old_name
        new_path = folder_path / new_name

        # Check if target already exists
        if new_path.exists() and new_path != old_path:
            stats['skipped'] += 1
            stats['details'].append(f"SKIP: {new_name} (target already exists)")
            continue

        # Perform rename
        try:
            old_path.rename(new_path)
            stats['details'].append(f"RENAMED: {old_name}")
            stats['details'].append(f"     TO: {new_name}")
            stats['success'] += 1
        except Exception as e:
            stats['failed'] += 1
            stats['details'].append(f"ERROR: {old_name}")
            stats['details'].append(f"  {str(e)}")

    return stats


def print_results(stats: dict):
    """Print renaming results"""
    print("\n" + "=" * 60)
    print("RENAME OPERATION COMPLETE")
    print("=" * 60)
    print(f"Success: {stats['success']}")
    print(f"Failed: {stats['failed']}")
    print(f"Skipped: {stats['skipped']}")
    print("=" * 60)

    if stats['details']:
        print("\nDetails:")
        for detail in stats['details']:
            print(detail)


def write_log(log_path: str, stats: dict, csv_path: str, folder_path: str):
    """Write rename log to file"""
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write("Chapter Organizer - Rename Log\n")
        f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Mapping CSV: {csv_path}\n")
        f.write(f"Target Folder: {folder_path}\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Success: {stats['success']}\n")
        f.write(f"Failed: {stats['failed']}\n")
        f.write(f"Skipped: {stats['skipped']}\n")
        f.write("=" * 60 + "\n\n")

        f.write("Details:\n")
        for detail in stats['details']:
            f.write(detail + "\n")


def verify_sorting(folder_path: Path, chapter_prefix: str):
    """
    Verify that renamed files are properly sorted

    Args:
        folder_path: Target folder
        chapter_prefix: Chapter prefix pattern (e.g., "02-HK-", "03-SEC-")
    """
    # Detect prefix from first file in mapping
    files = sorted([f.name for f in folder_path.glob(f"{chapter_prefix}*.md")])

    if not files:
        print("\nNo files found with prefix:", chapter_prefix)
        return

    print("\n" + "=" * 60)
    print("VERIFICATION: File Sorting Order")
    print("=" * 60)

    for i, fname in enumerate(files, 1):
        print(f"{i:2d}. {fname}")

    print("=" * 60)
    print(f"Total files: {len(files)}")
    print("=" * 60)


def main():
    """Main function"""
    if len(sys.argv) != 3:
        print("ERROR: Invalid number of arguments")
        print("\nUsage:")
        print("  python 15-chapter-organizer.py <mapping_csv> <folder>")
        print("\nExamples:")
        print("  python 15-chapter-organizer.py ./mapping-bab-2.csv ./BUKU-2/02-HOUSEKEEPING/markdown-ordered")
        print("  python 15-chapter-organizer.py ./mapping-bab-3.csv ./BUKU-3/03-SECURITY/markdown-ordered")
        print("\nCSV Format:")
        print("  old_name,new_name")
        print("  oldfile1.md,newfile1.md")
        print("  oldfile2.md,newfile2.md")
        sys.exit(1)

    csv_path = sys.argv[1]
    folder_arg = sys.argv[2]

    # Convert to Path object
    folder_path = Path(folder_arg)

    # Validate folder exists
    if not folder_path.exists():
        print(f"ERROR: Folder does not exist: {folder_path}")
        sys.exit(1)

    if not folder_path.is_dir():
        print(f"ERROR: Not a directory: {folder_path}")
        sys.exit(1)

    # Load mapping from CSV
    print(f"Loading mapping from: {csv_path}")
    mapping = load_mapping_from_csv(csv_path)

    if not mapping:
        print("ERROR: No valid mappings found in CSV")
        sys.exit(1)

    print(f"Target folder: {folder_path}")
    print(f"Total files in mapping: {len(mapping)}")

    # Perform rename operation
    stats = rename_files(folder_path, mapping)

    # Print results
    print_results(stats)

    # Write log
    log_path = generate_rename_log(folder_path)
    write_log(log_path, stats, csv_path, str(folder_path))
    print(f"\nLog written to: {log_path}")

    # Verify sorting if any renames succeeded
    if stats['success'] > 0:
        # Detect chapter prefix from first new_name in mapping
        first_new_name = next(iter(mapping.values()))
        # Extract prefix (e.g., "02-HK-" from "02-HK-2.1.0-PNGTR-Housekeeping.md")
        parts = first_new_name.split('-')
        if len(parts) >= 2:
            chapter_prefix = f"{parts[0]}-{parts[1]}-"
            verify_sorting(folder_path, chapter_prefix)


if __name__ == "__main__":
    main()
