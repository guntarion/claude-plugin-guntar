---
name: sop-deep-editing
description: Rules for editing and formatting SOP documents. Fixes OCR errors, typos, and applies standard formatting rules. Handles heading standardization, bullet points, and markdown formatting for PLN Corporate University SOPs.
---

# SOP Editing - Formatting and Error Correction

Edits and formats SOP documents ensuring consistency, fixing errors, and applying standard markdown formatting rules.

## Quick Reference

**Input**: Document path in 0B-improved-sop/, document type (IK, PF, FR, BP, PNGTR)
**Output**: Edited file with proper formatting, no errors
**Language**: Formal Bahasa Indonesia (maintain throughout)
**Key**: Format-focused editing - do NOT change content meaning

## Main Editing Rules

1. **Add/verify file title**: `### X.Y.Z Title` (or `##` for PNGTR)
2. **Convert section headings**: Roman (I, II, III) → Alphabetic (#### A, B, C) - skip for FR/BP/PNGTR
3. **Fix OCR errors**: =, >, ?, < in words; LOUNDRY→LAUNDRY
4. **Italicize foreign terms**: _check-in_, _online_, _email_
5. **Fix typos and grammar**: Double spaces, wrong affixes, punctuation
6. **Standardize lists**: Use `-` for bullets, fix numbering, proper indentation

## Special Document Handling

- **FR (forms)**: Add title, fix table typos, DON'T convert headings
- **BP (business process)**: Add title, fix narrative, DON'T add A-H sections
- **PNGTR (intro)**: Use `##` heading (level 2), no A-H sections

## Documentation

For complete guidelines including:
- Detailed OCR error patterns and fixes
- Section heading conversion table
- Document type specific rules
- Quality checklist
- Step-by-step workflow

See: [reference.md](./reference.md)
