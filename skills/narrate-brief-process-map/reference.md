# Brief Process Map Narrative - Complete Reference Guide

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Input Expected](#input-expected)
- [Output Format: Brief 4-Layer Structure](#output-format-brief-4-layer-structure)
- [Workflow: Step-by-Step](#workflow-step-by-step)
  - [Phase 0: Analysis](#phase-0-analysis)
  - [Phase 1: Write Layer 1 - Ringkasan Eksekutif](#phase-1-write-layer-1---ringkasan-eksekutif)
  - [Phase 2: Create Layer 2 - Peta Navigasi](#phase-2-create-layer-2---peta-navigasi)
  - [Phase 3: Write Layer 3 - Narrative Detail](#phase-3-write-layer-3---narrative-detail)
  - [Phase 4: Add Layer 4 - Referensi](#phase-4-add-layer-4---referensi)
  - [Phase 5: Generalization & Quality Check](#phase-5-generalization--quality-check)
- [Key Principles](#key-principles)
  - [Strategic Not Tactical](#strategic-not-tactical)
  - [Standalone Explanation](#standalone-explanation)
  - [No Complex Diagrams](#no-complex-diagrams)
  - [Brief Control Points](#brief-control-points)
- [Language Requirement](#language-requirement)
- [Conservative Approach](#conservative-approach)
- [Example Usage](#example-usage)
- [Related Documentation](#related-documentation)
- [Related Skills](#related-skills)

## When to Use This Skill

Activate when user provides:
- **Master process map** untuk Bab 1 (Gambaran Strategis) buku
- Request to create **"versi ringkas"** atau **"overview"** dari proses bisnis
- Explicitly states dokumen harus:
  - Lebih pendek dari narrate-master-process-map output
  - Bisa dipahami TANPA melihat diagram
  - Cocok untuk Word (tanpa diagram teks kompleks)
  - Level overview, bukan detail operasional

**Typical user request:**
- "Buatkan versi ringkas framework X.0 untuk Bab 1"
- "Buat overview proses bisnis yang bisa dipahami standalone"
- "Konversi swimlane diagram ke narasi brief untuk buku"

**DON'T use when:**
- User wants detailed operational SOP (use `narrate-master-process-map` instead)
- User explicitly requests "detailed" or "lengkap" narrative
- For non-strategic processes (use `narrate-business-process` for operational Level 3-4)

## Input Expected

User will provide:
- **PDF file path**: Master process map diagram (multi-page swimlane)
- **Optional**: Chapter number, process number (e.g., "Framework 1.0")
- **Optional**: Target file path for output

## Output Format: Brief 4-Layer Structure

**Target Length:** 330-550 baris (~400 baris ideal)
**Reduction:** 40-60% lebih pendek dari narrate-master-process-map

### Layer 1: Ringkasan Eksekutif (100-150 baris)
- 2-4 paragraf strategic overview
- Focus: "why" dan "what", minimal "how"
- Explain big picture, structure, interconnections, strategic impact
- **NO** step-by-step, **NO** reference ke diagram

### Layer 2: Peta Navigasi Strategis (50-100 baris)
- **B5-FRIENDLY FORMAT:**
  - **PREFER nested bullets** untuk Sub-Proses overview
  - Simple 2-3 column tables ONLY if necessary
  - **NO tables with 4+ kolom** (tidak muat di kertas B5)
- Panduan Navigasi per Peran (narasi paragraf)
- Interconnection dengan Proses Lain (narasi + bullet list)
- **NO** ASCII flowcharts, **NO** complex diagrams

### Layer 3: Narrative Detail Per Sub-Proses (150-250 baris)
For each sub-proses:
- Tujuan Strategis (1-2 kalimat)
- Alur Proses (2-3 paragraf flowing narrative)
- Pihak yang Terlibat (bullet list)
- Input/Output (bullet list)
- Titik Kontrol Kritis (2-4 items, brief)
- Koneksi dengan Proses Lain (brief)

**Style:** Flowing paragraphs, **NOT** step-by-step checklist

### Layer 4: Referensi (30-50 baris)
- Dokumen Sumber (minimal)
- Stakeholder Utama (brief list)
- Proses Terkait (brief list)
- **NO** glosarium (ada di buku level global), **NO** FAQ

---

## Workflow: Step-by-Step

### Phase 0: Analysis

**Step 1: Read entire PDF**
- Understand full framework (all pages)
- Identify main process number (e.g., 1.0, 2.0)
- Map sub-processes across pages

**Step 2: Extract strategic elements**
- Big picture: What dan why framework exists
- Structure: How many sub-processes, sequential/parallel
- Stakeholders: Who's involved at strategic level
- Interconnections: Upstream, downstream, horizontal
- Strategic value: Why important untuk organisasi

---

### Phase 1: Write Layer 1 - Ringkasan Eksekutif

**Step 3: Write 2-4 paragraf strategic overview**

**Paragraph 1: Big Picture** (3-5 kalimat)
- Apa proses ini dalam konteks organisasi PLN Corpu
- Mengapa proses ini exists (strategic purpose)
- Scope temporal (annual, multi-year, continuous)

Template:
```
Proses Bisnis [nomor] "[nama]" merupakan [strategic positioning]. Framework ini [strategic value proposition], mencakup [scope description]. Sebagai [role dalam organisasi], proses ini [contribution ke tujuan strategis].
```

**Paragraph 2: Structure dan Flow** (3-4 kalimat)
- Overview sub-proses utama (list names, no detail)
- Sequential atau parallel relationships
- Key phases atau stages

Template:
```
Framework ini mengintegrasikan [X] sub-proses utama yang mencakup [brief enumeration]. Proses dimulai dengan [awal], dilanjutkan dengan [middle], dan ditutup dengan [akhir]. Setiap fase [relationship description].
```

**Paragraph 3: Interconnection Ecosystem** (3-5 kalimat)
- Input dari proses upstream (Kantor Pusat, proses lain)
- Output ke proses downstream
- Dependencies horizontal

Template:
```
Arsitektur proses ini menghubungkan [stakeholders]. Proses [upstream processes] memberikan [inputs] yang menjadi landasan, sementara proses [downstream processes] menerima [outputs] untuk [purpose]. Integrasi dengan [horizontal processes] memastikan [coordination value].
```

**Paragraph 4 (Optional): Strategic Impact** (2-3 kalimat)
- Contribution ke tujuan organisasi
- Positioning sebagai enabler
- Value proposition

**Guidelines:**
- ✅ Use flowing narrative, connected sentences
- ✅ Explain "why" lebih banyak dari "how"
- ✅ Standalone (bisa dipahami tanpa diagram)
- ❌ NO "Langkah 1, 2, 3..."
- ❌ NO "Seperti terlihat di diagram..."
- ❌ NO step-by-step operational detail

---

### Phase 2: Create Layer 2 - Peta Navigasi

**Step 4: Create Overview Sub-Proses Utama**

**Format: Nested Bullets** (B5-friendly, NO wide tables)

```markdown
### Sub-Proses Utama

Framework ini mencakup beberapa sub-proses kunci:

- **Sub-Proses X.1: [Nama]**
  - Tujuan Strategis: [1 kalimat menjelaskan why]
  - Output Kunci: [1-2 deliverables utama]
  - Connects to: [Proses downstream jika relevan]

- **Sub-Proses X.2: [Nama]**
  - Tujuan Strategis: [1 kalimat menjelaskan why]
  - Output Kunci: [1-2 deliverables utama]
  - Connects to: [Proses downstream jika relevan]

[... max 5-7 sub-proses]
```

**Alternative: Simple 2-Column Table** (jika prefer table)
```markdown
| Sub-Proses | Deskripsi |
|------------|-----------|
| **X.1 [Nama]** | Tujuan: [brief]. Output: [deliverables]. |
| **X.2 [Nama]** | Tujuan: [brief]. Output: [deliverables]. |
```

**Guidelines:**
- ✅ **PREFER nested bullets** (lebih flexible untuk B5)
- ✅ If use table: **MAX 2-3 kolom** saja
- ❌ **NO tables with 4+ kolom** (tidak muat di B5)
- Focus pada strategic purpose, bukan detail

**Step 5: Write Panduan Navigasi Berdasarkan Peran**

Format narasi paragraf (NOT table):

```markdown
**Untuk [Role A]:**
Sebagai [description], fokus Anda adalah pada sub-proses [X.Y dan X.Z] yang mencakup [activities]. Tanggung jawab utama meliputi [responsibilities]. Titik kontrol kritis: [1-3 control points].

**Untuk [Role B]:**
[Same format...]
```

- Identify 2-4 key roles
- Narasi flowing, bukan bullet points
- Max 3-4 kalimat per role

**Step 6: Document Interconnection dengan Proses Lain**

Format narasi + bullet list:

```markdown
Proses ini terintegrasi dengan beberapa proses kunci:

**Upstream (Menerima Input):**
- **Proses A.B ([Nama])**: Menyediakan [input type] yang menjadi basis untuk [usage]
- **Proses C.D ([Nama])**: [Brief explanation]

**Downstream (Memberikan Output):**
- **Proses E.F ([Nama])**: Menerima [output type] untuk [purpose]

**Horizontal (Dependencies):**
- [Brief narrative if applicable]
```

**Guidelines:**
- ✅ **PREFER nested bullets** (B5-friendly, flexible)
- ✅ Simple 2-3 column tables ONLY if necessary
- ✅ Narrative paragraphs untuk flow dan relationships
- ❌ **NO tables with 4+ kolom** (tidak muat di kertas B5)
- ❌ NO ASCII flowcharts
- ❌ NO complex diagrams
- ❌ NO detailed checklists

---

### Phase 3: Write Layer 3 - Narrative Detail

**Step 7: For Each Sub-Proses, Create Section**

Template:
```markdown
### 3.X Sub-Proses [X.Y]: [Nama]

**Tujuan Strategis:**
[1-2 kalimat explaining "why" sub-proses exists]

**Alur Proses:**

[Paragraph 1: Opening - what happens at start]
[Paragraph 2: Middle - main transformation/processing]
[Paragraph 3: Closing - hasil akhir dan transition]

**Pihak yang Terlibat:**
- **[Stakeholder 1]**: [Role dalam 1 kalimat]
- **[Stakeholder 2]**: [Role dalam 1 kalimat]

**Input Utama:**
- [Input 1] (dari: [source])
- [Input 2] (dari: [source])

**Output/Deliverable:**
- [Output 1] (ke: [destination])
- [Output 2] (ke: [destination])

**Titik Kontrol Kritis:**
- **[Control Point 1]**: [Penjelasan singkat why kritis]
- **[Control Point 2]**: [Penjelasan singkat]

**Koneksi dengan Proses Lain:**
- Menerima dari: [Process A.B]
- Memberikan ke: [Process C.D]
```

**Writing Style untuk "Alur Proses":**
- Use transition words (setelah, kemudian, tahap berikutnya, dilanjutkan dengan)
- Explain cause-effect relationships
- Show interconnections naturally
- Humanize (Bidang X melakukan..., Tim Y mengkoordinir..., UPAC memastikan...)
- ❌ Avoid: "Langkah 1, Langkah 2, Langkah 3"
- ❌ Avoid: Checklist format
- ❌ Avoid: Reference ke diagram

**Length target per sub-proses:**
- Tujuan Strategis: 1-2 kalimat
- Alur Proses: 2-3 paragraf (total ~8-12 kalimat)
- Others: brief bullet lists
- **Total: 20-30 baris per sub-proses**

**Guideline:**
- ✅ Narrative paragraphs untuk alur (flowing, connected)
- ✅ Bullet lists untuk structured data (stakeholders, inputs, outputs)
- ✅ Focus pada strategic flow
- ❌ NO step-by-step operational details
- ❌ NO referensi diagram
- ❌ NO execution checklists

---

### Phase 4: Add Layer 4 - Referensi

**Step 8: Add Minimal Reference Section**

```markdown
### Layer 4: Referensi

#### 4.1 Dokumen Sumber
- **Swimlane Diagram**: [Filename.pdf]
- **Lokasi**: [Path atau keterangan]

#### 4.2 Stakeholder Utama
- **[Stakeholder A]**: [Role dalam 1 kalimat]
- **[Stakeholder B]**: [Role dalam 1 kalimat]

#### 4.3 Proses Terkait

**Proses Kantor Pusat:**
- [X.Y.Z]: [Nama proses] - [Brief connection]

**Proses Internal:**
- [A.B.C]: [Nama proses] - [Brief connection]
```

**Guidelines:**
- ✅ Minimal dan concise
- ❌ NO glosarium (akan ada global di buku)
- ❌ NO FAQ section
- ❌ NO template/form detail
- ❌ NO document output table (sudah disebutkan di Layer 3)

---

### Phase 5: Generalization & Quality Check

**Step 9: Generalize unit-specific references**

Same rules as other narrative skills:
- "UPDL PLN Palembang" → "Unit Pelaksana Diklat"
- "Kepala Perpustakaan UPDL Semarang" → "Kepala Perpustakaan"
- Generic role titles, applicable to all units

**Step 10: Quality check**

Verify:
- ✅ Strategic narrative flows well (not tactical)
- ✅ Standalone (bisa dipahami tanpa diagram)
- ✅ NO flowcharts atau diagram teks
- ✅ Control points brief (2-4 per sub-proses)
- ✅ Interconnections explained clearly
- ✅ Formal Bahasa Indonesia throughout
- ✅ Generalized (no unit-specific content)
- ✅ Heading level: ## sebagai tertinggi
- ✅ Length: 330-550 baris (target: ~400 baris)

**Length Check:**
- Layer 1: 100-150 baris
- Layer 2: 50-100 baris
- Layer 3: 150-250 baris (untuk 6-8 sub-proses)
- Layer 4: 30-50 baris
- **Total: 330-550 baris**

**Step 11: Save file**

Determine filename:
- If user provides: Use user's filename
- Otherwise: `Framework-[X.0]-[Process-Name].md`

---

## Key Principles

### Strategic Not Tactical

❌ DON'T:
```markdown
1. Petugas mengisi form dengan langkah:
   a. Buka aplikasi
   b. Input data nama
   c. Input data NIP
   [... detailed steps]
```

✅ DO:
```markdown
Tim administrasi melakukan verifikasi data peserta melalui sistem informasi terpadu. Proses verifikasi mencakup validasi identitas, kelengkapan prasyarat, dan konfirmasi ketersediaan kuota. Hasil verifikasi didokumentasikan dalam sistem untuk keperluan monitoring dan audit.
```

### Standalone Explanation

❌ DON'T:
```markdown
Seperti terlihat di diagram pada halaman 3, proses approval memiliki dua jalur...
```

✅ DO:
```markdown
Proses approval memiliki dua jalur tergantung pada nilai investasi: jalur cepat untuk nilai di bawah threshold dan jalur komprehensif untuk investasi strategis yang melibatkan komite evaluasi multi-fungsi.
```

### No Complex Diagrams

❌ DON'T:
```markdown
┌─────────────────────────────────────────┐
│     START                                │
│       ↓                                  │
│   ┌──────┐     ┌──────┐     ┌──────┐   │
│   │ A.1  │ → │ A.2  │ → │ A.3  │   │
│   └──────┘     └──────┘     └──────┘   │
[... complex ASCII art]
```

✅ DO (Option 1: Nested Bullets - BEST for B5):
```markdown
Proses ini terdiri dari tiga fase utama:

- **Fase Awal (Sub-Proses A.1: Persiapan)**
  - Kegiatan: Analisis kebutuhan dan penyusunan rencana kerja
  - Output: Dokumen perencanaan yang approved

- **Fase Eksekusi (Sub-Proses A.2: Pelaksanaan)**
  - Kegiatan: Implementasi sesuai rencana dengan monitoring berkelanjutan
  - Output: Hasil implementasi dan laporan progress

- **Fase Penutup (Sub-Proses A.3: Evaluasi)**
  - Kegiatan: Review hasil dan identifikasi lessons learned
  - Output: Laporan evaluasi dan rekomendasi
```

✅ DO (Option 2: Simple 2-Column Table - if needed):
```markdown
| Fase | Kegiatan dan Output |
|------|---------------------|
| **Awal (A.1)** | Persiapan: Analisis dan perencanaan. Output: Plan |
| **Eksekusi (A.2)** | Pelaksanaan sesuai rencana. Output: Results |
| **Penutup (A.3)** | Evaluasi dan review. Output: Report |
```

### Brief Control Points

❌ DON'T:
```markdown
**Checklist Control Point A:**
- [ ] Verify document completeness
- [ ] Check signature authority
- [ ] Validate budget code
- [ ] Confirm vendor registration
- [ ] Review historical performance
[... 20+ checklist items]
```

✅ DO:
```markdown
**Titik Kontrol Kritis:**
- **Verifikasi Dokumen**: Memastikan kelengkapan dan validitas dokumen kontrak sebelum approval
- **Budget Compliance**: Validasi ketersediaan anggaran dan kesesuaian kode budget
- **Vendor Qualification**: Konfirmasi vendor memenuhi standar kualifikasi organisasi
```

---

## Language Requirement

**CRITICAL**: All text in **FORMAL BAHASA INDONESIA**

Same standards as other narrative skills:
- Third person, professional tone
- Complete sentences
- Italicize foreign terms (_User Acceptance Testing_, _Go Live_, _Portal Asesmen_, _Master Plan_)
- No informal language
- Formal vocabulary suitable for corporate SOP documentation

---

## Conservative Approach

### DO:
✅ Extract visible information from diagram
✅ Create strategic narrative explaining framework
✅ Simplify complex visual into navigable structure
✅ Explain interconnections clearly
✅ Focus on strategic value dan big picture

### DON'T:
❌ Add strategic initiatives not shown in diagram
❌ Invent decision criteria not visible
❌ Hallucinate references or policies
❌ Change framework logic
❌ Add tactical details (that's for operational SOPs)

### When Uncertain:
- Control point items: Be generic, don't invent specifics
- Timeline: Mark as "ilustratif, dapat bervariasi"
- KP processes: Only mention if clearly referenced in diagram
- Decision gates: Mention if critical, don't elaborate if not visible

---

## Example Usage

**User:**
"Buatkan versi ringkas Framework 1.0 Penyelarasan Visi dan Strategi untuk Bab 1 dari diagram di ./BUKU-2/01-Chapter-01/Alur-Swimlane-PUSDIKLAT-probis-01.pdf"

**Your actions:**
1. Read entire 12-page PDF
2. Identify framework: Proses 1.0 dengan 4 sub-proses (1.1, 1.2, 1.3, 1.4)
3. Extract strategic overview
4. Create Layer 1: 2-4 paragraf big picture
5. Create Layer 2: Tabel, panduan peran, interconnections (NO flowchart)
6. Create Layer 3: Narrative detail per sub-proses (2-3 paragraf per sub-proses)
7. Create Layer 4: Minimal references
8. Generalize unit-specific content
9. Quality check: standalone, no diagram reference, ~400 baris
10. Save to markdown file
11. Report completion dengan summary

---

## Related Documentation

Detailed strategies available at:
- `./prompts/claude-code-plans/narrate-brief-process-map/00-ANALYSIS.md` - Analisis perbedaan detail vs ringkas
- `./prompts/claude-code-plans/narrate-brief-process-map/01-STRATEGY.md` - Comprehensive conversion strategy

---

## Related Skills

- **narrate-master-process-map**: For detailed operational navigation guides (600-1000+ lines)
- **narrate-business-process**: For operational (Level 3-4) single-process diagrams
- **sop-content-improvement**: For enhancing SOP content
- **sop-editing**: For formatting and error correction

---

**Created by**: Claude Code
**Purpose**: Convert master process maps to brief strategic overviews for book Chapter 1
**Language**: Formal Bahasa Indonesia
**Target Length**: 330-550 baris (~400 baris ideal)
**Reduction**: 40-60% lebih pendek dari narrate-master-process-map
**Status**: READY FOR USE
