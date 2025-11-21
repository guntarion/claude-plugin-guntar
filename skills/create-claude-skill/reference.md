# Create Claude Code Skills - Comprehensive Reference

## Table of Contents
1. [Overview](#overview)
2. [Skill Types](#skill-types)
3. [Naming Conventions](#naming-conventions)
4. [Folder Structure](#folder-structure)
5. [SKILL.md Guidelines](#skillmd-guidelines)
6. [Progressive Disclosure](#progressive-disclosure)
7. [Reference File Organization](#reference-file-organization)
8. [Script-Based Skills](#script-based-skills)
9. [AI-Only Skills](#ai-only-skills)
10. [Best Practices Summary](#best-practices-summary)
11. [Common Patterns](#common-patterns)
12. [Quality Checklist](#quality-checklist)

## Overview

Claude Code skills are modular capabilities that help Claude perform specific tasks. Well-designed skills follow the principle of **progressive disclosure**: show essential information upfront, load details only when needed.

### Key Principle

**"The context window is a public good"** - Keep SKILL.md concise to minimize context usage. Assume Claude knows general concepts; only provide skill-specific details.

## Skill Types

### 1. Script-Based Skills

Skills that execute Python scripts or other utilities.

**Examples:**
- `msword-format-table` - Format tables in Word documents
- `convert-docx-to-pdf` - Convert Word to PDF
- `msword-italicize-english-terms` - Italicize English terms

**Structure:**
```
skill-name/
├── SKILL.md              # Concise overview (~50 tokens)
├── reference.md          # Comprehensive documentation
├── README.md             # Original script readme
├── skill-name.py         # Main script (no numbering)
└── scripts/              # Helper scripts (optional)
    ├── helper1.py
    └── helper2.py
```

### 2. AI-Only Skills

Skills that provide guidance without executing scripts.

**Examples:**
- `sop-editing-content` - Rules for editing SOP files
- `sop-deep-editing` - Deep editing guidelines
- `narrate-business-process` - Process narration guide

**Structure:**
```
skill-name/
├── SKILL.md              # Concise overview (~50 tokens)
└── reference.md          # Comprehensive documentation with TOC
```

## Naming Conventions

### Skill Name Format

Use **gerund form** (verb + -ing) for skill names:
- ✅ `processing-pdfs`
- ✅ `analyzing-spreadsheets`
- ✅ `creating-reports`
- ❌ `pdf-processor`
- ❌ `analyze`

### Prefixes

Use domain prefixes for clarity:
- `msword-*` - Microsoft Word operations
- `pdf-*` - PDF operations
- `convert-*` - Conversion operations
- `sop-*` - SOP-specific operations
- `chapter-*` - Chapter/book operations

**Examples:**
- `msword-format-table`
- `pdf-split-pages`
- `convert-docx-to-pdf`
- `sop-editing-content`

### Character Limits

- **Name:** Max 64 characters, lowercase letters, numbers, hyphens only
- **Description:** Max 1024 characters

## Folder Structure

### Location Options

**Personal Skills:** `~/.claude/skills/`
- For individual workflows
- Not version controlled

**Project Skills:** `.claude/skills/` within projects
- Team shared
- Version controlled
- Recommended for project-specific skills

### Multi-File Structure

**Basic (AI-only):**
```
skill-name/
├── SKILL.md
└── reference.md
```

**Script-based:**
```
skill-name/
├── SKILL.md
├── reference.md
├── README.md
└── skill-name.py
```

**Advanced (with helpers):**
```
skill-name/
├── SKILL.md
├── reference.md
├── README.md
├── skill-name.py
├── scripts/
│   ├── helper1.py
│   └── helper2.py
└── templates/
    └── template.txt
```

## SKILL.md Guidelines

### Frontmatter (Required)

```yaml
---
name: skill-name
description: Brief description (max 1024 chars). Include what it does AND when to use it. Use specific trigger keywords.
---
```

### Content Structure

**Keep to ~50 tokens total:**

```markdown
# [Skill Title]

[One sentence summary]

## Quick Start

[Brief usage or key steps - 3-5 bullet points]

**For detailed documentation**, see [reference.md](./reference.md)
**For examples**, see [examples.md](./examples.md) [if exists]
**For script details**, see [README.md](./README.md) [if exists]
```

### Description Best Practices

**Include both:**
1. **What it does:** The capability
2. **When to use:** Trigger conditions

**Examples:**

✅ **Good:**
```yaml
description: Converts Microsoft Word (.docx) files to PDF format using LibreOffice. Supports single file, multiple files, or folders. Activate when user asks to convert Word documents to PDF.
```

❌ **Bad:**
```yaml
description: Converts documents.
```

**Use specific trigger keywords:**
- "convert Word documents"
- "format tables"
- "italicize English terms"
- "edit SOP content"

## Progressive Disclosure

### The Pattern

1. **SKILL.md (loads at startup):** Minimal, ~50 tokens
2. **reference.md (loads when needed):** Full details
3. **Additional files (loads if referenced):** Examples, scripts, templates

### Example: convert-docx-to-pdf

**SKILL.md (~50 tokens):**
```markdown
---
name: convert-docx-to-pdf
description: Converts Microsoft Word (.docx) files to PDF format...
---

# Convert Word Documents to PDF

Converts .docx files to PDF using LibreOffice. Supports single files,
multiple files, or batch folder conversion with test-first safety.

## Quick Start

```bash
source .venv/bin/activate
python .claude/skills/convert-docx-to-pdf/convert-docx-to-pdf.py <file|files|folder>
```

**For detailed documentation**, see [reference.md](./reference.md)
```

**reference.md (detailed):**
- Full usage instructions
- All input modes
- Examples
- Troubleshooting
- 200+ lines of comprehensive documentation

### Reference File Structure

**For files >100 lines, add table of contents:**

```markdown
# Skill Name - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Features](#features)
3. [Usage](#usage)
4. [Examples](#examples)
5. [Troubleshooting](#troubleshooting)
...

## When to Use This Skill

[Content]

## Features

[Content]
```

### Keep References One Level Deep

**✅ Good (one level):**
```
SKILL.md
  → reference.md
  → examples.md
  → README.md
```

**❌ Bad (nested references):**
```
SKILL.md
  → reference.md
      → advanced.md
          → details.md
```

## Reference File Organization

### Recommended Sections

1. **When to Use This Skill**
2. **Features** or **Operations**
3. **Usage** (with examples)
4. **How It Works**
5. **Examples** (practical use cases)
6. **What Gets Modified/Preserved**
7. **Limitations**
8. **Troubleshooting**
9. **Tips**
10. **Related Skills**
11. **Dependencies**
12. **Performance Notes**

### Section Guidelines

**When to Use This Skill:**
- List trigger conditions
- Be specific about use cases

**Features:**
- Bullet points
- Highlight key capabilities

**Usage:**
- Show command syntax
- Provide concrete examples
- Include different modes/options

**Examples:**
- Real-world scenarios
- Show expected output
- Include edge cases

**Troubleshooting:**
- Common errors
- Solutions
- Validation steps

## Script-Based Skills

### Creating from Existing Script

**Steps:**

1. **Create skill folder:**
   ```bash
   mkdir -p .claude/skills/skill-name/scripts
   ```

2. **Copy script (remove numbering):**
   ```bash
   cp python_scripts/25-script-name.py .claude/skills/skill-name/skill-name.py
   ```

3. **Copy readme:**
   ```bash
   cp python_scripts/25-script-name_readme.md .claude/skills/skill-name/README.md
   ```

4. **Copy helper scripts (if any):**
   ```bash
   cp python_scripts/helper.py .claude/skills/skill-name/scripts/
   ```

5. **Create concise SKILL.md**

6. **Create comprehensive reference.md**

7. **Update paths in all files:**
   - Change `python_scripts/NN-script.py`
   - To `.claude/skills/skill-name/skill-name.py`

### Script Path Updates

**Before:**
```bash
python python_scripts/25-italicize-english-terms.py <input>
```

**After:**
```bash
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py <input>
```

## AI-Only Skills

### When to Create AI-Only Skills

- Provide guidance/rules (no script execution)
- Complex multi-step workflows
- Editing/formatting guidelines
- Process orchestration

### Structure for AI-Only Skills

**If under 100 lines total:**
- Single SKILL.md with all content

**If over 100 lines:**
- Concise SKILL.md (~50 tokens)
- Comprehensive reference.md with TOC

### Example: sop-editing-content

```markdown
---
name: sop-editing-content
description: Rules for editing and proofreading SOP content files...
---

# Editing Content - SOP File Proofreading

Edits and proofreads content files to ensure they are clean,
properly formatted, and ready for conversion.

## Quick Reference

- Fix OCR errors
- Standardize formatting
- Apply consistent structure

**For detailed rules**, see [reference.md](./reference.md)
```

## Best Practices Summary

### From Official Documentation

1. **Conciseness is key:** SKILL.md under 500 lines (ideally ~50 tokens)
2. **Progressive disclosure:** Point to detailed materials as needed
3. **Specific descriptions:** Include both what and when
4. **Use gerund names:** `processing-pdfs` not `pdf-processor`
5. **One level deep:** All references link directly from SKILL.md
6. **Table of contents:** For reference files >100 lines
7. **Focused skills:** One capability per skill

### From This Session's Experience

1. **Consistent prefixes:** Use domain prefixes (`msword-`, `pdf-`, etc.)
2. **Self-contained:** All resources inside skill folder
3. **No numbering:** Remove numeric prefixes from script names
4. **Helper scripts:** Use `scripts/` subfolder for utilities
5. **Update paths:** Change all references to new skill paths
6. **Preserve READMEs:** Keep original documentation as README.md
7. **Quick Start section:** Always include basic usage example

## Common Patterns

### Pattern 1: Simple Script Skill

**File:** `skill-name.py`
**Structure:**
```
skill-name/
├── SKILL.md           # ~50 tokens
├── reference.md       # Detailed guide
├── README.md          # Original readme
└── skill-name.py      # Main script
```

**Example:** `convert-docx-to-pdf`, `sanitize-filenames`

### Pattern 2: Script with Helpers

**Files:** Main script + helper scripts
**Structure:**
```
skill-name/
├── SKILL.md
├── reference.md
├── README.md
├── skill-name.py
└── scripts/
    ├── helper1.py
    └── helper2.py
```

**Example:** `msword-move-citation-before-period`

### Pattern 3: AI-Only Guidance

**No scripts, just guidance**
**Structure:**
```
skill-name/
├── SKILL.md           # Concise overview
└── reference.md       # Comprehensive rules
```

**Example:** `sop-editing-content`, `sop-deep-editing`

### Pattern 4: Complex Workflow

**Multi-step orchestration**
**Structure:**
```
skill-name/
├── SKILL.md           # Overview with workflow
├── reference.md       # Detailed steps with TOC
└── examples.md        # Real examples
```

**Example:** `chapter-organizer`, `sop-improvement-orchestration`

## Quality Checklist

### Before Finalizing a Skill

**Structure:**
- [ ] Skill folder created in correct location
- [ ] SKILL.md exists with frontmatter
- [ ] reference.md exists (if needed)
- [ ] Scripts copied without numbering
- [ ] Helper scripts in `scripts/` folder (if any)

**SKILL.md:**
- [ ] Frontmatter has `name` and `description`
- [ ] Name uses lowercase, hyphens, gerund form
- [ ] Description includes "what" and "when"
- [ ] Content is ~50 tokens total
- [ ] Has "Quick Start" or similar section
- [ ] Links to reference.md and other files

**reference.md:**
- [ ] Has table of contents (if >100 lines)
- [ ] Sections are well-organized
- [ ] Includes "When to Use This Skill"
- [ ] Has concrete examples
- [ ] Includes troubleshooting section
- [ ] Script paths updated (if script-based)

**Scripts (if applicable):**
- [ ] Copied without numeric prefix
- [ ] Named same as skill folder
- [ ] All paths in files updated
- [ ] Helper scripts in correct location
- [ ] README.md included

**Documentation:**
- [ ] All information preserved from original
- [ ] Examples are clear and practical
- [ ] No external dependencies mentioned
- [ ] Related skills listed
- [ ] Performance notes included (if relevant)

### Testing

- [ ] SKILL.md renders correctly
- [ ] Links to reference files work
- [ ] Script paths are correct (if script-based)
- [ ] Examples are accurate
- [ ] No typos or formatting issues

## Tips for Creating Great Skills

1. **Start with the description:** Write a clear description that triggers appropriately
2. **Use real examples:** Show actual command syntax and output
3. **Be specific:** "Format tables in Word" not "Format documents"
4. **Think progressive:** What does Claude need now vs. later?
5. **Keep it maintainable:** Clear structure makes updates easier
6. **Test the flow:** Read SKILL.md and verify it points to right details
7. **Learn from others:** Look at existing skills for patterns
8. **Document edge cases:** Include limitations and workarounds
9. **Update paths consistently:** Don't leave old script references
10. **Version control friendly:** Skills should work across team

## Creating Skills: Step-by-Step

### For Script-Based Skills

**Step 1: Prepare**
```bash
# Create folder
mkdir -p .claude/skills/skill-name/scripts

# Copy script (remove numbering)
cp python_scripts/NN-original.py .claude/skills/skill-name/skill-name.py

# Copy readme
cp python_scripts/NN-original_readme.md .claude/skills/skill-name/README.md

# Copy helpers (if any)
cp python_scripts/helper*.py .claude/skills/skill-name/scripts/
```

**Step 2: Create SKILL.md**
- Write concise frontmatter
- Add one-sentence summary
- Include Quick Start
- Link to reference.md and README.md

**Step 3: Create reference.md**
- Start with table of contents (if >100 lines)
- Organize into clear sections
- Update all script paths
- Include comprehensive examples
- Add troubleshooting section

**Step 4: Verify**
- Check all links work
- Verify paths are updated
- Test script execution
- Review for clarity

### For AI-Only Skills

**Step 1: Analyze Existing Content**
- Read current SKILL.md (if exists)
- Identify total length
- Determine if split needed

**Step 2: If >100 Lines**
- Extract frontmatter
- Create concise SKILL.md (~50 tokens)
- Move details to reference.md
- Add table of contents

**Step 3: If <100 Lines**
- Keep as single SKILL.md
- Ensure good structure
- Add section headings

**Step 4: Verify**
- Check readability
- Ensure sections flow well
- Verify links (if split)

## Real-World Examples

See [examples.md](./examples.md) for complete examples of:
- Script-based skill (convert-docx-to-pdf)
- Script with helpers (msword-move-citation-before-period)
- AI-only skill (sop-editing-content)
- Complex workflow (chapter-organizer)
