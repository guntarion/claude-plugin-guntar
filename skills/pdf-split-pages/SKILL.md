---
name: pdf-split-pages
description: Splits PDF files into multiple parts. Supports page ranges (extract pages x-y to new PDF), per-page splitting (one PDF per page), and CSV-based splitting for batch operations. Uses pypdf library. Activate when user asks to split/extract/divide PDFs.
---

# Split PDF Files

Splits PDF files into multiple parts using page ranges, per-page splitting, or CSV-based batch operations.

## Quick Start

```bash
source .venv/bin/activate
python .claude/skills/pdf-split-pages/pdf-split-pages.py <input.pdf> <mode> [options]
```

**For detailed documentation**, see [reference.md](./reference.md)
