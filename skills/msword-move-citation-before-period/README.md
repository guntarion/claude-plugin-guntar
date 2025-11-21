# 24-move-citations-before-period.py

## Purpose
Moves citation numbers from after periods to before periods (with space) in Microsoft Word documents. This fixes citation formatting to comply with academic standards where citations should appear before punctuation.

## Transformation

**Before:**
```
Modul HJT menunjukkan koefisien suhu terbaik tersedia secara komersial, menjadikannya sumber energi Indonesia.[14]
```

**After:**
```
Modul HJT menunjukkan koefisien suhu terbaik tersedia secara komersial, menjadikannya sumber energi Indonesia [14].
```

## Features
- **Regex-based replacement:** Uses regular expressions for accurate pattern matching
- **Preserves formatting:** Maintains fonts, styles, bold, italic, etc.
- **Handles all locations:** Processes paragraphs and table cells
- **Flexible numbering:** Supports 1-3 digit citation numbers [1] to [999]
- **Auto-naming:** Generates output filename if not specified
- **Safe processing:** Creates new file, doesn't modify original

## Pattern Details

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

## Dependencies
- **python-docx**: For manipulating .docx files
- **re**: Built-in Python regex module
- **pathlib**: Built-in Python module for file paths

## Usage

### Basic Usage (Auto-generated output filename)
```bash
source .venv/bin/activate
python python_scripts/24-move-citations-before-period.py <input.docx>
```

This creates: `input-fixed.docx`

**Example:**
```bash
python python_scripts/24-move-citations-before-period.py ./GGGI/file-percobaan.docx
# Creates: ./GGGI/file-percobaan-fixed.docx
```

### Custom Output Filename
```bash
source .venv/bin/activate
python python_scripts/24-move-citations-before-period.py <input.docx> <output.docx>
```

**Example:**
```bash
python python_scripts/24-move-citations-before-period.py ./GGGI/file-percobaan.docx ./GGGI/corrected.docx
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
     - Replaces with `[citation].`

3. **Save Output:**
   - Saves to new file
   - Reports number of modifications made

## Example Output

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

**Only the specific pattern** `.[citation]` is changed to `[citation].`

Nothing else in the document is altered.

## Use Cases

**Academic papers:**
```bash
python python_scripts/24-move-citations-before-period.py thesis.docx thesis-corrected.docx
```

**Research reports:**
```bash
python python_scripts/24-move-citations-before-period.py report.docx
```

**Multiple documents (using loop):**
```bash
for file in ./documents/*.docx; do
    python python_scripts/24-move-citations-before-period.py "$file"
done
```

## Edge Cases Handled

**Mid-sentence citations:**
```
Before: "energy.[45] Studi terbaru"
After:  "energy [45]. Studi terbaru"
```

**End of paragraph citations:**
```
Before: "di iklim lembap Indonesia.[52]"
After:  "di iklim lembap Indonesia [52]."
```

**Multiple citations in one paragraph:**
```
Before: "text.[1] More text.[2] Final.[3]"
After:  "text [1]. More text [2]. Final [3]."
```

**Citations in tables:**
Works the same way in table cells as in regular paragraphs.

## Limitations

**Does not handle:**
- Multiple citations in brackets: `.[1,2,3]` (not a standard format)
- Citations with letters: `.[1a]` (would need pattern modification)
- Citations with spaces: `. [1]` (pattern expects no space)
- Citations in headers/footers (python-docx limitation)

**Workaround for headers/footers:**
If you have citations in headers/footers, you'll need to fix those manually in Word.

## Error Handling

The script validates:
- Input file exists
- Input file is .docx format
- Output path is writable

Error messages guide you to fix issues:

```
Error: File not found: nonexistent.docx

Error: File must be a .docx file: document.pdf
```

## Tips

1. **Preview changes:** Check the `-fixed.docx` file before replacing the original
2. **Backup first:** Always keep a copy of your original document
3. **Test on sample:** Try on a small test file first
4. **Batch processing:** Use shell loops to process multiple files

## Related Scripts

- **23-combine-docx.py**: Combine multiple .docx files
- **09-remove-headers-footers.py**: Remove headers/footers
- **21-md-to-docx.py**: Convert markdown to Word format

## Performance

- **Fast:** Processes documents in seconds
- **Memory efficient:** Handles large documents without issues
- **Example:** 100-page document with 200 citations: ~2-3 seconds
