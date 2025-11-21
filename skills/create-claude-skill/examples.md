# Real Skill Examples

This file contains complete examples from actual skills created in this project, demonstrating different patterns and best practices.

## Table of Contents
1. [Example 1: Script-Based Skill](#example-1-script-based-skill)
2. [Example 2: Script with Helpers](#example-2-script-with-helpers)
3. [Example 3: AI-Only Skill](#example-3-ai-only-skill)
4. [Example 4: Complex Workflow Skill](#example-4-complex-workflow-skill)
5. [Before/After Comparison](#beforeafter-comparison)

## Example 1: Script-Based Skill

### Skill: convert-docx-to-pdf

**Pattern:** Simple script skill with single Python file

**Structure:**
```
convert-docx-to-pdf/
├── SKILL.md              # 18 lines (~50 tokens)
├── reference.md          # 240 lines (comprehensive)
├── README.md             # Original script readme
└── convert-docx-to-pdf.py  # Main script
```

### SKILL.md
```markdown
---
name: convert-docx-to-pdf
description: Converts Microsoft Word (.docx) files to PDF format using LibreOffice/soffice. Supports single file, multiple comma-separated files, or entire folders with test-first safety for batch operations. Activate when user asks to convert Word documents to PDF.
---

# Convert Word Documents to PDF

Converts .docx files to PDF using LibreOffice. Supports single files, multiple files, or batch folder conversion with test-first safety.

## Quick Start

```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py <file|files|folder>
```

**For detailed documentation**, see [reference.md](./reference.md)
**For script details**, see [README.md](./README.md)
```

### reference.md Structure

```markdown
# Convert DOCX to PDF - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Conversion Method](#conversion-method)
3. [Usage Modes](#usage-modes)
4. [Expected Output](#expected-output)
5. [Examples](#examples)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Usage](#advanced-usage)
8. [Performance Notes](#performance-notes)

## When to Use This Skill

Activate this skill when the user requests to:
- Convert .docx files to PDF format
- Transform Word documents to PDF
- Batch convert documents in a folder

[... 230+ more lines of comprehensive documentation ...]
```

### Key Lessons

- **Concise SKILL.md:** Just 18 lines with essential info
- **Comprehensive reference:** 240 lines with full details
- **Clear sections:** Organized for easy navigation
- **Real examples:** Shows actual command syntax
- **Table of contents:** For easy reference navigation

---

## Example 2: Script with Helpers

### Skill: msword-move-citation-before-period

**Pattern:** Main script + helper utilities

**Structure:**
```
msword-move-citation-before-period/
├── SKILL.md                                    # Concise overview
├── reference.md                                # Comprehensive guide
├── README.md                                   # Original readme
├── msword-move-citation-before-period.py       # Main script
└── scripts/                                    # Helper scripts
    ├── debug-citations.py                      # Debug utility
    └── find-all-citations.py                   # Find utility
```

### SKILL.md
```markdown
---
name: msword-move-citation-before-period
description: Moves citation numbers from after periods to before periods in Microsoft Word documents. Transforms "text.[123]" to "text [123]." to comply with academic citation standards. Preserves all formatting. Activate when user asks to fix citation placement or move citations before periods.
---

# Move Citations Before Period in Word Documents

Fixes citation placement by moving citation numbers from after periods to before periods with space, complying with academic standards.

## Quick Start

```bash
source .venv/bin/activate
python .claude/skills/msword-move-citation-before-period/msword-move-citation-before-period.py <input.docx> [output.docx]
```

**For detailed documentation**, see [reference.md](./reference.md)
**For script details**, see [README.md](./README.md)
**Helper scripts**, see [scripts/](./scripts/)
```

### Helper Scripts

**scripts/debug-citations.py:**
- Debug citation patterns
- Helps identify issues
- Not loaded unless referenced

**scripts/find-all-citations.py:**
- Lists all citations in document
- Utility for verification
- Executed when needed

### Key Lessons

- **Helpers in subfolder:** Clean organization
- **Referenced but not loaded:** Progressive disclosure
- **Clear utility purpose:** Each helper has specific role
- **Optional execution:** Only run when user needs them

---

## Example 3: AI-Only Skill

### Skill: sop-editing-content

**Pattern:** Guidance without script execution

**Structure:**
```
sop-editing-content/
├── SKILL.md              # 37 lines (concise)
└── reference.md          # 387 lines (comprehensive)
```

### SKILL.md
```markdown
---
name: sop-editing-content
description: Rules for editing and proofreading SOP content files. Fixes OCR errors, formatting, typos, and standardizes structure. Use when editing book chapter content files (IK, FR, PF documents).
---

# Editing Content - SOP File Proofreading and Formatting

Edits and proofreads content files to ensure they are clean, properly formatted, and ready for conversion to .docx format.

## Quick Reference

- **Fix OCR errors:** Common misrecognitions
- **Standardize formatting:** Consistent structure
- **Apply templates:** IK, FR, PF specific rules
- **Validate content:** Completeness checks

**For detailed editing rules**, see [reference.md](./reference.md)
```

### reference.md Structure

```markdown
# SOP Editing Content - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Document Types](#document-types)
3. [OCR Error Patterns](#ocr-error-patterns)
4. [Formatting Rules](#formatting-rules)
5. [Content Validation](#content-validation)
6. [Examples](#examples)
...

[380+ lines of detailed editing rules, patterns, and examples]
```

### Key Lessons

- **No scripts needed:** Pure guidance skill
- **Still follows pattern:** Concise SKILL.md + detailed reference
- **Organized by sections:** Clear rule categories
- **Real-world examples:** Shows before/after patterns
- **Table of contents:** Essential for long reference

---

## Example 4: Complex Workflow Skill

### Skill: chapter-organizer

**Pattern:** Multi-step orchestration with data files

**Structure:**
```
chapter-organizer/
├── SKILL.md              # Workflow overview
├── reference.md          # Step-by-step details
└── chapter-organizer.py  # Execution script
```

### SKILL.md
```markdown
---
name: chapter-organizer
description: Organizes chapter markdown files into hierarchical structure based on content analysis. Creates structure plan, generates CSV mapping, executes rename, and validates results. Use when user needs to organize book chapter files.
---

# Chapter Organizer

Organizes markdown files into hierarchical structure. Multi-step workflow: analyze → plan → execute → validate.

## Quick Workflow

1. Read analysis file
2. Create structure plan
3. Generate CSV mapping
4. Execute rename script
5. Validate results

**For detailed workflow**, see [reference.md](./reference.md)
```

### reference.md - Workflow Sections

```markdown
# Chapter Organizer - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Prerequisites](#prerequisites)
3. [Workflow Overview](#workflow-overview)
4. [Step-by-Step Instructions](#step-by-step-instructions)
5. [Naming Convention Rules](#naming-convention-rules)
6. [Quality Checks](#quality-checks)
...

## Workflow Overview

```
1. Read & analyze Gemini analysis
2. Create structure plan (./report/.../bab-x-rencana-struktur.md)
3. Generate CSV mapping from structure plan
4. Execute rename using chapter-organizer.py
5. Validate results
6. Create organizing report
```

[Detailed step-by-step instructions for each phase...]
```

### Key Lessons

- **Clear workflow:** Step-by-step process
- **Prerequisites section:** User knows what to provide
- **Quality checks:** Built-in validation
- **No gaps:** Complete process from start to finish
- **Report creation:** Documents what was done

---

## Before/After Comparison

### Before: Monolithic SKILL.md (260 lines)

**Problem:** Everything in one file
```markdown
---
name: convert-docx-to-pdf
description: ...
---

# Convert Word Documents to PDF

## When to Use This Skill
[50 lines]

## Instructions
[80 lines]

### Mode 1: Single File
[30 lines]

### Mode 2: Multiple Files
[30 lines]

### Mode 3: Folder Mode
[40 lines]

## Expected Output
[20 lines]

## Troubleshooting
[30 lines]
```

**Issues:**
- ❌ Loads 260 lines every time skill activates
- ❌ High context usage
- ❌ Difficult to navigate
- ❌ Mixes essential with details

### After: Progressive Disclosure (18 + 240 lines)

**Solution:** Split into concise + detailed

**SKILL.md (18 lines - always loaded):**
```markdown
---
name: convert-docx-to-pdf
description: ...
---

# Convert Word Documents to PDF

Converts .docx files to PDF. Supports single files, multiple files, or folders.

## Quick Start

```bash
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py <file|files|folder>
```

**For detailed documentation**, see [reference.md](./reference.md)
```

**reference.md (240 lines - loaded only when needed):**
```markdown
# Convert DOCX to PDF - Reference Guide

## Table of Contents
[...]

## When to Use This Skill
[...]

## Conversion Method
[...]

[... all the details ...]
```

**Benefits:**
- ✅ Only 18 lines loaded at startup
- ✅ Details loaded only when Claude needs them
- ✅ Easy to navigate with TOC
- ✅ Separates essential from optional

**Context Savings:**
- Before: ~260 lines × 22 skills = 5,720 lines loaded at startup
- After: ~18 lines × 22 skills = 396 lines loaded at startup
- **Savings: 93% reduction in startup context usage**

---

## Pattern Summary

### Pattern 1: Simple Script (14 skills)

**Use when:** Single Python script, straightforward operation

**Example:** convert-docx-to-pdf, sanitize-filenames, convert-pdf-to-markdown

**Files:**
- SKILL.md (~18 lines)
- reference.md (200-300 lines)
- README.md (original)
- script.py

### Pattern 2: Script + Helpers (2 skills)

**Use when:** Main script + utility scripts

**Example:** msword-move-citation-before-period

**Files:**
- SKILL.md (~18 lines)
- reference.md (200-300 lines)
- README.md (original)
- main-script.py
- scripts/ folder with helpers

### Pattern 3: AI-Only (8 skills)

**Use when:** No script execution, guidance only

**Example:** sop-editing-content, sop-deep-editing

**Files:**
- SKILL.md (25-40 lines)
- reference.md (300-500 lines with TOC)

### Pattern 4: Workflow Orchestration (1 skill)

**Use when:** Multi-step process with phases

**Example:** chapter-organizer, sop-improvement-orchestration

**Files:**
- SKILL.md (workflow overview)
- reference.md (step-by-step guide)
- script.py (execution)

---

## Template Usage Guide

See [templates/](./templates/) for:

- `template-script-based.md` - Script-based skill template
- `template-ai-only.md` - AI-only skill template
- `template-reference.md` - Reference file template

Each template includes:
- Complete structure
- Placeholder text
- Section guidelines
- Fill-in-the-blank format

Copy and customize for new skills!
