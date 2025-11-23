---
name: update-changelog
description: Updates CHANGELOG.md with git commit messages and timestamps. Prepends entries at the top (most recent first). Automatically called by /commit and /commit-push slash commands to maintain project changelog.
---

# Update CHANGELOG

Updates CHANGELOG.md by prepending git commit messages with timestamps at the top of the file.

## Quick Start

```bash
python ~/.claude/skills/update-changelog/update-changelog.py "commit message" "timestamp"
```

**For detailed documentation**, see [reference.md](./reference.md)
**For integration details**, see [README.md](./README.md)
