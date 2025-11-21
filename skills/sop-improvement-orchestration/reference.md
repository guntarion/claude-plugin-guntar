# SOP Improvement Orchestration - Reference Documentation

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [User Request Format](#user-request-format)
- [Complete Workflow](#complete-workflow)
- [Phase 0: Analysis and Planning](#phase-0-analysis-and-planning)
- [Phase 1: Content Improvement](#phase-1-content-improvement)
- [Phase 2: Editing and Formatting](#phase-2-editing-and-formatting)
- [Phase 3: Structure and Organization](#phase-3-structure-and-organization)
- [Phase 4: Validation and Reporting](#phase-4-validation-and-reporting)
- [Error Handling](#error-handling)
- [Key Principles](#key-principles)
- [Quality Checklist](#quality-checklist)

## When to Use This Skill
Activate when chapter-composer agent receives SOP improvement request from user with source folder path.

## User Request Format
User provides:
- Source folder path (dokumen-asli)
- Optional: Chapter number and name

Examples:
- "Lakukan improvement SOP untuk [topic] di lokasi: [path]"
- "Review dan improve dokumen SOP di folder [path]"

## Complete Workflow

### Phase 0: Analysis and Planning

#### Step 1: Extract Information
```python
# Extract from user request:
source_folder = "[path from user]/dokumen-asli"
chapter_number = [extract if mentioned]
chapter_name = [extract if mentioned]
```

#### Step 2: Create Planning Folder
```bash
mkdir -p [parent_of_source]/0A-rencana-improvement
```

#### Step 3: Run Analysis Script
```bash
source .venv/bin/activate && python python_scripts/17-analyze-sop-files.py [source_folder]
```

**Output**: `[parent]/0A-rencana-improvement/sop-analysis-manifest.json`

#### Step 4: Read and Review Manifest
Extract key information from the generated manifest.

#### Step 5: Create Improvement Plan
Create file: `[parent]/0A-rencana-improvement/improvement-plan.md`

**Important**: Write plan in **FORMAL BAHASA INDONESIA**

#### Step 6: Set Up TodoWrite
Track progress through the workflow phases.

---

### Phase 1: Content Improvement

#### Step 7: Create Output Folder
```bash
mkdir -p [parent]/0B-improved-sop
```

#### Step 8: Determine Naming Convention
For each file, determine output filename following pattern:
`XX-ABC-X.Y.Z-[Seq]-[Type]-[Description].md`

#### Step 9: Launch sop-content-improver Agents (Parallel)

**Batching**: Max 10 agents at a time.

**For Each File or Merge Task**, create Task tool call with appropriate template:
- Single File Improvement
- Document Merge
- Business Process Conversion

#### Step 10-12: Launch Agents, Track Progress, Complete Phase 1

---

### Phase 2: Editing and Formatting

#### Step 13: List Improved Files
Get all .md files from 0B-improved-sop/

#### Step 14: Launch sop-editor Agents (Parallel)
**Batching**: Max 10 agents at a time.

**Editing Tasks**:
1. Add file title if missing
2. Convert section headings (Roman to alphabetic)
3. Fix OCR errors
4. Italicize foreign terms
5. Fix typos and spelling
6. Fix bullet points and numbering
7. Ensure formal Bahasa Indonesia

#### Step 15-16: Launch Batch, Track Progress, Complete Phase 2

---

### Phase 3: Structure and Organization

#### Step 17: Analyze Improved Files for Grouping
Group files by two-digit sub-chapters

#### Step 18: Identify Missing Introduction Files
Check for missing X.Y.0 files

#### Step 19: Create Introduction Files
Use sub-chapter-previewer agents

#### Step 20: Create Chapter Introduction (X.1.0)
Main introduction file for the chapter

#### Step 21-22: Launch Creation, Complete Phase 3

---

### Phase 4: Validation and Reporting

#### Step 23: Count and Verify Files
Ensure all expected files are present

#### Step 24: Spot-Check Quality
Verify:
- Has file title ### X.Y.Z
- Has required sections #### A, B, C...
- No obvious unit-specific references
- Formal Bahasa Indonesia
- Proper formatting

#### Step 25: Create Completion Report
Create file: `[parent]/0B-improved-sop/completion-report.md`

**Important**: Report in **FORMAL BAHASA INDONESIA**

#### Step 26-27: Final TodoWrite Update and Summarize to User

---

## Error Handling

### Agent Failure
- Note failure in TodoWrite
- Continue with other agents
- Report failure in completion report
- Mark file for manual review

### Missing Files
- Skip and log warning
- Continue with other files
- Report in completion report

### Insufficient Context
- Add placeholder: <!-- TODO: Review and complete -->
- Report in completion report
- Mark for manual review

### Merge Conflicts
- Keep separate
- Document decision in improvement plan
- Report in completion report

---

## Key Principles

### 1. Generalizability
- Work with ANY SOP chapter
- Infer chapter abbreviations from topic
- Adapt structure to content
- Don't hardcode chapter-specific details

### 2. Parallelization
- Max 10 concurrent agents
- Batch processing for > 10 tasks
- Single message with multiple Task calls
- Track progress actively

### 3. Formal Bahasa Indonesia
- All documents in formal Indonesian
- Professional, official tone
- Suitable for corporate SOP documentation

### 4. Conservative Editing
- Don't change meaning
- Only add for completeness and clarity
- Maintain stakeholder-approved content

### 5. Context Management
- Keep main agent context lean
- Provide complete context to sub-agents
- Validate outputs systematically

---

## Quality Checklist

Before marking complete, verify:
- ✅ All source files processed
- ✅ All outputs in 0B-improved-sop/
- ✅ Naming convention followed
- ✅ Spot-checked 3-5 files for quality
- ✅ Required sections present
- ✅ Formal Bahasa Indonesia used
- ✅ Unit references generalized
- ✅ Completion report created
- ✅ TodoWrite fully updated

---

**Created by**: Claude Code
**Purpose**: Guide chapter-composer orchestration
**Status**: READY FOR USE
