---
name: narrate-business-process
description: Converts business process diagrams (PDF flowcharts) into comprehensive narrative SOP documents. Analyzes visual flowcharts, extracts workflow information, creates clear written explanations in formal Bahasa Indonesia. Use when user provides business process diagram and requests narrative explanation or SOP document.
---

# Business Process Narrative - Diagram to SOP Conversion

Converts PDF business process flowcharts into clear narrative SOP documents in formal Bahasa Indonesia.

## Quick Reference

**Input**: PDF business process diagram (flowchart)
**Output**: Narrative markdown with Gambaran Umum, Pihak Terlibat, Alur Proses, Hasil Akhir
**Alternative**: Structured A-H format if requested
**Language**: Formal Bahasa Indonesia
**Key**: Conservative approach - extract visible info only, generalize unit references

## Default Format (Narrative)

1. **Gambaran Umum Proses** - Overview (2-3 paragraphs)
2. **Pihak yang Terlibat** - Actors/stakeholders list
3. **Alur Proses** - Detailed narrative by stages
4. **Hasil Akhir** - Final outcomes (1-2 paragraphs)

## Optional Structured Format

If user requests "dengan struktur A-H" or "complete SOP": A. Tujuan | B. Ruang Lingkup | C. Referensi | D. Istilah dan Definisi | E. Perlengkapan Kerja | F. Peralatan K3 | G. Material | H. Langkah Kerja

## Documentation

For complete workflow including:
- Phase-by-phase analysis and creation steps
- A-H section creation guidelines
- Conservative principles (when to infer, when not to)
- Generalization rules for unit-specific content

See: [reference.md](./reference.md)
