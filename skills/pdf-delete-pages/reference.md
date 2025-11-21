# Delete Pages from PDF Files - Reference Documentation

## When to Use This Skill
Activate when user requests to:
- Delete pages from PDF files
- Remove first/last pages from PDFs
- Remove specific page ranges
- Clean up PDF documents

## Script Location
`.claude/skills/pdf-delete-pages/pdf-delete-pages.py`

## Usage Syntax
```bash
source .venv/bin/activate
python .claude/skills/pdf-delete-pages/pdf-delete-pages.py <input> --pages <pages>
```

## Input Modes

### Single File
```bash
python .claude/skills/pdf-delete-pages/pdf-delete-pages.py file.pdf --pages 1-3
```

### Multiple Files
```bash
python .claude/skills/pdf-delete-pages/pdf-delete-pages.py "file1.pdf,file2.pdf" --pages 1-3
```

### Folder
```bash
python .claude/skills/pdf-delete-pages/pdf-delete-pages.py ./folder/ --pages 1-3
```

## Page Specifications

- **Range**: `1-3` (pages 1, 2, 3)
- **Individual**: `1,3,5` (pages 1, 3, 5)
- **Combined**: `1-3,5,7-9` (pages 1-3, 5, and 7-9)

Page numbers start from 1 (not 0).

## Examples

### Delete first 3 pages
```bash
python .claude/skills/pdf-delete-pages/pdf-delete-pages.py document.pdf --pages 1-3
```

### Delete first page only
```bash
python .claude/skills/pdf-delete-pages/pdf-delete-pages.py document.pdf --pages 1
```

### Delete pages 1-3 and 5
```bash
python .claude/skills/pdf-delete-pages/pdf-delete-pages.py document.pdf --pages 1-3,5
```

## Output
- Original file overwritten directly
- No backup created, no suffix added
- Example: `document.pdf` (modified in-place)

## Important Notes
- Original PDFs are replaced with modified versions
- Cannot delete all pages (at least 1 must remain)
- Pages validated before deletion
- Make backups before running if you need to preserve originals

## Related Skills
- **pdf-split-pages**: Split PDF into multiple parts
- **convert-pdf-to-markdown**: Convert PDF to Markdown

## Dependencies
- `pypdf` library
