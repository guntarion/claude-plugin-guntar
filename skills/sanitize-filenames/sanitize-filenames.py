#!/usr/bin/env python3
"""
Script to sanitize filenames and folder names

This script supports multiple input modes:
1. Single file/folder: python script.py path/to/file.txt
2. Multiple files/folders: python script.py path1,path2,path3
3. Folder (recursive): python script.py path/to/folder

Sanitization rules:
- Replace spaces with underscores
- Remove unsafe characters: , & @ '
- Keep safe characters: ( ) [ ] alphanumeric . - _
- Deduplicate consecutive symbols
"""

from pathlib import Path
import sys
import re


def sanitize_name(name: str) -> str:
    """
    Sanitize filename or folder name.
    
    Rules:
    - Replace spaces with underscores
    - Remove unsafe characters: , & @ ' (apostrophe)
    - Keep safe characters: ( ) [ ] alphanumeric . - _
    - Replace multiple consecutive spaces with single underscore
    - Replace multiple consecutive symbols (._-) with single symbol
    
    Args:
        name: Original name (without path)
    
    Returns:
        str: Sanitized name
    """
    # First, replace multiple consecutive spaces with single space
    name = re.sub(r' +', ' ', name)
    
    # Then replace spaces with underscores
    sanitized = name.replace(' ', '_')
    
    # Remove unsafe characters: comma, ampersand, at sign, apostrophe
    unsafe_chars = [',', '&', '@', "'"]
    for char in unsafe_chars:
        sanitized = sanitized.replace(char, '')
    
    # Remove any characters that are NOT:
    # - alphanumeric (a-z, A-Z, 0-9)
    # - dot (.)
    # - hyphen (-)
    # - underscore (_)
    # - parentheses ( )
    # - square brackets [ ]
    sanitized = re.sub(r'[^a-zA-Z0-9.\-_()\[\]]', '', sanitized)
    
    # Replace multiple consecutive underscores with single underscore
    sanitized = re.sub(r'_+', '_', sanitized)
    
    # Replace multiple consecutive dots with single dot
    sanitized = re.sub(r'\.+', '.', sanitized)
    
    # Replace multiple consecutive dashes with single dash
    sanitized = re.sub(r'-+', '-', sanitized)
    
    # Remove leading/trailing underscores, dots, or dashes
    sanitized = sanitized.strip('_.-')
    
    return sanitized


def sanitize_file(file_path: Path, dry_run: bool = False) -> tuple[bool, str, str]:
    """
    Sanitize a single file name.
    
    Args:
        file_path: Path to the file
        dry_run: If True, don't actually rename, just show what would happen
    
    Returns:
        tuple[bool, str, str]: (changed, old_name, new_name)
    """
    old_name = file_path.name
    
    # Split name and extension
    if file_path.is_file():
        stem = file_path.stem
        suffix = file_path.suffix
        new_stem = sanitize_name(stem)
        new_name = new_stem + suffix
    else:
        # It's a folder
        new_name = sanitize_name(old_name)
    
    if old_name == new_name:
        return False, old_name, new_name
    
    if not dry_run:
        new_path = file_path.parent / new_name
        # If target exists, add number suffix
        counter = 1
        while new_path.exists():
            if file_path.is_file():
                new_name = f"{new_stem}_{counter}{suffix}"
            else:
                new_name = f"{sanitize_name(old_name)}_{counter}"
            new_path = file_path.parent / new_name
            counter += 1
        
        file_path.rename(new_path)
    
    return True, old_name, new_name


def get_paths_to_sanitize(input_arg: str) -> list[Path]:
    """
    Parse input argument and return list of paths to sanitize.
    
    Args:
        input_arg: Command line argument string
    
    Returns:
        list[Path]: List of Path objects
    """
    paths = []
    
    # Check if input contains commas (multiple paths mode)
    if ',' in input_arg:
        path_strings = [p.strip() for p in input_arg.split(',')]
        for path_str in path_strings:
            path = Path(path_str)
            if not path.exists():
                print(f"Warning: Skipping non-existent path: {path}")
            else:
                paths.append(path)
        return paths
    
    # Single path
    input_path = Path(input_arg)
    
    if not input_path.exists():
        print(f"✗ Error: Path does not exist: {input_path}")
        return []
    
    return [input_path]


def sanitize_recursive(folder_path: Path, file_pattern: str = '*', dry_run: bool = False) -> dict:
    """
    Recursively sanitize all files in a folder matching pattern.
    
    Args:
        folder_path: Path to folder
        file_pattern: Glob pattern for files (default: '*' = all files)
        dry_run: If True, don't actually rename
    
    Returns:
        dict: Statistics about renaming
    """
    stats = {'total': 0, 'renamed': 0, 'unchanged': 0, 'changes': []}
    
    # Get all matching files recursively
    for file_path in folder_path.rglob(file_pattern):
        if file_path.is_file():
            stats['total'] += 1
            changed, old_name, new_name = sanitize_file(file_path, dry_run)
            
            if changed:
                stats['renamed'] += 1
                stats['changes'].append((str(file_path.parent), old_name, new_name))
            else:
                stats['unchanged'] += 1
    
    return stats


def main():
    """Main function to handle command line arguments."""
    
    if len(sys.argv) < 2:
        print("✗ Error: No input provided")
        print("\nUsage:")
        print("  Single file/folder:    python 11-sanitize-filenames.py path/to/file.txt")
        print("  Multiple paths:        python 11-sanitize-filenames.py path1,path2,path3")
        print("  Folder (all files):    python 11-sanitize-filenames.py path/to/folder/")
        print("  Folder (pattern):      python 11-sanitize-filenames.py path/to/folder/ *.pdf")
        print("\nSanitization rules:")
        print("  - Spaces → underscores")
        print("  - Remove: , & @ '")
        print("  - Keep: ( ) [ ] letters numbers . - _")
        print("  - Deduplicate consecutive symbols")
        sys.exit(1)
    
    input_arg = sys.argv[1]
    file_pattern = sys.argv[2] if len(sys.argv) > 2 else '*'
    
    # Get paths to process
    paths = get_paths_to_sanitize(input_arg)
    
    if not paths:
        sys.exit(1)
    
    print(f"\nFound {len(paths)} path(s) to process\n")
    
    # Process each path
    total_renamed = 0
    total_unchanged = 0
    
    for path in paths:
        if path.is_dir():
            # Folder mode - sanitize all files matching pattern
            print(f"Processing folder: {path}")
            print(f"Pattern: {file_pattern}\n")
            
            stats = sanitize_recursive(path, file_pattern, dry_run=False)
            
            print(f"{'='*60}")
            print(f"Folder: {path}")
            print(f"Total files processed: {stats['total']}")
            print(f"Renamed: {stats['renamed']}")
            print(f"Unchanged: {stats['unchanged']}")
            
            if stats['changes']:
                print(f"\nRenamed files:")
                for folder, old, new in stats['changes'][:20]:  # Show first 20
                    print(f"  {old}")
                    print(f"    → {new}")
                
                if len(stats['changes']) > 20:
                    print(f"  ... and {len(stats['changes']) - 20} more")
            
            print(f"{'='*60}\n")
            
            total_renamed += stats['renamed']
            total_unchanged += stats['unchanged']
            
        else:
            # File mode - sanitize single file
            print(f"Sanitizing: {path.name}... ", end="", flush=True)
            changed, old_name, new_name = sanitize_file(path, dry_run=False)
            
            if changed:
                print(f"✓")
                print(f"  {old_name}")
                print(f"    → {new_name}")
                total_renamed += 1
            else:
                print(f"○ (no change needed)")
                total_unchanged += 1
    
    # Final summary
    if len(paths) > 1 or (len(paths) == 1 and paths[0].is_dir()):
        print(f"\n{'='*60}")
        print(f"Summary:")
        print(f"Total renamed: {total_renamed}")
        print(f"Total unchanged: {total_unchanged}")
        print(f"{'='*60}")


if __name__ == "__main__":
    main()
