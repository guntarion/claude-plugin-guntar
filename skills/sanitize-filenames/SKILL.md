---
name: sanitize-filenames
description: Sanitizes filenames and folder names by replacing spaces with underscores, removing unsafe characters, and deduplicating symbols. Supports single files, multiple files, folders, and pattern matching. Activate when user asks to clean/sanitize/fix filenames.
---

# Sanitize Filenames and Folder Names

Sanitizes filenames by replacing spaces with underscores, removing unsafe characters, and deduplicating symbols for filesystem safety.

## Quick Start

```bash
source .venv/bin/activate
python .claude/skills/sanitize-filenames/sanitize-filenames.py <file_or_folder> [pattern]
```

**For detailed documentation**, see [reference.md](./reference.md)
