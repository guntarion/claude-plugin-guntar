# Checklist Narrative - Complete Reference Guide

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Purpose](#purpose)
- [Input Expected](#input-expected)
- [Output Structure](#output-structure)
- [Workflow: Step-by-Step](#workflow-step-by-step)
  - [Phase 1: Analysis](#phase-1-analysis)
  - [Phase 2: Infer Context](#phase-2-infer-context)
  - [Phase 3: Create Narrative](#phase-3-create-narrative)
  - [Phase 4: Finalization](#phase-4-finalization)
- [Language Requirement](#language-requirement)
- [Conservative Approach](#conservative-approach)
- [Example Usage](#example-usage)
- [Related Documentation](#related-documentation)
- [Related Skills](#related-skills)

## When to Use This Skill

Activate when user provides:
- **PDF checklist** (table format, originally from Excel)
- **Request for explanation/documentation** of checklist
- Checklist will remain as **appendix/lampiran**
- Need **main document** that explains context, details, and usage

**Typical characteristics:**
- Table with checkbox columns (Ada/Tidak Ada, Progres/Selesai, etc.)
- List of items to verify/complete
- May have phases/categories (Pra, Saat, Pasca) or sequential list
- Often includes: PIC column, Keterangan column
- Context: Learning delivery, event preparation, process execution

**Example checklists:**
- Kesiapan Kelas Daring (online learning readiness)
- Pelaksanaan Diklat (training execution)
- Persiapan Event (event preparation)

## Purpose

Create comprehensive guidance document that:
- Explains WHAT each checklist item means (detail)
- Explains WHY checklist is important (purpose/context)
- Explains HOW to execute each item (standards/procedures)
- Explains WHO is responsible (PIC assignment)
- Explains WHEN items should be done (timeline)
- Provides troubleshooting for common issues

**Checklist PDF remains as operational tool (appendix).**
**This narrative is the explanation/guidance document.**

## Input Expected

User will provide:
- **PDF file path**: Checklist document
- **Optional**: Context (for what process/activity)
- **Optional**: Target output file path

## Output Structure

```markdown
# [Nama Checklist] - Panduan Penggunaan

## A. Tujuan dan Ruang Lingkup

**Tujuan:**
[Mengapa checklist ini penting, apa fungsinya]

**Ruang Lingkup:**
[Dalam konteks proses/aktivitas apa checklist digunakan]

**Kapan Digunakan:**
[Timing - untuk event apa, frekuensi, trigger]

**Penanggung Jawab:**
[Siapa yang menggunakan checklist ini]

## B. Penjelasan Per Fase/Kategori

### Fase I: [Nama Fase]

**Overview:**
[Penjelasan umum tentang fase ini]

**Tujuan Fase:**
[Apa yang ingin dicapai dalam fase ini]

**Timeline:**
[Kapan fase ini dilakukan - H-X sampai H-Y]

**Kriteria Sukses:**
[Bagaimana tahu fase ini selesai dengan baik]

#### Penjelasan Item dalam Fase Ini

##### 1. [Nama Item]

**Deskripsi:**
[Penjelasan detail apa yang dimaksud dengan item ini]

**Standar/Kriteria:**
[Bagaimana memverifikasi - apa yang harus ada/terpenuhi]

**Cara Melaksanakan:**
[Langkah-langkah atau guidance untuk mengeksekusi]

**Penanggung Jawab:**
[Siapa yang bertanggung jawab untuk item ini]

**Timeline:**
[Kapan harus dilakukan - H-X, saat Y, dst]

**Dependencies:**
[Item lain yang harus selesai dulu atau terkait]

**Catatan Penting:**
[Tips, warning, atau informasi tambahan jika relevan]

[Ulangi untuk setiap item dalam fase]

[Ulangi struktur untuk setiap fase]

## C. Workflow Penggunaan Checklist

### Tahap 1: Inisiasi
[Kapan mulai menggunakan checklist, persiapan awal]

### Tahap 2: Eksekusi
[Cara mengisi dan melaksanakan per fase]

### Tahap 3: Review dan Verifikasi
[Cara memverifikasi kelengkapan sebelum/sesudah eksekusi]

### Tahap 4: Dokumentasi
[Cara menyimpan, melaporkan, filing]

## D. Matriks Penanggung Jawab

[Table showing PIC for phases/categories]

| Fase/Kategori | Item/Aktivitas | Primary PIC | Supporting PIC | Reviewer |
|---------------|----------------|-------------|----------------|----------|
| [Fase 1] | [Items] | [PIC] | [Support] | [Reviewer] |

## E. Troubleshooting dan Escalation

### Masalah Umum dan Solusi

**Problem 1: [Masalah yang mungkin terjadi]**
- **Impact**: [Konsekuensi jika tidak diatasi]
- **Solusi Immediate**: [Langkah segera]
- **Escalation**: [Ke mana escalate jika tidak bisa solved]
- **Preventive**: [Cara mencegah di masa depan]

### Escalation Path

**Level 1 Issues**: [Minor issues] → Action: [Handle sendiri]
**Level 2 Issues**: [Perlu koordinasi] → Action: [Escalate ke X]
**Level 3 Issues**: [Critical/blocking] → Action: [Escalate ke Y, urgent]

## F. Referensi dan Dokumen Terkait

**SOP Terkait:**
- [Nama SOP untuk detail prosedur]

**Formulir dan Template:**
- [Form-form lain yang relevan]

**Sistem dan Tools:**
- [Aplikasi/sistem yang digunakan]

**Contact Person:**
- [PIC untuk support/pertanyaan]

## Lampiran: Checklist Form

Untuk checklist form yang dapat diisi, silakan gunakan:
- **File**: [nama file PDF checklist]
- **Lokasi**: [path atau referensi]

Form checklist adalah tool operasional untuk eksekusi. Dokumen ini adalah panduan
penjelasan untuk memahami konteks dan detail dari setiap item dalam checklist.
```

## Workflow: Step-by-Step

### Phase 1: Analysis

**Step 1: Read checklist PDF**
- View entire checklist
- Understand table structure

**Step 2: Extract metadata**
- Form code/number
- Date (if specific event)
- Context clues from title
- Target audience

**Step 3: Identify structure**
Check if checklist has:
- **Phases/categories** (I, II, III or groups)
- **Sequential list** (just numbered items)
- Extract phase names if exist

**Step 4: Map columns**
Identify what columns exist:
- Checkboxes: Ada/Tidak Ada, Progres/Selesai, Yes/No
- PIC (Person in Charge)
- Keterangan (Notes/Remarks)
- Others

**Step 5: Extract all items**
Create inventory:
```
Phase I: [Name]
  1. [Item 1 description]
  2. [Item 2 description]
  ...

Phase II: [Name]
  1. [Item description]
  ...
```

**Step 6: Categorize items logically**
Even if no explicit categories, group by function:
- Administrative (surat, dokumen)
- Technical (setup, systems)
- Coordination (konfirmasi, komunikasi)
- Materials (materi, perlengkapan)
- Logistics (konsumsi, akomodasi, transport)

### Phase 2: Infer Context

**Step 7: Infer purpose from title**
Examples:
- "Kesiapan Kelas Daring" → Online learning readiness
- "Pelaksanaan Diklat" → Training execution logistics
- "Persiapan Event" → Event preparation

**Step 8: Infer timeline from structure**
- "Pra-X" → Before activity (H-X days)
- "Saat X" → During activity (real-time)
- "Pasca X" → After activity (H+X days)

**Step 9: Infer responsible parties**
From item content:
- Administrative items → Admin or Coordinator
- Technical items → Technical staff or IT
- Coordination items → Coordinator or Petugas
- Leadership items → Pejabat or Manager

### Phase 3: Create Narrative

**Step 10: Write Tujuan dan Ruang Lingkup**

Based on checklist title and items, infer:
- Purpose: Why this checklist exists
- Scope: What process/activity it supports
- When used: Frequency, timing, trigger
- Who uses: Primary user role

Format (2-3 paragraphs):
```
Checklist [nama] merupakan alat bantu operasional untuk memastikan [purpose].
Checklist ini wajib digunakan oleh [role] untuk setiap [activity/event].

Tujuan penggunaan checklist ini adalah:
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

Checklist ini mencakup [scope description].
```

**Step 11: For each Phase, write overview**

Template:
```markdown
### Fase [X]: [Nama Fase]

**Overview:**
Fase [nama] mencakup seluruh aktivitas [description] yang dilakukan
[when - before/during/after] [main activity].

**Tujuan Fase:**
Memastikan [specific goal of this phase].

**Timeline:**
[Inferensi dari nama fase - e.g., H-14 sampai H-1 untuk Pra-Pembelajaran]

**Kriteria Sukses:**
- Semua X items dalam fase ini ter-check [Selesai/Ada]
- Tidak ada blocker atau issue yang unresolved
- [Other relevant success criteria]
```

**Step 12: For each Item, write detailed explanation**

Template:
```markdown
##### X. [Nama Item dari Checklist]

**Deskripsi:**
[Penjelasan detail - expand singkatan, explain konteks, apa maksudnya]

**Standar/Kriteria:**
[Apa yang dimaksud "selesai" atau "ada" untuk item ini:
- Jika dokumen: format apa, konten minimal apa
- Jika konfirmasi: berapa persen response rate
- Jika technical: apa yang harus functional
- Jika coordination: apa yang harus dikomunikasikan]

**Cara Melaksanakan:**
[High-level steps atau guidance - bukan SOP detail, tapi cukup untuk tahu
bagaimana mengeksekusi item ini]

**Penanggung Jawab:**
[Infer dari konten item - siapa yang logically responsible]

**Timeline:**
[Infer dari fase dan item nature - kapan idealnya dilakukan]

**Dependencies:**
[Items lain yang harus done first, atau yang related]

**Catatan Penting:**
[Jika ada - tips, warnings, common pitfalls]
```

**Inference Guidelines untuk Item Explanation:**

**Example Item: "Konfirmasi kehadiran peserta"**

Deskripsi:
```
Memastikan seluruh peserta yang diundang telah memberikan konfirmasi kehadiran
(hadir/tidak hadir) sehingga dapat dipersiapkan jumlah yang pasti untuk
keperluan logistik.
```

Standar/Kriteria:
```
- Minimal 90% peserta yang diundang sudah memberikan konfirmasi
- Konfirmasi tercatat dalam sistem atau spreadsheet
- Peserta yang tidak konfirmasi sudah di-follow up minimal 2x
```

Cara Melaksanakan:
```
1. Kirim email/WA reminder ke peserta yang belum konfirmasi (H-7, H-3)
2. Catat response di tracking sheet
3. Follow up via telepon untuk non-responders (H-2)
4. Finalisasi jumlah dan informasikan ke bagian logistik
```

**Step 13: Create Workflow section**

Describe how to use checklist practically:
- When to start using
- How to mark items (checkbox, signature, date)
- When to review
- How to handle incomplete items
- Where to submit/file completed checklist

**Step 14: Create Troubleshooting section**

For common items, provide troubleshooting:
- Instructor tidak confirm → Solutions
- Technical system down → Backup plan
- Materials not ready → Escalation
- Logistics issue → Alternative

Structure:
```markdown
**Problem**: [Masalah]
- **Impact**: [Apa konsekuensi]
- **Solusi Immediate**: [Langkah cepat]
- **Escalation**: [Ke mana jika tidak bisa solved]
- **Preventive**: [Cara prevent next time]
```

**Step 15: Create reference section**

List (generically if not known specifically):
- SOP yang terkait (jika tahu dari context)
- Forms lain yang relevan (jika disebutkan di checklist)
- Systems/tools (jika disebutkan - Zoom, LMS, dll)
- Contact persons (generic roles if not specific names)

### Phase 4: Finalization

**Step 16: Add Lampiran section**

Reference back to original checklist PDF:
```markdown
## Lampiran: Checklist Form

Untuk checklist form yang dapat diisi, silakan gunakan:
- **File**: [nama file PDF checklist]
- **Lokasi**: [path]
- **Format**: PDF / Excel [tergantung available]

Form checklist tersebut adalah tool operasional untuk eksekusi harian.
Dokumen panduan ini adalah penjelasan konteks dan detail untuk memahami
setiap item dalam checklist.

**Cara Menggunakan Form:**
1. Download/print form checklist
2. Isi header (nama, tanggal, event/activity)
3. Check items sesuai progress
4. Catat keterangan jika ada issue
5. Submit completed form ke [PIC review]
```

**Step 17: Quality check**

Verify:
- ✅ All checklist items have explanation
- ✅ Each phase has overview and criteria
- ✅ Practical workflow provided
- ✅ Troubleshooting addresses likely issues
- ✅ Formal Bahasa Indonesia throughout
- ✅ Reference to original checklist included

**Step 18: Save file**

Filename format:
- If specific: `Panduan-[Nama-Checklist].md`
- If generic: `Checklist-[Context]-Guide.md`

Example: `Panduan-Kesiapan-Kelas-Daring.md`

## Language Requirement

**FORMAL BAHASA INDONESIA**

Same standards:
- Professional, official tone
- Third person perspective
- Complete sentences, proper grammar
- Italicize foreign terms: _Zoom_, _email_, _login_, _link_, _webinar_, _online_

## Conservative Approach

### DO:
✅ Extract all visible checklist items accurately
✅ Infer logical purpose and context from title/items
✅ Provide reasonable standards based on item nature
✅ Suggest typical timeline based on phase names
✅ Offer practical troubleshooting for common scenarios

### DON'T:
❌ Invent specific SOP codes/numbers if not provided
❌ Hallucinate detailed procedures beyond item scope
❌ Assume specific names for PIC (use generic roles)
❌ Create overly complex criteria for simple items

### WHEN UNCERTAIN:
⚠️ Use generic terms: "Koordinator atau petugas yang ditunjuk"
⚠️ Provide ranges: "Minimal H-7 hingga H-3"
⚠️ Acknowledge: "Untuk detail prosedur, rujuk ke SOP terkait"
⚠️ Standards: Be reasonable but not prescriptive

## Example Usage

**User**: "Buat panduan penggunaan untuk checklist di ./path/checklist.pdf"

**Your actions**:
1. Read checklist PDF
2. Extract structure and items
3. Infer context and purpose
4. Create comprehensive guide with all sections
5. Save to markdown
6. Report completion

## Related Documentation

Detailed analysis:
- `./prompts/claude-code-plans/create-sop-from-diagram-proses-bisnis/07-CHECKLIST-TO-NARRATIVE-ANALYSIS.md`

## Related Skills

- **sop-content-improvement**: For enhancing narrative content
- **sop-editing**: For formatting and error correction
- **business-process-narrative**: For process flow explanation

---

**Created by**: Claude Code
**Purpose**: Convert checklists to comprehensive guidance documents
**Language**: Formal Bahasa Indonesia
**Status**: READY FOR USE
