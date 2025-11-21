# SOP Content Improvement - Complete Reference Guide

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Task Overview](#task-overview)
- [Input Provided](#input-provided)
- [Language Requirement](#language-requirement)
- [Required Document Sections (A-H)](#required-document-sections-a-h)
  - [A. Tujuan](#a-tujuan-purpose)
  - [B. Ruang Lingkup](#b-ruang-lingkup-scope)
  - [C. Referensi](#c-referensi-references)
  - [D. Istilah dan Definisi](#d-istilah-dan-definisi-terms-and-definitions)
  - [E. Perlengkapan Kerja](#e-perlengkapan-kerja-work-equipment)
  - [F. Peralatan K3](#f-peralatan-k3-safety-equipment)
  - [G. Material](#g-material-materials)
  - [H. Langkah Kerja dan Tindakan](#h-langkah-kerja-dan-tindakan-work-steps-and-actions)
- [Creating Missing Sections](#creating-missing-sections)
- [Generalization Rules](#generalization-rules)
- [Merging Documents](#merging-documents)
- [Business Process Diagram Handling](#business-process-diagram-handling)
- [Conservative Editing Principles](#conservative-editing-principles)
- [Writing in Formal Bahasa Indonesia](#writing-in-formal-bahasa-indonesia)
- [Quality Checklist](#quality-checklist)
- [Reporting Back](#reporting-back)

## When to Use This Skill
Activate when `sop-content-improver` agent needs to improve SOP documents or merge duplicates.

## Task Overview
Review and improve SOP documents to ensure they are complete, generalized for all PLN Corporate University units, and well-written in formal Bahasa Indonesia.

## Input Provided
You will receive from chapter-composer:
- **Document path(s)**: Source file(s) to improve
- **Output path**: Where to create improved document
- **Document type**: IK, PF, FR, BP, SOP
- **Missing sections**: List of sections to add
- **Unit references**: Specific items to generalize
- **Merge decision** (if applicable): Which documents to combine

## Language Requirement

**CRITICAL**: All text must be in **FORMAL BAHASA INDONESIA** (formal Indonesian language).

- Use professional, official tone suitable for corporate SOP documentation
- Proper grammar and formal vocabulary
- Avoid colloquialisms or informal language
- Write as if for official government or corporate documentation
- Use third person, passive voice where appropriate
- Maintain consistency in terminology

---

## Required Document Sections (A-H)

All Standard Operating Procedures must have these sections (unless Business Process diagram):

### A. Tujuan (Purpose)

**What to include**:
- Why this SOP exists
- What objectives it serves
- Business/operational benefits
- Who benefits from following this SOP

**Length**: 2-4 sentences

**Example** (generic for any SOP):
```markdown
#### A. Tujuan

Prosedur [topic] disusun untuk menstandarisasikan proses [activity] agar terciptanya tertib administrasi dan pelayanan yang konsisten di seluruh unit PLN Corporate University. Standardisasi ini bertujuan memastikan [desired outcome] sesuai dengan ketentuan yang berlaku dan memberikan pengalaman layanan yang prima kepada [stakeholders].
```

**Pattern**:
1. First sentence: What is being standardized and why
2. Second sentence: Expected outcomes and benefits

### B. Ruang Lingkup (Scope)

**What to include**:
- What activities/processes are covered
- What areas or departments involved
- Who uses this procedure
- Boundaries (what's NOT covered)

**Length**: 2-5 sentences

**Example** (generic):
```markdown
#### B. Ruang Lingkup

Prosedur ini mencakup seluruh kegiatan [main activities] yang dilakukan di lingkungan PLN Corporate University. Ruang lingkup meliputi [aspect 1], [aspect 2], dan [aspect 3] yang menjadi tanggung jawab [generic role] di seluruh Unit Pelaksana Diklat. Prosedur ini berlaku untuk [who uses it] dan mencakup tahapan dari [starting point] hingga [ending point].
```

### C. Referensi (References)

**What to include**:
- Related policies, regulations, laws
- Other SOPs in the collection
- Industry standards
- Internal PLN guidelines

**IMPORTANT**: Only add references if certain. **DO NOT** hallucinate or guess reference names.

**If No References Found**:
```markdown
#### C. Referensi

-
```

### D. Istilah dan Definisi (Terms and Definitions)

**What to include**:
- Technical terms used in the SOP
- Acronyms and their meanings
- Specialized vocabulary

**IMPORTANT**: Only define terms if 100% certain. **DO NOT** guess acronym expansions.

**If Uncertain About Terms**:
```markdown
#### D. Istilah dan Definisi

Istilah dan definisi yang digunakan dalam dokumen ini dijelaskan secara rinci pada Manual Sistem Manajemen Integrasi PT PLN (Persero) Pusdiklat.
```

### E. Perlengkapan Kerja (Work Equipment)

**What to include**:
- Tools and equipment needed
- Software and systems
- Devices and technology
- Furniture if relevant

**Inference Guidelines**:
- Office procedures → computer, printer, stationery
- Physical services → tools relevant to the service
- Look for clues in Langkah Kerja section

### F. Peralatan K3 (Safety Equipment)

**What to include** (if relevant):
- Safety gear and protective equipment
- Health and safety tools
- Emergency equipment

**If Not Relevant**:
```markdown
#### F. Peralatan K3

-
```

### G. Material (Materials)

**What to include**:
- Consumable supplies
- Forms and templates
- Documents and paperwork
- Materials used in the process

### H. Langkah Kerja dan Tindakan (Work Steps and Actions)

**What to include**:
- Detailed step-by-step procedures
- Decision points and branches
- Responsible parties for each step
- Sequences and workflows

**IMPORTANT**:
- Preserve existing procedures (don't change meaning)
- Only clarify or add detail if needed for understanding
- Maintain numbering and structure

---

## Creating Missing Sections

### When Section Doesn't Exist

**Step 1**: Look for clues in the document
- Read entire document for context
- Check Langkah Kerja for process details
- Look at document title for topic

**Step 2**: Look for similar sections in other documents
- If merging, check the other document
- Use patterns from existing sections

**Step 3**: Create from context
- Use generic template appropriate to SOP topic
- Infer equipment from procedures
- Infer purpose from document title and content

**Step 4**: Be conservative
- Better to be generic than wrong
- If uncertain, use standard phrases
- For Referensi and Istilah: use standard disclaimer

---

## Generalization Rules

### Unit-Specific References to Remove

**Pattern Matching**:

1. **Unit Names with Locations**:
   - ❌ "UPDL PLN Palembang" → ✅ "Unit Pelaksana Diklat"
   - ❌ "UPDL Semarang" → ✅ "Unit Pelaksana Diklat"
   - ❌ "Unit Diklat Surabaya" → ✅ "Unit Pelaksana Diklat"

2. **Role Titles with Locations**:
   - ❌ "Kepala Perpustakaan UPDL Palembang" → ✅ "Kepala Perpustakaan"
   - ❌ "Manajer Keamanan UPDL Semarang" → ✅ "Manajer Keamanan"
   - ❌ "Petugas Front Office Pandaan" → ✅ "Petugas Front Office"

3. **Location References in Procedures**:
   - ❌ "di area gedung utama Palembang" → ✅ "di area gedung utama"
   - ❌ "sesuai dengan kondisi di Semarang" → ✅ "sesuai dengan kondisi setempat"

**Strategy**:
- Replace specific with generic
- Remove location names
- Keep role names but remove unit affiliation
- Make procedures applicable everywhere

**Test**: Ask yourself "Can this be used in Padang, Surabaya, Makassar, Banjarbaru, Pandaan equally?"

---

## Merging Documents

### When to Merge
chapter-composer will tell you which documents to merge. Common scenarios:
- Two IKs covering same topic
- IK + SOP covering same process
- Duplicate documents from different sources

### Merge Strategy

**Step 1**: Read all source documents completely

**Step 2**: Identify overlapping sections
- What content appears in both?
- Which version is more complete?
- Which has better wording?

**Step 3**: Identify unique content
- What does Document A have that B doesn't?
- What does Document B have that A doesn't?

**Step 4**: Create structure outline
```
Merged Document Structure:
A. Tujuan - [take from Doc A or B - most complete]
B. Ruang Lingkup - [combine if different aspects covered]
C. Referensi - [combine all unique references]
D. Istilah - [combine all unique terms]
E. Perlengkapan - [combine all equipment]
F. K3 - [take most complete]
G. Material - [combine all materials]
H. Langkah Kerja - [combine logical workflow]
```

**Step 5**: Merge Langkah Kerja (most complex)
- If procedures identical: use one version
- If procedures different but related: combine in logical sequence
- If procedures for different aspects: organize by sub-sections

**Step 6**: Validate completeness
- All A-H sections present
- No duplication
- Logical flow
- Nothing lost from source documents

---

## Business Process Diagram Handling

### When Document is Business Process

**Characteristics**:
- PDF with flowchart/diagram
- Shows roles and workflow
- Decision branches and paths
- Not standard IK/PF format

**Task**: Convert to narrative explanation

### Conversion Strategy

**Step 1**: Analyze diagram
- Identify all actors/roles
- Identify all activities
- Identify decision points
- Identify sequence/flow

**Step 2**: Create narrative structure
```markdown
### X.Y.Z [Process Name]

## Gambaran Umum Proses

[1-2 paragraph overview of what this process accomplishes]

## Pihak yang Terlibat

- **[Role 1]**: [Responsibility]
- **[Role 2]**: [Responsibility]

## Alur Proses

**Tahap 1: [Stage Name]**

[Role] melakukan [action]. [Explanation of what happens and why].

**Tahap 2: [Stage Name]**

Setelah [previous step], [Role] kemudian [action]. Jika [condition], maka [outcome].

## Hasil Akhir

Proses ini menghasilkan [output/deliverable] yang [purpose/use].
```

**Step 3**: Write in formal Bahasa Indonesia
- Clear, professional tone
- Explain who does what, when, why
- Make decision points explicit
- Maintain logical sequence

**Step 4**: No A-H structure for Business Processes
- Use narrative format instead
- Add file title: ### X.Y.Z [Process Name]
- Focus on clarity and completeness

---

## Conservative Editing Principles

### What You CAN Do

✅ Add missing sections (A-H)
✅ Clarify ambiguous wording
✅ Add transitional phrases for flow
✅ Combine related points logically
✅ Expand abbreviated steps if needed
✅ Fix obvious errors (spelling, grammar)
✅ Generalize unit-specific content
✅ Add sub-steps for clarity

### What You CANNOT Do

❌ Change the fundamental procedure or workflow
❌ Remove steps that exist (unless obvious duplicate)
❌ Change technical requirements or standards
❌ Add new procedural requirements not in source
❌ Change roles and responsibilities
❌ Modify safety or compliance requirements
❌ Invent references or technical terms

### Gray Areas - Be Careful

⚠️ **Adding detail**: Only if needed for understanding, not changing meaning
⚠️ **Combining procedures**: Ensure logical flow, don't skip steps
⚠️ **Inferring equipment**: Use obvious items, don't guess specialized tools
⚠️ **Creating purpose statements**: Base on document content, not assumptions

---

## Writing in Formal Bahasa Indonesia

### Tone and Style

**Formal characteristics**:
- Third person perspective
- Passive voice when appropriate: "dilakukan" not "lakukan"
- Complete sentences, proper grammar
- Professional vocabulary
- Objective, factual tone

**Examples of Formal vs Informal**:

❌ Informal: "Anda harus melakukan check-in dulu"
✅ Formal: "Peserta melakukan proses _check-in_ terlebih dahulu"

❌ Informal: "Kalau ada masalah, lapor ke atasan"
✅ Formal: "Apabila terjadi kendala, pelaporan dilakukan kepada atasan langsung"

### Common Formal Phrases

**Purpose statements**:
- "...disusun untuk menstandarisasikan..."
- "...bertujuan untuk memastikan..."
- "...dilakukan untuk mencapai..."

**Scope statements**:
- "...mencakup seluruh kegiatan..."
- "...meliputi aspek..."
- "...berlaku untuk..."

**Procedure statements**:
- "Petugas melakukan..."
- "...dilaksanakan oleh..."
- "Proses dilakukan dengan..."

---

## Quality Checklist

Before completing, verify:

### Content Completeness
- ✅ All required sections (A-H) present (or narrative for BP)
- ✅ Each section has appropriate content
- ✅ No placeholders or TODOs without good reason
- ✅ Procedures are clear and complete

### Generalization
- ✅ No unit-specific location references
- ✅ No unit-specific role titles
- ✅ Procedures applicable to all UPDL units
- ✅ Generic terminology used

### Language
- ✅ Formal Bahasa Indonesia throughout
- ✅ Professional tone maintained
- ✅ Proper grammar and spelling
- ✅ Consistent terminology

### Conservative Editing
- ✅ Original meaning preserved
- ✅ Procedures not changed fundamentally
- ✅ Only added for clarity and completeness
- ✅ No hallucinated content

---

## Reporting Back

After completing your work, report to chapter-composer:

**For Single Document Improvement**:
```
File created: [output_path]

Changes made:
- Added sections: [list]
- Generalized references: [count] instances
- Clarifications added: [brief description]
- Status: Complete
```

**For Document Merge**:
```
Files merged: [list of source files]
Output: [output_path]

Merge decisions:
- [How sections were combined]
- Unique content from each source preserved
- Status: Complete
```

**For Business Process**:
```
Business Process converted: [source]
Output: [output_path]

Narrative structure:
- Roles identified: [count]
- Process stages: [count]
- Status: Complete
```

---

**Created by**: Claude Code
**Purpose**: Guide sop-content-improver agent
**Status**: READY FOR USE
