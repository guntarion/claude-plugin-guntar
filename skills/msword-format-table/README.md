# 26-format-tables.py

## Purpose
Applies consistent formatting to all tables in Word documents. Performs three operations: center-aligns headers, removes bold from first column body, and left-aligns all body content.

## Features
- **Center align headers:** Horizontal and vertical centering for header row
- **Unbold first column:** Removes bold from first column (excluding headers)
- **Left align body:** Sets all body content to left alignment
- **Merged cell safe:** Handles tables with merged cells
- **Batch processing:** Formats all tables in document at once
- **Preserves content:** Only modifies formatting, not content

## Operations

### 1. Center Align Headers
- **Target:** First row of each table (header row)
- **Horizontal:** Center aligned
- **Vertical:** Center aligned
- **Example:**

```
Before:                     After:
┌────────────────────┐     ┌────────────────────┐
│ Name (left)        │     │      Name          │
│ (top aligned)      │  →  │   (centered)       │
└────────────────────┘     └────────────────────┘
```

### 2. Unbold First Column Body
- **Target:** First column, excluding header row
- **Operation:** Removes bold formatting
- **Preserves:** Bold in other columns and header
- **Example:**

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
- **Target:** All cells except header row
- **Operation:** Sets left alignment
- **Preserves:** Header alignment (stays centered from operation #1)
- **Example:**

```
Before:                     After:
┌────────────────────┐     ┌────────────────────┐
│      Header        │  →  │      Header        │  (stays centered)
├────────────────────┤     ├────────────────────┤
│   Centered text    │     │ Left aligned text  │
│     More text      │     │ More text          │
└────────────────────┘     └────────────────────┘
```

## Dependencies
- **python-docx**: For manipulating .docx files
- **pathlib**: Built-in Python module for file paths

## Usage

### Basic Usage (Auto-generated output filename)
```bash
source .venv/bin/activate
python python_scripts/26-format-tables.py <input.docx>
```

This creates: `input-formatted.docx`

**Example:**
```bash
python python_scripts/26-format-tables.py ./GGGI/file-percobaan.docx
# Creates: ./GGGI/file-percobaan-formatted.docx
```

### Custom Output Filename
```bash
source .venv/bin/activate
python python_scripts/26-format-tables.py <input.docx> <output.docx>
```

**Example:**
```bash
python python_scripts/26-format-tables.py input.docx formatted.docx
```

## How It Works

1. **Load Document:**
   - Opens the input .docx file
   - Finds all tables in document

2. **Process Each Table:**
   - **Step 1:** Center align header row (row 0)
     - Horizontal: `WD_ALIGN_PARAGRAPH.CENTER`
     - Vertical: `WD_CELL_VERTICAL_ALIGNMENT.CENTER`

   - **Step 2:** Unbold first column body
     - Iterates rows 1+ (skip header)
     - Sets `run.bold = False` for first column cells

   - **Step 3:** Left align body
     - Iterates rows 1+ (skip header)
     - Sets `WD_ALIGN_PARAGRAPH.LEFT` for all cells

3. **Save Output:**
   - Creates new file with `-formatted` suffix
   - Reports statistics

## Example Output

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

## Handling Merged Cells

The script handles merged cells properly:

**Horizontal merge (header):**
```
┌─────────────────────────┐
│    Merged Header Cell    │  ← Centered
├──────────┬──────────────┤
│ Data 1   │ Data 2       │
└──────────┴──────────────┘
```

**Vertical merge (first column):**
```
┌──────────┬────────┐
│ Header   │ Value  │
├──────────┼────────┤
│ **Row1** │ 100    │  ← Bold removed from merged cell
│          │ 200    │
└──────────┴────────┘
```

## VBA Equivalent

This Python script replicates the functionality of these VBA macros:

**VBA: CenterHeaderAllTables** → **Python: center_align_headers()**
- Centers header row horizontally and vertically

**VBA: UnboldFirstColumnBody** → **Python: unbold_first_column_body()**
- Removes bold from first column body

**VBA: (New)** → **Python: left_align_body()**
- Left aligns all body content

## Use Cases

**Standardize table formatting:**
```bash
python python_scripts/26-format-tables.py report.docx
```

**Format multiple documents:**
```bash
for file in ./documents/*.docx; do
    python python_scripts/26-format-tables.py "$file"
done
```

**Before/after comparison:**
```bash
# Original: report.docx
# Formatted: report-formatted.docx
# Compare side-by-side in Word
```

## What Gets Modified

**Headers (row 0):**
- ✓ Horizontal alignment → Center
- ✓ Vertical alignment → Center

**First column body (column 0, rows 1+):**
- ✓ Bold → Removed

**All body cells (rows 1+):**
- ✓ Horizontal alignment → Left

## What Gets Preserved

- **Content:** All text remains unchanged
- **Other formatting:** Fonts, sizes, colors preserved
- **Bold in other columns:** Only first column affected
- **Header bold:** Headers keep bold formatting
- **Table structure:** Borders, shading, merges intact
- **Cell width/height:** Dimensions unchanged

## Comparison: Python vs VBA

| Feature | VBA | Python |
|---------|-----|--------|
| Center headers | ✓ | ✓ |
| Unbold first column | ✓ | ✓ |
| Left align body | Manual | ✓ (included) |
| Merged cell handling | ✓ | ✓ |
| Cross-platform | Windows only | Mac/Windows/Linux |
| Batch processing | Manual loop | Built-in |
| Version control | Difficult | Easy (git) |

## Tips

1. **Preview first:** Check output file before replacing original
2. **Backup originals:** Always keep copy of source files
3. **Test on sample:** Try on small document first
4. **Batch carefully:** Verify results on first file before batch processing

## Common Table Formats

**Before formatting:**
- Headers: Various alignments
- First column: Often bold (from template)
- Body: Mixed alignments

**After formatting:**
- Headers: Consistently centered
- First column: Normal weight (not bold)
- Body: Consistently left-aligned

## Error Handling

The script validates:
- Input file exists
- Input file is .docx format
- Tables are accessible

Error messages guide you to fix issues:

```
Error: File not found: document.docx

Error: File must be a .docx file: document.pdf
```

## Performance

- **Fast:** Processes tables efficiently
- **Example:** 100 tables in 10-page document: ~2-3 seconds
- **Memory:** Minimal memory usage

## Limitations

**Does not modify:**
- **Text content:** No text changes
- **Table structure:** No row/column additions or deletions
- **Complex formatting:** Advanced table styles may need manual adjustment
- **Embedded tables:** Tables in text boxes not accessible

## Related Scripts

- **25-italicize-english-terms.py**: Format English terms
- **24-move-citations-before-period.py**: Fix citations
- **23-combine-docx.py**: Combine multiple files

## When to Use

Use this script when you need to:
- Standardize table formatting across documents
- Fix inconsistent header alignment
- Remove unnecessary bold from first column
- Ensure consistent body text alignment
- Prepare documents for professional presentation
- Apply corporate style guidelines to tables
