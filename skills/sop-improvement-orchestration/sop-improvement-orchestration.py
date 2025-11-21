#!/usr/bin/env python3
"""
SOP Files Analyzer
Analyzes SOP documents and creates work manifest for improvement workflow.

Usage:
    python python_scripts/17-analyze-sop-files.py <folder_path>

Example:
    python python_scripts/17-analyze-sop-files.py ./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/dokumen-asli
"""

from pathlib import Path
import json
import re
import sys
from collections import defaultdict, Counter
from datetime import datetime
from difflib import SequenceMatcher


def classify_document(filename: str, content: str = None) -> str:
    """
    Classify document type based on filename and content

    Types:
    - IK: Instruksi Kerja
    - PF: Prosedur Fungsi
    - FR: Formulir/Form
    - BP: Business Process
    - SOP: Standard Operating Procedure
    - UNKNOWN: Cannot classify
    """
    filename_upper = filename.upper()

    # Check filename first
    if 'IK ' in filename_upper or filename_upper.startswith('IK-') or filename_upper.startswith('IK_'):
        return 'IK'
    if 'PF ' in filename_upper or filename_upper.startswith('PF-') or filename_upper.startswith('PF_'):
        return 'PF'
    if 'FR ' in filename_upper or filename_upper.startswith('FR-') or filename_upper.startswith('FR_'):
        return 'FR'
    if 'FORMULIR' in filename_upper or 'FORM' in filename_upper or 'CHECKLIST' in filename_upper:
        return 'FR'
    if 'BPM' in filename_upper or 'DIAGRAM' in filename_upper or 'PROSES BISNIS' in filename_upper:
        return 'BP'
    if 'SOP' in filename_upper:
        return 'SOP'

    # Check content if available
    if content:
        content_upper = content.upper()
        if '**INSTRUKSI KERJA**' in content_upper or 'INSTRUKSI KERJA' in content_upper[:200]:
            return 'IK'
        if '**PROSEDUR' in content_upper or 'PROSEDUR FUNGSI' in content_upper[:200]:
            return 'PF'
        if 'FORMULIR' in content_upper[:200] or '| ' in content[:500]:  # Table indicator
            return 'FR'
        if 'SOP' in content_upper[:200] or 'STANDARD OPERATING PROCEDURE' in content_upper[:200]:
            return 'SOP'

    return 'UNKNOWN'


def analyze_sections(content: str) -> dict:
    """
    Analyze markdown content for required sections

    Returns:
        dict with section presence information
    """
    required_sections = {
        'tujuan': {
            'patterns': [
                r'(?i)(I{1,3}|A|\d+)\.?\s*\*{0,2}TUJUAN\*{0,2}',
                r'(?i)#{1,4}\s*(I{1,3}|A|\d+)\.?\s*Tujuan',
            ],
            'label': 'A. Tujuan'
        },
        'ruang_lingkup': {
            'patterns': [
                r'(?i)(I{1,3}|B|\d+)\.?\s*\*{0,2}RUANG LINGKUP\*{0,2}',
                r'(?i)#{1,4}\s*(I{1,3}|B|\d+)\.?\s*Ruang Lingkup',
            ],
            'label': 'B. Ruang Lingkup'
        },
        'referensi': {
            'patterns': [
                r'(?i)(I{1,3}|C|\d+)\.?\s*\*{0,2}(REFERENSI|DASAR HUKUM)\*{0,2}',
                r'(?i)#{1,4}\s*(I{1,3}|C|\d+)\.?\s*(Referensi|Dasar Hukum)',
            ],
            'label': 'C. Referensi'
        },
        'istilah_definisi': {
            'patterns': [
                r'(?i)(I{1,3}|D|\d+)\.?\s*\*{0,2}(ISTILAH|DEFINISI)\*{0,2}',
                r'(?i)#{1,4}\s*(I{1,3}|D|\d+)\.?\s*(Istilah|Definisi)',
            ],
            'label': 'D. Istilah dan Definisi'
        },
        'perlengkapan': {
            'patterns': [
                r'(?i)(I{1,3}|E|\d+)\.?\s*\*{0,2}(PERLENGKAPAN|PERALATAN KERJA)\*{0,2}',
                r'(?i)#{1,4}\s*(I{1,3}|E|\d+)\.?\s*(Perlengkapan|Peralatan Kerja)',
            ],
            'label': 'E. Perlengkapan Kerja'
        },
        'k3': {
            'patterns': [
                r'(?i)(I{1,3}|F|\d+)\.?\s*\*{0,2}PERALATAN K3\*{0,2}',
                r'(?i)#{1,4}\s*(I{1,3}|F|\d+)\.?\s*Peralatan K3',
            ],
            'label': 'F. Peralatan K3'
        },
        'material': {
            'patterns': [
                r'(?i)(I{1,3}|G|\d+)\.?\s*\*{0,2}MATERIAL\*{0,2}',
                r'(?i)#{1,4}\s*(I{1,3}|G|\d+)\.?\s*Material',
            ],
            'label': 'G. Material'
        },
        'langkah_kerja': {
            'patterns': [
                r'(?i)(I{1,3}|H|\d+)\.?\s*\*{0,2}(LANGKAH KERJA|URAIAN KEGIATAN|PROSEDUR)\*{0,2}',
                r'(?i)#{1,4}\s*(I{1,3}|H|\d+)\.?\s*(Langkah Kerja|Uraian Kegiatan|Prosedur)',
            ],
            'label': 'H. Langkah Kerja dan Tindakan'
        }
    }

    result = {
        'found': [],
        'missing': []
    }

    for section_key, section_info in required_sections.items():
        found = False
        for pattern in section_info['patterns']:
            if re.search(pattern, content):
                found = True
                break

        if found:
            result['found'].append(section_info['label'])
        else:
            result['missing'].append(section_info['label'])

    return result


def detect_unit_references(content: str) -> list:
    """
    Detect unit-specific references that need generalization

    Returns:
        List of unit-specific references found
    """
    patterns = [
        # UPDL with location
        (r'UPDL\s+(?:PLN\s+)?([A-Z][a-z]+)', r'UPDL \1'),
        # Role titles with UPDL location
        (r'(Kepala|Manajer|Manager|Petugas)\s+\w+\s+UPDL\s+(?:PLN\s+)?([A-Z][a-z]+)', r'\1 ... UPDL \2'),
        # Common typo
        (r'UDPL', 'UDPL (should be UPDL)'),
    ]

    references = []
    for pattern, description in patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            ref = match.group(0)
            if ref not in references:
                references.append(ref)

    return references


def detect_ocr_errors(content: str) -> list:
    """
    Detect common OCR error patterns

    Returns:
        List of potential OCR errors with line context
    """
    patterns = [
        (r'\w+[=]\w+', '= in word'),
        (r'\w+[>]\w+', '> in word'),
        (r'\w+[?]\w+', '? in word'),
        (r'\w+[<]\w+', '< in word'),
        (r'LOUNDRY', 'LOUNDRY (should be LAUNDRY)'),
        (r'UDPL(?!\s)', 'UDPL (should be UPDL)'),
        (r'\bpda\b', 'pda (should be pada)'),
        (r'PANGADAAN', 'PANGADAAN (should be PENGADAAN)'),
    ]

    errors = []
    lines = content.split('\n')

    for i, line in enumerate(lines, 1):
        for pattern, description in patterns:
            if re.search(pattern, line):
                errors.append({
                    'line': i,
                    'pattern': description,
                    'context': line.strip()[:80]  # First 80 chars
                })

    return errors


def detect_duplicates(files_info: list) -> list:
    """
    Detect potential duplicate documents

    Returns:
        List of duplicate groups
    """
    # Group by similar keywords in filename
    keyword_groups = defaultdict(list)

    for file_info in files_info:
        filename = file_info['filename']
        # Extract keywords
        words = re.findall(r'[A-Z][a-z]+', filename)
        keywords = ' '.join(words).lower()

        # Group by keywords
        for word in words:
            if len(word) > 3:  # Only meaningful words
                keyword_groups[word.lower()].append(file_info)

    # Find groups with multiple files
    duplicate_groups = []
    group_id = 1

    for keyword, files in keyword_groups.items():
        if len(files) >= 2:
            filenames = [f['filename'] for f in files]
            duplicate_groups.append({
                'group_id': group_id,
                'keyword': keyword,
                'files': filenames,
                'reason': f"Similar topic: {keyword.capitalize()}",
                'recommendation': "Review for potential merge"
            })
            group_id += 1

    # Remove duplicates in duplicate_groups (same file set)
    seen = set()
    unique_groups = []
    for group in duplicate_groups:
        file_set = frozenset(group['files'])
        if file_set not in seen:
            seen.add(file_set)
            unique_groups.append(group)

    return unique_groups


def analyze_sop_files(folder_path: Path) -> dict:
    """
    Analyze SOP folder and create work manifest

    Returns:
        dict with analysis results
    """
    # Discover files
    pdf_files = list(folder_path.glob("*.pdf"))
    md_files = list(folder_path.glob("*.md"))

    total_files = len(pdf_files) + len(md_files)

    if total_files == 0:
        print(f"WARNING: No PDF or MD files found in {folder_path}")
        return None

    # Analyze each file
    files_info = []

    # Analyze MD files (can read content)
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except:
            content = ""

        doc_type = classify_document(md_file.name, content)
        sections = analyze_sections(content) if content else {'found': [], 'missing': []}
        unit_refs = detect_unit_references(content) if content else []
        ocr_errors = detect_ocr_errors(content) if content else []

        # Determine improvement tasks
        improvement_tasks = []
        for missing_section in sections['missing']:
            improvement_tasks.append(f"Add missing section: {missing_section}")
        for ref in unit_refs:
            improvement_tasks.append(f"Generalize: {ref}")
        if ocr_errors:
            improvement_tasks.append(f"Fix {len(ocr_errors)} OCR errors")

        needs_improvement = len(improvement_tasks) > 0

        files_info.append({
            'filename': md_file.name,
            'path': str(md_file),
            'document_type': doc_type,
            'sections': sections,
            'unit_references': unit_refs,
            'ocr_errors': ocr_errors,
            'needs_improvement': needs_improvement,
            'improvement_tasks': improvement_tasks
        })

    # Analyze PDF files (limited - can't read content)
    for pdf_file in pdf_files:
        doc_type = classify_document(pdf_file.name)

        files_info.append({
            'filename': pdf_file.name,
            'path': str(pdf_file),
            'document_type': doc_type,
            'sections': {'found': [], 'missing': []},
            'unit_references': [],
            'ocr_errors': [],
            'needs_improvement': True,
            'improvement_tasks': ["Convert PDF to MD for analysis"],
            'note': "PDF file - content analysis skipped"
        })

    # Detect duplicates
    duplicate_groups = detect_duplicates(files_info)

    # Statistics
    type_counts = Counter([f['document_type'] for f in files_info])
    needs_improvement_count = sum(1 for f in files_info if f['needs_improvement'])
    complete_count = total_files - needs_improvement_count
    missing_sections_total = sum(len(f['sections']['missing']) for f in files_info)
    unit_refs_total = sum(len(f['unit_references']) for f in files_info)
    ocr_errors_total = sum(len(f['ocr_errors']) for f in files_info)

    # Build manifest
    manifest = {
        'analysis_info': {
            'source_folder': str(folder_path),
            'analysis_date': datetime.now().isoformat(),
            'total_files': total_files,
            'pdf_files': len(pdf_files),
            'md_files': len(md_files)
        },
        'files': files_info,
        'duplicate_groups': duplicate_groups,
        'statistics': {
            'by_type': dict(type_counts),
            'needs_improvement': needs_improvement_count,
            'complete_documents': complete_count,
            'missing_sections_total': missing_sections_total,
            'unit_references_total': unit_refs_total,
            'ocr_errors_total': ocr_errors_total
        },
        'recommendations': {
            'merge_candidates': len(duplicate_groups),
            'create_from_scratch': 0,  # Will be determined by chapter-composer
            'improvement_priority': 'high' if needs_improvement_count > total_files * 0.5 else 'medium',
            'estimated_agents_needed': needs_improvement_count
        }
    }

    return manifest


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("ERROR: Invalid number of arguments")
        print("\nUsage:")
        print("  python python_scripts/17-analyze-sop-files.py <folder_path>")
        print("\nExample:")
        print("  python python_scripts/17-analyze-sop-files.py ./BUKU-2/14-PENGELOLAAN-PERPUSTAKAAN-(UPDL-PALEMBANG)/dokumen-asli")
        sys.exit(1)

    folder_arg = sys.argv[1]
    folder_path = Path(folder_arg)

    # Validate folder exists
    if not folder_path.exists():
        print(f"ERROR: Folder does not exist: {folder_path}")
        sys.exit(1)

    if not folder_path.is_dir():
        print(f"ERROR: Not a directory: {folder_path}")
        sys.exit(1)

    print(f"Analyzing SOP files in: {folder_path}")

    # Analyze files
    manifest = analyze_sop_files(folder_path)

    if not manifest:
        print("ERROR: No files found to analyze")
        sys.exit(1)

    # Create output folder
    parent_folder = folder_path.parent
    output_folder = parent_folder / "0A-rencana-improvement"
    output_folder.mkdir(exist_ok=True)

    # Write manifest
    output_path = output_folder / "sop-analysis-manifest.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # Print summary
    stats = manifest['statistics']
    print("\n" + "=" * 60)
    print("SOP ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"Source Folder: {manifest['analysis_info']['source_folder']}")
    print(f"Total Files: {manifest['analysis_info']['total_files']} " +
          f"({manifest['analysis_info']['md_files']} MD, {manifest['analysis_info']['pdf_files']} PDF)")
    print()
    print("DOCUMENT TYPES:")
    for doc_type, count in stats['by_type'].items():
        type_labels = {
            'IK': 'IK (Instruksi Kerja)',
            'PF': 'PF (Prosedur Fungsi)',
            'FR': 'FR (Formulir)',
            'BP': 'BP (Business Process)',
            'SOP': 'SOP (Standard Operating)',
            'UNKNOWN': 'UNKNOWN'
        }
        label = type_labels.get(doc_type, doc_type)
        print(f"  {label:30} {count}")
    print()
    print("ANALYSIS SUMMARY:")
    print(f"  Documents needing improvement: {stats['needs_improvement']}/{manifest['analysis_info']['total_files']}")
    print(f"  Complete documents:            {stats['complete_documents']}/{manifest['analysis_info']['total_files']}")
    print(f"  Missing sections total:        {stats['missing_sections_total']}")
    print(f"  Unit-specific references:      {stats['unit_references_total']}")
    print(f"  OCR errors detected:           {stats['ocr_errors_total']}")
    print(f"  Potential duplicate groups:    {len(manifest['duplicate_groups'])}")

    if manifest['duplicate_groups']:
        print()
        print("MERGE CANDIDATES:")
        for group in manifest['duplicate_groups'][:5]:  # Show first 5
            print(f"  Group {group['group_id']}: {', '.join(group['files'][:2])}" +
                  (f", +{len(group['files'])-2} more" if len(group['files']) > 2 else ""))
            print(f"             Reason: {group['reason']}")
        if len(manifest['duplicate_groups']) > 5:
            print(f"  ... and {len(manifest['duplicate_groups']) - 5} more groups")

    print()
    print("NEXT STEPS:")
    print("  1. Review manifest: " + str(output_path))
    print("  2. Create improvement plan")
    print("  3. Launch sop-content-improver agents")
    print(f"  4. Estimated agents needed: {manifest['recommendations']['estimated_agents_needed']}")
    print()
    print("=" * 60)
    print("Ready for SOP improvement workflow!")
    print("=" * 60)


if __name__ == "__main__":
    main()
