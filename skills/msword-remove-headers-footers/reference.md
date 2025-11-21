# Remove Headers and Footers - Reference Documentation

## When to Use This Skill
Activate this skill when the user requests to:
- Remove headers and footers from .docx files
- Delete headers/footers from Word documents
- Clean up headers/footers in a folder of documents
- Process individual files, collections of files, or entire folders

## Script Location & Usage
Script: `.claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py`

Always activate the virtual environment:
```bash
source .venv/bin/activate
```

## Three Input Modes

### Mode 1: Single File
```bash
python .claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py path/to/file.docx
```
Output: Headers/footers removed from the specified file in place.

### Mode 2: Multiple Files (Comma-Separated)
```bash
python .claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py "file1.docx,file2.docx,file3.docx"
```
Output: Headers/footers removed from each specified file in place.

**User input variations accepted**:
- Comma-separated: `"file1.docx, file2.docx, file3.docx"`
- Space-separated list: Pass multiple arguments
- Mixed paths: `"./folder/file1.docx,../other/file2.docx"`

### Mode 3: Folder Mode (Test-First Safety)
```bash
python .claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py ./path/to/folder
```

**Workflow**:
1. Scans folder for all .docx files
2. Tests removal on first file
3. Shows result and prompts for confirmation
4. If user enters `y`, processes all remaining files
5. Shows progress and final summary

## What Gets Removed
- **Headers**: All paragraphs and tables in document headers
- **Footers**: All paragraphs and tables in document footers
- **All sections**: Applies to all sections in the document
- **Scope**: Affects entire document, all pages

## Important Notes
- **Files modified in place**: Original .docx files are overwritten
- **No backups created**: Make backups before running if needed
- **Test-first for folders**: Always tests first file before batch
- **User confirmation**: Batch operations require confirmation
- **Reversible manually**: Headers/footers must be re-added manually in Word if needed

## Examples

### Single File
```bash
python .claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py "./path/to/document.docx"
```

### Multiple Specific Files
```bash
python .claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py "report.docx,proposal.docx,invoice.docx"
```

### Entire Folder
```bash
python .claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py "./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)"
```

## Troubleshooting

### Files not found
- Verify file/folder path is correct
- Check that .docx files exist
- Use forward slashes

### Permission errors
- Ensure files are not locked (closed in Word)
- Check file permissions: files should be readable/writable

### Processing fails for some documents
- File may be corrupted or have complex headers
- Check if Word can open the file normally
- Script will continue with other files even if one fails

## Advanced Usage

### Processing Multiple Folders
```bash
python .claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py "./FOLDER1"
python .claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py "./FOLDER2"
```

### Specific Files Across Folders
```bash
python .claude/skills/msword-remove-headers-footers/msword-remove-headers-footers.py "./FOLDER1/doc1.docx,./FOLDER2/doc2.docx"
```

## Related Skills
- **convert-md-to-docx**: Convert markdown to Word documents

## Dependencies
- Python 3.6+
- `python-docx` library
- Project virtual environment (.venv)
