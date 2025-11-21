# Chapter Files Analyzer

## Purpose
Analyzes chapter markdown files and creates a work manifest for the content composition workflow. The manifest identifies which introduction files (x.x.0) need to be created and which content files need editing.

## How It Works
1. Scans folder for markdown files matching pattern: `0X-ABC-X.Y.Z-Seq-Type-Description.md`
2. Parses filenames to extract metadata (chapter, hierarchy, document type)
3. Groups files by two-digit sub-chapters (e.g., 2.2, 2.3, 2.4)
4. Identifies missing x.x.0 introduction files
5. Creates JSON manifest for orchestration workflow

## Requirements
- **Python version**: 3.6+
- **Virtual environment**: Project `.venv` should be activated
- **Dependencies**: None (uses only Python standard library)

## Usage

### Basic Usage
```bash
source .venv/bin/activate
python python_scripts/16-analyze-chapter-files.py <folder_path>
```

### Example
```bash
python python_scripts/16-analyze-chapter-files.py \
  ./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/markdown-composed
```

## Output

### Console Output
```
Analyzing chapter files in: ./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/markdown-composed

============================================================
CHAPTER ANALYSIS COMPLETE
============================================================
Chapter: 02 (HK)
Total files found: 45
Introduction files to create: 7
Content files to edit: 45
Sub-chapters: 8
============================================================

Introduction files to create:
  - 02-HK-2.2.0-PNGTR-Prosedur.md (2.2: Prosedur Induk dan Kerangka Umum)
  - 02-HK-2.3.0-PNGTR-Layanan.md (2.3: Layanan Akomodasi (Wisma))
  - 02-HK-2.4.0-PNGTR-Area.md (2.4: Area Pembelajaran)
  - 02-HK-2.5.0-PNGTR-Area.md (2.5: Area Kerja dan Khusus)
  - 02-HK-2.6.0-PNGTR-Area.md (2.6: Area Makanan dan Minuman (F&B))
  - 02-HK-2.7.0-PNGTR-Area.md (2.7: Area Publik, Fasilitas Pendukung, dan Outdoor)
  - 02-HK-2.8.0-PNGTR-Sistem.md (2.8: Sistem Pengelolaan Mutu dan Dokumentasi)

Manifest saved to: ./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/markdown-composed/chapter-work-manifest.json

Ready for content composition workflow!
```

### JSON Manifest File
Creates `chapter-work-manifest.json` in the target folder:

```json
{
  "chapter_info": {
    "folder": "./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/markdown-composed",
    "chapter_number": "02",
    "chapter_abbrev": "HK",
    "total_files": 45
  },
  "introduction_files_to_create": [
    {
      "file_to_create": "02-HK-2.2.0-PNGTR-Prosedur.md",
      "sub_chapter": "2.2",
      "title": "Prosedur Induk dan Kerangka Umum",
      "source_files": [
        "02-HK-2.2.1-PF-Prosedur_Akomodasi.md",
        "02-HK-2.2.2-PF-Prosedur_Area_Publik_Kerja.md"
      ]
    }
    // ... more intro files
  ],
  "content_files_to_edit": [
    "02-HK-2.2.1-PF-Prosedur_Akomodasi.md",
    "02-HK-2.2.2-PF-Prosedur_Area_Publik_Kerja.md"
    // ... all files
  ],
  "sub_chapters": {
    "2.2": {
      "title": "Prosedur Induk dan Kerangka Umum",
      "file_count": 2
    }
    // ... more sub-chapters
  }
}
```

## Filename Pattern

### Expected Pattern
```
0X-ABC-X.Y.Z-Seq-Type-Description.md
```

### Components
- **0X**: Chapter number (02, 03, 04, etc.)
- **ABC**: Chapter abbreviation (HK, SEC, FO, FB, etc.)
- **X.Y.Z**: Hierarchical numbering (2.3.1, 2.4.2, etc.)
- **Seq**: Alphabetic sequence (A, B, C, ...) or empty for x.x.0 files
- **Type**: Document type (PNGTR, PF, IK, FR)
- **Description**: Short descriptive name (underscores for spaces)

### Examples
- `02-HK-2.1.0-PNGTR-Housekeeping.md` - Introduction (already exists)
- `02-HK-2.3.1-A-IK-Pembersihan_Kamar.md` - Work instruction
- `02-HK-2.3.1-B-FR-Checklist_Kamar.md` - Form/checklist
- `03-SEC-3.2.1-A-IK-Patroli_Rutin.md` - Different chapter example

## Error Handling

### Folder Not Found
```
ERROR: Folder does not exist: ./path/to/folder
```

### No Markdown Files
```
Warning: No markdown files found in ./path/to/folder
ERROR: No files matched expected naming pattern
```

### Invalid Filename Pattern
```
Warning: Could not parse filename: invalid-name.md
```

Files that don't match the pattern are skipped but a warning is shown.

## Use Cases

### Initial Chapter Analysis
Before running content composition workflow, analyze the chapter to understand:
- How many introduction files need to be created
- How many content files need editing
- Sub-chapter structure

### Validation
After organizing files with `15-chapter-organizer.py`, verify:
- All files follow naming convention
- Sub-chapter groupings are correct
- Identify any missing introduction files

### Planning
Use manifest to estimate:
- How many sub-agents will be needed
- How many batches for parallel processing
- Total processing time

## Integration

### Used By
- Main orchestration workflow (via `orkestrasi-pembenahan-bab` skill)
- Content composition system

### Produces
- `chapter-work-manifest.json` consumed by orchestration workflow

### Next Step
After running this script, the orchestration workflow uses the manifest to:
1. Launch sub-chapter-previewer agents for introduction files
2. Launch sub-chapter-editor agents for content files
3. Track progress and create completion report

## Performance Notes
- **Speed**: Instant for 50 files (< 1 second)
- **Memory**: Minimal (only reads filenames, not file contents)
- **Scalability**: Can handle hundreds of files

## Troubleshooting

### Script Won't Run
- Ensure virtual environment is activated: `source .venv/bin/activate`
- Check Python version: `python --version` (need 3.6+)

### Incorrect Sub-Chapter Titles
The script uses hardcoded title mapping for Bab 2. For other chapters:
- Titles default to "Sub-Bab X.Y" if not in mapping
- Manually update `get_sub_chapter_title()` function for new chapters
- Or user can manually edit manifest JSON after generation

### Unexpected File Count
- Verify all files follow naming pattern
- Check for any non-standard filenames (warnings will be shown)
- Ensure no duplicate files in folder

---

**Created by**: Claude Code
**Date**: 19 Januari 2025
**Script**: `python_scripts/16-analyze-chapter-files.py`
**Status**: READY FOR USE
