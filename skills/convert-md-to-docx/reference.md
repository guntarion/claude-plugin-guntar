# Convert Markdown to Word - Reference Documentation

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Conversion Method](#conversion-method)
- [Document Specifications](#document-specifications)
- [Three Input Modes](#three-input-modes)
- [Expected Output](#expected-output)
- [Output Location & Filename](#output-location--filename)
- [What Gets Converted](#what-gets-converted)
- [Important Notes](#important-notes)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Advanced Usage](#advanced-usage)
- [Technical Notes](#technical-notes)

## When to Use This Skill
Activate this skill when the user requests to:
- Convert .md files to .docx format
- Merge multiple markdown files into one Word document
- Generate Word document from markdown folder
- Combine markdown chapters into single .docx
- Use the existing `21-md-to-docx.py` script

## Instructions

### Script Location & Usage
The reusable script is located at: `.claude/skills/convert-md-to-docx/convert-md-to-docx.py`

Always activate the virtual environment before running:
```bash
source .venv/bin/activate
```

### Conversion Method
Uses **pypandoc** (Python wrapper for Pandoc) with **python-docx** for formatting:
- Automatic markdown to Word conversion
- Preserves formatting (headings, bold, italic, lists, tables)
- Custom paper size and margins
- Reference template for consistent styling
- Files merged in alphabetical order

### Document Specifications

**Paper Size**: B5 JIS (18.2 x 25.71 cm)

**Margins (Mirror Layout)**:
- Top: 2.5 cm
- Bottom: 2.5 cm
- Inside: 2.5 cm (binding side)
- Outside: 2.0 cm
- Gutter: 0 cm

**Formatting**:
- Heading 1/2/3 styles from markdown `#`, `##`, `###`
- Bold and italic formatting preserved
- Bullet and numbered lists
- Tables converted to Word tables

### Three Input Modes

#### Mode 1: Comma-Separated Files
For converting specific markdown files:
```bash
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py file1.md,file2.md,file3.md output.docx
```

**Important**: Files are always merged in **alphabetical order** regardless of input order.

Usage example:
```bash
source .venv/bin/activate
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py "chapter1.md,chapter2.md,chapter3.md" my_book.docx
```

Output: `my_book.docx` in the **source folder** (same folder as first file)

#### Mode 2: Folder Path with Custom Output
For converting all .md files in a folder:
```bash
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py ./path/to/folder output.docx
```

Usage example:
```bash
source .venv/bin/activate
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop" perpustakaan.docx
```

Output: `perpustakaan.docx` in the **source folder** (`0B-improved-sop/`)

#### Mode 3: Folder Path with Auto-Generated Name (from First Line)
For automatic filename from first line of first file:
```bash
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py ./path/to/folder
```

Usage example:
```bash
source .venv/bin/activate
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop"
```

Output: Filename generated from first line (e.g., `PENGANTAR BAB 14_ PENGELOLAAN PERPUSTAKAAN.docx`)

**How it works**:
1. Reads first line of first markdown file (alphabetically)
2. Removes markdown heading symbols (`#`, `##`, etc.)
3. Sanitizes filename (removes unsafe characters: `< > : " / \ | ? *`)
4. Uses result as filename

### Expected Output

#### Folder Conversion (Auto-Generated Filename)
```
============================================================
Markdown to Word Document Converter
============================================================
✓ Using first line as filename: 'PENGANTAR BAB 14_ PENGELOLAAN PERPUSTAKAAN'
Output folder: BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop
Output file: PENGANTAR BAB 14_ PENGELOLAAN PERPUSTAKAAN.docx
✓ Created reference template: .temp_reference.docx

Merging 6 markdown file(s):
  [1/6] 14-LIB-14.1.0-PNGTR-Pengantar.md
  [2/6] 14-LIB-14.1.1-PF-Pengadaan.md
  [3/6] 14-LIB-14.2.0-PNGTR-Pengelolaan.md
  [4/6] 14-LIB-14.2.1-PF-Pengelolaan.md
  [5/6] 14-LIB-14.3.0-PNGTR-Sirkulasi.md
  [6/6] 14-LIB-14.3.1-PF-Sirkulasi.md

Converting to .docx...
✓ Conversion complete: BUKU-2/.../0B-improved-sop/PENGANTAR BAB 14_ PENGELOLAAN PERPUSTAKAAN.docx
✓ Added page numbers to document
✓ Cleaned up temporary template

============================================================
SUCCESS!
============================================================
Output: BUKU-2/.../0B-improved-sop/PENGANTAR BAB 14_ PENGELOLAAN PERPUSTAKAAN.docx
Size: 33.1 KB

Document Settings Applied:
  • Paper: B5 JIS (18.2 x 25.71 cm)
  • Margins: Mirror (Top: 2.5, Bottom: 2.5, Inside: 2.5, Outside: 2.0 cm)
  • Styles: Heading 1/2/3, Bold, Italic, Lists, Tables
```

## Output Location & Filename

**IMPORTANT**: Output file is always created in the **source folder** (where markdown files are located), not in current directory.

### Auto-Generated Filename
When no filename is provided:
1. Reads **first line** of first markdown file (alphabetically)
2. Removes heading symbols (`#`, `##`, etc.)
3. Sanitizes filename (removes: `< > : " / \ | ? *`)
4. Uses result as filename

**Example**:
- First line: `# PENGANTAR BAB 14: PENGELOLAAN PERPUSTAKAAN`
- Generated: `PENGANTAR BAB 14_ PENGELOLAAN PERPUSTAKAAN.docx`
- Note: Colon (`:`) → underscore (`_`)

### Output Location Rules
- **Folder input**: Output in that folder
- **Comma-separated files**: Output in first file's folder
- **Single file**: Output in same folder

## What Gets Converted

### Input
- **Format**: .md (markdown) files
- **Source**: Multiple files or folder
- **Processing**: Files merged in alphabetical order

### Output
- **Format**: .docx (Word document)
- **Location**: Source folder (not current directory)
- **Filename**: User-provided or auto-generated from first line
- **Content**: All input files merged into single document
- **Formatting**: Proper Word styles applied

### Style Mapping
| Markdown | Word Style |
|----------|------------|
| `# Heading 1` | Heading 1 |
| `## Heading 2` | Heading 2 |
| `### Heading 3` | Heading 3 |
| `**bold**` | Bold |
| `*italic*` | Italic |
| `- item` | Bullet List |
| `1. item` | Numbered List |
| `| table |` | Word Table |

## Important Notes

### Alphabetical Order
- Files are **always** processed in alphabetical order
- Regardless of input order or comma-separated list order
- This ensures consistent output
- Example: `03-chapter.md,01-intro.md,02-overview.md` → processes as 01, 02, 03

### Temporary Files
- Script creates `.temp_reference.docx` during conversion
- Automatically deleted after successful conversion
- No manual cleanup needed

### File Preservation
- Original .md files remain unchanged
- Output .docx created in source directory

## Examples

### Example 1: Convert Test Folder (Auto-Name from First Line)
User: "Convert the markdown files in the perpustakaan folder to Word"
```bash
source .venv/bin/activate
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop"
```
Output: `PENGANTAR BAB 14_ PENGELOLAAN PERPUSTAKAAN.docx` (in `0B-improved-sop/` folder)

### Example 2: Convert with Custom Name
User: "Merge all markdown files in the folder and create perpustakaan.docx"
```bash
source .venv/bin/activate
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop" perpustakaan.docx
```
Output: `perpustakaan.docx`

### Example 3: Convert Specific Files
User: "Combine chapter1.md, chapter2.md, and chapter3.md into final.docx"
```bash
source .venv/bin/activate
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py "chapter1.md,chapter2.md,chapter3.md" final.docx
```
Output: `final.docx` (files merged in alphabetical order)

## Troubleshooting

### "No .md files found in folder"
- Verify folder path is correct
- Check that folder contains .md files
- Ensure files have `.md` extension (not `.txt` or `.markdown`)

### Files not found
- Verify file paths are correct (use forward slashes)
- Check that all specified files exist
- Use absolute paths if relative paths fail

### Conversion errors
- Check markdown syntax is valid
- Verify no corrupted files
- Test with single file to isolate issue
- Check error message for specific file causing problem

### Missing pypandoc
- Verify pypandoc-binary is installed: `pip list | grep pypandoc`
- Reinstall: `pip install pypandoc-binary`
- Check version: `pypandoc.get_pandoc_version()`

### Styles not applied
- Verify reference template was created
- Open output file in Word and check styles
- Manually reapply styles if needed
- Check Word compatibility mode

### Output file issues
- Ensure write permissions in output directory
- Check available disk space
- Verify output path is valid
- Close Word if output file is open

## Advanced Usage

### Custom Output Location
Specify full path for output:
```bash
source .venv/bin/activate
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py "./markdown_folder" "./output/final_document.docx"
```

### Processing in Pipeline
Combine with other scripts:
```bash
# Convert markdown to docx
source .venv/bin/activate
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py "./markdown" document.docx

# Then convert docx to pdf
python python_scripts/10-convert-docx-to-pdf.py document.docx
```

## Related Skills
- **convert-docx-to-pdf**: Convert resulting .docx to PDF format
- **remove-headers-footers**: Remove headers/footers from Word documents

## Dependencies
- Python 3.6+
- pypandoc-binary (Python wrapper for Pandoc)
- python-docx (Word document manipulation)
- Project virtual environment (.venv)

## Performance Notes
- **Speed**: ~1-2 seconds for small files (< 100KB)
- **Large files**: Files > 1MB may take 5-10 seconds
- **Memory**: Uses ~50MB RAM during conversion
- **File limit**: No hard limit, but 100+ files may slow down

## Technical Notes

### Alphabetical Sorting
Files are sorted using Python's `sorted()` function with `key=lambda x: x.name`. This ensures:
- Case-insensitive sorting
- Natural ordering (01, 02, ... 10, 11)
- Consistent results across platforms

### Markdown Merging
Files are joined with double newlines (`\n\n`) to ensure proper separation between documents.

### Template Creation
A temporary reference document is created with:
- B5 JIS paper size
- Mirror margins
- Proper section settings
- This template guides pypandoc's conversion

### Page Numbers
Basic page number implementation using Word XML fields. For advanced formatting (different odd/even, outside alignment), manual adjustment in Word may be needed.
