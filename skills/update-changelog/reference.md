# Update CHANGELOG - Reference Guide

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
- Maintain a CHANGELOG.md file automatically with git commits
- Track project changes with timestamps
- Have most recent changes appear first in changelog
- Integrate changelog updates with git workflow

This skill is **automatically invoked** by:
- `/commit` slash command
- `/commit-push` slash command

## Features

- **Automatic prepending**: New entries added at the top (most recent first)
- **Timestamp support**: Records exact time of commit
- **File creation**: Creates CHANGELOG.md if it doesn't exist
- **Portable**: Global skill accessible from any project
- **Simple format**: Markdown-formatted with clear separators

## Usage

### Command Syntax

```bash
python ~/.claude/skills/update-changelog/update-changelog.py <commit_message> [timestamp]
```

### Parameters

- `commit_message` (required): The git commit message
- `timestamp` (optional): Custom timestamp. If not provided, uses current time

### Direct Invocation

```bash
# With automatic timestamp
python ~/.claude/skills/update-changelog/update-changelog.py "feat: add new feature"

# With custom timestamp
python ~/.claude/skills/update-changelog/update-changelog.py "fix: bug fix" "2025-11-23 14:30:00"
```

### Via Slash Commands

The skill is automatically called when using:
- `/commit` - Commits and updates CHANGELOG.md
- `/commit-push` - Commits, updates CHANGELOG.md, and pushes to remote

## How It Works

1. **Receives commit message and timestamp** (or generates current time)
2. **Reads existing CHANGELOG.md** (if it exists in current working directory)
3. **Creates new entry** with format:
   ```markdown
   ## YYYY-MM-DD HH:MM:SS

   commit message

   ---
   ```
4. **Prepends entry** to beginning of file (most recent first)
5. **Writes back** to CHANGELOG.md in project root

## Examples

### Example 1: Feature Addition

**Input:**
```bash
python ~/.claude/skills/update-changelog/update-changelog.py "feat: add user authentication system"
```

**Output in CHANGELOG.md:**
```markdown
## 2025-11-23 15:30:00

feat: add user authentication system

---
```

### Example 2: Bug Fix with Custom Timestamp

**Input:**
```bash
python ~/.claude/skills/update-changelog/update-changelog.py "fix: resolve login timeout issue" "2025-11-23 14:00:00"
```

**Output in CHANGELOG.md:**
```markdown
## 2025-11-23 14:00:00

fix: resolve login timeout issue

---

## 2025-11-23 15:30:00

feat: add user authentication system

---
```

### Example 3: Multiple Commits Over Time

**CHANGELOG.md after several commits:**
```markdown
## 2025-11-23 17:00:00

docs: update README with installation instructions

---

## 2025-11-23 16:15:00

refactor: simplify authentication logic

---

## 2025-11-23 14:00:00

fix: resolve login timeout issue

---

## 2025-11-23 15:30:00

feat: add user authentication system

---
```

## Integration with Slash Commands

### /commit Command

The `/commit` slash command automatically calls this skill after creating a git commit:

```bash
# Step 8 in /commit workflow:
python ~/.claude/skills/update-changelog/update-changelog.py "<commit-message>" "$(date '+%Y-%m-%d %H:%M:%S')"
```

### /commit-push Command

The `/commit-push` slash command also calls this skill:

```bash
# Step 9 in /commit-push workflow:
python ~/.claude/skills/update-changelog/update-changelog.py "<commit-message>" "$(date '+%Y-%m-%d %H:%M:%S')"
```

Both commands:
1. Review changes with `git status` and `git diff`
2. Create conventional commit message
3. Execute `git commit`
4. **Call update-changelog skill**
5. (For `/commit-push`) Push to remote

## Output Format

### Timestamp Header
```markdown
## YYYY-MM-DD HH:MM:SS
```

### Commit Message Body
```markdown
commit message (can be multi-line)
```

### Separator
```markdown
---
```

### Complete Entry Example
```markdown
## 2025-11-23 15:30:00

feat: add user authentication

Implemented JWT-based authentication with refresh tokens.
Added middleware for protected routes.

---
```

## Tips

### Best Practices

1. **Use with slash commands**: Let `/commit` and `/commit-push` handle the integration automatically
2. **Conventional commits**: Use conventional commit format (feat:, fix:, docs:, etc.) for clear changelog
3. **Multi-line messages**: Commit messages can span multiple lines for detailed entries
4. **Consistent timestamps**: Let the script auto-generate timestamps for accuracy

### Copying to Other Projects

This is a **global personal skill** stored in `~/.claude/skills/`, so:
- No need to copy - accessible from any project
- CHANGELOG.md created in each project's root directory
- Copy `/commit` and `/commit-push` slash commands to new projects

### Manual Usage

While designed for automatic use, you can invoke manually:
```bash
# Quick update from command line
python ~/.claude/skills/update-changelog/update-changelog.py "manual update: $(git log -1 --pretty=%B)"
```

### Version Control

- Add CHANGELOG.md to your git repository
- The file will grow over time with project history
- Most recent changes always at the top for easy review

## Related Skills

- `/commit` - Git commit with automatic changelog update
- `/commit-push` - Git commit, changelog update, and push to remote
- `create-claude-slash-commands` - Create custom slash commands
