#!/usr/bin/env python3
"""
Script to convert .docx files to PDF format using LibreOffice/soffice

This script supports three input modes:
1. Single file: python script.py path/to/file.docx
2. Multiple files: python script.py path/file1.docx,path/file2.docx
3. Folder: python script.py path/to/folder (processes all .docx files)

Uses soffice (LibreOffice) for reliable, fast conversion.
Output PDFs have sanitized filenames (spaces→underscores, unsafe chars removed).
"""

from pathlib import Path
import sys
import subprocess
import shutil
import re


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for PDF output.
    
    Rules:
    - Replace spaces with underscores
    - Remove unsafe characters: , & @ ' (apostrophe)
    - Keep safe characters: ( ) [ ] alphanumeric . - _
    - Replace multiple consecutive spaces with single underscore
    - Replace multiple consecutive symbols (._-) with single symbol
    
    Args:
        filename: Original filename (without extension)
    
    Returns:
        str: Sanitized filename
    """
    # First, replace multiple consecutive spaces with single space
    filename = re.sub(r' +', ' ', filename)
    
    # Then replace spaces with underscores
    sanitized = filename.replace(' ', '_')
    
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


def convert_single_file(docx_path: Path) -> tuple[bool, str]:
    """
    Convert a single .docx file to PDF using soffice.
    PDF filename will be sanitized (spaces→underscores, unsafe chars removed).

    Args:
        docx_path: Path object pointing to the .docx file

    Returns:
        tuple[bool, str]: (success, error_message_or_method)
    """
    try:
        # Validate input file
        if not docx_path.exists():
            return False, f"File not found: {docx_path}"

        if not docx_path.suffix.lower() == '.docx':
            return False, f"Not a .docx file: {docx_path}"

        # Check if soffice is available
        soffice_path = shutil.which("soffice")
        if not soffice_path:
            return False, "soffice command not found. Please install LibreOffice."

        # soffice creates PDF with same name as .docx (with spaces)
        temp_pdf_path = docx_path.with_suffix('.pdf')
        
        # Create final PDF path with sanitized filename
        pdf_filename = sanitize_filename(docx_path.stem) + '.pdf'
        final_pdf_path = docx_path.parent / pdf_filename
        output_dir = docx_path.parent

        # Run soffice conversion
        result = subprocess.run(
            [soffice_path, "--headless", "--convert-to", "pdf", "--outdir", str(output_dir), str(docx_path)],
            capture_output=True,
            text=True,
            timeout=90
        )

        # Check if conversion succeeded
        if result.returncode == 0 and temp_pdf_path.exists():
            # Rename PDF to sanitized filename
            if temp_pdf_path != final_pdf_path:
                # If target file exists, remove it first
                if final_pdf_path.exists():
                    final_pdf_path.unlink()
                temp_pdf_path.rename(final_pdf_path)
            return True, "soffice (LibreOffice)"
        else:
            error_msg = result.stderr if result.stderr else result.stdout
            return False, f"Conversion failed: {error_msg}"

    except subprocess.TimeoutExpired:
        return False, "Conversion timed out after 90 seconds"
    except Exception as e:
        return False, f"Error: {str(e)}"


def get_file_list(input_arg: str) -> list[Path]:
    """
    Parse input argument and return list of .docx file paths.

    Args:
        input_arg: Command line argument string

    Returns:
        list[Path]: List of Path objects for .docx files to convert
    """
    # Check if input contains commas (multiple files mode)
    if ',' in input_arg:
        file_paths = [Path(f.strip()) for f in input_arg.split(',')]
        valid_paths = []
        for path in file_paths:
            if not path.exists():
                print(f"Warning: Skipping non-existent file: {path}")
            elif not path.suffix.lower() == '.docx':
                print(f"Warning: Skipping non-.docx file: {path}")
            else:
                valid_paths.append(path)
        return valid_paths

    # Single path - could be file or folder
    input_path = Path(input_arg)

    if not input_path.exists():
        print(f"✗ Error: Path does not exist: {input_path}")
        return []

    # Check if it's a directory
    if input_path.is_dir():
        docx_files = sorted(input_path.glob('*.docx'))
        if not docx_files:
            print(f"✗ Error: No .docx files found in folder: {input_path}")
            return []
        return docx_files

    # Single file
    if input_path.suffix.lower() == '.docx':
        return [input_path]
    else:
        print(f"✗ Error: Not a .docx file: {input_path}")
        return []


def get_output_filename(docx_path: Path) -> str:
    """Get the output PDF filename with sanitized name."""
    return sanitize_filename(docx_path.stem) + '.pdf'


def main():
    """Main function to handle command line arguments and orchestrate conversion."""

    if len(sys.argv) < 2:
        print("✗ Error: Invalid number of arguments")
        print("\nUsage:")
        print("  Single file:     python 10-convert-docx-to-pdf.py path/to/file.docx")
        print("  Multiple files:  python 10-convert-docx-to-pdf.py file1.docx,file2.docx,file3.docx")
        print("  Folder:          python 10-convert-docx-to-pdf.py path/to/folder [--yes]")
        print("\nOptions:")
        print("  --yes, -y        Skip confirmation prompt in folder mode")
        print("\nNote: Output PDF filenames will be sanitized:")
        print("  - Spaces replaced with underscores")
        print("  - Unsafe characters (,&@') removed")
        print("  - Multiple consecutive symbols deduplicated")
        sys.exit(1)

    # Check for --yes flag
    auto_confirm = '--yes' in sys.argv or '-y' in sys.argv

    # Get input path (first non-flag argument)
    input_arg = sys.argv[1] if not sys.argv[1].startswith('-') else sys.argv[2]

    # Get list of files to convert
    files_to_convert = get_file_list(input_arg)

    if not files_to_convert:
        sys.exit(1)

    print(f"\nFound {len(files_to_convert)} .docx file(s) to convert\n")

    # Determine mode and process accordingly
    if len(files_to_convert) == 1:
        # Single file mode
        file_path = files_to_convert[0]
        print(f"Converting: {file_path.name}... ", end="", flush=True)
        success, message = convert_single_file(file_path)

        if success:
            print(f"✓")
            print(f"  Output: {get_output_filename(file_path)}")
            print(f"  Method: {message}")
        else:
            print(f"✗")
            print(f"  Error: {message}")
            sys.exit(1)

    elif ',' in input_arg:
        # Multiple files mode (no confirmation needed)
        print(f"Processing {len(files_to_convert)} files...\n")
        success_count = 0
        failed_count = 0
        failed_files = []

        for i, file_path in enumerate(files_to_convert, 1):
            print(f"[{i}/{len(files_to_convert)}] {file_path.name}... ", end="", flush=True)
            success, message = convert_single_file(file_path)

            if success:
                print("✓")
                success_count += 1
            else:
                print("✗")
                failed_count += 1
                failed_files.append((file_path.name, message))

        print(f"\n{'='*60}")
        print(f"Conversion complete!")
        print(f"Success: {success_count}/{len(files_to_convert)}")
        if failed_count > 0:
            print(f"Failed: {failed_count}/{len(files_to_convert)}")
            print(f"\nFailed files:")
            for filename, error in failed_files:
                print(f"  - {filename}: {error}")
        print(f"{'='*60}")

    else:
        # Folder mode (test-first with confirmation)
        test_file = files_to_convert[0]
        print(f"Testing on: {test_file.name}")

        success, message = convert_single_file(test_file)

        if success:
            print(f"✓ Successfully converted test document")
            print(f"  Output: {get_output_filename(test_file)}\n")

            if auto_confirm:
                response = 'y'
                print("Auto-confirm enabled. Processing all documents...")
            else:
                response = input(f"Test successful! Process all {len(files_to_convert)} documents? (y/n): ").strip().lower()

            if response == 'y':
                print(f"\nProcessing all {len(files_to_convert)} documents...\n")
                success_count = 0
                failed_count = 0
                failed_files = []

                for i, file_path in enumerate(files_to_convert, 1):
                    print(f"[{i}/{len(files_to_convert)}] {file_path.name}... ", end="", flush=True)
                    success, msg = convert_single_file(file_path)

                    if success:
                        print("✓")
                        success_count += 1
                    else:
                        print("✗")
                        failed_count += 1
                        failed_files.append((file_path.name, msg))

                print(f"\n{'='*60}")
                print(f"Conversion complete!")
                print(f"Success: {success_count}/{len(files_to_convert)}")
                if failed_count > 0:
                    print(f"Failed: {failed_count}/{len(files_to_convert)}")
                    print(f"\nFailed files:")
                    for filename, error in failed_files:
                        print(f"  - {filename}: {error}")
                print(f"{'='*60}")
            else:
                print("Cancelled. Only test document was converted.")
        else:
            print(f"✗ Failed to convert test document")
            print(f"Error: {message}")
            sys.exit(1)


if __name__ == "__main__":
    main()
