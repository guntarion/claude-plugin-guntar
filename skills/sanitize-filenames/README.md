# Sanitize Filenames and Folder Names

## Purpose
This script sanitizes filenames and folder names by replacing spaces with underscores, removing unsafe characters, and deduplicating consecutive symbols. It ensures clean, filesystem-safe names across all files and folders.

## How It Works
1. **Scans input**: Processes single file, multiple files/folders, or all files in a folder
2. **Sanitizes names**: Applies sanitization rules to each filename/folder name
3. **Renames files**: Automatically renames files with sanitized names
4. **Shows results**: Displays before/after names and summary statistics

## Requirements
- **Python version**: 3.6+
- **Dependencies**: None (uses only built-in modules: pathlib, re, sys)

## Usage

### Activate Virtual Environment
```bash
source .venv/bin/activate
```

### Mode 1: Single File or Folder
Sanitize one file or folder name:
```bash
python python_scripts/11-sanitize-filenames.py path/to/file.txt
```

**Example**:
```bash
python python_scripts/11-sanitize-filenames.py "./Document Name  Test.pdf"
```
Output: `Document_Name_Test.pdf`

### Mode 2: Multiple Files or Folders (Comma-Separated)
Sanitize multiple specific paths:
```bash
python python_scripts/11-sanitize-filenames.py "path1,path2,path3"
```

**Example**:
```bash
python python_scripts/11-sanitize-filenames.py "file 1.pdf,file 2.pdf,folder name"
```

### Mode 3: All Files in Folder
Sanitize all files in a folder:
```bash
python python_scripts/11-sanitize-filenames.py ./folder/path/
```

**Example**:
```bash
python python_scripts/11-sanitize-filenames.py "./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/"
```
Sanitizes all files in the folder (recursive).

### Mode 4: Files Matching Pattern in Folder
Sanitize only files matching a specific pattern:
```bash
python python_scripts/11-sanitize-filenames.py ./folder/path/ "*.pdf"
```

**Examples**:
```bash
# Only PDF files
python python_scripts/11-sanitize-filenames.py "./documents/" "*.pdf"

# Only Word documents
python python_scripts/11-sanitize-filenames.py "./documents/" "*.docx"

# All image files
python python_scripts/11-sanitize-filenames.py "./images/" "*.jpg"
```

## Sanitization Rules

### 1. Space Handling
- Multiple consecutive spaces → single underscore
- Single spaces → underscore
- Example: `Document  Name` → `Document_Name`

### 2. Unsafe Characters (Removed)
- Commas: `,`
- Ampersands: `&`
- At signs: `@`
- Apostrophes: `'`
- Example: `File's & Co, Test` → `Files_Co_Test`

### 3. Safe Characters (Kept)
- Alphanumeric: `a-z`, `A-Z`, `0-9`
- Parentheses: `(`, `)`
- Square brackets: `[`, `]`
- Dots: `.`
- Hyphens: `-`
- Underscores: `_`

### 4. Symbol Deduplication
- Multiple underscores → single underscore
- Multiple dots → single dot
- Multiple dashes → single dash
- Example: `Test___File...Name--Final` → `Test_File.Name-Final`

### 5. Trimming
- Removes leading/trailing: `_`, `.`, `-`
- Example: `_test-` → `test`

## Examples

### Before and After

| Original Filename | Sanitized Filename |
|-------------------|-------------------|
| `Document  Name  Test.pdf` | `Document_Name_Test.pdf` |
| `File, with, commas.txt` | `File_with_commas.txt` |
| `Name & Company @ Home.doc` | `Name_Company_Home.doc` |
| `File's apostrophe test.pdf` | `Files_apostrophe_test.pdf` |
| `Keep (parentheses) and [brackets].txt` | `Keep_(parentheses)_and_[brackets].txt` |
| `Multiple___underscores.pdf` | `Multiple_underscores.pdf` |
| `Dots...test.txt` | `Dots.test.txt` |
| `Dash--test.pdf` | `Dash-test.pdf` |

### Usage Examples

**Sanitize all PDFs in a folder**:
```bash
python python_scripts/11-sanitize-filenames.py "./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/" "*.pdf"
```

**Sanitize all files (any type) in a folder**:
```bash
python python_scripts/11-sanitize-filenames.py "./documents/"
```

**Sanitize specific files**:
```bash
python python_scripts/11-sanitize-filenames.py "file 1.pdf,file 2.docx,report  final.txt"
```

## Output

### Single File Mode
```
Sanitizing: Document  Name.pdf... ✓
  Document  Name.pdf
    → Document_Name.pdf
```

### Folder Mode
```
Processing folder: ./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)
Pattern: *.pdf

============================================================
Folder: ./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)
Total files processed: 50
Renamed: 50
Unchanged: 0

Renamed files:
  Form Pembersihan Ruang Lobby.pdf
    → Form_Pembersihan_Ruang_Lobby.pdf
  FR.PKU.001 Formulir Checklist.pdf
    → FR.PKU.001_Formulir_Checklist.pdf
  ... and 48 more
============================================================
```

## Important Notes
- **Files are renamed in place**: Original filenames are replaced
- **No backups created**: Make backups before running if needed
- **Recursive processing**: Folder mode processes all subdirectories
- **Collision handling**: If sanitized name exists, adds numeric suffix (e.g., `_1`, `_2`)
- **Extension preserved**: File extensions remain unchanged

## Troubleshooting

### Script not found
- Verify you're in the project root directory
- Check that `python_scripts/` folder exists

### Permission denied error
- Make sure files are not locked (closed in applications)
- Check file permissions: files should be writable
- Run: `python python_scripts/11-sanitize-filenames.py "path"`

### Files not renamed
- Check if filenames already comply with sanitization rules
- Verify you have write permissions to the folder
- Check console output for specific error messages

### Duplicate filename after sanitization
- Script automatically adds numeric suffix (e.g., `filename_1.pdf`)
- Multiple files with same sanitized name will be numbered sequentially

## Reusable Script
This script is designed for reuse across different folders and file types:
- Change folder path in command
- Change file pattern to target different types (`*.pdf`, `*.docx`, `*.jpg`, etc.)
- Use comma-separated paths for multiple targets

## Dependencies Used
- **pathlib**: File path operations (built-in)
- **re**: Regular expressions for pattern matching (built-in)
- **sys**: Command-line arguments (built-in)

## Performance Notes
- **Speed**: ~100-500 files per second (depends on system)
- **Memory**: Very low (processes one file at a time)
- **Large batches**: 1000+ files may take a few seconds
