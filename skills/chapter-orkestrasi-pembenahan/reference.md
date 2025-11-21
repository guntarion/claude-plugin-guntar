# Orkestrasi Pembenahan Bab - Content Composition Orchestration Reference

## Table of Contents
- [When to Use This Skill](#when-to-use-this-skill)
- [Prerequisites](#prerequisites)
- [Workflow Overview](#workflow-overview)
- [Phase 0: Analysis and Planning](#phase-0-analysis-and-planning)
- [Phase 1: Create Introduction Files](#phase-1-create-introduction-files)
- [Phase 2: Edit Content Files](#phase-2-edit-content-files)
- [Phase 3: Validation and Reporting](#phase-3-validation-and-reporting)
- [Parallelization Rules](#parallelization-rules)
- [Error Handling](#error-handling)
- [Important Notes](#important-notes)

## When to Use This Skill
Activate when user requests content composition/editing for a book chapter with commands like:
- "Lakukan pembenahan untuk pembuatan konten Bab X di lokasi/path berikut: ..."
- "Compose content untuk Bab X"
- "Edit dan proofread files di folder X"

## Prerequisites
User must provide:
1. **Chapter folder path**: Location of markdown-composed files
2. **Structure reference** (optional): Path to structure plan file

## Workflow Overview

```
Phase 0: Analysis
├─ Run 16-analyze-chapter-files.py
└─ Create work manifest

Phase 1: Create Introduction Files (x.x.0)
├─ Launch sub-chapter-previewer agents (parallel)
├─ Track progress with TodoWrite
└─ Validate completion

Phase 2: Edit Content Files
├─ Launch sub-chapter-editor agents (parallel, max 10 at a time)
├─ Process in batches
├─ Track progress with TodoWrite
└─ Validate completion

Phase 3: Report
└─ Create completion report
```

## Phase 0: Analysis and Planning

**Step 1**: Extract folder path from user request
```python
# Example user input:
"Lakukan pembenahan untuk pembuatan konten Bab 2 di lokasi: ./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/markdown-composed"

# Extract:
folder_path = "./BUKU-2/02-HOUSEKEEPING-(UPDL-PANDAAN)/markdown-composed"
```

**Step 2**: Run analysis script
```bash
source .venv/bin/activate && python python_scripts/16-analyze-chapter-files.py "<folder_path>"
```

**Step 3**: Read generated manifest
```python
manifest_path = f"{folder_path}/chapter-work-manifest.json"
# Read manifest to get:
# - intro_files: List of x.x.0 files to create
# - content_files: List of files to edit
```

**Step 4**: Create TodoWrite list
```python
todos = [
    {"content": f"Analyze chapter files in {folder_path}", "activeForm": "...", "status": "completed"},
    {"content": f"Create {len(intro_files)} introduction files", "activeForm": "...", "status": "pending"},
    {"content": f"Edit {len(content_files)} content files", "activeForm": "...", "status": "pending"},
    {"content": "Validate all files and create report", "activeForm": "...", "status": "pending"}
]
```

---

## Phase 1: Create Introduction Files

**Step 5**: Launch sub-chapter-previewer agents in parallel

**Agent Assignment**:
- One agent per x.x.0 file to create
- Launch all agents in single message (if ≤ 10 files)
- If > 10 files, launch in batches of 10

**Prompt Template for Each Agent**:
```markdown
You are a sub-chapter-previewer agent. Your task is to create an introduction file.

**Input**:
- File to create: {file_to_create}
- Sub-chapter: {sub_chapter}
- Title: {title}
- Source files to preview: {source_files}
- Folder: {folder_path}

**Instructions**:
1. Read the first 15 lines of each source file
2. Synthesize an introduction following the chapter-compose-preview skill rules
3. Create the file at: {folder_path}/{file_to_create}
4. Use heading format: ## {sub_chapter} {title}
5. Write in FORMAL BAHASA INDONESIA

Refer to skill: .claude/skills/chapter-compose-preview/SKILL.md
```

**Step 6**: Update TodoWrite as agents complete
```python
# After Phase 1 completes
update_todo("Create X introduction files", "completed")
```

---

## Phase 2: Edit Content Files

**Step 7**: Launch sub-chapter-editor agents in parallel batches

**Batching Strategy**:
- Maximum 10 agents running concurrently
- Each agent handles 1 file
- Process in sequential batches until all files edited

**Batch Processing**:
- Batch 1 (files 1-10): Launch 10 agents in parallel
- Batch 2 (files 11-20): Wait for Batch 1, then launch next 10
- Continue until all files processed

**Prompt Template for Each Agent**:
```markdown
You are a sub-chapter-editor agent. Your task is to edit and proofread a content file.

**Input**:
- File to edit: {file_to_edit}
- Full path: {folder_path}/{file_to_edit}

**Instructions**:
1. Read the entire file
2. Apply all editing rules from editing-content skill
3. Save changes directly to the file (no backup needed - user has backup)
4. Write in FORMAL BAHASA INDONESIA

Key edits to make:
- Add ### file title with chapter notation
- Convert Roman numerals (I, II, III) to alphabetic headings (A, B, C) with ####
  - Skip for FR (form) files that are pure tables
- Fix OCR errors
- Italicize foreign terms
- Fix typos and grammar
- Improve clarity minimally
- Fix bullet points/numbering

Refer to skill: .claude/skills/editing-content/SKILL.md
```

**Step 8**: Track batch progress with TodoWrite
```python
# After each batch completes
update_todo_message(f"Editing content files: Batch {batch_num}/{total_batches} completed")

# After all batches complete
update_todo("Edit X content files", "completed")
```

---

## Phase 3: Validation and Reporting

**Step 9**: Validate results
- Check all x.x.0 files were created
- Verify file count matches manifest
- Spot-check a few edited files for formatting

**Step 10**: Create completion report
```markdown
# Bab Composition Report - Chapter {chapter_number}

Date: {current_date}
Folder: {folder_path}

## Summary
- Introduction files created: {created_count}/{expected_count}
- Content files edited: {edited_count}/{expected_count}
- Total files processed: {total_count}

## Phase 1: Introduction Files
{list of created x.x.0 files}

## Phase 2: Content Editing
{list of edited files, organized by batch}

## Validation
- ✅ All introduction files created successfully
- ✅ All content files edited successfully
- ✅ Formatting standards applied consistently
- ✅ FORMAL BAHASA INDONESIA used throughout

## Next Steps
- Review sample files for quality
- Proceed to .docx conversion when ready
```

**Step 11**: Update final TodoWrite status
```python
update_todo("Validate all files and create report", "completed")
```

---

## Parallelization Rules

### Maximum Concurrency
- **Hard limit**: 10 agents at a time
- **Reasoning**: Balance between speed and resource usage

### Batch Processing
1. Divide work into batches of 10
2. Launch all agents in a batch with single message
3. Wait for batch completion before next batch
4. Use TodoWrite to track batch progress

### Example Batch Launch (Single Message)
```markdown
I'm launching 10 sub-chapter-editor agents in parallel to edit Batch 1 files.

[Task tool call 1: edit file 1]
[Task tool call 2: edit file 2]
[Task tool call 3: edit file 3]
...
[Task tool call 10: edit file 10]
```

---

## Error Handling

### Agent Failures
- If an agent fails, note the failure in TodoWrite
- Continue with other agents
- Report failures in final report
- User can manually fix failed files

### Missing Files
- If source files don't exist, skip creation
- Log warning in report
- Don't halt entire process

### Validation Failures
- If validation finds issues, report them
- Don't mark todos as completed until issues resolved

---

## Important Notes

### Direct File Editing
- All edits are made directly to source files
- User has already created backups
- No need to ask for confirmation

### No Skill/Agent Creation
- Don't create new skills or agents during execution
- Use existing sub-chapter-previewer and sub-chapter-editor agents
- Refer to their respective skills

### Progress Visibility
- Use TodoWrite actively throughout process
- Update status as each phase completes
- Provide clear progress indication to user

### Language Requirement
- All text must be in **FORMAL BAHASA INDONESIA**
- This applies to both introduction files and edited content
- Maintain professional, official tone

---

**Created by**: Claude Code
**Purpose**: Guide main agent orchestration
**Status**: READY FOR USE
