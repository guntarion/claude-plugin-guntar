# Editing Content - Complete Reference Guide

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Task Overview](#task-overview)
- [Input Provided](#input-provided)
- [Language Requirement](#language-requirement)
- [Editing Rules](#editing-rules)
  - [1. Add File Title](#1-add-file-title--heading)
  - [2. Convert Roman Numerals to Alphabetic Headings](#2-convert-roman-numerals-to-alphabetic-headings)
  - [3. Fix OCR Errors](#3-fix-ocr-errors)
  - [4. Mark Foreign Terms with Italic](#4-mark-foreign-terms-with-italic)
  - [5. Fix Typos and Grammar](#5-fix-typos-and-grammar)
  - [6. Generalize Unit-Specific References](#6-generalize-unit-specific-references-critical)
  - [7. Improve Clarity](#7-improve-clarity-minimal-additions)
  - [8. Fix Bullet Points and Numbering](#8-fix-bullet-points-and-numbering)
- [Handling FR (Formulir) Files](#handling-fr-formulir-files)
- [Editing Workflow](#editing-workflow)
- [Quality Checks](#quality-checks)
- [Important Notes](#important-notes)

## When to Use This Skill
Activate when `sub-chapter-editor` agent needs to edit content files for book chapters.

## Task Overview
Edit and proofread content files to ensure they are clean, properly formatted, and ready for conversion to .docx format.

## Input Provided
You will receive:
- **File(s) to edit**: One or more markdown files
- **File location**: Full path to the file(s)

## Language Requirement

**CRITICAL**: All text must be in **FORMAL BAHASA INDONESIA** (formal Indonesian language). Maintain professional, official tone suitable for corporate SOP documentation.

## Editing Rules

### 1. Add File Title (### Heading)

**Rule**: Every file must start with a level 3 heading that includes the chapter notation and descriptive title.

**Format**: `### X.Y.Z [Title with Proper Capitalization]`

**Examples**:
- `### 2.2.1 Prosedur Pembersihan Kamar`
- `### 2.3.1 Instruksi Kerja Pembersihan Kamar`
- `### 2.4.2 Checklist Kebersihan Laboratorium`

**Capitalization Rule**: Capitalize first letter of each significant word (title case)
- Capitalize: Prosedur, Pembersihan, Kamar, Instruksi, Kerja
- Lowercase: dan, di, untuk, yang, dari (unless first word)

**Where to add**: At the very beginning of the file, before any other content.

**Note for FR (Formulir/Form) Files**:
If the file is primarily a table/form with no prose sections, still add the file title but skip the Roman numeral conversion (forms typically don't have I, II, III sections).

---

### 2. Convert Roman Numerals to Alphabetic Headings

**IMPORTANT**: This rule applies to IK (Instruksi Kerja) and PF (Prosedur) files. FR (Formulir) files that are pure tables may not have these sections - skip if not applicable.

**Rule**: All section headings using Roman numerals (I, II, III, IV, V, etc.) must be converted to alphabetic letters (A, B, C, D, E, etc.) and formatted as level 4 headings.

**Pattern to find**:
- `I. **TUJUAN**`
- `II. **RUANG LINGKUP**`
- `III. **REFERENSI**`
- `IV. ISTILAH DAN DEFINISI`
- `V. **PERLENGKAPAN KERJA**`
- `VI. **LANGKAH KERJA**`
- etc.

**Convert to**:
- `#### A. Tujuan`
- `#### B. Ruang Lingkup`
- `#### C. Referensi`
- `#### D. Istilah dan Definisi`
- `#### E. Perlengkapan Kerja`
- `#### F. Langkah Kerja`

**Conversion Table**:
```
I   → A
II  → B
III → C
IV  → D
V   → E
VI  → F
VII → G
VIII→ H
IX  → I
X   → J
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
| Error Pattern | Correct Form | Example |
|---------------|--------------|---------|
| `=` in words | appropriate letter | penda=aran → pendaftaran |
| `>` in words | appropriate letter | menempa> → menempati |
| `?` in words | appropriate letter | veri?kasi → verifikasi |
| `<` in words | appropriate letter | pen<ng → penting |
| Missing letters | add missing letters | buk> → bukti |
| `0` instead of `O` | use letter O | 0perasi → Operasi |
| `1` instead of `I` | use letter I | 1nstruksi → Instruksi |

**Strategy**:
1. Read sentences carefully for context
2. Identify words that make no sense
3. Infer correct word from context
4. Replace with proper Indonesian word
5. Verify grammar and meaning

**Example Fixes**:
- ❌ "proses penda=aran tamu" → ✅ "proses pendaftaran tamu"
- ❌ "menempa> kamar" → ✅ "menempati kamar"
- ❌ "veri?kasi data" → ✅ "verifikasi data"
- ❌ "pen>ng untuk" → ✅ "penting untuk"
- ❌ "LOUNDRY" → ✅ "LAUNDRY"
- ❌ "UDPL" → ✅ "UPDL"

---

### 4. Mark Foreign Terms with Italic

**Rule**: All foreign (non-Indonesian) terms must be italicized using markdown italic syntax.

**How to mark**: Surround term with underscores `_term_` or asterisks `*term*`

**Common Foreign Terms in SOP Context**:
- _Check-in_
- _Check-out_
- _Checklist_
- _Exhaust fan_
- _Hand dryer_
- _Refrigerator_
- _Receptionist_
- _Lobby_
- _Security_
- _Driver_
- _Pantry_
- _Meeting room_
- _Front office_
- _Back office_
- _Housekeeping_

**Note**: Some terms may already be italicized - leave them as is.

---

### 5. Fix Typos and Grammar

**Rule**: Correct spelling mistakes and grammatical errors.

**Common Typos**:
- Extra spaces between words
- Missing spaces after punctuation
- Inconsistent spacing around bullet points
- Misspelled Indonesian words

**Grammar Checks**:
- Subject-verb agreement
- Proper use of imbuhan (affixes)
- Consistent tense usage
- Proper punctuation

**Example**:
- ❌ "Petugas  kebersihan harus" (double space) → ✅ "Petugas kebersihan harus"
- ❌ "mem-bersihkan" (wrong affix) → ✅ "membersihkan"

---

### 6. Generalize Unit-Specific References (CRITICAL)

**Rule**: Remove specific unit designations (UPDL Pandaan, Udiklat names, etc.) and make the SOP applicable to all units in PLN Corporate University.

**Purpose**: These SOPs originated from specific units (Udiklat or UPDL) under Pusdiklat, but should be generalized to apply across all units in PLN Corporate University.

**What to Generalize**:
- Replace specific unit names with generic references
- Remove clauses that only apply to one specific unit
- Modify location-specific details to be universally applicable

**Common Replacements**:
| Specific Reference | Generalized Version |
|-------------------|---------------------|
| "PLN UPDL Pandaan" | "PLN Corporate University" or "unit PLN Corporate University" |
| "di lingkungan PLN UPDL Pandaan" | "di lingkungan PLN Corporate University" |
| "UPDL Pandaan" | "unit" or "PLN Corporate University" |
| "Udiklat [specific name]" | "unit PLN Corporate University" |
| "di UPDL" | "di unit PLN Corporate University" |
| "Asman Pelayanan dan Keuangan" | "Asisten Manajer terkait" or keep if universally applicable |

**Examples**:

❌ **Specific (Before)**:
> "Pedoman ini disusun untuk memastikan kebersihan di PLN UPDL Pandaan."

✅ **Generalized (After)**:
> "Pedoman ini disusun untuk memastikan kebersihan di seluruh unit PLN Corporate University."

❌ **Specific (Before)**:
> "Instruksi kerja ini berlaku untuk seluruh kegiatan pembersihan kamar wisma di UPDL Pandaan."

✅ **Generalized (After)**:
> "Instruksi kerja ini berlaku untuk seluruh kegiatan pembersihan kamar wisma di unit PLN Corporate University."

**When to Generalize**:
- Geographic/location-specific mentions
- Specific organizational unit names
- Procedures that seem unit-specific but can apply universally

**When NOT to Generalize**:
- "PLN Corporate University" (this is already the general entity)
- Technical procedures that are truly universal
- Job titles that are standardized across all units
- Equipment or facility names that are generic

**Strategy**:
1. Scan for specific unit names (UPDL, Udiklat, location names)
2. Evaluate if the reference is unit-specific or universal
3. Replace with generic reference if needed
4. Ensure the modified sentence still makes sense
5. Verify the SOP remains applicable to all units

**Important**: If a clause or procedure seems impossible to generalize (truly only applicable to one unit), note it but attempt to modify for broader applicability. In rare cases, such content may need to be removed.

---

### 7. Improve Clarity (Minimal Additions)

**Rule**: Add clarifying words ONLY when absolutely necessary to make sentence understandable.

**When to add**:
- Missing verbs that make sentence incomplete
- Missing subjects that create ambiguity
- Missing articles (yang, dari, di) needed for clarity

**When NOT to add**:
- Don't expand SOP procedures (they are already standardized)
- Don't add explanatory notes or comments
- Don't change technical terminology
- Don't add extra examples

**Example**:
- ❌ "Petugas melakukan" (incomplete) → ✅ "Petugas melakukan pembersihan"
- ✅ "Pastikan ruangan bersih" (complete) → ✅ Keep as is

---

### 8. Fix Bullet Points and Numbering

**Rule**: Ensure consistent formatting for lists.

**Bullet Point Format**:
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
```

**Common Issues to Fix**:
- Inconsistent bullet characters (mixing `-`, `*`, `•`)
- Improper indentation
- Missing spaces after bullet/number
- Broken numbering sequence

---

## Handling FR (Formulir) Files

**Special Considerations for Table-Based Forms**:

FR files are often pure tables/forms with minimal prose. For these files:

1. **Add file title** as usual: `### X.Y.Z [Form Name]`
2. **Fix typos in table headers and content** (e.g., LOUNDRY → LAUNDRY)
3. **Clean table formatting** if needed (proper alignment, spacing)
4. **DON'T try to convert Roman numerals** (forms don't have I, II, III sections)
5. **DON'T add prose content** - forms are meant to be tables
6. **Maintain table structure** - don't try to convert tables to prose

**Example FR File**: A laundry form with columns for item, unit, quantity is perfectly fine as-is. Just add title and fix typos.

## Editing Workflow

### Step 1: Read Entire File
- Understand document type (IK, FR, PF)
- Identify structure and sections
- Note overall content and purpose
- **If FR (form)**: Check if it's table-based or has prose sections

### Step 2: Add File Title
- Add `### X.Y.Z Title` at the very top
- Ensure proper capitalization

### Step 3: Convert Section Headings
- Find all Roman numeral headings
- Convert to alphabetic with `####` format
- Update capitalization
- **Skip for FR (form) files** that are pure tables

### Step 4: Fix Content Issues
- Scan for OCR errors
- Correct typos
- Italicize foreign terms
- **Generalize unit-specific references** (CRITICAL - remove "UPDL Pandaan", "Udiklat" specifics)
- Fix bullet points/numbering
- Add minimal clarifications if needed

### Step 5: Final Review
- Read through edited file
- Verify all changes make sense
- Check formatting consistency
- Ensure no new errors introduced
- Verify **FORMAL BAHASA INDONESIA** is used throughout

---

## Quality Checks

Before completing edits, verify:
- ✅ File has `### X.Y.Z Title` heading
- ✅ All Roman numerals converted to A, B, C, etc. with `####` (except FR forms)
- ✅ No obvious OCR errors remaining
- ✅ Foreign terms are italicized
- ✅ **Unit-specific references generalized** (no "UPDL Pandaan", "Udiklat" specifics)
- ✅ No typos or grammar errors
- ✅ Bullet points and numbering are consistent
- ✅ Content reads naturally and clearly
- ✅ **FORMAL BAHASA INDONESIA** used throughout

---

## Important Notes

### What NOT to Do
- ❌ Don't change technical procedures or SOP content
- ❌ Don't add explanatory text beyond minimal clarification
- ❌ Don't remove content (unless it's obvious duplication/error)
- ❌ Don't change document structure (order of sections)
- ❌ Don't translate foreign terms to Indonesian
- ❌ Don't add Roman numeral conversions to pure table/form files

### What TO Do
- ✅ Focus on formatting and readability
- ✅ Fix errors that impede understanding
- ✅ Maintain professional SOP tone
- ✅ Preserve technical accuracy
- ✅ Apply changes consistently across file
- ✅ Use **FORMAL BAHASA INDONESIA** at all times
- ✅ Treat FR (form) files differently from IK/PF files

---

**Created by**: Claude Code
**Purpose**: Guide sub-chapter-editor agent
**Status**: READY FOR USE
