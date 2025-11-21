# Remove Headers and Footers from .docx Files

## Purpose
This script removes all headers and footers from Microsoft Word documents (.docx format). It processes multiple files in a folder with a safety mechanism: it tests on the first document before processing all remaining documents.

## How It Works
1. **Scans folder**: Finds all .docx files in the target directory
2. **Test run**: Tests the removal process on the first document found
3. **User confirmation**: Asks for confirmation before processing all remaining files
4. **Batch processing**: Removes headers and footers from all documents
5. **Progress tracking**: Shows success/failure count for each file

## Requirements
- **Library**: `python-docx` (included in project dependencies)
- **Python version**: 3.6+
- **Virtual environment**: Must activate project `.venv` before running

## Usage

### Single File Mode
```bash
source .venv/bin/activate
python python_scripts/09-remove-headers-footers.py path/to/file.docx
```

### Multiple Files Mode
```bash
source .venv/bin/activate
python python_scripts/09-remove-headers-footers.py file1.docx,file2.docx,file3.docx
```

### Folder Mode (Interactive)
```bash
source .venv/bin/activate
python python_scripts/09-remove-headers-footers.py path/to/folder
```

**Interactive Workflow:**
1. Script finds all .docx files in the folder
2. Tests on first document
3. Shows result: `✓ Successfully removed headers/footers from test document`
4. Prompts: `Test successful! Process all documents? (y/n):`
5. Enter `y` to process all files
6. Script displays progress and final summary

### Folder Mode (Auto-Confirm)
```bash
source .venv/bin/activate
python python_scripts/09-remove-headers-footers.py path/to/folder --yes
```

**Non-Interactive Workflow:**
- Use `--yes` or `-y` flag to skip confirmation prompt
- Automatically processes all files after successful test
- Useful for automation and scripting

### Example Output
```
Found 45 .docx files

Testing on: 02_Housekeeping_IK.PKU.001 - PEMBERSIHAN AREA GUDANG.docx
✓ Successfully removed headers/footers from test document

Test successful! Process all documents? (y/n): y

Processing all 45 documents...

[1/45] Document1.docx... ✓
[2/45] Document2.docx... ✓
...
============================================================
Processing complete!
Success: 45/45
============================================================
```

## What Gets Removed
- **Headers**: All content in all header types:
  - Default/odd page headers
  - First page headers (when different first page is enabled)
  - Even page headers
- **Footers**: All content in all footer types:
  - Default/odd page footers
  - First page footers (when different first page is enabled)
  - Even page footers
- **Content Types**: Removes all XML elements including:
  - Paragraphs and text
  - Tables
  - SDT (Structured Document Tags / Content Controls)
  - Any other embedded elements
- **All sections**: Applies to all sections in the document

## Important Notes
- **Files are modified in place**: Original files are overwritten
- **No backups created**: Make backups before running if needed
- **Test first**: Always review the test document after running
- **Reversible**: If headers/footers are needed again, they must be re-added manually

## Reusable Script
This script is designed to be reused for multiple document folders. To use with a different folder:

**Edit the script** (line 61):
```python
folder_path = Path("./YOUR-NEW-FOLDER-PATH")
```

Then run as normal. No need to create a new script for different folders.

## Troubleshooting

### Script not found
- Verify you're in the project root directory
- Check that `python_scripts/` folder exists

### Permission denied error
- Make sure the script file has execute permissions
- Or use: `python python_scripts/09-remove-headers-footers.py`

### Module not found error
- Activate virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

### Document fails to process
- Check the error message displayed
- Document may be corrupted or unsupported format
- Try processing other documents first

## Dependencies Used
- **python-docx**: Manipulates .docx file structure and content
- **pathlib**: Modern file path operations
- **sys**: System-level operations and exit codes
- **typing**: Type hints for better code documentation


  What Was Fixed

  1. SDT Elements: The script now removes Structured Document Tags (content controls) that contain footer text like
  "FR-SMT-004" and "Uncontrolled when printed or downloaded"
  2. All Footer Types: Removes default, first page, and even page footers
  3. Auto-Confirm Flag: Added --yes flag for non-interactive batch processing

  Script Improvements

  - 09-remove-headers-footers.py:49-54 - Now removes all XML elements (not just paragraphs/tables)
  - 09-remove-headers-footers.py:64-79 - Added --yes/-y flag support
  - 09-remove-headers-footers.py:158-164 - Auto-confirm logic for folder mode
  - Updated readme with comprehensive usage documentation