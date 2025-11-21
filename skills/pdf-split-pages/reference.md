# Split PDF Files - Reference Documentation

## When to Use This Skill
Activate when user requests to:
- Split PDF into multiple parts
- Extract specific page ranges from PDF
- Create separate PDF for each page
- Divide PDF based on CSV mapping
- Break down large PDF into smaller files
- Separate chapters or sections from PDF

## Script Location
`.claude/skills/pdf-split-pages/pdf-split-pages.py`

## Usage Syntax
```bash
source .venv/bin/activate
python .claude/skills/pdf-split-pages/pdf-split-pages.py <input.pdf> <mode> [options]
```

## Mode 1: Split by Page Ranges

Extract specific page ranges to named output files.

### Syntax
```bash
python .claude/skills/pdf-split-pages/pdf-split-pages.py file.pdf --ranges "x-y:output1.pdf,a-b:output2.pdf"
```

### Examples
```bash
# Split into two parts
python .claude/skills/pdf-split-pages/pdf-split-pages.py document.pdf --ranges "1-10:part1.pdf,11-20:part2.pdf"

# Split into chapters
python .claude/skills/pdf-split-pages/pdf-split-pages.py book.pdf --ranges "1-5:intro.pdf,6-15:ch1.pdf,16-25:ch2.pdf"
```

### Output
- Creates folder: `{input_name}_split/`
- Saves files with specified names in the folder

## Mode 2: Split Per Page

Split PDF into individual pages (one PDF per page).

### Syntax
```bash
python .claude/skills/pdf-split-pages/pdf-split-pages.py file.pdf --per-page
```

### Output
- Default folder: `{input_name}_pages/`
- File naming: `{input_name}_page_001.pdf`, `{input_name}_page_002.pdf`, etc.
- Numbers padded with zeros

## Mode 3: CSV-Based Splitting

Use CSV file to define splitting instructions. **Most powerful mode for batch operations.**

### CSV Format
```csv
output_name,page_range,description
01-FRONT-OFFICE.pdf,1-10,Proses 6.0 Pelayanan Pelanggan
02-HOUSEKEEPING.pdf,11-25,Proses 12.4 Layanan Umum
03-FOOD-BEVERAGE.pdf,26-40,Proses 12.4 Penyediaan Konsumsi
```

### Syntax
```bash
python .claude/skills/pdf-split-pages/pdf-split-pages.py file.pdf --csv mapping.csv
```

### Output
- Creates folder: `{input_name}_split/`
- Saves files according to CSV `output_name` column

## When User Provides List/Table

If user provides a list or table, convert it to CSV format:

**Your workflow:**
1. Convert the user's list to CSV format
2. Save as `mapping.csv` in project folder
3. Run the script with `--csv` mode

## Command-Line Options

### Mode Selection (choose one)
- `--ranges` / `-r`: Page ranges with output names
- `--per-page` / `-p`: Split into individual pages
- `--csv` / `-c`: CSV file with splitting instructions

### Optional
- `--output-dir` / `-o`: Custom output directory (only for `--per-page` mode)

## Page Specification
- **Format**: `x-y` (e.g., `1-5`, `10-20`)
- **Start from 1**: Page numbers are 1-indexed (first page = 1)
- **Inclusive**: Both start and end are included
- **Single page**: Use `x-x` or specify in range (e.g., `5-5`)

## Use Cases

### Extract Chapters from Book
```bash
python .claude/skills/pdf-split-pages/pdf-split-pages.py book.pdf --ranges "1-20:ch1.pdf,21-45:ch2.pdf"
```

### Split SOP Manual by Department (CSV Mode)
Create `dept-mapping.csv`:
```csv
output_name,page_range,description
front-office.pdf,6-15,Front Office
housekeeping.pdf,16-30,Housekeeping
security.pdf,31-50,Security
```

Run:
```bash
python .claude/skills/pdf-split-pages/pdf-split-pages.py "SOP-Manual.pdf" --csv dept-mapping.csv
```

### Create Individual Page Files
```bash
python .claude/skills/pdf-split-pages/pdf-split-pages.py presentation.pdf --per-page
```

## Important Notes
- **Original file preserved**: Source PDF is never modified
- **Output directory created automatically**: Script creates folder if needed
- **Overwrites existing files**: If output files exist, they will be replaced
- **Page validation**: Script checks that page ranges are valid
- **No backup needed**: Original PDF remains untouched

## Error Handling

### Invalid Page Range
```
✗ part1.pdf: Page range 1-100 exceeds PDF length (50 pages)
```
**Solution**: Check PDF page count and adjust ranges

### Invalid Format
```
✗ Error: Invalid ranges format
```
**Solution**: Use correct format: `"1-5:out1.pdf,6-10:out2.pdf"`

### CSV Missing Data
```
✗ Skipping row with missing data
```
**Solution**: Ensure CSV has all required columns (output_name, page_range)

## Related Skills
- **pdf-delete-pages**: Delete pages from PDF
- **convert-pdf-to-markdown**: Convert PDF to Markdown
