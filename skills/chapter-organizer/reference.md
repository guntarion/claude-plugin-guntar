# Chapter Organizer - Reference Documentation

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Prerequisites](#prerequisites)
- [Workflow Overview](#workflow-overview)
- [Step-by-Step Instructions](#step-by-step-instructions)
- [Naming Convention Rules](#naming-convention-rules)
- [Hierarchical Structure Guidelines](#hierarchical-structure-guidelines)
- [Important Notes](#important-notes)
- [Example Usage](#example-usage)
- [Related Files](#related-files)
- [Performance Notes](#performance-notes)

## When to Use This Skill
Activate when user requests to:
- Organize markdown files for a book chapter into hierarchical structure
- Rename chapter files based on table of contents structure
- Create structured file naming that reflects sub-chapters and sub-sub-chapters
- Apply the organizational structure from Bab 2 HOUSEKEEPING to other chapters

## Prerequisites

User must provide:
1. **Chapter analysis file**: Path to Gemini analysis markdown file (e.g., `./report/report-analysis/bab-x/bab-x-analysis.md`)
2. **Source folder**: Path to folder containing markdown files to organize (e.g., `./BUKU-X/0X-CHAPTER/markdown-ordered`)
3. **Chapter info**: Chapter number and abbreviation (e.g., "3, SEC" for Security chapter)

## Workflow Overview

```
1. Read & analyze Gemini analysis
2. Create structure plan (./report/report-analysis/bab-x/bab-x-rencana-struktur.md)
3. Generate CSV mapping from structure plan
4. Execute rename using chapter-organizer.py
5. Validate results
6. Create organizing report (./report/report-analysis/bab-x/bab-x-laporan-organizing.txt)
```

## Step-by-Step Instructions

### Step 1: Read Analysis File

Read the Gemini analysis file provided by user. This file contains:
- Grouping of files by topic/area
- Logical order of presentation
- Relationship between files (e.g., IK with supporting FR)

**Important**: Do NOT add gaps or suggest new sub-chapters. Work only with existing files.

### Step 2: Create Structure Plan

Create file: `./report/report-analysis/bab-x/bab-x-rencana-struktur.md`

**Content structure**:
```markdown
# Rencana Struktur Final Bab X: [CHAPTER NAME]

## STRUKTUR HIERARKI BAB X
[Hierarchical structure tree]

## MAPPING DETAIL: FILE LAMA → FILE BARU

### X.1 [SUB-CHAPTER NAME]
| No | File Lama | File Baru | Keterangan |
|:---|:---|:---|:---|
| 1 | old-file.md | 0X-ABC-X.1.0-TYPE-Description.md | Description |

### X.2 [SUB-CHAPTER NAME]
#### X.2.1 [SUB-SUB-CHAPTER NAME]
| No | File Lama | File Baru | Keterangan |
|:---|:---|:---|:---|
| 2 | old-file2.md | 0X-ABC-X.2.1-A-IK-Description.md | Work Instruction |
| 3 | old-file3.md | 0X-ABC-X.2.1-B-FR-Description.md | Form/Checklist |

[Continue for all sub-chapters...]

## NAMING CONVENTION
Format: 0X-ABC-[X.Y.Z]-[Seq]-[Type]-[Description].md

Components:
- 0X: Chapter number (02, 03, 04, etc.)
- ABC: Chapter abbreviation (HK, SEC, FO, FB, etc.)
- X.Y.Z: Hierarchical numbering (e.g., 2.3.1)
- Seq: Alphabetic sequence (A, B, C...) - IK before FR
- Type: PNGTR, PF, IK, FR
- Description: Short area/function name
```

### Step 3: Generate CSV Mapping

From the structure plan, create CSV file: `./report/report-analysis/bab-x/mapping-bab-x.csv`

**CSV format**:
```csv
old_name,new_name
old-file1.md,0X-ABC-X.1.0-TYPE-Description.md
old-file2.md,0X-ABC-X.2.1-A-IK-Description.md
old-file3.md,0X-ABC-X.2.1-B-FR-Description.md
```

**Important**: Ensure CSV has header row: `old_name,new_name`

### Step 4: Execute Rename Script

Run the chapter organizer script:

```bash
source .venv/bin/activate
python .claude/skills/chapter-organizer/chapter-organizer.py \
  ./report/report-analysis/bab-x/mapping-bab-x.csv \
  ./BUKU-X/0X-CHAPTER/markdown-ordered
```

**No user confirmation needed** - script runs automatically.

### Step 5: Validate Results

After rename completes:
1. Check all files renamed successfully (Success: N/N)
2. Verify sorting order (files should be in hierarchical order)
3. Check log file created in target folder

### Step 6: Create Organizing Report

Create file: `./report/report-analysis/bab-x/bab-x-laporan-organizing.txt`

**Content template**:
```
LAPORAN ORGANIZING BAB X: [CHAPTER NAME]
========================================

Tanggal: [DATE]
Script: .claude/skills/chapter-organizer/chapter-organizer.py
Folder Target: [PATH]

=========================================================
HASIL EKSEKUSI
=========================================================

Status: [SUCCESS/PARTIAL/FAILED]
Total File Diproses: [N]/[N]
Success: [N]
Failed: [N]
Skipped: [N]

Log File: [FILENAME]

=========================================================
VALIDASI HASIL
=========================================================

[Checklist of validations]
✓ Semua file berhasil di-rename
✓ Sorting alfabetik sesuai hirarki
✓ IK muncul sebelum FR
✓ Struktur hierarki tercermin

=========================================================
STATISTIK
=========================================================

[Summary of sub-chapters and file counts]

=========================================================
KESIMPULAN
=========================================================

[Brief conclusion and next steps]
```

## Naming Convention Rules

### Format
```
0X-ABC-[X.Y.Z]-[Seq]-[Type]-[Description].md
```

### Document Types
- **PNGTR**: Pengantar (Introduction) - use X.Y.0 numbering
- **PF**: Prosedur/Pedoman (Procedure) - main policy documents
- **IK**: Instruksi Kerja (Work Instruction) - detailed steps
- **FR**: Formulir (Form/Checklist) - supporting forms

### Sequence Rules
- Use alphabetic sequence (A, B, C...) to control order within sub-sub-chapter
- IK documents always get sequence A
- FR documents get sequence B, C, D... in order of relevance

### Examples
```
02-HK-2.1.0-PNGTR-Housekeeping.md           # Introduction to chapter
02-HK-2.2.1-PF-Prosedur_Akomodasi.md        # Main procedure document
02-HK-2.3.1-A-IK-Pembersihan_Kamar.md       # Work instruction (A = first)
02-HK-2.3.1-B-FR-Checklist_Kamar.md         # Related form (B = after IK)
02-HK-2.7.5-C-FR-Logistik_Permintaan.md     # Additional form (C = third)
```

## Hierarchical Structure Guidelines

### Typical Chapter Structure
```
BAB X: [CHAPTER NAME]
├── X.1 Pengantar Pembahasan (Introduction)
├── X.2 Prosedur Induk (Main Procedures)
├── X.3-X.7 Topik-topik Utama (Main Topics)
│   ├── X.3.1 Sub-topik dengan IK + FR
│   ├── X.3.2 Sub-topik dengan IK + FR
│   └── X.3.3 ...
└── X.8 Sistem Pengelolaan/Dokumentasi (if applicable)
```

### Grouping Principles
1. **Functional grouping**: Group by area/function (e.g., akomodasi, pembelajaran, F&B)
2. **IK-FR pairing**: Keep work instructions with their supporting forms
3. **Logical flow**: Order from general to specific, or by user journey
4. **Consistent depth**: Aim for 2-3 levels (X.Y.Z) maximum

## Important Notes

### What NOT to Do
- ❌ Do not suggest new sub-chapters or gaps
- ❌ Do not add content beyond existing files
- ❌ Do not skip files from the analysis
- ❌ Do not ask for user confirmation during rename (automated process)

### What TO Do
- ✅ Work only with existing files from analysis
- ✅ Follow the naming convention strictly
- ✅ Create complete CSV mapping
- ✅ Validate results after rename
- ✅ Create concise organizing report

### Quality Checks
Before finalizing:
1. All files from analysis are mapped
2. No duplicate new names
3. Hierarchical numbers are sequential (2.1, 2.2, 2.3... not 2.1, 2.3, 2.5)
4. IK always has sequence A, FR has B+
5. CSV has correct header: old_name,new_name

## Troubleshooting

### CSV Loading Error
- Check CSV has header row: `old_name,new_name`
- Ensure no empty rows
- Check file encoding is UTF-8

### Files Not Found
- Verify folder path is correct
- Check old_name matches exact filename
- Ensure files exist before running script

### Rename Failed
- Check file permissions
- Ensure no files are open in editors
- Verify target names are valid (no illegal characters)

## Example Usage

**User request**:
> "Organize the Security chapter files in ./BUKU-3/03-SECURITY-(UPDL-SEMARANG)/markdown-ordered based on analysis at ./report/report-analysis/bab-3/bab-3-security.md. Chapter number is 3, abbreviation is SEC."

**Your response**:
1. Read ./report/report-analysis/bab-3/bab-3-security.md
2. Create ./report/report-analysis/bab-3/bab-3-rencana-struktur.md with hierarchical mapping
3. Generate ./report/report-analysis/bab-3/mapping-bab-3.csv
4. Execute: `python .claude/skills/chapter-organizer/chapter-organizer.py ./report/report-analysis/bab-3/mapping-bab-3.csv ./BUKU-3/03-SECURITY-(UPDL-SEMARANG)/markdown-ordered`
5. Validate results and show sorted file list
6. Create ./report/report-analysis/bab-3/bab-3-laporan-organizing.txt

## Related Files
- **Script**: `.claude/skills/chapter-organizer/chapter-organizer.py`
- **Example structure plan**: `./report/report-analysis/bab-2/bab-2-rencana-struktur-final.md`
- **Example CSV**: Can be generated from structure plan
- **Example report**: `./report/report-analysis/bab-2/bab-2-laporan-organizing.txt`

## Performance Notes
- Typical processing time: < 1 second for 50 files
- CSV generation: Manual process based on structure plan
- Rename is atomic operation (all or nothing per file)

---

**Created by**: Claude Code
**Date**: 19 Januari 2025
**Based on**: Bab 2 HOUSEKEEPING organizing process
**Status**: READY FOR USE
