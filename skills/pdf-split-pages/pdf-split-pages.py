#!/usr/bin/env python3
"""
Script to split PDF files into multiple parts

This script supports multiple splitting modes:
1. By page ranges: python script.py file.pdf --ranges "1-5:part1.pdf,6-10:part2.pdf"
2. Individual pages: python script.py file.pdf --per-page
3. CSV-based splitting: python script.py file.pdf --csv mapping.csv

Uses pypdf library for PDF manipulation.
"""

from pypdf import PdfReader, PdfWriter
from pathlib import Path
import sys
import argparse
import csv


def parse_page_range(range_str: str) -> tuple[int, int]:
    """
    Parse a page range string like "1-5" into start and end page numbers.

    Args:
        range_str: Page range (e.g., "1-5", "3-7")

    Returns:
        tuple[int, int]: (start_page, end_page) in 0-indexed format

    Examples:
        "1-5" → (0, 4)
        "3-7" → (2, 6)
    """
    parts = range_str.split('-')
    if len(parts) != 2:
        raise ValueError(f"Invalid range format: {range_str}. Expected format: 'x-y'")

    start = int(parts[0].strip()) - 1  # Convert to 0-indexed
    end = int(parts[1].strip()) - 1

    if start < 0 or end < 0:
        raise ValueError(f"Page numbers must be positive: {range_str}")

    if start > end:
        raise ValueError(f"Start page cannot be greater than end page: {range_str}")

    return (start, end)


def split_pdf_by_range(input_path: Path, start_page: int, end_page: int, output_path: Path) -> tuple[bool, str]:
    """
    Extract a range of pages from PDF to a new file.

    Args:
        input_path: Source PDF file
        start_page: Starting page (0-indexed)
        end_page: Ending page (0-indexed, inclusive)
        output_path: Output PDF file path

    Returns:
        tuple[bool, str]: (success, message)
    """
    try:
        reader = PdfReader(str(input_path))
        total_pages = len(reader.pages)

        # Validate page range
        if start_page >= total_pages or end_page >= total_pages:
            return False, f"Page range {start_page+1}-{end_page+1} exceeds PDF length ({total_pages} pages)"

        # Create new PDF with specified pages
        writer = PdfWriter()
        for page_num in range(start_page, end_page + 1):
            writer.add_page(reader.pages[page_num])

        # Create output directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write to output file
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        pages_count = end_page - start_page + 1
        return True, f"Created {output_path.name} with {pages_count} page(s) (pages {start_page+1}-{end_page+1})"

    except Exception as e:
        return False, f"Error: {str(e)}"


def split_pdf_per_page(input_path: Path, output_dir: Path = None) -> tuple[int, int, list]:
    """
    Split PDF into individual pages (one PDF per page).

    Args:
        input_path: Source PDF file
        output_dir: Output directory (default: same directory as input)

    Returns:
        tuple[int, int, list]: (success_count, failed_count, failed_files)
    """
    try:
        reader = PdfReader(str(input_path))
        total_pages = len(reader.pages)

        # Determine output directory
        if output_dir is None:
            output_dir = input_path.parent / f"{input_path.stem}_pages"

        output_dir.mkdir(parents=True, exist_ok=True)

        success_count = 0
        failed_count = 0
        failed_files = []

        print(f"\nSplitting {input_path.name} ({total_pages} pages)...")

        for page_num in range(total_pages):
            # Create output filename: original_name_page_001.pdf
            output_name = f"{input_path.stem}_page_{page_num+1:03d}.pdf"
            output_path = output_dir / output_name

            try:
                writer = PdfWriter()
                writer.add_page(reader.pages[page_num])

                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                success_count += 1
                print(f"  [{page_num+1}/{total_pages}] Created: {output_name}")

            except Exception as e:
                failed_count += 1
                failed_files.append((output_name, str(e)))
                print(f"  [{page_num+1}/{total_pages}] ✗ Failed: {output_name} - {str(e)}")

        return success_count, failed_count, failed_files

    except Exception as e:
        print(f"✗ Error reading PDF: {str(e)}")
        return 0, 1, [(input_path.name, str(e))]


def split_pdf_by_csv(input_path: Path, csv_path: Path) -> tuple[int, int, list]:
    """
    Split PDF based on CSV mapping file.

    CSV format:
    output_name,page_range,description
    part1.pdf,1-10,Front Office
    part2.pdf,11-25,Housekeeping

    Args:
        input_path: Source PDF file
        csv_path: CSV mapping file

    Returns:
        tuple[int, int, list]: (success_count, failed_count, failed_files)
    """
    try:
        # Read CSV file
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader_csv = csv.DictReader(f)
            mappings = list(reader_csv)

        if not mappings:
            print(f"✗ Error: CSV file is empty or has no data rows")
            return 0, 0, []

        # Determine output directory (same as CSV file)
        output_dir = csv_path.parent / f"{input_path.stem}_split"
        output_dir.mkdir(parents=True, exist_ok=True)

        success_count = 0
        failed_count = 0
        failed_files = []

        print(f"\nSplitting {input_path.name} using {csv_path.name}...")
        print(f"Output directory: {output_dir}\n")

        for i, row in enumerate(mappings, 1):
            output_name = row.get('output_name', '').strip()
            page_range = row.get('page_range', '').strip()
            description = row.get('description', '').strip()

            if not output_name or not page_range:
                print(f"[{i}/{len(mappings)}] ✗ Skipping row with missing data")
                failed_count += 1
                continue

            try:
                # Parse page range
                start_page, end_page = parse_page_range(page_range)

                # Create output path
                output_path = output_dir / output_name

                # Split PDF
                success, message = split_pdf_by_range(input_path, start_page, end_page, output_path)

                if success:
                    desc_text = f" ({description})" if description else ""
                    print(f"[{i}/{len(mappings)}] ✓ {message}{desc_text}")
                    success_count += 1
                else:
                    print(f"[{i}/{len(mappings)}] ✗ {output_name}: {message}")
                    failed_count += 1
                    failed_files.append((output_name, message))

            except ValueError as e:
                print(f"[{i}/{len(mappings)}] ✗ {output_name}: Invalid page range '{page_range}' - {str(e)}")
                failed_count += 1
                failed_files.append((output_name, str(e)))
            except Exception as e:
                print(f"[{i}/{len(mappings)}] ✗ {output_name}: {str(e)}")
                failed_count += 1
                failed_files.append((output_name, str(e)))

        return success_count, failed_count, failed_files

    except FileNotFoundError:
        print(f"✗ Error: CSV file not found: {csv_path}")
        return 0, 0, []
    except Exception as e:
        print(f"✗ Error reading CSV file: {str(e)}")
        return 0, 0, []


def parse_ranges_argument(ranges_arg: str) -> list[tuple[str, str]]:
    """
    Parse ranges argument in format "1-5:output1.pdf,6-10:output2.pdf".

    Args:
        ranges_arg: Ranges string

    Returns:
        list[tuple[str, str]]: List of (page_range, output_name) tuples

    Examples:
        "1-5:part1.pdf,6-10:part2.pdf" → [("1-5", "part1.pdf"), ("6-10", "part2.pdf")]
    """
    result = []
    parts = ranges_arg.split(',')

    for part in parts:
        part = part.strip()
        if ':' not in part:
            raise ValueError(f"Invalid format: {part}. Expected 'x-y:output.pdf'")

        range_str, output_name = part.split(':', 1)
        result.append((range_str.strip(), output_name.strip()))

    return result


def main():
    """Main function to handle command line arguments."""

    parser = argparse.ArgumentParser(
        description='Split PDF files into multiple parts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  Split by page ranges:
    python 18-split-pdf.py file.pdf --ranges "1-5:part1.pdf,6-10:part2.pdf"

  Split into individual pages:
    python 18-split-pdf.py file.pdf --per-page

  Split into individual pages with custom output directory:
    python 18-split-pdf.py file.pdf --per-page --output-dir ./pages/

  Split using CSV mapping:
    python 18-split-pdf.py file.pdf --csv mapping.csv

CSV Format (for --csv mode):
  output_name,page_range,description
  front-office.pdf,1-10,Front Office
  housekeeping.pdf,11-25,Housekeeping
  food-beverage.pdf,26-40,Food and Beverage

Page numbers start from 1 (not 0).
        '''
    )

    parser.add_argument('input', help='PDF file to split')

    # Splitting modes (mutually exclusive)
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('--ranges', '-r', help='Page ranges with output names (format: "1-5:out1.pdf,6-10:out2.pdf")')
    mode_group.add_argument('--per-page', '-p', action='store_true', help='Split into individual pages (one PDF per page)')
    mode_group.add_argument('--csv', '-c', help='CSV file with splitting instructions')

    # Optional arguments
    parser.add_argument('--output-dir', '-o', help='Output directory (for --per-page mode)')

    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"✗ Error: Input file does not exist: {input_path}")
        sys.exit(1)

    if not input_path.suffix.lower() == '.pdf':
        print(f"✗ Error: Input file is not a PDF: {input_path}")
        sys.exit(1)

    # Process based on mode
    if args.per_page:
        # Per-page mode
        output_dir = Path(args.output_dir) if args.output_dir else None
        success_count, failed_count, failed_files = split_pdf_per_page(input_path, output_dir)

        # Summary
        print(f"\n{'='*60}")
        print(f"Splitting complete!")
        print(f"Success: {success_count}")
        if failed_count > 0:
            print(f"Failed: {failed_count}")
            print(f"\nFailed files:")
            for filename, error in failed_files:
                print(f"  - {filename}: {error}")
        print(f"{'='*60}")

    elif args.csv:
        # CSV mode
        csv_path = Path(args.csv)
        success_count, failed_count, failed_files = split_pdf_by_csv(input_path, csv_path)

        # Summary
        total = success_count + failed_count
        print(f"\n{'='*60}")
        print(f"Splitting complete!")
        print(f"Success: {success_count}/{total}")
        if failed_count > 0:
            print(f"Failed: {failed_count}/{total}")
            print(f"\nFailed files:")
            for filename, error in failed_files:
                print(f"  - {filename}: {error}")
        print(f"{'='*60}")

    elif args.ranges:
        # Ranges mode
        try:
            # Parse ranges
            ranges = parse_ranges_argument(args.ranges)

            # Determine output directory
            output_dir = input_path.parent / f"{input_path.stem}_split"
            output_dir.mkdir(parents=True, exist_ok=True)

            success_count = 0
            failed_count = 0
            failed_files = []

            print(f"\nSplitting {input_path.name}...")
            print(f"Output directory: {output_dir}\n")

            for i, (range_str, output_name) in enumerate(ranges, 1):
                try:
                    # Parse page range
                    start_page, end_page = parse_page_range(range_str)

                    # Create output path
                    output_path = output_dir / output_name

                    # Split PDF
                    success, message = split_pdf_by_range(input_path, start_page, end_page, output_path)

                    if success:
                        print(f"[{i}/{len(ranges)}] ✓ {message}")
                        success_count += 1
                    else:
                        print(f"[{i}/{len(ranges)}] ✗ {output_name}: {message}")
                        failed_count += 1
                        failed_files.append((output_name, message))

                except ValueError as e:
                    print(f"[{i}/{len(ranges)}] ✗ {output_name}: Invalid range '{range_str}' - {str(e)}")
                    failed_count += 1
                    failed_files.append((output_name, str(e)))

            # Summary
            total = success_count + failed_count
            print(f"\n{'='*60}")
            print(f"Splitting complete!")
            print(f"Success: {success_count}/{total}")
            if failed_count > 0:
                print(f"Failed: {failed_count}/{total}")
                print(f"\nFailed files:")
                for filename, error in failed_files:
                    print(f"  - {filename}: {error}")
            print(f"{'='*60}")

        except ValueError as e:
            print(f"✗ Error: Invalid ranges format - {str(e)}")
            print(f"  Expected format: '1-5:out1.pdf,6-10:out2.pdf'")
            sys.exit(1)


if __name__ == "__main__":
    main()
