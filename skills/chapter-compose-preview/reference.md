# Compose Preview - Complete Reference Guide

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Task Overview](#task-overview)
- [Input Provided](#input-provided)
- [Creation Rules](#creation-rules)
  - [File Structure](#1-file-structure)
  - [Heading Format](#2-heading-format)
  - [Language Requirement](#3-language-requirement)
  - [Content Guidelines](#4-content-guidelines)
  - [Reading Strategy](#5-reading-strategy)
  - [Handling Different Document Types](#6-handling-different-document-types)
  - [Generalization Requirement](#7-generalization-requirement)
  - [Writing Style](#8-writing-style)
  - [Example Output](#9-example-output)
- [Quality Checks](#quality-checks)
- [Important Notes](#important-notes)

## When to Use This Skill
Activate when `sub-chapter-previewer` agent needs to create x.x.0 introduction files for book sub-chapters.

## Task Overview
Read the first 15 lines of sibling files (x.x.1, x.x.2, etc.) within a sub-chapter and synthesize an introduction that provides context and overview for that sub-chapter.

## Input Provided
You will receive:
- **Sub-chapter number**: e.g., "2.3"
- **Sub-chapter title**: e.g., "Layanan Akomodasi (Wisma)"
- **List of source files**: e.g., ["02-HK-2.3.1-A-IK-Pembersihan_Kamar.md", "02-HK-2.3.1-B-FR-Checklist_Kamar.md", ...]
- **Target file to create**: e.g., "02-HK-2.3.0-PNGTR-Akomodasi.md"

## Creation Rules

### 1. File Structure
```markdown
## X.Y [Sub-Chapter Title]

[Introduction paragraph 1: Context and importance]

[Introduction paragraph 2: Scope and coverage]

[Introduction paragraph 3: Structure overview - what documents are included]
```

### 2. Heading Format
- Use markdown heading level 2 (`##`)
- Format: `## X.Y [Sub-Chapter Title]`
- Example: `## 2.3 Layanan Akomodasi (Wisma)`

### 3. Language Requirement

**CRITICAL**: All text must be in **FORMAL BAHASA INDONESIA** (formal Indonesian language).

- Use professional, official tone suitable for corporate SOP documentation
- Use proper grammar and formal vocabulary
- Avoid colloquialisms or informal language
- Write as if for official government or corporate documentation

### 4. Content Guidelines

**Paragraph 1 - Context** (2-3 sentences):
- Explain the importance of this sub-chapter area
- Connect to overall chapter objectives
- Provide business/operational context

**Paragraph 2 - Scope** (2-3 sentences):
- Describe what this sub-chapter covers
- Highlight key areas or functions
- Mention who will use these procedures

**Paragraph 3 - Structure** (2-4 sentences):
- Overview of document types included (IK, FR, PF)
- Brief mention of sub-sub-chapters (x.x.1, x.x.2, etc.)
- Reading order or logical flow

### 5. Reading Strategy

For each source file, read **first 15 lines** to understand:
- Document purpose (from TUJUAN section if IK/PF file)
- Scope (from RUANG LINGKUP section if IK/PF file)
- Key topics or areas covered

### 6. Handling Different Document Types

When reading source files:
- **IK (Instruksi Kerja)**: Read purpose, scope, and key procedures
- **FR (Formulir)**: Note that it's a form/checklist, mention its purpose but don't detail table contents
- **PF (Prosedur)**: Read overall procedure objectives and scope

For FR files that are primarily tables, simply mention: "dilengkapi dengan formulir [name] untuk pendataan/pencatatan"

### 7. Generalization Requirement

**CRITICAL**: Make the introduction applicable to ALL units in PLN Corporate University, not just specific units.

**What to Generalize**:
- Replace specific unit names (UPDL Pandaan, Udiklat names) with "PLN Corporate University" or "unit PLN Corporate University"
- Remove or modify references that only apply to one specific unit
- Use universal language applicable to all units under Pusdiklat

**Examples**:
- ❌ "di lingkungan PLN UPDL Pandaan" → ✅ "di lingkungan PLN Corporate University"
- ❌ "di UPDL Pandaan" → ✅ "di unit PLN Corporate University"
- ❌ "peserta diklat di UPDL" → ✅ "peserta diklat"

**Purpose**: These SOPs should serve all units (UPDL and Udiklat) under Pusdiklat, not just the originating unit.

### 8. Writing Style

- **Professional and formal tone** (this is an official SOP document)
- **FORMAL BAHASA INDONESIA** - Use proper, formal Indonesian language throughout
- **Generalized language** - Applicable to all PLN Corporate University units
- **Concise**: Keep total length to 6-10 sentences (3 paragraphs)
- **Avoid repetition**: Don't repeat content already in detail files
- **Focus on overview**: Provide high-level summary, not detailed procedures

### 9. Example Output

```markdown
## 2.3 Layanan Akomodasi (Wisma)

Sub-bab ini membahas standar pelayanan dan kebersihan akomodasi di lingkungan PLN Corporate University. Akomodasi yang bersih, nyaman, dan terawat merupakan faktor kunci dalam menciptakan pengalaman belajar yang optimal bagi peserta diklat. Layanan wisma yang prima mencerminkan profesionalisme PLN Corporate University sebagai pusat pengembangan SDM kelas dunia.

Cakupan layanan akomodasi meliputi pembersihan kamar, pengelolaan laundry, dan sistem pelaporan kerusakan barang. Setiap aspek layanan dirancang untuk memastikan kenyamanan dan keamanan pengguna wisma, baik peserta diklat maupun tamu institusional.

Sub-bab ini terdiri dari tiga bagian utama: (1) Pembersihan Kamar yang mencakup instruksi kerja dan checklist kebersihan, (2) Pengelolaan Laundry untuk linen mess dan pakaian siswa dilengkapi dengan formulir pencatatan, serta (3) Prosedur Pelaporan Kerusakan Barang untuk memastikan pemeliharaan fasilitas yang responsif. Setiap bagian dilengkapi dengan Instruksi Kerja (IK) dan Formulir (FR) pendukung yang siap digunakan.
```

## Quality Checks

Before finalizing the x.x.0 file, verify:
- ✅ Heading uses `##` format with correct numbering
- ✅ Three clear paragraphs (context, scope, structure)
- ✅ **FORMAL BAHASA INDONESIA** used throughout
- ✅ **Generalized language** - no specific unit names (UPDL Pandaan, Udiklat names)
- ✅ Professional Indonesian language
- ✅ No typos or grammatical errors
- ✅ Accurate reflection of sub-chapter content
- ✅ Appropriate length (6-10 sentences total)

## Important Notes

- **Do not copy-paste** from source files - synthesize new content
- **Do not include procedural details** - those belong in IK/FR files
- **Do not add headings beyond level 2** - keep it simple
- **Write for the reader** - assume they're seeing this sub-chapter for the first time
- **Use FORMAL BAHASA INDONESIA** at all times - this is official corporate documentation

---

**Created by**: Claude Code
**Purpose**: Guide sub-chapter-previewer agent
**Status**: READY FOR USE
