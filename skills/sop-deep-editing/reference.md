# SOP Editing - Complete Reference Guide

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Task Overview](#task-overview)
- [Input Provided](#input-provided)
- [Language Requirement](#language-requirement)
- [Editing Rules](#editing-rules)
  - [1. Add File Title](#1-add-file-title--heading)
  - [2. Convert Section Headings](#2-convert-section-headings-roman--alphabetic)
  - [3. Fix OCR Errors](#3-fix-ocr-errors)
  - [4. Italicize Foreign Terms](#4-italicize-foreign-terms)
  - [5. Fix Typos and Grammar](#5-fix-typos-and-grammar)
  - [6. Fix Bullet Points and Numbering](#6-fix-bullet-points-and-numbering)
  - [7. Special Handling for Document Types](#7-special-handling-for-document-types)
- [Editing Workflow](#editing-workflow)
- [Quality Checklist](#quality-checklist)
- [What NOT to Do](#what-not-to-do)
- [What TO Do](#what-to-do)
- [Reporting Back](#reporting-back)

## When to Use This Skill
Activate when `sop-editor` agent needs to edit and format SOP documents.

## Task Overview
Edit and format SOP documents to ensure consistency, fix errors, and apply standard markdown formatting rules.

## Input Provided
You will receive from chapter-composer:
- **Document path**: File to edit in 0B-improved-sop/
- **Document type**: IK, PF, FR, BP, PNGTR

## Language Requirement

**CRITICAL**: All text must be in **FORMAL BAHASA INDONESIA** (formal Indonesian language). Maintain professional, official tone throughout.

---

## Editing Rules

### 1. Add File Title (### Heading)

**Rule**: Every file must start with a level 3 heading that includes the hierarchical notation and descriptive title.

**Format**: `### X.Y.Z [Title with Proper Capitalization]`

**Capitalization Rule**: Capitalize first letter of each significant word (title case)
- Capitalize: Main nouns, verbs, adjectives
- Lowercase: dan, di, untuk, yang, dari, ke, oleh (unless first word)

**Examples** (generic for various SOPs):
```markdown
### 14.3.1 Prosedur Sirkulasi Peminjaman Bahan Pustaka
### 2.4.2 Instruksi Kerja Pembersihan Ruang Kelas
### 5.2.1 Prosedur Keamanan dan Akses Kontrol
### 8.3.2 Pengelolaan Sistem Pembelajaran Hybrid
### 11.4.1 Layanan Konsumsi dan Katering
```

**Where to add**: At the very beginning of the file, before any other content.

**Special Cases**:
- Introduction files (PNGTR): Use `## X.Y [Title]` (level 2, not level 3)
- Business Process files: Use `### X.Y.Z [Process Name]`

---

### 2. Convert Section Headings (Roman → Alphabetic)

**Rule**: All section headings using Roman numerals must be converted to alphabetic letters and formatted as level 4 headings.

**IMPORTANT**: This rule applies to IK, PF, and SOP files. FR (Formulir) files that are pure tables may not have these sections - skip if not applicable. BP (Business Process) files use narrative format - skip.

**Patterns to Find**:
```
I. **TUJUAN** or I. TUJUAN or **I. TUJUAN**
II. **RUANG LINGKUP**
III. **REFERENSI** or III. **DASAR HUKUM**
IV. **ISTILAH DAN DEFINISI** or IV. DEFINISI
V. **PERLENGKAPAN KERJA** or V. **PERALATAN KERJA**
VI. **PERALATAN K3**
VII. **MATERIAL**
VIII. **LANGKAH KERJA** or VIII. **URAIAN KEGIATAN** or VIII. **PROSEDUR**
```

**Convert To**:
```markdown
#### A. Tujuan
#### B. Ruang Lingkup
#### C. Referensi
#### D. Istilah dan Definisi
#### E. Perlengkapan Kerja
#### F. Peralatan K3
#### G. Material
#### H. Langkah Kerja dan Tindakan
```

**Conversion Table**:
```
I    → A
II   → B
III  → C
IV   → D
V    → E
VI   → F
VII  → G
VIII → H
IX   → I
X    → J
XI   → K
XII  → L
```

**Formatting Rules**:
- Use level 4 heading: `####`
- Capitalize first letter only: "Tujuan" not "TUJUAN"
- Remove bold formatting from heading text
- Keep proper spacing after heading

---

### 3. Fix OCR Errors

**Rule**: Identify and fix common OCR errors from PDF-to-markdown conversion.

**Common Error Patterns**:

| Error Type | Pattern | Example | Correction |
|------------|---------|---------|------------|
| Equals in word | `=` mid-word | penda=aran | pendaftaran |
| Greater than | `>` mid-word | menempa> | menempati |
| Less than | `<` mid-word | pen<ng | penting |
| Question mark | `?` mid-word | veri?kasi | verifikasi |
| Vertical bar | `\|` mid-word | men\|adi | menjadi |
| Wrong letter | `0` for `O` | 0perasi | Operasi |
| Wrong letter | `1` for `I` | 1nstruksi | Instruksi |
| Missing letter | truncated | buk> | bukti |

**Specific Common Errors** (fix on sight):
- LOUNDRY → LAUNDRY
- UDPL → UPDL (unless correct context)
- pda → pada
- di-nput → diinput or di-input
- memberi-kan → memberikan
- PANGADAAN → PENGADAAN
- Perpusta-kaan → Perpustakaan

**Strategy**:
1. Read sentences carefully for context
2. Identify words that make no sense
3. Infer correct word from context
4. Replace with proper Indonesian word
5. Verify grammar and meaning
6. Fix or Rewrite broken sentences with forced line-break

---

### 4. Italicize Foreign Terms

**Rule**: All foreign (non-Indonesian) terms must be italicized using markdown italic syntax.

**How to Mark**: Surround term with underscores `_term_` or asterisks `*term*`

**Common Foreign Terms** (in SOP context):

**General Office/Admin**:
- _Check-in_, _Check-out_, _Checklist_
- _Email_, _Online_, _Software_
- _Database_, _Password_, _Username_
- _Login_, _Logout_

**Housekeeping/Facilities**:
- _Housekeeping_, _Lobby_, _Pantry_
- _Toilet_, _Exhaust fan_, _Hand dryer_, _Tissue_

**Food & Beverage**:
- _Catering_, _Buffet_, _Menu_, _Snack_

**Technology/Learning**:
- _E-learning_, _Hybrid learning_
- _Meeting room_, _Projector_
- _Zoom_, _Webinar_

**Security/Safety**:
- _CCTV_, _Access card_, _Security_, _Alarm_

**Library/Documentation**:
- _Scanning_, _Barcode_, _Database_

**Accommodation**:
- _Receptionist_, _Front office_, _Back office_
- _Laundry_, _Linen_

---

### 5. Fix Typos and Grammar

**Rule**: Correct spelling mistakes and grammatical errors.

**Common Typo Categories**:

**1. Extra Spaces**:
- ❌ "Petugas  kebersihan" (double space) → ✅ "Petugas kebersihan"
- ❌ "proses    administrasi" → ✅ "proses administrasi"

**2. Missing Spaces**:
- ❌ "Petugasmelakukan" → ✅ "Petugas melakukan"
- ❌ "di-lakukan" → ✅ "dilakukan" (unless intentional hyphenation)

**3. Wrong Affixes** (imbuhan):
- ❌ "mem-bersihkan" → ✅ "membersihkan"
- ❌ "pem-buatan" → ✅ "pembuatan"
- ❌ "di bersihkan" → ✅ "dibersihkan"

**4. Punctuation**:
- Missing spaces after punctuation: "keamanan,kebersihan" → "keamanan, kebersihan"
- Multiple punctuation: "...!!" → "..."

**Grammar Checks**:
- Subject-verb agreement
- Proper use of imbuhan (me-, di-, pe-, etc.)
- Consistent tense usage
- Proper use of yang, di, ke, dari

---

### 6. Fix Bullet Points and Numbering

**Rule**: Ensure consistent formatting for lists.

**Bullet Point Format** (markdown):
```markdown
- Item 1
- Item 2
- Item 3
```

**Numbered List Format**:
```markdown
1. First step
2. Second step
3. Third step
```

**Sub-list Format**:
```markdown
1. Main item
   - Sub-item 1
   - Sub-item 2
2. Next main item
   - Sub-item A
   - Sub-item B
```

**Common Issues to Fix**:

**1. Inconsistent Bullet Characters**:
```markdown
Before:
* Item 1
- Item 2
• Item 3

After:
- Item 1
- Item 2
- Item 3
```

**2. Improper Indentation**:
```markdown
Before:
1. Main item
- Sub-item (wrong indentation)

After:
1. Main item
   - Sub-item (3 spaces indent)
```

**3. Missing Spaces**:
```markdown
Before:
-Item 1 (no space after dash)

After:
- Item 1 (space after dash)
```

**4. Broken Numbering**:
```markdown
Before:
1. First
2. Second
4. Third (should be 3)

After:
1. First
2. Second
3. Third
```

---

### 7. Special Handling for Document Types

#### FR (Formulir/Form) Files

**Characteristics**:
- Primarily tables and checklists
- May have minimal prose
- Forms for data collection

**Special Rules**:
1. **Add file title** as usual: `### X.Y.Z [Form Name]`
2. **Fix typos in table headers and content**
3. **Clean table formatting** if needed
4. **DON'T convert Roman numerals** (forms don't have I, II, III sections)
5. **DON'T add prose content** - forms are meant to be tables
6. **Maintain table structure** - don't try to convert tables to prose

#### BP (Business Process) Files

**Characteristics**:
- Narrative format
- Explains workflow and roles
- No A-H sections

**Special Rules**:
1. **Add file title**: `### X.Y.Z [Process Name]`
2. **Fix OCR errors and typos** in narrative
3. **Italicize foreign terms**
4. **DON'T try to add A-H headings** (narrative format is correct)
5. **Fix paragraph formatting**

#### PNGTR (Pengantar/Introduction) Files

**Characteristics**:
- Introduction to sub-chapter
- Usually 3-4 paragraphs
- Uses `##` heading (level 2)

**Special Rules**:
1. **Heading format**: `## X.Y [Sub-Chapter Title]` (level 2, not 3)
2. **No A-H sections** (intro files don't have structured sections)
3. **Fix formatting in paragraphs**
4. **Ensure formal Bahasa Indonesia**

---

## Editing Workflow

### Step 1: Read Entire File
- Understand document type (IK, PF, FR, BP, PNGTR)
- Identify current structure
- Note obvious issues

### Step 2: Add/Verify File Title
- Check if file has proper title heading
- Add if missing: `### X.Y.Z Title` (or `##` for PNGTR)
- Ensure proper capitalization

### Step 3: Convert Section Headings (if applicable)
- Find all Roman numeral headings (I, II, III, etc.)
- Convert to alphabetic with `####` format
- Update capitalization
- **Skip** for FR (form) files that are pure tables
- **Skip** for BP (business process) narrative files
- **Skip** for PNGTR (introduction) files

### Step 4: Fix Content Issues
- Scan for OCR error patterns
- Correct typos and spelling
- Italicize foreign terms
- Fix grammar issues
- Clean up spacing

### Step 5: Fix List Formatting
- Standardize bullet points (use `-`)
- Fix numbering sequences
- Correct indentation
- Add missing spaces

### Step 6: Final Review
- Read through edited file
- Verify all changes make sense
- Check formatting consistency
- Ensure no new errors introduced
- Verify **FORMAL BAHASA INDONESIA** maintained

---

## Quality Checklist

Before completing edits, verify:

### Heading and Structure
- ✅ File has proper title: `### X.Y.Z Title` (or `##` for PNGTR)
- ✅ Section headings use `####` with A, B, C... (if IK/PF/SOP)
- ✅ Proper capitalization applied
- ✅ No Roman numerals remain (except in specific contexts like "Tahap III" which is part of content)

### Error Correction
- ✅ No obvious OCR errors remaining
- ✅ Typos corrected
- ✅ Grammar checked
- ✅ Spacing fixed

### Formatting
- ✅ Foreign terms italicized
- ✅ Bullet points consistent (use `-`)
- ✅ Numbering sequences correct
- ✅ Proper indentation
- ✅ Markdown syntax valid

### Language
- ✅ **FORMAL BAHASA INDONESIA** maintained
- ✅ Professional tone preserved
- ✅ No informal language introduced

### Document Type Specific
- ✅ FR (forms): Tables maintained, no prose added
- ✅ BP (business process): Narrative format preserved
- ✅ PNGTR (intro): Level 2 heading used

---

## What NOT to Do

❌ **Don't change content meaning**: Only fix format and errors
❌ **Don't add new content**: Not your job (sop-content-improver does that)
❌ **Don't remove content**: Unless obvious duplication error
❌ **Don't change document structure**: Order of sections should remain
❌ **Don't translate foreign terms**: Italicize them, don't replace
❌ **Don't change technical procedures**: Even if wording seems odd, preserve meaning
❌ **Don't add section headings to forms**: FR files with tables don't need A-H structure
❌ **Don't convert tables to prose**: Maintain table format

---

## What TO Do

✅ **Focus on formatting and readability**: Make documents look professional
✅ **Fix errors that impede understanding**: OCR errors, typos, broken formatting
✅ **Apply standards consistently**: Same rules across all files
✅ **Maintain professional tone**: Keep formal Bahasa Indonesia
✅ **Preserve technical accuracy**: Don't change procedures, just format
✅ **Treat document types differently**: FR, BP, PNGTR have special rules
✅ **Edit in place**: Save changes to the same file

---

## Reporting Back

After completing edits, report to chapter-composer:

```
File edited: [filename]

Edits completed:
- File title: [added/verified]
- Section headings: [converted/skipped - document type]
- OCR errors fixed: [count] instances
- Typos corrected: [count if significant]
- Foreign terms italicized: [count if significant]
- List formatting: [fixed/verified]
- Status: Complete
```

**Special Cases**:
```
File edited: [FR form filename]

Edits completed:
- File title: added
- Table formatting: cleaned
- Typos in table: [count] fixed
- Note: Form file - no section heading conversion needed
- Status: Complete
```

---

**Created by**: Claude Code
**Purpose**: Guide sop-editor agent
**Status**: READY FOR USE
