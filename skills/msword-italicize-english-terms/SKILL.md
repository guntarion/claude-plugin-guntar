---
name: msword-italicize-english-terms
description: Automatically italicizes English terms in Bahasa Indonesia Word documents based on CSV term list. Smart sorting prevents partial matches, preserves formatting, sets language to English, and disables spell check. Activate when user asks to italicize English terms in Indonesian documents.
---

# Italicize English Terms in Word Documents

Automatically italicizes English terms in Indonesian language Word documents using a CSV-based term list. Preserves formatting and handles smart matching.

## Quick Start

```bash
source .venv/bin/activate
python .claude/skills/msword-italicize-english-terms/msword-italicize-english-terms.py <terms.csv> <input.docx> [output.docx]
```

**For detailed documentation**, see [reference.md](./reference.md)
**For script details**, see [README.md](./README.md)
