---
name: sop-editing-content
description: Rules for editing and proofreading SOP content files. Fixes OCR errors, formatting, typos, and standardizes structure. Use when editing book chapter content files (IK, FR, PF documents).
---

# Editing Content - SOP File Proofreading and Formatting

Edits and proofreads content files to ensure they are clean, properly formatted, and ready for conversion to .docx format.

## Quick Reference

**Input**: File(s) to edit with full path
**Output**: Edited markdown with proper structure
**Language**: Formal Bahasa Indonesia
**Key Actions**: Add file title (###), convert Roman→Alphabetic headings (I→A), fix OCR errors, italicize foreign terms, generalize unit references

## Main Editing Rules

1. Add `### X.Y.Z Title` at file start
2. Convert section headings: I, II, III → #### A, B, C
3. Fix OCR errors (=, >, ?, < in words)
4. Italicize foreign terms (_check-in_, _online_)
5. Generalize unit-specific references (UPDL Pandaan → Unit PLN Corporate University)
6. Fix typos, grammar, bullet points

**Special**: FR (forms) skip Roman conversion; maintain tables

## Documentation

For complete guidelines including:
- Detailed editing rules for each type of fix
- OCR error patterns and solutions
- Generalization rules and examples
- FR/BP/PNGTR special handling
- Quality checks and workflow

See: [reference.md](./reference.md)
