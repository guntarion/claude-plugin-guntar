# Update CHANGELOG Skill

Personal skill for maintaining CHANGELOG.md across projects.

## Purpose

Automatically updates CHANGELOG.md with git commit messages and timestamps. New entries are prepended to the top (most recent first).

## Usage

```bash
python ~/.claude/skills/update-changelog/update-changelog.py "commit message" ["timestamp"]
```

## Examples

```bash
# With automatic timestamp
python ~/.claude/skills/update-changelog/update-changelog.py "feat: add new feature"

# With custom timestamp
python ~/.claude/skills/update-changelog/update-changelog.py "fix: bug fix" "2025-11-23 14:30:00"
```

## Integration

This skill is designed to be called from slash commands:
- `/commit` - Creates git commit and updates CHANGELOG.md
- `/commit-push` - Creates git commit, updates CHANGELOG.md, and pushes to remote

## Copying to Other Projects

This is a personal skill stored in `~/.claude/skills/` and can be accessed from any project. No need to copy - just reference the full path in slash commands or scripts.

## Output Format

```markdown
## 2025-11-23 14:30:00

feat: add new feature

---

## 2025-11-22 10:15:00

fix: bug fix

---
```

Most recent entries appear at the top of CHANGELOG.md.
