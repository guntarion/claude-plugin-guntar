# Markdown to Word Document Converter

**Script**: `21-md-to-docx.py`
**Purpose**: Merge multiple markdown files and convert to .docx with specific formatting
**Library**: pypandoc (Python wrapper for Pandoc), python-docx

---

## Features

- **Merge Multiple Files**: Combine multiple .md files in alphabetical order
- **Automatic Sorting**: Always processes files alphabetically regardless of input order
- **Format Retention**: Preserves markdown formatting (headings, bold, italic, lists, tables)
- **Custom Paper Size**: B5 JIS (18.2 x 25.71 cm)
- **Mirror Margins**: Professional book layout
- **Reference Template**: Creates proper .docx template for consistent formatting

---

## Usage

### Activate Virtual Environment

```bash
source .venv/bin/activate
```

### Three Input Modes

#### Mode 1: Multiple Files (Comma-Separated)

```bash
python python_scripts/21-md-to-docx.py file1.md,file2.md,file3.md output.docx
```

Files will be merged in **alphabetical order** regardless of the order you specify.

#### Mode 2: Folder Path

```bash
python python_scripts/21-md-to-docx.py ./folder_path output.docx
```

All `.md` files in the folder will be merged in alphabetical order.

#### Mode 3: Auto-Generated Output Name (from First Line)

```bash
python python_scripts/21-md-to-docx.py ./folder_path
```

Output file will be named using the first line of the first markdown file (sanitized for filesystem safety). For example, if the first line is `# Chapter 1: Introduction`, the output will be `Chapter 1_ Introduction.docx`.

---

## Markdown to Word Style Mapping

| Markdown Syntax | Word Style |
|-----------------|------------|
| `# Heading 1` | Heading 1 style |
| `## Heading 2` | Heading 2 style |
| `### Heading 3` | Heading 3 style |
| `**bold text**` | Bold formatting |
| `*italic text*` | Italic formatting |
| `- List item` | Bullet list |
| `1. Numbered item` | Numbered list |
| `| Table |` | Word table |

---

## Document Specifications

### Paper Size
- **Format**: B5 JIS
- **Dimensions**: 18.2 x 25.71 cm
- **Orientation**: Portrait

### Margins (Mirror Layout)
- **Top**: 2.5 cm
- **Bottom**: 2.5 cm
- **Inside**: 2.5 cm (left on odd pages, right on even pages)
- **Outside**: 2.0 cm (right on odd pages, left on even pages)
- **Gutter**: 0 cm

### Header & Footer
- **Page Numbers**: Bottom outside (automatic)
- **Different Odd & Even**: Enabled
- **Background Images**: Requires manual setup (see notes below)

---

## Examples

### Example 1: Convert Files from Test Folder (Auto-Name)

```bash
source .venv/bin/activate
python python_scripts/21-md-to-docx.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop"
```

Output: File named from first line (e.g., `PENGANTAR BAB 14_ PENGELOLAAN PERPUSTAKAAN.docx`) in the **source folder** (`0B-improved-sop/`)

### Example 2: Specific Files with Custom Output

```bash
source .venv/bin/activate
python python_scripts/21-md-to-docx.py "chapter1.md,chapter2.md,chapter3.md" my_book.docx
```

Output: `my_book.docx` in the **source folder** (same folder as first file)

### Example 3: Single Folder with Custom Name

```bash
source .venv/bin/activate
python python_scripts/21-md-to-docx.py "./markdown_files" final_document.docx
```

Output: `final_document.docx` in the **source folder** (`./markdown_files/`)

---

## Expected Output

### Console Output

```
============================================================
Markdown to Word Document Converter
============================================================
✓ Created reference template: .temp_reference.docx

Merging 6 markdown file(s):
  [1/6] file1.md
  [2/6] file2.md
  [3/6] file3.md
  [4/6] file4.md
  [5/6] file5.md
  [6/6] file6.md

Converting to .docx...
✓ Conversion complete: output.docx
✓ Added page numbers to document
✓ Cleaned up temporary template

============================================================
SUCCESS!
============================================================
Output: /path/to/output.docx
Size: 125.3 KB

Document Settings Applied:
  • Paper: B5 JIS (18.2 x 25.71 cm)
  • Margins: Mirror (Top: 2.5, Bottom: 2.5, Inside: 2.5, Outside: 2.0 cm)
  • Styles: Heading 1/2/3, Bold, Italic, Lists, Tables
```

---

## Background Images (Manual Setup Required)

Due to API limitations, background images must be added manually in Microsoft Word:

### If Background Images Exist

If the script finds these files:
- `./Desain/inner-buku2-ganjil.jpg` (odd pages)
- `./Desain/inner-buku2-genap.jpg` (even pages)

It will display instructions for manual setup.

### Manual Setup Steps

1. Open the generated `.docx` file in Microsoft Word
2. Go to **Design** > **Page Color** > **Fill Effects**
3. Select **Picture** tab
4. Choose the background image:
   - For odd pages: `inner-buku2-ganjil.jpg`
   - For even pages: `inner-buku2-genap.jpg`
5. For different odd/even backgrounds:
   - Insert section breaks between pages
   - Apply different backgrounds to different sections

---

## File Processing Order

**IMPORTANT**: Files are **always** processed in alphabetical order.

### Example

If you provide:
```bash
python 21-md-to-docx.py "03-chapter.md,01-intro.md,02-overview.md"
```

Processing order will be:
1. `01-intro.md`
2. `02-overview.md`
3. `03-chapter.md`

This ensures consistent output regardless of input order.

---

## Output Location

**IMPORTANT**: The output `.docx` file is always created in the **source folder** (where the markdown files are located), not in the current directory.

- For folder input: Output goes in that folder
- For comma-separated files: Output goes in the first file's folder
- For single file: Output goes in the same folder as that file

### Auto-Generated Filename

When no filename is provided, the script:
1. Reads the **first line** of the **first markdown file** (alphabetically)
2. Removes markdown heading symbols (`#`, `##`, etc.)
3. Sanitizes the text (removes unsafe characters: `< > : " / \ | ? *`)
4. Uses the result as the filename

**Example**:
- First line: `# PENGANTAR BAB 14: PENGELOLAAN PERPUSTAKAAN`
- Generated filename: `PENGANTAR BAB 14_ PENGELOLAAN PERPUSTAKAAN.docx`
- Note: Colon (`:`) replaced with underscore (`_`)

## What Gets Created

### Input Files
- Multiple `.md` markdown files
- Can be from different locations or same folder

### Output File
- Single `.docx` Word document
- Located in the **source folder** (not current directory)
- Filename from user or auto-generated from first line
- Contains merged content from all input files
- Formatted with proper styles and layout

### Temporary Files
- `.temp_reference.docx` (automatically deleted after conversion)

---

## Troubleshooting

### "No .md files found"
- Verify the folder contains `.md` files
- Check folder path is correct
- Ensure files have `.md` extension (not `.txt` or `.markdown`)

### "File not found"
- Check file paths are correct
- Use forward slashes: `./folder/file.md`
- Ensure files exist before running

### Missing pypandoc
- The script requires `pypandoc-binary` package
- Install: `pip install pypandoc-binary` (already in requirements.txt)

### Conversion errors
- Verify markdown syntax is valid
- Check for unusual characters or malformed tables
- Try converting files individually to isolate issues

### Output file not created
- Check write permissions in output directory
- Ensure sufficient disk space
- Verify pypandoc is working: `pypandoc.get_pandoc_version()`

### Styles not applied correctly
- Verify reference template was created
- Check Word version compatibility
- Open in Word and reapply styles if needed

---

## Technical Details

### Dependencies
- **pypandoc-binary**: Markdown to Word conversion
- **python-docx**: Document formatting and template creation
- **pathlib**: File path handling (built-in)

### Conversion Process

1. **Input Parsing**: Identify .md files from input (files or folder)
2. **Sorting**: Sort files alphabetically by filename
3. **Template Creation**: Generate reference .docx with proper formatting
4. **Merging**: Combine all markdown content with double newlines
5. **Conversion**: Use pypandoc to convert markdown to .docx
6. **Post-Processing**: Add page numbers (simplified implementation)
7. **Cleanup**: Remove temporary template file

### Limitations

1. **Background Images**: Cannot be automated via python-docx API, requires manual setup
2. **Page Numbers**: Basic implementation, may need refinement in Word
3. **Different Odd/Even Backgrounds**: Requires manual section breaks and formatting
4. **Complex Tables**: Very complex tables may need manual adjustment

---

## Performance

- **Speed**: ~1-2 seconds for small files (< 100KB total)
- **Large Files**: May take longer for files > 1MB
- **Memory**: Uses ~50MB RAM during conversion
- **File Limit**: No hard limit, but 100+ files may be slow

---

## Related Scripts

- **10-convert-docx-to-pdf.py**: Convert resulting .docx to PDF
- **09-remove-headers-footers.py**: Remove headers/footers if needed

---

**Created**: 2025-11-20
**Author**: Claude Code
**Version**: 1.0
