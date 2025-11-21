#!/usr/bin/env python3
"""Debug script to find all citations in a document."""

import sys
import re
from pathlib import Path
from docx import Document

def find_citations_in_text(text):
    """Find all citation patterns in text."""
    # Pattern 1: .[123] (what we're looking for)
    pattern1 = r'\.(\[\d{1,3}\])'
    matches1 = re.findall(pattern1, text)

    # Pattern 2: Just [123] anywhere
    pattern2 = r'\[\d{1,3}\]'
    matches2 = re.findall(pattern2, text)

    return matches1, matches2

def analyze_document(doc_path):
    """Analyze document for citations."""
    doc = Document(str(doc_path))

    total_para_citations = []
    total_all_citations = []

    print(f"Analyzing: {doc_path.name}\n")

    # Check paragraphs
    for idx, para in enumerate(doc.paragraphs[:50], 1):  # First 50 paragraphs
        text = para.text
        cit1, cit2 = find_citations_in_text(text)

        if cit2:  # Has any citations
            total_para_citations.extend(cit1)
            total_all_citations.extend(cit2)
            print(f"Para {idx}: Found {len(cit2)} citations")
            print(f"  Text snippet: ...{text[-80:]}")

            # Show runs
            print(f"  Runs ({len(para.runs)}):")
            for run_idx, run in enumerate(para.runs):
                if run.text:
                    print(f"    Run {run_idx}: '{run.text}'")
            print()

    print(f"\n{'='*60}")
    print(f"Summary (first 50 paragraphs):")
    print(f"  Citations with .[n] pattern: {len(total_para_citations)}")
    print(f"  Total citation brackets found: {len(total_all_citations)}")
    print(f"  Citations: {total_all_citations[:20]}")  # First 20
    print(f"{'='*60}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python debug-citations.py <file.docx>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    analyze_document(file_path)
