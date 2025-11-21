# PDF to Markdown Converter

## Overview
This script converts PDF files to Markdown format using the `pymupdf4llm` library, which provides fast conversion with accurate table extraction optimized for LLM processing.

## Script Information
- **Script Name**: `13-convert-pdf-to-markdown.py`
- **Location**: `python_scripts/13-convert-pdf-to-markdown.py`
- **Primary Library**: `pymupdf4llm`
- **Python Version**: 3.6+

## Features
- ✅ Convert single PDF file to Markdown
- ✅ Convert multiple PDF files (comma-separated list)
- ✅ Convert all PDFs in a folder with test-first safety
- ✅ Accurate table extraction and preservation
- ✅ Fast conversion optimized for LLM processing
- ✅ Output saved in same directory as source files
- ✅ Progress tracking with success/failure indicators
- ✅ Detailed error reporting

## Installation

### Dependencies
The script requires the `pymupdf4llm` library:

```bash
# Activate virtual environment
source .venv/bin/activate

# Install pymupdf4llm (if not already installed)
pip install pymupdf4llm
```

The dependency is already listed in `requirements.txt`.

## Usage

### Basic Command Structure
```bash
source .venv/bin/activate
python python_scripts/13-convert-pdf-to-markdown.py <input>
```

### Input Modes

#### Mode 1: Single File
Convert one PDF file to Markdown:

```bash
python python_scripts/13-convert-pdf-to-markdown.py "./path/to/document.pdf"
```

**Example**:
```bash
source .venv/bin/activate
python python_scripts/13-convert-pdf-to-markdown.py "./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/report.pdf"
```

**Output**:
- Input: `report.pdf`
- Output: `report.md` (same directory)

#### Mode 2: Multiple Files (Comma-Separated)
Convert specific PDF files without confirmation prompt:

```bash
python python_scripts/13-convert-pdf-to-markdown.py "file1.pdf,file2.pdf,file3.pdf"
```

**Example**:
```bash
source .venv/bin/activate
python python_scripts/13-convert-pdf-to-markdown.py "./doc1.pdf,./doc2.pdf,./doc3.pdf"
```

**Output**:
- Each PDF converted to `.md` in its respective directory
- Progress shown: `[1/3] doc1.pdf... ✓`

#### Mode 3: Folder (Test-First Safety)
Convert all PDF files in a folder:

```bash
python python_scripts/13-convert-pdf-to-markdown.py "./path/to/folder"
```

**Example**:
```bash
source .venv/bin/activate
python python_scripts/13-convert-pdf-to-markdown.py "./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)"
```

**Workflow**:
1. Scans folder for all `.pdf` files
2. Tests conversion on first file
3. Shows result: `✓ Successfully converted test document`
4. Prompts user: `Test successful! Process all [N] documents? (y/n):`
5. Waits for user confirmation (`y` to continue)
6. Processes all remaining files with progress tracking
7. Displays final summary with success/failure counts

## Output Format

### Markdown Files
- **Extension**: `.md`
- **Location**: Same directory as source PDF
- **Encoding**: UTF-8
- **Naming**: Same filename as PDF
  - Example: `document.pdf` → `document.md`
  - Example: `report-2024.pdf` → `report-2024.md`

### Content Features
The `pymupdf4llm` library extracts:
- Text content with proper formatting
- Headings and structure
- Tables (accurately preserved)
- Lists and bullet points
- Basic formatting (bold, italic)
- Optimized for LLM processing

## Expected Output

### Single File Success
```
Found 1 PDF file to convert

Converting: document.pdf... ✓
  Output: document.md

============================================================
Conversion complete!
============================================================
```

### Multiple Files Success
```
Found 3 valid PDF file(s)

Processing 3 file(s)...

[1/3] report.pdf... ✓
[2/3] summary.pdf... ✓
[3/3] analysis.pdf... ✓

============================================================
Conversion complete!
Success: 3/3
============================================================
```

### Folder Mode - Test Phase
```
Found 15 PDF file(s) to convert

Testing on: document001.pdf
✓ Successfully converted test document
  Output: document001.md

Test successful! Process all 15 documents? (y/n):
```

### Folder Mode - After Confirmation
```
Processing remaining 14 documents...

[2/15] document002.pdf... ✓
[3/15] document003.pdf... ✓
...
[15/15] document015.pdf... ✓

============================================================
Conversion complete!
Success: 15/15
============================================================
```

### Error Handling
```
[1/5] corrupted.pdf... ✗
  Error: Failed to read PDF file

============================================================
Conversion complete!
Success: 4/5
Failed: 1
Failed files:
  - corrupted.pdf
============================================================
```

## Use Cases

### 1. Extract PDF Content for LLM Processing
Convert PDF documents to Markdown for easier text analysis and LLM processing:
```bash
python python_scripts/13-convert-pdf-to-markdown.py "./research-paper.pdf"
```

### 2. Batch Convert Documentation
Convert all PDF manuals in a folder to Markdown:
```bash
python python_scripts/13-convert-pdf-to-markdown.py "./documentation/"
```

### 3. Archive PDF Content as Text
Create searchable Markdown archives of PDF files:
```bash
python python_scripts/13-convert-pdf-to-markdown.py "./archive/*.pdf"
```

### 4. Table Extraction
Extract tables from PDF reports to Markdown format for further processing:
```bash
python python_scripts/13-convert-pdf-to-markdown.py "./reports/quarterly-data.pdf"
```

## Advantages of pymupdf4llm

### Fast Performance
- Optimized C++ backend via PyMuPDF
- Significantly faster than OCR-based solutions
- Efficient memory usage

### Accurate Table Extraction
- Preserves table structure in Markdown format
- Maintains cell alignment and content
- Handles complex tables with merged cells

### LLM-Optimized Output
- Clean Markdown formatting
- Preserves document structure
- Removes unnecessary formatting artifacts
- Ready for text analysis and processing

## Limitations

### PDF Format Limitations
- **Scanned PDFs**: Requires OCR for scanned images (not included)
- **Complex Layouts**: Multi-column layouts may not preserve exactly
- **Embedded Images**: Images are not extracted or embedded in Markdown
- **Forms**: Interactive PDF forms may not convert properly
- **Encryption**: Password-protected PDFs are not supported

### Content Accuracy
- Conversion accuracy depends on PDF structure
- Some formatting may be lost or altered
- Best results with text-based PDFs

## Troubleshooting

### Issue: "No module named 'pymupdf4llm'"
**Solution**: Install the library:
```bash
source .venv/bin/activate
pip install pymupdf4llm
```

### Issue: "No PDF files found in folder"
**Causes**:
- Folder path is incorrect
- No `.pdf` files exist in the folder
- Files have different extensions (.PDF in uppercase)

**Solution**:
- Verify folder path: `ls "./path/to/folder"`
- Check file extensions are lowercase `.pdf`

### Issue: "Error: Path not found"
**Solution**:
- Use absolute paths or paths relative to project root
- Verify folder exists: `ls "./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)"`
- Use forward slashes: `./folder/subfolder`

### Issue: Conversion fails for specific PDF
**Possible causes**:
- Corrupted PDF file
- Encrypted/password-protected PDF
- Scanned image PDF (requires OCR)
- Unsupported PDF version

**Solution**:
- Try opening PDF in a viewer to verify it's valid
- Remove encryption if present
- Use OCR software for scanned PDFs first
- Check error message for specific issue

### Issue: Output Markdown is messy or incomplete
**Causes**:
- Complex PDF layout (multi-column, floating elements)
- Scanned PDF without proper text layer
- Heavily formatted PDF with lots of graphics

**Solution**:
- For scanned PDFs: Use OCR preprocessing
- For complex layouts: May require manual cleanup
- Check source PDF quality and structure

### Issue: Missing tables in output
**Possible cause**: Table format not recognized by library

**Solution**:
- Verify table exists in source PDF
- Try converting table-heavy page separately
- Consider alternative table extraction tools if needed

## Performance

### Speed
- **Small PDFs** (1-10 pages): < 1 second per file
- **Medium PDFs** (10-50 pages): 1-3 seconds per file
- **Large PDFs** (50+ pages): 3-10 seconds per file

### Memory Usage
- Minimal memory footprint
- Can handle large batches efficiently
- Processes files sequentially to avoid memory issues

## Related Scripts
- **12-delete-pdf-pages.py**: Delete specific pages from PDF files
- **10-convert-docx-to-pdf.py**: Convert Word documents to PDF

## Related Skills
- **convert-pdf-to-markdown**: Claude skill for using this script
- **delete-pdf-pages**: Delete pages from PDF files

## Version History
- **v1.0** (2025-11-19): Initial release
  - Single file conversion
  - Multiple files conversion
  - Folder mode with test-first safety
  - Progress tracking and error reporting

## Author
Created by Claude Code for the UPDL-Pandaan project.

## License
Internal use for UPDL-Pandaan documentation processing.
