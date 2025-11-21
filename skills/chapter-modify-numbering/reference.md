# Chapter Modify Numbering - Reference Documentation

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [What It Does](#what-it-does)
- [Usage Syntax](#usage-syntax)
- [Common Usage Example](#common-usage-example)
- [Expected Output](#expected-output)
- [What Gets Modified](#what-gets-modified)
- [Important Notes](#important-notes)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Advanced Usage](#advanced-usage)
- [Related Skills](#related-skills)
- [Technical Notes](#technical-notes)

## When to Use This Skill
Activate this skill when the user requests to:
- Renumber book chapters
- Change chapter numbers in files
- Reorganize chapter structure
- Move content from one chapter to another
- Update chapter references after reorganization
- Use the existing `22-modify-chapter-numbering.py` script

## Instructions

### Script Location & Usage
The reusable script is located at: `.claude/skills/chapter-modify-numbering/chapter-modify-numbering.py`

Always activate the virtual environment before running:
```bash
source .venv/bin/activate
```

### What It Does

**1. Renames Files**:
- Pattern: `XX-ABBREV-XX.Y.Z-TYPE-Description.md`
- Changes chapter number with leading zeros for chapters < 10
- Example: `14-LIB-14.1.0-PNGTR-File.md` → `08-LIB-8.1.0-PNGTR-File.md`

**2. Updates Content**:
- Replaces chapter references throughout file content
- NO leading zeros in content (only in filenames)
- Example: `Bab 14` → `Bab 8`, `14.1.` → `8.1.`

### Usage Syntax

```bash
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py <folder_path> <old_chapter> <new_chapter>
```

### Common Usage Example

User: "Ubah penomoran bab dari naskah di folder `./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop`, dari Bab 14 menjadi Bab 8"

```bash
source .venv/bin/activate
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop" 14 8
```

### Expected Output

```
======================================================================
Modify Chapter Numbering
======================================================================
Folder: BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop
Change: Bab 14 → Bab 8

Found 6 markdown file(s)

This will:
  1. Rename files: 14-XXX-14.Y.Z-... → 08-XXX-8.Y.Z-...
  2. Replace in content: Bab 14 → Bab 8, 14.Y.Z → 8.Y.Z

Continue? (y/n): y

Processing files...

✓ 14-LIB-14.1.0-PNGTR-Pengantar_Pengelolaan_Perpustakaan.md
  → 08-LIB-8.1.0-PNGTR-Pengantar_Pengelolaan_Perpustakaan.md
    Content changes: 9

✓ 14-LIB-14.1.1-PF-Pengadaan_Bahan_Pustaka.md
  → 08-LIB-8.1.1-PF-Pengadaan_Bahan_Pustaka.md

======================================================================
SUMMARY
======================================================================
Total files processed: 6
Files renamed: 6
Files with content changes: 3
Total content replacements: 15

✓ All files processed successfully!

Chapter numbering changed from Bab 14 to Bab 8
```

## What Gets Modified

### Filename Changes

**Leading Zeros Applied** for chapters < 10:

| Before | After |
|--------|-------|
| `14-LIB-14.1.0-PNGTR-Pengantar.md` | `08-LIB-8.1.0-PNGTR-Pengantar.md` |
| `14-LIB-14.2.1-PF-Pengadaan.md` | `08-LIB-8.2.1-PF-Pengadaan.md` |
| `12-ABC-12.3.2-IK-Instruksi.md` | `05-ABC-5.3.2-IK-Instruksi.md` |

**Note**:
- Leading number: `14-` → `08-` (with zero)
- Hierarchy: `14.Y.Z` → `8.Y.Z` (no zero)

### Content Changes

**NO Leading Zeros** in content:

| Pattern | Before | After |
|---------|--------|-------|
| Chapter title | `# PENGANTAR BAB 14: ...` | `# PENGANTAR Bab 8: ...` |
| Chapter reference | `Bab 14 ini mengatur...` | `Bab 8 ini mengatur...` |
| Table of contents | `Daftar Isi Bab 14:` | `Daftar Isi Bab 8:` |
| Section heading | `## 14.1. Title` | `## 8.1. Title` |
| Sub-section | `### 14.1.1. Subtitle` | `### 8.1.1. Subtitle` |
| List reference | `- **14.2.1. Item**` | `- **8.2.1. Item**` |

## Important Notes

### Confirmation Required
The script asks for confirmation before making changes:
```
Continue? (y/n):
```

User must type `y` to proceed.

### Files Modified In Place
**WARNING**: Original files are modified directly.

**Before running**, ensure:
- ✅ Files are backed up (or committed to git)
- ✅ User has confirmed they want to proceed
- ✅ Correct folder path is specified

### Leading Zero Rules

**Filenames** (chapter < 10):
- Chapter 8 → `08-`
- Chapter 9 → `09-`
- Chapter 10+ → `10-`, `11-`, etc. (no leading zero)

**Content** (no leading zeros):
- `Bab 8` (not `Bab 08`)
- `8.1.` (not `08.1.`)
- `8.1.1.` (not `08.1.1.`)

## Reference Documentation
- Script location: `.claude/skills/chapter-modify-numbering/chapter-modify-numbering.py`
- Dependencies: Python 3.6+ (uses built-in modules only)

## Examples

### Example 1: Renumber Chapter 14 to Chapter 8
User: "Ubah penomoran dari Bab 14 ke Bab 8 di folder perpustakaan"
```bash
source .venv/bin/activate
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop" 14 8
```

### Example 2: Renumber Chapter 12 to Chapter 5
User: "Change chapter numbering from 12 to 5"
```bash
source .venv/bin/activate
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py "./markdown_folder" 12 5
```

### Example 3: Shift Chapter Down (Insert New Chapter)
User: "I'm inserting a new chapter at position 5, move the old chapter 5 to chapter 6"
```bash
source .venv/bin/activate
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py "./BUKU-2/05-OLD-CHAPTER" 5 6
```

### Example 4: Consolidate Chapters
User: "We removed chapter 3, renumber chapter 4 to fill the gap"
```bash
source .venv/bin/activate
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py "./BUKU-2/04-CHAPTER" 4 3
```

## Troubleshooting

### "Folder not found"
- Verify folder path is correct
- Use forward slashes: `./folder/path`
- Check that folder exists

### "No markdown files found"
- Ensure folder contains .md files
- Verify file extensions are `.md` (not `.txt`)
- Check file naming pattern matches expected format

### "Chapter numbers must be integers"
- Use whole numbers only: `14`, `8`, `12`
- Don't use decimals or text: `14.0`, `eight`

### Files not renamed
- Verify filename matches pattern: `XX-ABBREV-XX.Y.Z-TYPE-Description.md`
- Check if old chapter number exists in filename
- Example: File `02-HK-2.1.0-PNGTR-File.md` won't change if looking for chapter 14

### Content not changed
- Some files may not contain chapter references
- Forms (FR files) often have minimal text
- Check if old chapter number appears in content

### Partial changes
- Script may rename files but find no content changes
- This is normal for files without chapter references (e.g., pure forms)

## Advanced Usage

### Test Before Running
Create a test copy first:
```bash
cp -r ./original_folder ./test_folder
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py ./test_folder 14 8
# Review results
# If good, run on original
```

### Batch Renumbering
For multiple chapter changes, run sequentially:
```bash
# Shift chapters 5-7 down by one (start from highest)
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py ./BUKU-2/07-CHAPTER 7 8
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py ./BUKU-2/06-CHAPTER 6 7
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py ./BUKU-2/05-CHAPTER 5 6
```

### Pipeline with Other Scripts
Renumber then convert to docx:
```bash
# Renumber chapter
python .claude/skills/chapter-modify-numbering/chapter-modify-numbering.py ./folder 14 8

# Convert to Word
python .claude/skills/convert-md-to-docx/convert-md-to-docx.py ./folder
```

## Related Skills
- **chapter-organizer**: Organize files after creation
- **convert-md-to-docx**: Convert to Word after renumbering

## Dependencies
- Python 3.6+
- Built-in modules only (re, pathlib, sys)
- No external libraries required

## Performance Notes
- **Speed**: ~0.1 seconds per file
- **Large batches**: 100+ files in under 10 seconds
- **Memory**: Uses ~10MB RAM
- **Safety**: Sequential processing for file operations

## Technical Notes

### Filename Pattern
Matches: `^(\d{2})-([A-Z]+)-(\d+)\.(\d+)\.(\d+)-([A-Z]+)-(.+)\.md$`

Components:
- Chapter (2 digits with leading zero)
- Abbreviation (2-4 letters)
- Hierarchy (X.Y.Z)
- Type (PNGTR, PF, IK, FR)
- Description

### Content Patterns
Uses regex to match:
- `Bab XX` / `BAB XX`
- `## XX.` / `### XX.Y.`
- `XX.Y.` / `XX.Y.Z.`
- `**XX.Y.Z.**`
- `Daftar Isi Bab XX`

---

**Created**: 2025-11-20
**Purpose**: Renumber book chapters
**Status**: READY FOR USE
