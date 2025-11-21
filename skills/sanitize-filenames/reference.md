# Sanitize Filenames - Reference Documentation

## When to Use This Skill
Activate this skill when the user requests to:
- Sanitize or clean up filenames
- Remove spaces from filenames
- Fix unsafe characters in filenames
- Rename files to be filesystem-safe
- Batch rename files in a folder

## Script Location & Usage
Script: `.claude/skills/sanitize-filenames/sanitize-filenames.py`

Always activate the virtual environment:
```bash
source .venv/bin/activate
```

## Sanitization Method
Applies comprehensive filename sanitization:
- Replaces spaces with underscores
- Removes unsafe characters (,&@')
- Keeps safe characters (()[] letters numbers .-_)
- Deduplicates consecutive symbols
- Works on files and folders

## Four Input Modes

### Mode 1: Single File or Folder
```bash
python .claude/skills/sanitize-filenames/sanitize-filenames.py path/to/file.pdf
```
Output: Renames to cleaned filename

### Mode 2: Multiple Files or Folders (Comma-Separated)
```bash
python .claude/skills/sanitize-filenames/sanitize-filenames.py "path1,path2,path3"
```
Output: Sanitizes each specified path

### Mode 3: All Files in Folder (Recursive)
```bash
python .claude/skills/sanitize-filenames/sanitize-filenames.py ./folder/path/
```
Workflow: Recursively processes all files in folder and subdirectories

### Mode 4: Pattern Matching in Folder
```bash
python .claude/skills/sanitize-filenames/sanitize-filenames.py ./folder/path/ "*.pdf"
```

Common patterns:
- `"*.pdf"` - PDF files only
- `"*.docx"` - Word documents only
- `"*.jpg"` - JPEG images only
- `"*"` - All files (default)

## Sanitization Rules

### What Gets Changed
- **Spaces** → underscores (`_`)
- **Multiple spaces** → single underscore
- **Commas** (`,`) → removed
- **Ampersands** (`&`) → removed
- **At signs** (`@`) → removed
- **Apostrophes** (`'`) → removed
- **Multiple consecutive symbols** → single symbol

### What Stays Safe
- Alphanumeric: `a-z`, `A-Z`, `0-9`
- Parentheses: `(`, `)`
- Square brackets: `[`, `]`
- Dots: `.`
- Hyphens: `-`
- Underscores: `_`

## Important Notes
- **Files renamed in place**: Original filenames are replaced
- **No backups**: Make backups before running if needed
- **Recursive**: Folder mode processes all subdirectories
- **Collision handling**: Adds numeric suffix if sanitized name exists
- **Extension preserved**: File extensions remain unchanged
- **Fast**: Processes hundreds of files per second

## Examples

### Sanitize Single File
```bash
python .claude/skills/sanitize-filenames/sanitize-filenames.py "./Document  Name.pdf"
```

### Sanitize Multiple Files
```bash
python .claude/skills/sanitize-filenames/sanitize-filenames.py "file 1.pdf,file 2.docx,report  final.txt"
```

### Sanitize All PDFs in Folder
```bash
python .claude/skills/sanitize-filenames/sanitize-filenames.py "./FOLDER/" "*.pdf"
```

### Sanitize All Files in Folder
```bash
python .claude/skills/sanitize-filenames/sanitize-filenames.py "./documents/"
```

## Troubleshooting

### Files not renamed
- Check if filenames already comply with rules
- Verify write permissions
- Ensure files aren't locked

### Permission errors
- Ensure files are closed in applications
- Check folder write permissions

### Duplicate filenames after sanitization
- Script adds numeric suffix automatically
- Example: `file_1.pdf`, `file_2.pdf`, `file_3.pdf`

### Pattern not matching files
- Verify pattern syntax: `"*.pdf"` not `*.pdf`
- Check file extensions match pattern
- Use `"*"` to match all files

## Advanced Usage

### Different File Types
```bash
# PDFs only
python .claude/skills/sanitize-filenames/sanitize-filenames.py "./folder/" "*.pdf"

# Word documents only
python .claude/skills/sanitize-filenames/sanitize-filenames.py "./folder/" "*.docx"

# All files
python .claude/skills/sanitize-filenames/sanitize-filenames.py "./folder/"
```

## Dependencies
- Python 3.6+
- Built-in modules only (pathlib, re, sys)
- Project virtual environment (.venv)

## Performance
- Speed: ~100-500 files/second
- Memory: Very low
- Large batches: 1000+ files in seconds
