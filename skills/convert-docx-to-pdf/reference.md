# Convert DOCX to PDF - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Conversion Method](#conversion-method)
3. [Usage Modes](#usage-modes)
4. [Expected Output](#expected-output)
5. [Examples](#examples)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Usage](#advanced-usage)
8. [Performance Notes](#performance-notes)

## When to Use This Skill

Activate this skill when the user requests to:
- Convert .docx files to PDF format
- Transform Word documents to PDF
- Batch convert documents in a folder
- Use LibreOffice for document conversion

## Conversion Method

Uses **LibreOffice/soffice** for fast, reliable conversion:
- No dependency on Microsoft Word
- Direct command-line conversion
- Consistent results across documents
- Requires LibreOffice to be installed (typically via `brew install --cask libreoffice`)

## Usage Modes

### Mode 1: Single File Conversion

For converting one document:

```bash
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py path/to/file.docx
```

**Example:**
```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "./BUKU-2/01-FRONT-OFFICE-(UPDL-SEMARANG)/Document.docx"
```

**Output:** PDF saved in same directory as source file

### Mode 2: Multiple Files (Comma-Separated)

For converting specific documents without confirmation prompt:

```bash
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py file1.docx,file2.docx,file3.docx
```

**Example:**
```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "doc1.docx,doc2.docx,doc3.docx"
```

**Output:** Each PDF saved in same directory as respective .docx file

### Mode 3: Folder Mode (Test-First Safety)

For converting all .docx files in a folder:

```bash
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py ./path/to/folder
```

**Example:**
```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "./BUKU-2/01-FRONT-OFFICE-(UPDL-SEMARANG)"
```

**Workflow:**
1. Scans folder for all .docx files
2. Tests conversion on first file
3. Shows result: `✓ Successfully converted Document.docx`
4. Prompts user: `Test successful! Process all [N] documents? (y/n):`
5. Waits for user confirmation
6. If user enters `y`, processes all remaining files
7. Shows progress: `[1/N] filename... ✓`
8. Displays final summary with success/failure counts

## Expected Output

### Single File Success
```
Found 1 .docx file(s) to convert

Converting: Document.docx... ✓
  Output: Document.pdf
  Method: soffice (LibreOffice)
```

### Multiple Files Success
```
Found 3 .docx file(s) to convert

Processing 3 files...

[1/3] Document1.docx... ✓
[2/3] Document2.docx... ✓
[3/3] Document3.docx... ✓

============================================================
Conversion complete!
Success: 3/3
============================================================
```

### Folder Mode - Test Phase
```
Found 45 .docx file(s) to convert

Testing on: Document001.docx
✓ Successfully converted test document

Test successful! Process all 45 documents? (y/n):
```

### Folder Mode - Batch Processing (After User Confirms 'y')
```
Processing all 45 documents...

[1/45] Document001.docx... ✓
[2/45] Document002.docx... ✓
[3/45] Document003.docx... ✓
...
[45/45] Document045.docx... ✓

============================================================
Conversion complete!
Success: 45/45
============================================================
```

## What Gets Converted

- **Input format**: .docx files only
- **Output format**: PDF (Portable Document Format)
- **Output location**: Same directory as source file
- **Naming**: Same filename, .pdf extension
  - Example: `Report.docx` → `Report.pdf`
  - Example: `ProjectProposal.docx` → `ProjectProposal.pdf`

## Important Notes

- **Files preserved**: Original .docx files remain unchanged
- **Output location**: PDFs saved alongside source files in same directory
- **Rendering**: Uses LibreOffice for accurate PDF conversion
- **Test-first for folders**: Always tests first file before batch
- **User confirmation**: Batch operations require confirmation
- **Requirements**: LibreOffice must be installed (`brew install --cask libreoffice`)

## Examples

### Example 1: Convert Single File
User: "Convert this Word document to PDF"
```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "./path/to/document.docx"
```

### Example 2: Convert Multiple Specific Files
User: "Convert these three documents to PDF: report.docx, proposal.docx, invoice.docx"
```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "report.docx,proposal.docx,invoice.docx"
```

### Example 3: Convert All Files in Folder (Test-First)
User: "Convert all Word documents in the front office folder to PDF"
```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "./BUKU-2/01-FRONT-OFFICE-(UPDL-SEMARANG)"
```
Script tests first file, shows result, waits for confirmation, then processes all.

### Example 4: Mix of Paths
User: "Convert documents in different locations"
```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "./folder1/doc1.docx,./folder2/doc2.docx"
```

### Example 5: Verify Conversion
User: "Check if the conversion worked"
- Look in the same directory as the original .docx files
- PDF files should have same name as .docx files
- Open in PDF viewer to verify conversion quality

## Troubleshooting

### "soffice command not found"
- LibreOffice is not installed
- Install: `brew install --cask libreoffice`
- Verify: `which soffice` (should show `/opt/homebrew/bin/soffice`)

### Files not found
- Verify folder path is correct
- Check that .docx files exist in the folder
- Use forward slashes: `./FOLDER/SUBFOLDER`

### Permission errors
- Ensure files are not locked (closed in Word)
- Check file permissions: files should be readable
- Output directory should be writable

### Conversion fails for some documents
- File may be corrupted or have complex formatting
- Check if Word or LibreOffice can open the file normally
- Script will continue with other files even if one fails
- Check error message for specific document

### Missing output files
- Verify conversion succeeded (✓ indicator shown)
- Check the source directory for PDF files
- Ensure output directory is writable
- Check available disk space

### Conversion timeout (90 seconds)
- Very large or complex documents may timeout
- Try converting file individually
- Reduce document complexity if possible

## Advanced Usage

### For Different Folders
Change the folder path in the command:
```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "./YOUR-DIFFERENT-FOLDER-PATH"
```

### Automating Multiple Folders
Run the script separately for each folder:
```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "./BUKU-2/01-FRONT-OFFICE-(UPDL-SEMARANG)"
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py "./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)"
```

## Related Skills
- **remove-headers-footers**: Remove headers/footers from Word documents

## Dependencies
- Python 3.6+
- LibreOffice (`soffice` command-line tool)
- Project virtual environment (.venv)

## Performance Notes
- **Speed**: ~1-5 seconds per document
- **Large batches**: 100+ documents may take several minutes
- **System resources**: Uses ~100MB RAM per conversion
- **Concurrent**: Processes files sequentially for stability
