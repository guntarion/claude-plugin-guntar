# Convert .docx to PDF

## Purpose
This script converts Microsoft Word documents (.docx format) to PDF files using the `docx2pdf` library. It supports three input modes: single file, multiple files (comma-separated), and entire folders with optional test-first confirmation.

## How It Works
1. **Single file mode**: Converts one .docx file to PDF
2. **Multiple files mode**: Converts specified .docx files (comma-separated)
3. **Folder mode**: Finds all .docx files in folder, tests on first file, then processes all with confirmation
4. **Safety**: Includes test-first workflow for batch operations
5. **Progress tracking**: Shows real-time progress with success/failure counts

## Requirements
- **Library**: `docx2pdf` (included in project dependencies)
- **Python version**: 3.6+
- **Virtual environment**: Must activate project `.venv` before running
- **Platform**: macOS (uses Microsoft Word for accurate rendering)

## Usage

### Activate Virtual Environment
```bash
source .venv/bin/activate
```

### Mode 1: Single File
Convert one .docx file to PDF:
```bash
python python_scripts/10-convert-docx-to-pdf.py path/to/document.docx
```

**Output**: `path/to/document.pdf` (saved in same directory)

### Mode 2: Multiple Files (Comma-Separated)
Convert specific .docx files:
```bash
python python_scripts/10-convert-docx-to-pdf.py file1.docx,file2.docx,file3.docx
```

**Output**: `file1.pdf`, `file2.pdf`, `file3.pdf` (each in same directory as source)

### Mode 3: Folder Mode (With Test-First Safety)
Convert all .docx files in a folder:
```bash
python python_scripts/10-convert-docx-to-pdf.py ./BUKU-2/01-FRONT-OFFICE-(UPDL-SEMARANG)
```

**Interactive Workflow**:
1. Finds all .docx files in folder
2. Tests on first file
3. Shows result: `✓ Successfully converted document.docx`
4. Prompts: `Test successful! Process all [N] documents? (y/n):`
5. Enter `y` to process all remaining files
6. Shows progress and final summary

### Mode 4: Folder Mode (Auto-Confirm)
Convert all .docx files without confirmation prompt:
```bash
python python_scripts/10-convert-docx-to-pdf.py ./BUKU-2/01-FRONT-OFFICE-(UPDL-SEMARANG) --yes
```

**Non-Interactive Workflow**:
- Use `--yes` or `-y` flag to skip confirmation prompt
- Automatically processes all files after successful test
- Useful for automation and scripting

**Example output**:
```
Found 30 .docx files

Testing on: Document1.docx
✓ Successfully converted Document1.docx

Test successful! Process all 30 documents? (y/n): y

Processing all 30 documents...

[1/30] Document1.docx... ✓
[2/30] Document2.docx... ✓
[3/30] Document3.docx... ✓
...
[30/30] Document30.docx... ✓

============================================================
Conversion complete!
Success: 30/30
============================================================
```

### Display Help
```bash
python python_scripts/10-convert-docx-to-pdf.py
```

Shows usage instructions and examples.

## Output Files
- **Location**: Same directory as source .docx file
- **Naming**: Same filename with `.pdf` extension
- **Example**: `Report.docx` → `Report.pdf`

## Features

### File Support
- **Accepts**: .docx files only
- **Converts to**: PDF format
- **Validation**: Checks file existence and format before conversion

### Progress Tracking
- Shows `[current/total]` format
- Uses ✓ for successful conversions
- Uses ✗ for failed conversions
- Final summary with counts

### Error Handling
- Displays meaningful error messages
- Continues processing other files if one fails
- Lists all failed files in summary
- Appropriate exit codes

### Safety Features
- Test-first approach for folders
- User confirmation before batch operations
- Validates file paths and formats
- No automatic file deletion or replacement

## Practical Examples

### Example 1: Convert Single Document
```bash
source .venv/bin/activate
python python_scripts/10-convert-docx-to-pdf.py "Reports/2024-Annual-Report.docx"
```
Creates: `Reports/2024-Annual-Report.pdf`

### Example 2: Convert Multiple Specific Documents
```bash
source .venv/bin/activate
python python_scripts/10-convert-docx-to-pdf.py "doc1.docx,doc2.docx,doc3.docx"
```
Creates: `doc1.pdf`, `doc2.pdf`, `doc3.pdf`

### Example 3: Convert All Documents in Folder
```bash
source .venv/bin/activate
python python_scripts/10-convert-docx-to-pdf.py "./BUKU-2/01-FRONT-OFFICE-(UPDL-SEMARANG)"
```
Tests first, then converts all .docx files in the folder.

## Troubleshooting

### "File not found" error
- Verify the file path is correct
- Check that file extension is .docx (not .doc)
- Ensure file exists in the specified location

### "Module not found: docx2pdf"
- Activate virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

### "Permission denied"
- Check file permissions (file should be readable)
- Ensure the script has execute permissions
- Files should not be locked (closed in Word)

### "Conversion failed" on some files
- File may be corrupted or have incompatible format
- Try converting other files first
- Check Word can open the file normally
- Script will continue with other files

### No output files created
- Check that conversion succeeded (✓ indicator)
- Verify output directory is writable
- Check file system has available space

## Reusable Script
This script is designed for reuse. You can:
1. Use with different folders by changing the input path
2. Batch convert multiple folders by running script multiple times
3. Integrate into larger workflows

## Dependencies Used
- **docx2pdf**: Converts .docx to PDF (uses Word on Mac)
- **pathlib**: Modern file path operations
- **sys**: Command-line arguments and system operations

## Performance Notes
- **Conversion time**: Depends on document complexity and system load
- **Large batches**: May take longer for folders with 100+ documents
- **System resources**: Briefly opens Word for each conversion (requires ~100MB per file)

## Mac-Specific Notes
- Requires Microsoft Word to be installed on macOS
- Uses native Word engine for accurate PDF rendering
- Preserves formatting, fonts, images, and layout
