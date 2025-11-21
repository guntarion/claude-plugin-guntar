# SOP Files Analyzer - Documentation

## Purpose

Analyzes SOP (Standard Operating Procedure) documents in a source folder to create a comprehensive work manifest for the SOP improvement workflow. This script is the first step in the chapter-composer agent's orchestration process.

## Usage

```bash
source .venv/bin/activate && python python_scripts/17-analyze-sop-files.py <folder_path>
```

## Example

```bash
python python_scripts/17-analyze-sop-files.py ./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/dokumen-asli
```

## What It Does

The script performs comprehensive analysis of SOP documents:

### 1. File Discovery
- Scans folder for PDF and MD files
- Counts total files by type
- Provides file inventory

### 2. Document Classification
Classifies each document into types:
- **IK** (Instruksi Kerja) - Work Instructions
- **PF** (Prosedur Fungsi) - Functional Procedures
- **FR** (Formulir) - Forms and Checklists
- **BP** (Business Process) - Process Diagrams
- **SOP** (Standard Operating Procedure) - General SOPs
- **UNKNOWN** - Cannot classify

Classification based on:
- Filename patterns (e.g., "IK Document.md")
- Content analysis (first 200 characters for keywords)

### 3. Section Analysis (MD files only)
Checks for required sections (A-H):
- A. Tujuan (Purpose)
- B. Ruang Lingkup (Scope)
- C. Referensi (References)
- D. Istilah dan Definisi (Terms and Definitions)
- E. Perlengkapan Kerja (Work Equipment)
- F. Peralatan K3 (Safety Equipment)
- G. Material (Materials)
- H. Langkah Kerja dan Tindakan (Work Steps)

Reports:
- Sections found
- Sections missing

### 4. Unit-Specific Reference Detection
Identifies references that need generalization:
- "UPDL [Location]" (e.g., UPDL Palembang, UPDL Semarang)
- "Kepala [Role] UPDL [Location]"
- "UDPL" (common typo for UPDL)

### 5. OCR Error Detection
Detects common OCR error patterns:
- Words with `=` in them (penda=aran)
- Words with `>` in them (menempa>)
- Words with `?` in them (veri?kasi)
- Common misspellings (LOUNDRY, PANGADAAN, pda)

Reports:
- Line number
- Error pattern type
- Line context (first 80 characters)

### 6. Duplicate Detection
Identifies potential duplicate documents based on:
- Similar keywords in filenames
- Common topics
- Overlapping content indicators

Groups files that may need merging.

## Output

### JSON Manifest

**Location**: `[parent_folder]/0A-rencana-improvement/sop-analysis-manifest.json`

**Structure**:
```json
{
  "analysis_info": {
    "source_folder": "./BUKU-2/.../dokumen-asli",
    "analysis_date": "2025-01-20T10:30:00",
    "total_files": 9,
    "pdf_files": 2,
    "md_files": 7
  },
  "files": [
    {
      "filename": "IK PENGELOLAAN.md",
      "path": "...",
      "document_type": "IK",
      "sections": {
        "found": ["E. Perlengkapan Kerja", "H. Langkah Kerja"],
        "missing": ["A. Tujuan", "B. Ruang Lingkup", "C. Referensi", "D. Istilah dan Definisi"]
      },
      "unit_references": [],
      "ocr_errors": [],
      "needs_improvement": true,
      "improvement_tasks": [
        "Add missing section: A. Tujuan",
        "Add missing section: B. Ruang Lingkup",
        ...
      ]
    },
    ...
  ],
  "duplicate_groups": [
    {
      "group_id": 1,
      "keyword": "pengelolaan",
      "files": ["IK PENGELOLAAN.md", "PF PENGELOLAAN.md"],
      "reason": "Similar topic: Pengelolaan",
      "recommendation": "Review for potential merge"
    }
  ],
  "statistics": {
    "by_type": {
      "IK": 3,
      "PF": 3,
      "SOP": 1,
      "BP": 2
    },
    "needs_improvement": 7,
    "complete_documents": 2,
    "missing_sections_total": 12,
    "unit_references_total": 8,
    "ocr_errors_total": 3
  },
  "recommendations": {
    "merge_candidates": 2,
    "create_from_scratch": 0,
    "improvement_priority": "high",
    "estimated_agents_needed": 7
  }
}
```

### Console Output

```
Analyzing SOP files in: ./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/dokumen-asli

============================================================
SOP ANALYSIS COMPLETE
============================================================
Source Folder: ./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/dokumen-asli
Total Files: 9 (7 MD, 2 PDF)

DOCUMENT TYPES:
  IK (Instruksi Kerja)              3
  PF (Prosedur Fungsi)              3
  SOP (Standard Operating)          1
  BP (Business Process)             2

ANALYSIS SUMMARY:
  Documents needing improvement: 7/9
  Complete documents:            2/9
  Missing sections total:        12
  Unit-specific references:      8
  OCR errors detected:           3
  Potential duplicate groups:    2

MERGE CANDIDATES:
  Group 1: IK PENGELOLAAN.md, PF PENGELOLAAN.md
           Reason: Similar topic: Pengelolaan
  Group 2: IK SIRKULASI.md, SOP_Peminjaman.md
           Reason: Similar topic: Peminjaman

NEXT STEPS:
  1. Review manifest: ./0A-rencana-improvement/sop-analysis-manifest.json
  2. Create improvement plan
  3. Launch sop-content-improver agents
  4. Estimated agents needed: 7

============================================================
Ready for SOP improvement workflow!
============================================================
```

## Dependencies

- **Python 3.7+**
- **Standard library only** (no external dependencies):
  - `pathlib` - File system operations
  - `json` - JSON manifest creation
  - `re` - Pattern matching
  - `sys` - Command line arguments
  - `collections` - Data structures
  - `datetime` - Timestamps
  - `difflib` - Similarity matching

## How It Works

### Step 1: Discover Files
```python
pdf_files = folder.glob("*.pdf")
md_files = folder.glob("*.md")
```

### Step 2: Classify Documents
```python
def classify_document(filename, content):
    # Check filename patterns
    if 'IK ' in filename: return 'IK'
    if 'PF ' in filename: return 'PF'
    # Check content patterns
    if '**INSTRUKSI KERJA**' in content: return 'IK'
    # etc.
```

### Step 3: Analyze Sections
```python
# Pattern matching for each required section
patterns = {
    'tujuan': r'(?i)(I|A)\.?\s*\*{0,2}TUJUAN\*{0,2}',
    'ruang_lingkup': r'(?i)(II|B)\.?\s*\*{0,2}RUANG LINGKUP\*{0,2}',
    # etc.
}
```

### Step 4: Detect Unit References
```python
patterns = [
    r'UPDL\s+(?:PLN\s+)?([A-Z][a-z]+)',  # UPDL Palembang
    r'Kepala\s+\w+\s+UPDL\s+([A-Z][a-z]+)',  # Kepala X UPDL Y
]
```

### Step 5: Detect OCR Errors
```python
patterns = [
    (r'\w+[=]\w+', '= in word'),
    (r'\w+[>]\w+', '> in word'),
    (r'LOUNDRY', 'should be LAUNDRY'),
]
```

### Step 6: Detect Duplicates
```python
# Group files by keywords
# Find groups with 2+ files
# Report as merge candidates
```

### Step 7: Create Manifest
```python
manifest = {
    'analysis_info': {...},
    'files': [...],
    'duplicate_groups': [...],
    'statistics': {...},
    'recommendations': {...}
}
```

## Error Handling

### Folder Not Found
```
ERROR: Folder does not exist: [path]
Exit code: 1
```

### Not a Directory
```
ERROR: Not a directory: [path]
Exit code: 1
```

### No Files Found
```
WARNING: No PDF or MD files found in [path]
ERROR: No files found to analyze
Exit code: 1
```

### Invalid Arguments
```
ERROR: Invalid number of arguments
Usage: python python_scripts/17-analyze-sop-files.py <folder_path>
Exit code: 1
```

## Use Cases

### Standalone Use
Run script to analyze a folder of SOPs:
```bash
python python_scripts/17-analyze-sop-files.py ./BUKU-X/XX-TOPIC/dokumen-asli
```

Review the manifest:
```bash
cat ./BUKU-X/XX-TOPIC/0A-rencana-improvement/sop-analysis-manifest.json
```

### Integrated Use (by chapter-composer)
The chapter-composer agent automatically:
1. Runs this script on source folder
2. Reads the generated manifest
3. Creates improvement plan based on analysis
4. Launches sub-agents for improvement tasks

## Example Workflow

### 1. Analyze Files
```bash
$ python python_scripts/17-analyze-sop-files.py ./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/dokumen-asli

Analyzing SOP files in: ./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/dokumen-asli
...
Ready for SOP improvement workflow!
```

### 2. Review Manifest
```bash
$ cat ./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/0A-rencana-improvement/sop-analysis-manifest.json
```

### 3. chapter-composer Takes Over
The chapter-composer agent uses the manifest to:
- Create improvement plan
- Launch sop-content-improver agents (parallel)
- Launch sop-editor agents (parallel)
- Create structure and introductions
- Generate completion report

## Performance

- **Typical runtime**: < 5 seconds for 50 files
- **Memory usage**: Minimal (reads files one at a time)
- **Output size**: ~10-50 KB JSON (depends on file count)

## Limitations

### PDF Files
- Cannot analyze content (would require PDF parsing library)
- Classification based on filename only
- Marked as "needs improvement" automatically
- Recommendation: "Convert PDF to MD for analysis"

### Complex Formatting
- May miss sections with unusual formatting
- Pattern matching is strict but flexible
- Some edge cases may be missed

### Language Detection
- Assumes Indonesian language documents
- OCR patterns specific to Indonesian text
- May not detect errors in English sections

## Troubleshooting

### "No files found"
- Check folder path is correct
- Ensure folder contains .pdf or .md files
- Check file extensions (must be lowercase)

### "Folder does not exist"
- Verify path is correct
- Use absolute path if relative path fails
- Check folder name spelling

### Missing sections not detected
- Check section heading format in document
- Pattern matching may need adjustment
- Section may use non-standard format

### Duplicates not detected
- Requires similar keywords in filenames
- Very different filenames won't be grouped
- Manual review of files may be needed

## Extending the Script

### Add New Document Type
```python
def classify_document(filename, content):
    # Add new type check
    if 'LAPORAN' in filename_upper:
        return 'LAPORAN'
```

### Add New OCR Pattern
```python
def detect_ocr_errors(content):
    patterns = [
        # Add new pattern
        (r'newpattern', 'description'),
    ]
```

### Customize Section Patterns
```python
required_sections = {
    'new_section': {
        'patterns': [r'your_pattern'],
        'label': 'Z. New Section'
    }
}
```

## Related Documentation

- **Agent Definition**: `.claude/agents/chapter-composer.md`
- **Orchestration Skill**: `.claude/skills/sop-improvement-orchestration/SKILL.md`
- **Planning Documents**: `./prompts/claude-code-plans/sop-improver/`

---

**Created**: 2025-01-20
**Version**: 1.0
**Author**: Claude Code (Sonnet 4.5)
**Status**: Production Ready
