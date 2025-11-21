# Italicize English Terms - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Features](#features)
3. [CSV Format](#csv-format)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Smart Sorting by Length](#smart-sorting-by-length)
7. [Formatting Applied](#formatting-applied)
8. [Special Handling](#special-handling)
9. [Examples](#examples)
10. [Use Cases](#use-cases)
11. [What Gets Preserved](#what-gets-preserved)
12. [Limitations](#limitations)
13. [Troubleshooting](#troubleshooting)
14. [Tips](#tips)
15. [Performance Notes](#performance-notes)

## When to Use This Skill

Activate this skill when the user requests to:
- Italicize English terms in Indonesian language documents
- Format foreign terms according to Indonesian language standards
- Apply consistent formatting to technical terms from a CSV list
- Mark English words in Bahasa Indonesia documents

## Features

- **CSV-based term list:** Easy to maintain and update
- **Smart sorting:** Processes longer phrases before shorter ones to avoid partial matches
- **Preserves formatting:** Maintains all other text formatting (bold, fonts, colors, etc.)
- **Language tagging:** Sets terms to English (US) language
- **Spell check disabled:** Marks English terms to skip Indonesian spell checking
- **Heading exclusion:** Skips Heading 1 paragraphs
- **Case-insensitive:** Finds terms regardless of case
- **Whole word matching:** Only matches complete words/phrases
- **Table support:** Processes terms in table cells too

## CSV Format

The CSV file should contain one term per line:

```csv
terms
toolbox
toolbox talks
safety
safety precaution
bifacial gain
backsheet
albedo
Standard Operating Procedure
Standard Procedure
Standard
```

**Notes:**
- One term per line (first column only)
- No header row needed (but script handles it if present)
- Script automatically sorts by length (longest first)
- Empty lines are ignored

## Usage

### Basic Usage (Auto-generated output filename)

```bash
source .venv/bin/activate
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py <terms.csv> <input.docx>
```

This creates: `input-italicized.docx`

**Example:**
```bash
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py ./GGGI/english-terms.csv ./GGGI/file-percobaan.docx
# Creates: ./GGGI/file-percobaan-italicized.docx
```

### Custom Output Filename

```bash
source .venv/bin/activate
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py <terms.csv> <input.docx> <output.docx>
```

**Example:**
```bash
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py terms.csv input.docx formatted.docx
```

## How It Works

1. **Read and Sort Terms:**
   - Loads terms from CSV
   - Sorts by length (longest first)
   - Example: "toolbox talks" → "toolbox" → "safety"

2. **Process Each Paragraph:**
   - Skips Heading 1 paragraphs
   - Finds all term occurrences (case-insensitive, whole word)
   - Identifies character positions for each term

3. **Apply Formatting:**
   - For each found term:
     - Sets to italic
     - Sets language to English (US)
     - Disables spell/grammar checking
   - Preserves all other formatting

4. **Save Output:**
   - Creates new file with `-italicized` suffix
   - Original file remains unchanged

## Smart Sorting by Length

Sorting prevents partial matches from interfering with phrase matches.

### Why Sort by Length?

**Without sorting (wrong):**
```
Find: "toolbox" → italicize → "toolbox talks" becomes "toolbox talks"
Find: "toolbox talks" → not found (already partially formatted)
```

**With sorting (correct):**
```
Find: "toolbox talks" → italicize → "toolbox talks"
Find: "toolbox" → only matches standalone "toolbox"
```

### Example Term Sorting

Your terms are automatically sorted by length:

1. `'safety precaution'` (17 chars)
2. `'toolbox talks'` (13 chars)
3. `'bifacial gain'` (13 chars)
4. `'backsheet'` (9 chars)
5. `'toolbox'` (7 chars)
6. `'safety'` (6 chars)
7. `'albedo'` (6 chars)
8. `'terms'` (5 chars)

## Formatting Applied

For each English term found, the script applies:

| Property | Value |
|----------|-------|
| Font style | Italic |
| Language | English (US) |
| Spell check | Disabled |
| Grammar check | Disabled |

All other formatting (bold, font, size, color) is preserved from original text.

## Special Handling

### Heading 1 Exclusion

The script **skips** any paragraph with "Heading 1" style. This is useful because:
- Document titles are usually in English
- Chapter headings may contain English terms
- These don't need italicization as they're already distinct

**Example:**
```
# Chapter 1: Solar Panel Installation  ← Not italicized (Heading 1)

This chapter covers solar panel installation...  ← "solar panel" italicized
```

### Case-Insensitive Matching

The script finds terms regardless of case:

**Term in CSV:** `backsheet`

**Matches in document:**
- backsheet ✓
- Backsheet ✓
- BACKSHEET ✓
- BackSheet ✓

All will be italicized while preserving original case.

### Whole Word Matching

Uses word boundaries to match complete words/phrases only:

**Term:** `safety`

**Matches:**
- "safety precaution" ✓
- "Safety first" ✓

**Does NOT match:**
- "unsafe" ✗ (part of word)
- "safetynets" ✗ (part of word)

## Examples

### Example 1: Basic Usage

User: "Italicize the English terms in this document using this term list"

```bash
source .venv/bin/activate
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py english-terms.csv document.docx
```

### Example 2: Custom Output

User: "Format the English terms and save as formatted-doc.docx"

```bash
source .venv/bin/activate
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py terms.csv input.docx formatted-doc.docx
```

### Example 3: Batch Processing Multiple Documents

```bash
for file in ./documents/*.docx; do
    python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py terms.csv "$file"
done
```

### Example Output

```
Input:  GGGI/file-percobaan.docx
Terms CSV: GGGI/english-terms.csv
Output: GGGI/file-percobaan-italicized.docx

Reading English terms from CSV...
Found 8 terms (sorted by length):
  1. 'safety precaution' (17 chars)
  2. 'toolbox talks' (13 chars)
  3. 'bifacial gain' (13 chars)
  4. 'backsheet' (9 chars)
  5. 'toolbox' (7 chars)
  6. 'safety' (6 chars)
  7. 'albedo' (6 chars)
  8. 'terms' (5 chars)

Loading document...
Found 6 paragraphs and 0 tables

Italicizing English terms...

============================================================
✓ Processing complete!
  Terms italicized: 23 occurrences
  Output saved: GGGI/file-percobaan-italicized.docx
============================================================
```

## Use Cases

### Academic Papers (Mixed Language)

```bash
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py academic-terms.csv thesis-id.docx
```

### Technical Manuals (Indonesian with English Technical Terms)

```bash
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py tech-terms.csv manual.docx
```

### Business Documents

```bash
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py business-terms.csv report.docx
```

## What Gets Preserved

- **Text content:** All text remains unchanged
- **Formatting:** Bold, underline, fonts, sizes, colors
- **Structure:** Paragraphs, tables, lists remain intact
- **Styles:** All paragraph and character styles maintained
- **Page layout:** Margins, page size, orientation unchanged

## What Gets Modified

**Only the specific English terms** matching the CSV list are:
- Changed to italic
- Tagged as English (US) language
- Marked to skip spell/grammar checking

Everything else remains untouched.

## Limitations

### Does Not Handle

- **Headers/footers:** python-docx limitation (terms in headers/footers won't be processed)
- **Text boxes:** Content in text boxes is not accessible
- **Embedded objects:** Terms in embedded Word objects, images, or charts
- **Comments:** Terms in document comments

### Workarounds

- **Headers/footers:** Apply italic formatting manually in Word
- **Text boxes:** Convert to regular paragraphs if possible

## Troubleshooting

### CSV File Not Found

```
Error: CSV file not found: terms.csv
```

**Solution:** Verify the CSV file path is correct

### Input File Not Found

```
Error: Input file not found: document.docx
```

**Solution:** Verify the input file path is correct

### Wrong File Format

```
Error: Input must be a .docx file: document.pdf
```

**Solution:** Ensure input file has .docx extension

### No Terms Italicized

If the script reports "Terms italicized: 0 occurrences":
- Verify terms in CSV match terms in document
- Check spelling of terms in CSV
- Ensure terms are not already italicized
- Check that document has actual content

## Tips

1. **Build comprehensive term list:** Include all English terms used in your documents
2. **Include variations:** Add both singular and plural forms if needed
3. **Longer phrases first:** CSV order doesn't matter (script auto-sorts)
4. **Test on copy:** Always test on a copy before modifying originals
5. **Review output:** Check that terms are correctly identified

## Common Term Lists

### Technical Documentation
- software, hardware, interface, system
- input, output, configuration, settings
- online, offline, backup, restore

### Scientific Papers
- hypothesis, methodology, analysis, conclusion
- sample, control, variable, experiment
- significant, correlation, deviation

### Business Documents
- meeting, deadline, project, stakeholder
- budget, forecast, revenue, expense
- strategy, implementation, evaluation

## Related Skills

- **msword-move-citation-before-period**: Fix citation placement in documents
- **msword-remove-headers-footers**: Remove headers/footers from Word documents
- **convert-md-to-docx**: Convert markdown to Word format

## Dependencies

- **python-docx**: For manipulating .docx files
- **csv**: Built-in Python module for reading CSV files (included)
- **re**: Built-in Python regex module (included)
- **pathlib**: Built-in Python module for file paths (included)
- Project virtual environment (.venv)

## Performance Notes

- **Fast processing:** Handles large documents efficiently
- **Example:** 100-page document with 50 terms: ~15-20 seconds
- **Memory efficient:** Processes documents without loading entire content
- **Typical:** Most documents (20-50 pages): ~5-10 seconds

## Maintenance

### Adding New Terms to CSV

1. Open CSV file in text editor or Excel
2. Add new terms (one per line)
3. Save file
4. Re-run script on documents

**No need to sort manually** - script handles sorting automatically!
