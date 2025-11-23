# Update Progress Log Skill

Personal skill for maintaining PROGRESS.md across projects.

## Purpose

Automatically updates PROGRESS.md with progress notes and timestamps. New entries are prepended to the top (most recent first).

## Usage

```bash
python ~/.claude/skills/update-progresslog/update-progresslog.py "progress note" ["timestamp"]
```

## Examples

```bash
# With automatic timestamp
python ~/.claude/skills/update-progresslog/update-progresslog.py "Currently working on LDAP auth"

# With custom timestamp
python ~/.claude/skills/update-progresslog/update-progresslog.py "Completed API integration" "2025-11-23 14:30:00"
```

## Integration

This skill is designed to be called from the `/progress` slash command:
- `/progress "note"` - Records progress entry in PROGRESS.md

## Copying to Other Projects

This is a personal skill stored in `~/.claude/skills/` and can be accessed from any project. No need to copy - just reference the full path in slash commands or scripts.

## Output Format

```markdown
## 2025-11-23 14:30:00

Currently working on LDAP auth. See folder /docs/ldap for detail

---

## 2025-11-22 10:15:00

Completed user authentication module

---
```

Most recent entries appear at the top of PROGRESS.md.
