# Update Progress Log - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Features](#features)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Examples](#examples)
6. [Integration with Slash Commands](#integration-with-slash-commands)
7. [Output Format](#output-format)
8. [Tips](#tips)

## When to Use This Skill

Use this skill when you need to:
- Track daily progress on projects
- Maintain a chronological log of work activities
- Record implementation notes and decisions
- Document blockers and solutions
- Keep stakeholders informed of progress

This skill is **automatically invoked** by:
- `/progress` slash command

## Features

- **Automatic prepending**: New entries added at the top (most recent first)
- **Timestamp support**: Records exact time of entry
- **File creation**: Creates PROGRESS.md if it doesn't exist
- **Portable**: Global skill accessible from any project
- **Simple format**: Markdown-formatted with clear separators

## Usage

### Command Syntax

```bash
python ~/.claude/skills/update-progresslog/update-progresslog.py <progress_note> [timestamp]
```

### Parameters

- `progress_note` (required): The progress note to add
- `timestamp` (optional): Custom timestamp. If not provided, uses current time

### Direct Invocation

```bash
# With automatic timestamp
python ~/.claude/skills/update-progresslog/update-progresslog.py "Currently working on LDAP auth"

# With custom timestamp
python ~/.claude/skills/update-progresslog/update-progresslog.py "Completed API integration" "2025-11-23 14:30:00"
```

### Via Slash Commands

The skill is automatically called when using:
- `/progress "note"` - Records progress entry in PROGRESS.md

## How It Works

1. **Receives progress note and timestamp** (or generates current time)
2. **Reads existing PROGRESS.md** (if it exists in current working directory)
3. **Creates new entry** with format:
   ```markdown
   ## YYYY-MM-DD HH:MM:SS

   progress note

   ---
   ```
4. **Prepends entry** to beginning of file (most recent first)
5. **Writes back** to PROGRESS.md in project root

## Examples

### Example 1: Starting New Task

**Input:**
```bash
python ~/.claude/skills/update-progresslog/update-progresslog.py "Starting work on LDAP authentication module"
```

**Output in PROGRESS.md:**
```markdown
## 2025-11-23 15:30:00

Starting work on LDAP authentication module

---
```

### Example 2: Recording Blocker

**Input:**
```bash
python ~/.claude/skills/update-progresslog/update-progresslog.py "Blocked on LDAP integration - waiting for IT to provide test credentials"
```

**Output in PROGRESS.md:**
```markdown
## 2025-11-23 16:15:00

Blocked on LDAP integration - waiting for IT to provide test credentials

---

## 2025-11-23 15:30:00

Starting work on LDAP authentication module

---
```

### Example 3: Multiple Progress Updates

**PROGRESS.md after several entries:**
```markdown
## 2025-11-23 17:00:00

LDAP auth completed and tested. See /docs/ldap for configuration details

---

## 2025-11-23 16:45:00

Received test credentials from IT. Resuming LDAP integration

---

## 2025-11-23 16:15:00

Blocked on LDAP integration - waiting for IT to provide test credentials

---

## 2025-11-23 15:30:00

Starting work on LDAP authentication module

---
```

## Integration with Slash Commands

### /progress Command

The `/progress` slash command automatically calls this skill:

```bash
python ~/.claude/skills/update-progresslog/update-progresslog.py "$ARGUMENTS" "$(date '+%Y-%m-%d %H:%M:%S')"
```

Usage:
```
/progress "Currently working on API endpoint refactoring"
```

## Output Format

### Timestamp Header
```markdown
## YYYY-MM-DD HH:MM:SS
```

### Progress Note Body
```markdown
progress note (can be multi-line)
```

### Separator
```markdown
---
```

### Complete Entry Example
```markdown
## 2025-11-23 15:30:00

Currently working on LDAP auth. See folder /docs/ldap for detail.
Testing connection with dev server.

---
```

## Tips

### Best Practices

1. **Use descriptive notes**: Include context, decisions made, and next steps
2. **Reference files/folders**: Help future you find related work quickly
3. **Record blockers immediately**: Document what's blocking and why
4. **Daily summaries**: Add end-of-day summary of accomplishments
5. **Link to commits**: Reference relevant commit SHAs for code changes

### Example Progress Notes

**Good:**
```
Currently working on LDAP auth. See folder /docs/ldap for detail.
Implemented basic connection pooling and added retry logic.
Next: Add integration tests
```

**Better:**
```
LDAP Integration Progress:
- Implemented connection pooling (see src/auth/ldap.ts)
- Added retry logic with exponential backoff
- Fixed memory leak in connection cleanup (commit: a1b2c3d)
Next steps:
- Add integration tests
- Update documentation
- Request code review from @security team
```

### Common Use Cases

**Daily standup prep:**
```bash
/progress "Yesterday: Completed API endpoints. Today: Working on frontend integration. Blockers: None"
```

**Documenting decisions:**
```bash
/progress "Decision: Using JWT instead of sessions for auth. Rationale: Better for microservices. See ADR-003"
```

**Tracking debugging:**
```bash
/progress "Debugging memory leak in worker process. Profiled with heapdump. Issue identified in event listener cleanup"
```

### Version Control

- Add PROGRESS.md to your git repository
- Include in commits to share progress with team
- Most recent changes always at the top for easy review
- Great for async teams to stay in sync

### Privacy

- PROGRESS.md stays in project directory
- Not automatically shared (unless committed to git)
- Use for personal tracking or team transparency

## Related Skills

- `/progress` - Record progress entry in PROGRESS.md
- `update-changelog` - Update CHANGELOG.md with git commits
- `create-claude-slash-commands` - Create custom slash commands
