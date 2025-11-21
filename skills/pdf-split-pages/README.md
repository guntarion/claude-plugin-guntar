# Split PDF Files

## Purpose
This script splits PDF files into multiple parts. It supports three splitting modes:
1. **By page ranges**: Extract specific ranges to named output files
2. **Per-page**: Split into individual pages (one PDF per page)
3. **CSV-based**: Use CSV mapping to split PDF into multiple parts

## How It Works
1. **Reads input PDF**: Opens the source PDF file
2. **Validates parameters**: Checks page ranges and output specifications
3. **Creates new PDFs**: Extracts specified pages to new PDF files
4. **Saves to output**: Writes split PDFs to output directory

## Requirements
- **Library**: `pypdf` (included in project dependencies)
- **Python version**: 3.6+
- **Virtual environment**: Must activate project `.venv` before running

## Usage

### Activate Virtual Environment
```bash
source .venv/bin/activate
```

### Basic Syntax
```bash
python python_scripts/18-split-pdf.py <input.pdf> <mode> [options]
```

## Mode 1: Split by Page Ranges

Extract specific page ranges to named output files.

### Syntax
```bash
python python_scripts/18-split-pdf.py file.pdf --ranges "x-y:output1.pdf,a-b:output2.pdf"
```

### Examples

**Split into two parts:**
```bash
python python_scripts/18-split-pdf.py document.pdf --ranges "1-10:part1.pdf,11-20:part2.pdf"
```

**Split into three parts:**
```bash
python python_scripts/18-split-pdf.py document.pdf --ranges "1-5:intro.pdf,6-15:main.pdf,16-20:appendix.pdf"
```

**Extract specific sections:**
```bash
python python_scripts/18-split-pdf.py manual.pdf --ranges "1-3:cover.pdf,10-25:chapter1.pdf,50-75:chapter2.pdf"
```

### Output
- Creates folder: `{input_name}_split/`
- Saves files with specified names
- Example: If input is `document.pdf`, creates `document_split/part1.pdf`, `document_split/part2.pdf`

## Mode 2: Split Per Page

Split PDF into individual pages (one PDF per page).

### Syntax
```bash
python python_scripts/18-split-pdf.py file.pdf --per-page
```

### Examples

**Basic per-page split:**
```bash
python python_scripts/18-split-pdf.py document.pdf --per-page
```
- Input: `document.pdf` (20 pages)
- Output folder: `document_pages/`
- Output files: `document_page_001.pdf`, `document_page_002.pdf`, ..., `document_page_020.pdf`

**Per-page with custom output directory:**
```bash
python python_scripts/18-split-pdf.py document.pdf --per-page --output-dir ./individual-pages/
```
- Output folder: `individual-pages/`

### Output
- Default folder: `{input_name}_pages/`
- File naming: `{input_name}_page_001.pdf`, `{input_name}_page_002.pdf`, etc.
- Numbers padded with zeros (001, 002, ... 099, 100, etc.)

## Mode 3: CSV-Based Splitting

Use CSV file to define splitting instructions. This mode is useful when you need to split a PDF into many parts based on a structured mapping.

### CSV Format

Create a CSV file with these columns:
- `output_name`: Name of output PDF file
- `page_range`: Page range (format: `x-y`)
- `description`: Optional description (for reference)

**Example CSV** (`mapping.csv`):
```csv
output_name,page_range,description
01-front-office.pdf,1-10,Front Office procedures
02-housekeeping.pdf,11-25,Housekeeping procedures
03-food-beverage.pdf,26-40,Food and Beverage
04-maintenance.pdf,41-60,Maintenance procedures
05-security.pdf,61-80,Security and K3L
```

### Syntax
```bash
python python_scripts/18-split-pdf.py file.pdf --csv mapping.csv
```

### Examples

**Basic CSV-based split:**
```bash
python python_scripts/18-split-pdf.py manual.pdf --csv chapter-mapping.csv
```

**Real-world example (SOP document):**
```bash
python python_scripts/18-split-pdf.py "Panduan-Lengkap.pdf" --csv "unit-mapping.csv"
```

### Output
- Creates folder: `{input_name}_split/`
- Saves files according to CSV `output_name` column
- Example: If input is `manual.pdf`, creates `manual_split/01-front-office.pdf`, `manual_split/02-housekeeping.pdf`, etc.

## Page Specification

### Range Format (x-y)
- `1-5`: Pages 1 through 5 (inclusive)
- `10-20`: Pages 10 through 20
- `1-1`: Single page (page 1)

**Important**:
- Page numbers start from 1 (not 0)
- Both start and end are inclusive
- Start page must be ≤ end page

## Command-Line Options

### Required Arguments
- `input`: Path to PDF file to split

### Mode Selection (choose one)
- `--ranges` / `-r`: Page ranges with output names
- `--per-page` / `-p`: Split into individual pages
- `--csv` / `-c`: CSV file with splitting instructions

### Optional Arguments
- `--output-dir` / `-o`: Custom output directory (only for `--per-page` mode)

## Output Examples

### Mode 1: Ranges
```
Splitting document.pdf...
Output directory: document_split

[1/3] ✓ Created part1.pdf with 10 page(s) (pages 1-10)
[2/3] ✓ Created part2.pdf with 10 page(s) (pages 11-20)
[3/3] ✓ Created part3.pdf with 5 page(s) (pages 21-25)

============================================================
Splitting complete!
Success: 3/3
============================================================
```

### Mode 2: Per-Page
```
Splitting document.pdf (25 pages)...
  [1/25] Created: document_page_001.pdf
  [2/25] Created: document_page_002.pdf
  [3/25] Created: document_page_003.pdf
  ...
  [25/25] Created: document_page_025.pdf

============================================================
Splitting complete!
Success: 25
============================================================
```

### Mode 3: CSV
```
Splitting manual.pdf using mapping.csv...
Output directory: manual_split

[1/5] ✓ Created 01-front-office.pdf with 10 page(s) (pages 1-10) (Front Office procedures)
[2/5] ✓ Created 02-housekeeping.pdf with 15 page(s) (pages 11-25) (Housekeeping procedures)
[3/5] ✓ Created 03-food-beverage.pdf with 15 page(s) (pages 26-40) (Food and Beverage)
[4/5] ✓ Created 04-maintenance.pdf with 20 page(s) (pages 41-60) (Maintenance procedures)
[5/5] ✓ Created 05-security.pdf with 20 page(s) (pages 61-80) (Security and K3L)

============================================================
Splitting complete!
Success: 5/5
============================================================
```

## Important Notes
- **Original file preserved**: Source PDF is never modified
- **Output directory created automatically**: Script creates output folder if it doesn't exist
- **Page validation**: Script validates that specified page ranges exist in PDF
- **Overwrites existing files**: If output files exist, they will be overwritten
- **Page numbering**: Pages numbered from 1 (user-friendly), internally 0-indexed

## Error Handling

### Invalid Page Range
```
[1/3] ✗ part1.pdf: Page range 1-100 exceeds PDF length (50 pages)
```

### Invalid Format (Ranges Mode)
```
✗ Error: Invalid ranges format
  Expected format: '1-5:out1.pdf,6-10:out2.pdf'
```

### File Not Found
```
✗ Error: Input file does not exist: missing.pdf
```

### CSV Missing Columns
```
[1/5] ✗ Skipping row with missing data
```

## Use Cases

### 1. Extract Chapters from Book
Split a book PDF into individual chapter files:
```bash
python python_scripts/18-split-pdf.py book.pdf --ranges "1-20:ch1.pdf,21-45:ch2.pdf,46-80:ch3.pdf"
```

### 2. Separate Cover, Content, and Appendix
```bash
python python_scripts/18-split-pdf.py report.pdf --ranges "1-1:cover.pdf,2-50:content.pdf,51-60:appendix.pdf"
```

### 3. Create Individual Page Scans
Convert multi-page PDF into separate page files:
```bash
python python_scripts/18-split-pdf.py scanned-document.pdf --per-page
```

### 4. Split SOP Manual by Unit/Department
Use CSV mapping to organize SOP manual by departments:

**Create `unit-mapping.csv`:**
```csv
output_name,page_range,description
01-FRONT-OFFICE.pdf,6-15,Proses 6.0 Pelayanan Pelanggan
02-HOUSEKEEPING.pdf,16-30,Proses 12.4 Layanan Umum
03-FOOD-BEVERAGE.pdf,31-45,Proses 12.4 Penyediaan Konsumsi
04-MAINTENANCE.pdf,46-65,Proses 10.0 Aset dan 12.4 GA
05-SECURITY.pdf,66-85,Proses 11.5 Keamanan dan 13.7 K3L
```

**Run the split:**
```bash
python python_scripts/18-split-pdf.py "Panduan-Proses-Bisnis.pdf" --csv unit-mapping.csv
```

### 5. Extract Specific Sections
Extract only the sections you need:
```bash
python python_scripts/18-split-pdf.py manual.pdf --ranges "10-15:section-a.pdf,25-30:section-b.pdf"
```

## Advanced Examples

### Create Test/Sample PDFs
Extract first few pages for review:
```bash
python python_scripts/18-split-pdf.py large-document.pdf --ranges "1-5:sample.pdf"
```

### Split by Document Sections
```bash
python python_scripts/18-split-pdf.py thesis.pdf --ranges "1-10:abstract.pdf,11-50:chapter1.pdf,51-100:chapter2.pdf,101-120:references.pdf"
```

### Batch Organization with CSV
Organize large procedural manual into 14 units:
```bash
python python_scripts/18-split-pdf.py "UPDL-Pandaan-Manual.pdf" --csv "14-unit-mapping.csv"
```

## Troubleshooting

### Module not found: pypdf
- Activate virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

### Invalid page specification
- Ensure pages are specified correctly: `"1-5:out.pdf"` not `"1 - 5:out.pdf"`
- Use commas to separate ranges: `"1-5:a.pdf,6-10:b.pdf"`
- Page numbers must be positive integers
- Start page must be ≤ end page

### Page range exceeds PDF length
- Check PDF page count first
- Adjust page ranges to be within valid range
- Page numbers are 1-indexed (first page = 1, not 0)

### CSV file format errors
- Ensure CSV has header row: `output_name,page_range,description`
- Check for missing commas or quotes
- Use UTF-8 encoding for CSV file
- Ensure page_range format is correct: `x-y`

### Permission denied
- Ensure output directory is writable
- Check that output files aren't open in PDF viewer

## Reusable Script
This script is designed for reuse across different PDF splitting tasks:
- Change input file path
- Change splitting mode (ranges, per-page, CSV)
- Reuse CSV files for similar documents
- Create multiple CSV mappings for different splitting strategies

## Dependencies Used
- **pypdf**: PDF manipulation (read pages, write new PDFs)
- **pathlib**: File path operations
- **argparse**: Command-line argument parsing
- **csv**: CSV file reading and parsing
- **sys**: System operations

## Performance Notes
- **Speed**: ~0.5-2 seconds per output file (depends on page count)
- **Memory**: Efficient - processes pages sequentially
- **Large files**: PDFs with 500+ pages handled smoothly
- **Output**: Files written sequentially

## Help
Display full help and examples:
```bash
python python_scripts/18-split-pdf.py --help
```

## Comparison with Other Approaches

| Feature | This Script | Manual (PDF Editor) | Online Tools |
|---------|-------------|-------------------|--------------|
| Batch splitting | Yes (CSV mode) | No | Limited |
| Command-line | Yes | No | No |
| Free | Yes | Varies | Free with limits |
| Automation-friendly | Yes | No | No |
| Offline | Yes | Yes | No |
| Custom naming | Yes | Yes | Limited |
| Original preserved | Yes | Yes | Varies |
| Privacy | Full | Full | Risk |

## Related Scripts
- **12-delete-pdf-pages.py**: Delete pages from PDFs
- **10-convert-docx-to-pdf.py**: Convert Word to PDF
- **sanitize-filenames**: Clean output filenames
