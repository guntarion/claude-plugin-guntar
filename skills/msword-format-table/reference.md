# Format Tables - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Features](#features)
3. [Operations](#operations)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Handling Merged Cells](#handling-merged-cells)
7. [Examples](#examples)
8. [What Gets Modified](#what-gets-modified)
9. [What Gets Preserved](#what-gets-preserved)
10. [Use Cases](#use-cases)
11. [VBA Equivalent](#vba-equivalent)
12. [Troubleshooting](#troubleshooting)
13. [Tips](#tips)
14. [Performance Notes](#performance-notes)

## When to Use This Skill

Activate this skill when the user requests to:
- Format tables in Word documents
- Standardize table formatting across documents
- Center align table headers
- Remove bold from first column body
- Left align table body content
- Apply consistent table styles

## Features

- **Center align headers:** Horizontal and vertical centering for header row
- **Unbold first column:** Removes bold from first column (excluding headers)
- **Left align body:** Sets all body content to left alignment
- **Merged cell safe:** Handles tables with merged cells
- **Batch processing:** Formats all tables in document at once
- **Preserves content:** Only modifies formatting, not content
- **Table styles:** Optional table style application

## Operations

### 1. Center Align Headers

**Target:** First row of each table (header row)
- **Horizontal:** Center aligned
- **Vertical:** Center aligned
- **Bold:** Applied to header text

**Example:**
```
Before:                     After:
┌────────────────────┐     ┌────────────────────┐
│ Name (left)        │     │      Name          │
│ (top aligned)      │  →  │   (centered)       │
└────────────────────┘     └────────────────────┘
```

### 2. Unbold First Column Body

**Target:** First column, excluding header row
- **Operation:** Removes bold formatting
- **Preserves:** Bold in other columns and header

**Example:**
```
Before:                     After:
┌──────────┬────────┐      ┌──────────┬────────┐
│ **Name** │ Age    │  →   │ **Name** │ Age    │  (header stays bold)
├──────────┼────────┤      ├──────────┼────────┤
│ **John** │ 25     │      │ John     │ 25     │  (body unbold)
│ **Jane** │ 30     │      │ Jane     │ 30     │  (body unbold)
└──────────┴────────┘      └──────────┴────────┘
```

### 3. Left Align Body

**Target:** All cells except header row
- **Operation:** Sets left alignment
- **Preserves:** Header alignment (stays centered from operation #1)

**Example:**
```
Before:                     After:
┌────────────────────┐     ┌────────────────────┐
│      Header        │  →  │      Header        │  (stays centered)
├────────────────────┤     ├────────────────────┤
│   Centered text    │     │ Left aligned text  │
│     More text      │     │ More text          │
└────────────────────┘     └────────────────────┘
```

## Usage

### Basic Usage (Auto-generated output filename)

```bash
source .venv/bin/activate
python .claude/skills/msword-format-table/msword-format-table.py <input.docx>
```

This creates: `input-formatted.docx`

**Example:**
```bash
python .claude/skills/msword-format-table/msword-format-table.py ./GGGI/file-percobaan.docx
# Creates: ./GGGI/file-percobaan-formatted.docx
```

### Custom Output Filename

```bash
source .venv/bin/activate
python .claude/skills/msword-format-table/msword-format-table.py <input.docx> <output.docx>
```

**Example:**
```bash
python .claude/skills/msword-format-table/msword-format-table.py input.docx formatted.docx
```

### With Table Style

```bash
source .venv/bin/activate
python .claude/skills/msword-format-table/msword-format-table.py <input.docx> <output.docx> --style "Table Grid"
```

**Common Table Styles:**
- `"Table Grid"`
- `"Light Shading"`
- `"Light List"`
- `"Medium Shading 1"`

## How It Works

1. **Load Document:**
   - Opens the input .docx file
   - Finds all tables in document

2. **Process Each Table:**
   - **Step 1:** Center align header row (row 0)
     - Horizontal: `WD_ALIGN_PARAGRAPH.CENTER`
     - Vertical: `WD_CELL_VERTICAL_ALIGNMENT.CENTER`
     - Bold all header text

   - **Step 2:** Unbold first column body
     - Iterates rows 1+ (skip header)
     - Sets `run.bold = False` for first column cells

   - **Step 3:** Left align body
     - Iterates rows 1+ (skip header)
     - Sets `WD_ALIGN_PARAGRAPH.LEFT` for all cells

   - **Step 4:** Set repeat header rows (optional)
   - **Step 5:** Apply table style (if specified)

3. **Save Output:**
   - Creates new file with `-formatted` suffix
   - Reports statistics

## Handling Merged Cells

The script handles merged cells properly:

### Horizontal Merge (Header)

```
┌─────────────────────────┐
│    Merged Header Cell    │  ← Centered
├──────────┬──────────────┤
│ Data 1   │ Data 2       │
└──────────┴──────────────┘
```

### Vertical Merge (First Column)

```
┌──────────┬────────┐
│ Header   │ Value  │
├──────────┼────────┤
│ **Row1** │ 100    │  ← Bold removed from merged cell
│          │ 200    │
└──────────┴────────┘
```

## Examples

### Example 1: Basic Formatting

User: "Format all tables in this document"

```bash
source .venv/bin/activate
python .claude/skills/msword-format-table/msword-format-table.py document.docx
```

### Example 2: Custom Output

User: "Format tables and save as formatted-doc.docx"

```bash
source .venv/bin/activate
python .claude/skills/msword-format-table/msword-format-table.py input.docx formatted-doc.docx
```

### Example 3: With Table Style

User: "Format tables and apply Table Grid style"

```bash
source .venv/bin/activate
python .claude/skills/msword-format-table/msword-format-table.py input.docx output.docx --style "Table Grid"
```

### Example 4: Batch Processing

```bash
for file in ./documents/*.docx; do
    python .claude/skills/msword-format-table/msword-format-table.py "$file"
done
```

### Example Output

```
Input:  GGGI/file-percobaan.docx
Output: GGGI/file-percobaan-formatted.docx

Loading document...
Formatting tables...

============================================================
✓ Processing complete!
  Tables found: 3
  Headers centered: 15 cells
  First column unbolded: 12 cells
  Body cells left-aligned: 36 cells
  Output saved: GGGI/file-percobaan-formatted.docx
============================================================
```

## What Gets Modified

### Headers (row 0)
- ✓ Horizontal alignment → Center
- ✓ Vertical alignment → Center
- ✓ Bold → Applied

### First Column Body (column 0, rows 1+)
- ✓ Bold → Removed

### All Body Cells (rows 1+)
- ✓ Horizontal alignment → Left

## What Gets Preserved

- **Content:** All text remains unchanged
- **Other formatting:** Fonts, sizes, colors preserved
- **Bold in other columns:** Only first column affected
- **Header bold:** Headers keep bold formatting
- **Table structure:** Borders, shading, merges intact
- **Cell width/height:** Dimensions unchanged

## Use Cases

### Standardize Table Formatting

```bash
python .claude/skills/msword-format-table/msword-format-table.py report.docx
```

### Format Multiple Documents

```bash
for file in ./documents/*.docx; do
    python .claude/skills/msword-format-table/msword-format-table.py "$file"
done
```

### Before/After Comparison

```bash
# Original: report.docx
# Formatted: report-formatted.docx
# Compare side-by-side in Word
```

### Apply Corporate Style Guidelines

Use this script to ensure all tables follow corporate formatting standards before distribution.

## VBA Equivalent

This Python script replicates the functionality of these VBA macros:

| VBA Macro | Python Function | Purpose |
|-----------|----------------|---------|
| `CenterHeaderAllTables` | `center_align_headers()` | Centers header row |
| `UnboldFirstColumnBody` | `unbold_first_column_body()` | Removes bold from first column |
| (New) | `left_align_body()` | Left aligns body content |
| (New) | Apply table style | Applies consistent table style |

### Comparison: Python vs VBA

| Feature | VBA | Python |
|---------|-----|--------|
| Center headers | ✓ | ✓ |
| Unbold first column | ✓ | ✓ |
| Left align body | Manual | ✓ (included) |
| Merged cell handling | ✓ | ✓ |
| Cross-platform | Windows only | Mac/Windows/Linux |
| Batch processing | Manual loop | Built-in |
| Version control | Difficult | Easy (git) |

## Common Table Formats

### Before Formatting
- Headers: Various alignments
- First column: Often bold (from template)
- Body: Mixed alignments

### After Formatting
- Headers: Consistently centered and bold
- First column: Normal weight (not bold)
- Body: Consistently left-aligned

## Troubleshooting

### File Not Found Error

```
Error: File not found: document.docx
```

**Solution:** Verify the input file path is correct

### Wrong File Format

```
Error: File must be a .docx file: document.pdf
```

**Solution:** Ensure input file has .docx extension

### No Tables Found

If the script reports "Tables found: 0":
- Verify document contains tables
- Check if content is in text boxes (not accessible)
- Ensure tables are not embedded in other objects

### Table Style Not Applied

If specified table style doesn't apply:
- Verify style name is correct (case-sensitive)
- Check if style exists in document template
- Try with a different style name

## Tips

1. **Preview first:** Check output file before replacing original
2. **Backup originals:** Always keep copy of source files
3. **Test on sample:** Try on small document first
4. **Batch carefully:** Verify results on first file before batch processing
5. **Custom styles:** Use `--style` parameter for consistent appearance

## Related Skills

- **msword-italicize-english-terms**: Format English terms in documents
- **msword-move-citation-before-period**: Fix citation placement
- **msword-remove-headers-footers**: Remove headers/footers from documents

## Dependencies

- **python-docx**: For manipulating .docx files
- **pathlib**: Built-in Python module for file paths (included)
- Project virtual environment (.venv)

## Performance Notes

- **Fast:** Processes tables efficiently
- **Example:** 100 tables in 10-page document: ~2-3 seconds
- **Memory:** Minimal memory usage
- **Typical:** Most documents (5-20 tables): < 1 second

## Limitations

### Does Not Modify

- **Text content:** No text changes
- **Table structure:** No row/column additions or deletions
- **Complex formatting:** Advanced table styles may need manual adjustment
- **Embedded tables:** Tables in text boxes not accessible
- **Headers/footers:** Tables in headers/footers not processed
