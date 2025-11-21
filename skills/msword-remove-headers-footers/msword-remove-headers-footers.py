#!/usr/bin/env python3
"""
Script to remove all headers and footers from .docx files
"""

from docx import Document
from pathlib import Path
import sys
from typing import List

def remove_headers_footers(docx_path: str) -> bool:
    """
    Remove all headers and footers from a .docx file

    Args:
        docx_path: Path to the .docx file

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        doc = Document(docx_path)

        # Remove all headers and footers from all sections
        for section in doc.sections:
            # List of all header/footer types to process
            header_footer_types = [
                ('header', section.header),
                ('footer', section.footer),
            ]

            # Add first page header/footer if different first page is enabled
            if section.different_first_page_header_footer:
                header_footer_types.extend([
                    ('first_page_header', section.first_page_header),
                    ('first_page_footer', section.first_page_footer),
                ])

            # Add even page header/footer (python-docx provides these regardless of settings)
            try:
                header_footer_types.extend([
                    ('even_page_header', section.even_page_header),
                    ('even_page_footer', section.even_page_footer),
                ])
            except AttributeError:
                # even_page_header/footer not available in older versions
                pass

            # Process each header/footer type
            for hf_name, hf_obj in header_footer_types:
                # Remove all child elements directly from the XML
                # This includes paragraphs, tables, and SDT (content controls)
                for element in list(hf_obj._element):
                    hf_obj._element.remove(element)

        # Save the modified document
        doc.save(docx_path)
        return True

    except Exception as e:
        print(f"Error processing {docx_path}: {e}")
        return False

def main():
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file:       python 09-remove-headers-footers.py path/to/file.docx")
        print("  Multiple files:    python 09-remove-headers-footers.py file1.docx,file2.docx,file3.docx")
        print("  Folder mode:       python 09-remove-headers-footers.py path/to/folder [--yes]")
        print("\nOptions:")
        print("  --yes, -y          Skip confirmation prompt in folder mode")
        sys.exit(1)

    # Check for --yes flag
    auto_confirm = '--yes' in sys.argv or '-y' in sys.argv

    # Get input path (first non-flag argument)
    input_path = sys.argv[1] if not sys.argv[1].startswith('-') else sys.argv[2]

    # Check if input contains comma (multiple files mode)
    if ',' in input_path:
        # Multiple files mode
        file_paths = [p.strip() for p in input_path.split(',')]
        docx_files = []

        for file_path in file_paths:
            path = Path(file_path)
            if not path.exists():
                print(f"Error: File not found: {file_path}")
                sys.exit(1)
            if not path.suffix.lower() == '.docx':
                print(f"Error: Not a .docx file: {file_path}")
                sys.exit(1)
            docx_files.append(path)

        print(f"Processing {len(docx_files)} files...\n")
        success_count = 0
        failed_count = 0

        for i, docx_file in enumerate(docx_files, 1):
            print(f"[{i}/{len(docx_files)}] {docx_file.name}... ", end="", flush=True)
            if remove_headers_footers(str(docx_file)):
                print("✓")
                success_count += 1
            else:
                print("✗")
                failed_count += 1

        print(f"\n{'='*60}")
        print(f"Processing complete!")
        print(f"Success: {success_count}/{len(docx_files)}")
        if failed_count > 0:
            print(f"Failed: {failed_count}/{len(docx_files)}")
        print(f"{'='*60}")

    else:
        # Single path mode (file or folder)
        path = Path(input_path)

        if not path.exists():
            print(f"Error: Path not found: {input_path}")
            sys.exit(1)

        if path.is_file():
            # Single file mode
            if not path.suffix.lower() == '.docx':
                print(f"Error: Not a .docx file: {input_path}")
                sys.exit(1)

            print(f"Processing: {path.name}... ", end="", flush=True)
            if remove_headers_footers(str(path)):
                print("✓")
                print(f"\n{'='*60}")
                print(f"Successfully removed headers/footers from {path.name}")
                print(f"{'='*60}")
            else:
                print("✗")
                sys.exit(1)

        elif path.is_dir():
            # Folder mode with test-first approach
            docx_files = list(path.glob("*.docx"))

            if not docx_files:
                print(f"No .docx files found in folder: {input_path}")
                sys.exit(1)

            print(f"Found {len(docx_files)} .docx files\n")

            # Test on first document
            test_file = docx_files[0]
            print(f"Testing on: {test_file.name}")

            if remove_headers_footers(str(test_file)):
                print(f"✓ Successfully removed headers/footers from test document\n")

                # Ask user to confirm before processing all files (unless --yes flag is used)
                if auto_confirm:
                    response = 'y'
                    print("Auto-confirm enabled. Processing all documents...")
                else:
                    response = input("Test successful! Process all documents? (y/n): ").strip().lower()

                if response == 'y':
                    print(f"\nProcessing all {len(docx_files)} documents...\n")
                    success_count = 0
                    failed_count = 0

                    for i, docx_file in enumerate(docx_files, 1):
                        print(f"[{i}/{len(docx_files)}] {docx_file.name}... ", end="", flush=True)
                        if remove_headers_footers(str(docx_file)):
                            print("✓")
                            success_count += 1
                        else:
                            print("✗")
                            failed_count += 1

                    print(f"\n{'='*60}")
                    print(f"Processing complete!")
                    print(f"Success: {success_count}/{len(docx_files)}")
                    if failed_count > 0:
                        print(f"Failed: {failed_count}/{len(docx_files)}")
                    print(f"{'='*60}")
                else:
                    print("Cancelled. Only test document was modified.")
            else:
                print(f"✗ Failed to process test document")
                sys.exit(1)

        else:
            print(f"Error: Invalid path: {input_path}")
            sys.exit(1)

if __name__ == "__main__":
    main()
