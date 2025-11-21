# Move Citations Before Period - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Transformation Details](#transformation-details)
3. [Features](#features)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [What Gets Preserved](#what-gets-preserved)
7. [Use Cases](#use-cases)
8. [Edge Cases Handled](#edge-cases-handled)
9. [Limitations](#limitations)
10. [Troubleshooting](#troubleshooting)
11. [Helper Scripts](#helper-scripts)
12. [Performance Notes](#performance-notes)

## When to Use This Skill

Activate this skill when the user requests to:
- Move citations before periods in Word documents
- Fix citation placement to comply with academic standards
- Transform `text.[123]` to `text [123].`
- Correct citation formatting in research papers or reports

## Transformation Details

### Before and After

**Before:**
```
Modul HJT menunjukkan koefisien suhu terbaik tersedia secara komersial, menjadikannya sumber energi Indonesia.[14]
```

**After:**
```
Modul HJT menunjukkan koefisien suhu terbaik tersedia secara komersial, menjadikannya sumber energi Indonesia [14].
```

### Pattern Details

**Regex Pattern:** `\.(\[\d{1,3}\])`
**Replacement:** ` \1.` (space + citation + period)

This matches:
- A literal period `.`
- Followed by a bracketed number `[123]` (1-3 digits)

And replaces with:
- Space + citation + period

**Examples of transformations:**
- `text.[1]` → `text [1].`
- `word.[14]` → `word [14].`
- `sentence.[123]` → `sentence [123].`
- `paragraph.[999]` → `paragraph [999].`

## Features

- **Regex-based replacement:** Uses regular expressions for accurate pattern matching
- **Preserves formatting:** Maintains fonts, styles, bold, italic, etc.
- **Handles all locations:** Processes paragraphs and table cells
- **Flexible numbering:** Supports 1-3 digit citation numbers [1] to [999]
- **Auto-naming:** Generates output filename if not specified
- **Safe processing:** Creates new file, doesn't modify original

## Usage

### Basic Usage (Auto-generated output filename)

```bash
source .venv/bin/activate
python .claude/skills/msword-move-citation-before-period/msword-move-citation-before-period.py <input.docx>
```

This creates: `input-fixed.docx`

**Example:**
```bash
python .claude/skills/msword-move-citation-before-period/msword-move-citation-before-period.py ./GGGI/file-percobaan.docx
# Creates: ./GGGI/file-percobaan-fixed.docx
```

### Custom Output Filename

```bash
source .venv/bin/activate
python .claude/skills/msword-move-citation-before-period/msword-move-citation-before-period.py <input.docx> <output.docx>
```

**Example:**
```bash
python .claude/skills/msword-move-citation-before-period/msword-move-citation-before-period.py ./GGGI/file-percobaan.docx ./GGGI/corrected.docx
```

## How It Works

1. **Load Document:**
   - Opens the input .docx file
   - Counts paragraphs and tables

2. **Process Content:**
   - Iterates through all paragraphs
   - Iterates through all table cells
   - For each text run (to preserve formatting):
     - Searches for pattern `.[citation]`
     - Replaces with ` [citation].`

3. **Save Output:**
   - Saves to new file
   - Reports number of modifications made

### Example Output

```
Input:  ./GGGI/file-percobaan.docx
Output: ./GGGI/file-percobaan-fixed.docx

Loading document...
Found 45 paragraphs and 2 tables

Processing citations...

============================================================
✓ Processing complete!
  Modified elements: 12
  Output saved: ./GGGI/file-percobaan-fixed.docx
============================================================
```

## What Gets Preserved

- **Text formatting:** Bold, italic, underline, fonts, sizes, colors
- **Document structure:** All paragraphs, tables, headings remain intact
- **Styles:** All paragraph and character styles maintained
- **Page layout:** Margins, page size, orientation unchanged

## What Gets Modified

**Only the specific pattern** `.[citation]` is changed to ` [citation].`

Nothing else in the document is altered.

## Use Cases

### Academic Papers

```bash
python .claude/skills/msword-move-citation-before-period/msword-move-citation-before-period.py thesis.docx thesis-corrected.docx
```

### Research Reports

```bash
python .claude/skills/msword-move-citation-before-period/msword-move-citation-before-period.py report.docx
```

### Multiple Documents (Using Loop)

```bash
for file in ./documents/*.docx; do
    python .claude/skills/msword-move-citation-before-period/msword-move-citation-before-period.py "$file"
done
```

## Edge Cases Handled

### Mid-sentence Citations

```
Before: "energy.[45] Studi terbaru"
After:  "energy [45]. Studi terbaru"
```

### End of Paragraph Citations

```
Before: "di iklim lembap Indonesia.[52]"
After:  "di iklim lembap Indonesia [52]."
```

### Multiple Citations in One Paragraph

```
Before: "text.[1] More text.[2] Final.[3]"
After:  "text [1]. More text [2]. Final [3]."
```

### Citations in Tables

Works the same way in table cells as in regular paragraphs.

## Limitations

### Does Not Handle

- **Multiple citations in brackets:** `.[1,2,3]` (not a standard format)
- **Citations with letters:** `.[1a]` (would need pattern modification)
- **Citations with spaces:** `. [1]` (pattern expects no space)
- **Citations in headers/footers:** (python-docx limitation)

### Workaround for Headers/Footers

If you have citations in headers/footers, you'll need to fix those manually in Word.

## Troubleshooting

### File Not Found Error

```
Error: File not found: nonexistent.docx
```

**Solution:** Verify the input file path is correct

### Wrong File Format

```
Error: File must be a .docx file: document.pdf
```

**Solution:** Ensure input file has .docx extension

### Output Path Not Writable

**Solution:** Check folder permissions and ensure you have write access

### No Changes Made

If the script reports "Modified elements: 0", this means:
- No citations found in the format `.[citation]`
- Citations may already be correctly formatted
- Citations may use a different format

## Helper Scripts

The skill includes helper scripts in the `scripts/` folder:

### debug-citations.py

Debug script to help identify citation patterns in your document.

### find-all-citations.py

Utility to find and list all citations in a document.

**Usage:**
```bash
python .claude/skills/msword-move-citation-before-period/scripts/find-all-citations.py document.docx
```

## Tips

1. **Preview changes:** Check the `-fixed.docx` file before replacing the original
2. **Backup first:** Always keep a copy of your original document
3. **Test on sample:** Try on a small test file first
4. **Batch processing:** Use shell loops to process multiple files

## Related Skills

- **convert-md-to-docx**: Convert markdown to Word format
- **remove-headers-footers**: Remove headers/footers from Word documents
- **chapter-modify-numbering**: Modify chapter numbering in documents

## Dependencies

- **python-docx**: For manipulating .docx files
- **re**: Built-in Python regex module (included)
- **pathlib**: Built-in Python module for file paths (included)
- Project virtual environment (.venv)

## Performance Notes

- **Fast:** Processes documents in seconds
- **Memory efficient:** Handles large documents without issues
- **Example:** 100-page document with 200 citations: ~2-3 seconds
- **Typical:** Most academic papers (20-50 pages): < 1 second
