# Business Process Narrative - Complete Reference Guide

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Task Overview](#task-overview)
- [Input Expected](#input-expected)
- [Default Output Format: Narrative](#default-output-format-narrative)
- [Alternative Format: Structured (A-H)](#alternative-format-structured-a-h)
- [Step-by-Step Workflow](#step-by-step-workflow)
  - [Phase 1: Analysis](#phase-1-analysis-extract-information-from-diagram)
  - [Phase 2: Create Narrative](#phase-2-create-narrative)
  - [Phase 3: Add A-H Sections](#phase-3-add-a-h-sections-if-requested)
  - [Phase 4: Generalization](#phase-4-generalization)
  - [Phase 5: Quality Check and Save](#phase-5-quality-check-and-save)
- [Language Requirement](#language-requirement)
- [Conservative Principles](#conservative-principles)
- [Example Usage](#example-usage)
- [Related Documentation](#related-documentation)
- [Related Skills](#related-skills)

## When to Use This Skill

Activate when user:
- Provides a PDF file containing a business process diagram (flowchart)
- Asks to "create narrative from diagram" or "explain the business process"
- Requests "SOP document from business process diagram"
- Says "buat narasi dari bagan proses bisnis" or "jelaskan diagram ini"

**Typical request patterns:**
- "Buat dokumen SOP dari bagan proses bisnis di file X.pdf"
- "Jelaskan alur proses dari diagram ini"
- "Convert this business process flowchart to written procedure"

## Task Overview

Analyze business process diagrams and convert them into clear narrative SOP documents.

## Input Expected

User will provide:
- **PDF file path**: Business process diagram to analyze
- **Optional**: Target file path for output
- **Optional**: Whether to use narrative or structured (A-H) format
- **Optional**: Hierarchical notation (e.g., "7.3.1") and description for filename

## Default Output Format: Narrative

Unless user explicitly requests structured format, use **narrative format** with these sections:

1. **Gambaran Umum Proses** - Overview (2-3 paragraphs)
2. **Pihak yang Terlibat** - Actors/stakeholders list
3. **Alur Proses** - Detailed narrative by stages
4. **Hasil Akhir** - Final outcomes (1-2 paragraphs)

## Alternative Format: Structured (A-H)

If user requests "dengan struktur A-H" or "complete SOP", add standard SOP sections:
A. Tujuan | B. Ruang Lingkup | C. Referensi | D. Istilah dan Definisi | E. Perlengkapan Kerja | F. Peralatan K3 | G. Material | H. Langkah Kerja dan Tindakan

## Step-by-Step Workflow

### Phase 1: Analysis (Extract Information from Diagram)

1. **Read PDF diagram** - View the business process flowchart
2. **Extract header info** - Title, unit, process name, document number
3. **Identify columns** - Actor organizational units (PUSDIKLAT, UPDL, HTD AREA, etc.)
4. **Map activities** - List all boxes with their descriptions and owning actors
5. **Find decisions** - Identify diamond shapes, conditions, branches
6. **Note I/O** - Inputs (left) and Outputs (right) columns
7. **Trace flow** - Follow arrows to understand sequence and handoffs

### Phase 2: Create Narrative

8. **Gambaran Umum** - Write 2-3 paragraphs: what is this process, why it exists, what it covers, benefits
9. **Pihak Terlibat** - List each actor with role description (1-2 sentences each)
10. **Alur Proses** - Narrate by stages:
   - Organize activities into logical phases
   - Explain who does what, using what inputs
   - Describe decision points: "Jika [condition], maka [outcome]"
   - Show handoffs between actors
   - Use transitions: "Selanjutnya...", "Setelah itu...", "Secara bersamaan..."
11. **Hasil Akhir** - Summarize deliverables and outcomes (1-2 paragraphs)

### Phase 3: Add A-H Sections (If Requested)

Only if user explicitly requests structured format:

12. **A. Tujuan** - Infer purpose from process name, outputs, objectives
13. **B. Ruang Lingkup** - Define scope based on activities, actors, start/end points
14. **C. Referensi** - CONSERVATIVE: Only include if certain, otherwise "-"
15. **D. Istilah dan Definisi** - CONSERVATIVE: Only define terms you're 100% sure about
16. **E. Perlengkapan Kerja** - Infer equipment from activities (computer, printer, systems, etc.)
17. **F. Peralatan K3** - Usually "-" for administrative processes, include if safety-relevant
18. **G. Material** - Infer forms, templates, consumables from process
19. **H. Langkah Kerja** - Convert narrative to numbered procedural steps by stage

### Phase 4: Generalization

20. **Remove unit-specific references**:
   - "UPDL Palembang" → "Unit Pelaksana Diklat"
   - "Kepala UPDL Semarang" → "Kepala Unit Pelaksana Diklat"
   - Remove all location names

### Phase 5: Quality Check and Save

21. **Quality review** - Verify formal Bahasa Indonesia, completeness, no hallucination
22. **Determine filename** - Use hierarchical notation if provided, otherwise generic name
23. **Save markdown** - Write to file
24. **Report completion** - Summarize to user

## Language Requirement

**CRITICAL**: All text in **FORMAL BAHASA INDONESIA**

- Third person: "Pusdiklat melakukan..." not "Anda melakukan..."
- Professional vocabulary: "memastikan" not "cek"
- Complete sentences, proper grammar
- Italicize foreign terms: _Check-in_, _Online_, _Self Learning_

## Conservative Principles

### DO:
✅ Extract visible information accurately
✅ Create clear narrative explaining workflow
✅ Infer equipment/materials reasonably from activities

### DON'T:
❌ Hallucinate steps not in diagram
❌ Guess technical terms or acronyms
❌ Invent references or policies
❌ Add procedures not shown

### When Uncertain:
⚠️ Referensi: Use "-" or standard safe reference
⚠️ Istilah: Use disclaimer instead of guessing
⚠️ Technical terms: Keep as-is if unsure

## Example Usage

**User**: "Buat narasi dari ./dokumen/alur-proses-level-3.pdf"

**Actions**:
1. Read PDF → analyze structure
2. Create narrative (Gambaran Umum, Pihak Terlibat, Alur Proses, Hasil Akhir)
3. Generalize unit references
4. Save to markdown
5. Report completion

## Related Documentation

Detailed plans available at:
- `./prompts/claude-code-plans/create-sop-from-diagram-proses-bisnis/`

## Related Skills

- **sop-content-improvement** - For A-H section enhancement
- **sop-editing** - For formatting and error correction

---

**Created by**: Claude Code
**Language**: Formal Bahasa Indonesia
**Status**: READY FOR USE
