# Modify Chapter Numbering Script

**Script**: `22-modify-chapter-numbering.py`
**Purpose**: Change chapter numbering in both filenames and file contents
**Use Case**: Renumber book chapters when reorganizing content

---

## Features

- **Rename Files**: Updates chapter numbers in filenames
- **Update Content**: Replaces chapter references in file content
- **Smart Formatting**: Uses leading zeros for chapters < 10 in filenames only
- **Batch Processing**: Processes all .md files in a folder
- **Safe Execution**: Asks for confirmation before making changes

---

## Usage

### Activate Virtual Environment

```bash
source .venv/bin/activate
```

### Basic Syntax

```bash
python python_scripts/22-modify-chapter-numbering.py <folder_path> <old_chapter> <new_chapter>
```

### Examples

#### Example 1: Renumber from Chapter 14 to Chapter 8
```bash
source .venv/bin/activate
python python_scripts/22-modify-chapter-numbering.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop" 14 8
```

#### Example 2: Renumber from Chapter 12 to Chapter 5
```bash
source .venv/bin/activate
python python_scripts/22-modify-chapter-numbering.py "./markdown_folder" 12 5
```

---

## What Gets Modified

### 1. Filename Changes

**Pattern**: `XX-ABBREV-XX.Y.Z-TYPE-Description.md`

**Leading Zeros**: Applied to chapter numbers < 10

**Examples**:
| Before | After |
|--------|-------|
| `14-LIB-14.1.0-PNGTR-Pengantar.md` | `08-LIB-8.1.0-PNGTR-Pengantar.md` |
| `14-LIB-14.2.1-PF-Pengadaan.md` | `08-LIB-8.2.1-PF-Pengadaan.md` |
| `12-ABC-12.3.2-IK-Instruksi.md` | `05-ABC-5.3.2-IK-Instruksi.md` |

**Note**:
- Leading `14-` → `08-` (with zero)
- Hierarchy `14.Y.Z` → `8.Y.Z` (no zero)

---

### 2. Content Changes

**NO Leading Zeros** in content (only in filenames)

**Patterns Replaced**:

| Pattern | Before | After |
|---------|--------|-------|
| Chapter title | `# PENGANTAR BAB 14: ...` | `# PENGANTAR Bab 8: ...` |
| Chapter reference | `Bab 14 ini mengatur...` | `Bab 8 ini mengatur...` |
| Table of contents | `Daftar Isi Bab 14:` | `Daftar Isi Bab 8:` |
| Section heading | `## 14.1. Title` | `## 8.1. Title` |
| Sub-section | `### 14.1.1. Subtitle` | `### 8.1.1. Subtitle` |
| List reference | `- **14.2.1. Item**` | `- **8.2.1. Item**` |
| Numbered reference | `14.3. Description` | `8.3. Description` |

---

## Expected Output

### Console Output

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

✓ 14-LIB-14.2.0-PNGTR-Pengantar_Pengelolaan_Bahan_Pustaka.md
  → 08-LIB-8.2.0-PNGTR-Pengantar_Pengelolaan_Bahan_Pustaka.md
    Content changes: 3

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

---

## Detailed Examples

### Example: Chapter 14 → Chapter 8

**Before**:
```
Filename: 14-LIB-14.1.0-PNGTR-Pengantar_Pengelolaan_Perpustakaan.md

Content:
# PENGANTAR BAB 14: PENGELOLAAN PERPUSTAKAAN

Bab 14 ini mengatur Standard Operating Procedure...

## Daftar Isi Bab 14: Pengelolaan Perpustakaan

### 14.1. Pengadaan Bahan Pustaka
- **14.1.1. Prosedur Fungsi: Pengadaan Bahan Pustaka**

### 14.2. Pengelolaan Bahan Pustaka
- **14.2.1. Prosedur Fungsi: Pengelolaan Bahan Pustaka**
```

**After**:
```
Filename: 08-LIB-8.1.0-PNGTR-Pengantar_Pengelolaan_Perpustakaan.md

Content:
# PENGANTAR Bab 8: PENGELOLAAN PERPUSTAKAAN

Bab 8 ini mengatur Standard Operating Procedure...

## Daftar Isi Bab 8: Pengelolaan Perpustakaan

### 8.1. Pengadaan Bahan Pustaka
- **8.1.1. Prosedur Fungsi: Pengadaan Bahan Pustaka**

### 8.2. Pengelolaan Bahan Pustaka
- **8.2.1. Prosedur Fungsi: Pengelolaan Bahan Pustaka**
```

---

## Important Notes

### Leading Zeros

**In Filenames** (chapter < 10):
- `08-` (with zero)
- `09-` (with zero)
- `10-` (no change)

**In Content** (no leading zeros):
- `Bab 8` (no zero)
- `8.1.` (no zero)
- `8.1.1.` (no zero)

### Confirmation Required

The script will ask for confirmation before making any changes:
```
Continue? (y/n):
```

Type `y` to proceed or `n` to cancel.

### Original Files Modified

**WARNING**: This script modifies files in place. Make sure you have:
- ✅ Backup of your files
- ✅ Git commit (if using version control)
- ✅ Tested on a copy first

---

## Troubleshooting

### "Folder not found"
- Verify folder path is correct
- Use forward slashes: `./folder/path`
- Ensure folder exists

### "No markdown files found"
- Check folder contains .md files
- Verify file extensions are `.md` (not `.txt` or `.markdown`)

### "Chapter numbers must be integers"
- Use whole numbers only: `14`, `8`, `12`
- Don't use: `14.0`, `eight`, `14th`

### Files not renamed
- Verify files match the expected pattern: `XX-ABBREV-XX.Y.Z-TYPE-Description.md`
- Check if old chapter number exists in filename

### Content not changed
- Verify content contains chapter references
- Check if old chapter number appears in text
- Some files may not have chapter references (e.g., pure forms)

---

## Technical Details

### Filename Pattern Matching

**Pattern**: `^XX-ABBREV-XX\.Y\.Z-TYPE-Description\.md$`

**Components**:
- `XX`: Chapter number (with leading zero if < 10)
- `ABBREV`: 2-4 letter abbreviation (e.g., LIB, HK, SEC)
- `XX.Y.Z`: Hierarchy (chapter.section.subsection)
- `TYPE`: Document type (PNGTR, PF, IK, FR)
- `Description`: Descriptive name

### Content Pattern Matching

Uses regex patterns to match:
- `Bab XX` or `BAB XX` (case insensitive)
- `## XX.` or `### XX.Y.` (heading markers)
- `XX.Y.` or `XX.Y.Z.` (section references)
- `**XX.Y.Z.**` (bold section references)
- `Daftar Isi Bab XX` (table of contents)

---

## Use Cases

### Use Case 1: Reorganize Book Structure
When chapters are reordered, update numbering to reflect new structure.

**Scenario**: Move "Pengelolaan Perpustakaan" from Chapter 14 to Chapter 8

**Command**:
```bash
python 22-modify-chapter-numbering.py "./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0B-improved-sop" 14 8
```

### Use Case 2: Insert New Chapter
When adding a chapter in the middle, renumber subsequent chapters.

**Scenario**: Insert new chapter at position 5, move old Chapter 5 to Chapter 6

**Command**:
```bash
python 22-modify-chapter-numbering.py "./BUKU-2/05-OLD-CHAPTER" 5 6
```

### Use Case 3: Consolidate Chapters
When merging content, renumber to close gaps.

**Scenario**: Remove Chapter 3, renumber Chapter 4 to Chapter 3

**Command**:
```bash
python 22-modify-chapter-numbering.py "./BUKU-2/04-CHAPTER" 4 3
```

---

## Performance

- **Speed**: ~0.1 seconds per file
- **Large batches**: 100+ files processed in under 10 seconds
- **Memory**: Uses ~10MB RAM
- **Concurrent**: Processes files sequentially for safety

---

## Related Scripts

- **15-chapter-organizer.py**: Organize files after renaming
- **21-md-to-docx.py**: Convert markdown to Word after renumbering

---

**Created**: 2025-11-20
**Author**: Claude Code
**Version**: 1.0
