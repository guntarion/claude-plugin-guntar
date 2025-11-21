#!/usr/bin/env python3
"""
PDF to Markdown Converter using pymupdf4llm

This script converts PDF files to Markdown format using the pymupdf4llm library,
which provides fast conversion with accurate table extraction.

Usage:
    python 13-convert-pdf-to-markdown.py <file|files|folder>

Input Modes:
    1. Single file: python 13-convert-pdf-to-markdown.py "./path/to/file.pdf"
    2. Multiple files (comma-separated): python 13-convert-pdf-to-markdown.py "file1.pdf,file2.pdf"
    3. Folder: python 13-convert-pdf-to-markdown.py "./path/to/folder"

Output:
    - Markdown files saved in same directory as source PDFs
    - Same filename with .md extension
    - Example: document.pdf → document.md

Dependencies:
    - pymupdf4llm (install via: pip install pymupdf4llm)

Author: Claude Code
Date: 2025-11-19
"""

import sys
import pymupdf4llm
from pathlib import Path


def is_interactive():
    """Check if the script is running in an interactive terminal."""
    return sys.stdin.isatty()


def convert_pdf_to_markdown(pdf_path):
    """
    Convert a single PDF file to Markdown format.

    Args:
        pdf_path (Path): Path to the PDF file

    Returns:
        tuple: (success: bool, output_path: Path or None, error_message: str or None)
    """
    try:
        # Convert PDF to markdown
        md_text = pymupdf4llm.to_markdown(str(pdf_path))

        # Create output path (same directory, .md extension)
        output_path = pdf_path.with_suffix('.md')

        # Save markdown to file
        output_path.write_text(md_text, encoding='utf-8')

        return True, output_path, None

    except Exception as e:
        return False, None, str(e)


def process_single_file(file_path):
    """Process a single PDF file."""
    print(f"\nConverting: {file_path.name}...", end=" ", flush=True)

    success, output_path, error = convert_pdf_to_markdown(file_path)

    if success:
        print("✓")
        print(f"  Output: {output_path.name}")
        return True
    else:
        print("✗")
        print(f"  Error: {error}")
        return False


def process_multiple_files(file_paths):
    """Process multiple PDF files."""
    total = len(file_paths)
    success_count = 0
    failed_files = []

    print(f"\nProcessing {total} file(s)...\n")

    for idx, file_path in enumerate(file_paths, 1):
        print(f"[{idx}/{total}] {file_path.name}...", end=" ", flush=True)

        success, output_path, error = convert_pdf_to_markdown(file_path)

        if success:
            print("✓")
            success_count += 1
        else:
            print("✗")
            print(f"  Error: {error}")
            failed_files.append(file_path.name)

    # Print summary
    print("\n" + "=" * 60)
    print("Conversion complete!")
    print(f"Success: {success_count}/{total}")
    if failed_files:
        print(f"Failed: {len(failed_files)}")
        print("Failed files:")
        for fname in failed_files:
            print(f"  - {fname}")
    print("=" * 60)


def process_folder(folder_path, test_first=True):
    """
    Process all PDF files in a folder.

    Args:
        folder_path (Path): Path to the folder
        test_first (bool): If True, test first file before processing all
    """
    # Find all PDF files in folder
    pdf_files = sorted(folder_path.glob("*.pdf"))

    if not pdf_files:
        print(f"\nNo PDF files found in: {folder_path}")
        return

    total = len(pdf_files)
    print(f"\nFound {total} PDF file(s) to convert")

    if test_first and total > 1:
        # Test mode: convert first file and ask for confirmation
        print(f"\nTesting on: {pdf_files[0].name}")
        success, output_path, error = convert_pdf_to_markdown(pdf_files[0])

        if success:
            print(f"✓ Successfully converted test document")
            print(f"  Output: {output_path.name}")

            # Ask for confirmation (or auto-proceed in non-interactive mode)
            if is_interactive():
                response = input(f"\nTest successful! Process all {total} documents? (y/n): ").strip().lower()
                if response != 'y':
                    print("Conversion cancelled.")
                    return
            else:
                # Non-interactive mode: automatically proceed
                print(f"\nAuto-proceeding with all {total} documents (non-interactive mode)...")

            # Process remaining files
            remaining_files = pdf_files[1:]
            if remaining_files:
                print(f"\nProcessing remaining {len(remaining_files)} documents...\n")
                success_count = 1  # Include the test file
                failed_files = []

                for idx, file_path in enumerate(remaining_files, 2):
                    print(f"[{idx}/{total}] {file_path.name}...", end=" ", flush=True)

                    success, output_path, error = convert_pdf_to_markdown(file_path)

                    if success:
                        print("✓")
                        success_count += 1
                    else:
                        print("✗")
                        print(f"  Error: {error}")
                        failed_files.append(file_path.name)

                # Print summary
                print("\n" + "=" * 60)
                print("Conversion complete!")
                print(f"Success: {success_count}/{total}")
                if failed_files:
                    print(f"Failed: {len(failed_files)}")
                    print("Failed files:")
                    for fname in failed_files:
                        print(f"  - {fname}")
                print("=" * 60)
        else:
            print(f"✗ Test conversion failed")
            print(f"  Error: {error}")
            print("\nPlease fix the issue and try again.")
    else:
        # Process all files without testing
        process_multiple_files(pdf_files)


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python 13-convert-pdf-to-markdown.py <file|files|folder>")
        print("\nExamples:")
        print('  Single file:    python 13-convert-pdf-to-markdown.py "./path/to/file.pdf"')
        print('  Multiple files: python 13-convert-pdf-to-markdown.py "file1.pdf,file2.pdf"')
        print('  Folder:         python 13-convert-pdf-to-markdown.py "./path/to/folder"')
        sys.exit(1)

    input_arg = sys.argv[1]

    # Check if input contains comma (multiple files)
    if ',' in input_arg:
        # Multiple files mode
        file_paths = [Path(f.strip()).resolve() for f in input_arg.split(',')]

        # Validate all files exist and are PDFs
        valid_files = []
        for fp in file_paths:
            if not fp.exists():
                print(f"Warning: File not found: {fp}")
            elif not fp.is_file():
                print(f"Warning: Not a file: {fp}")
            elif fp.suffix.lower() != '.pdf':
                print(f"Warning: Not a PDF file: {fp}")
            else:
                valid_files.append(fp)

        if not valid_files:
            print("\nNo valid PDF files to process.")
            sys.exit(1)

        print(f"Found {len(valid_files)} valid PDF file(s)")
        process_multiple_files(valid_files)

    else:
        # Single path (file or folder)
        input_path = Path(input_arg).resolve()

        if not input_path.exists():
            print(f"Error: Path not found: {input_path}")
            sys.exit(1)

        if input_path.is_file():
            # Single file mode
            if input_path.suffix.lower() != '.pdf':
                print(f"Error: Not a PDF file: {input_path}")
                sys.exit(1)

            print(f"Found 1 PDF file to convert")
            if process_single_file(input_path):
                print("\n" + "=" * 60)
                print("Conversion complete!")
                print("=" * 60)
            else:
                sys.exit(1)

        elif input_path.is_dir():
            # Folder mode
            process_folder(input_path, test_first=True)

        else:
            print(f"Error: Invalid path: {input_path}")
            sys.exit(1)


if __name__ == "__main__":
    main()
