# Create Claude Code Slash Commands - Reference Guide

## Table of Contents

1. [Purpose](#purpose)
2. [Quick Start](#quick-start)
3. [Usage Modes](#usage-modes)
4. [Command Scopes](#command-scopes)
5. [Configuration Options](#configuration-options)
6. [Argument Handling](#argument-handling)
7. [Examples](#examples)
8. [File Format](#file-format)
9. [Best Practices](#best-practices)
10. [Advanced Features](#advanced-features)
11. [Troubleshooting](#troubleshooting)

---

## Purpose

Create custom slash commands for Claude Code that provide quick shortcuts for common tasks, workflows, and prompts.

**What are Slash Commands?**
- Quick shortcuts invoked with `/command-name`
- Markdown files with optional YAML frontmatter
- Can accept arguments for flexibility
- Support tool restrictions and model selection

**When to Create Slash Commands:**
- Repetitive prompts or workflows
- Team-wide standards and practices
- Common operations (git, testing, reviews)
- Personal productivity shortcuts

---

## Quick Start

### Interactive Mode (Recommended for First Time)

```bash
source .venv/bin/activate
python .claude/skills/create-claude-slash-commands/create-claude-slash-commands.py
```

Follow the prompts to configure your command.

### Command-Line Mode (For Automation)

```bash
python .claude/skills/create-claude-slash-commands/create-claude-slash-commands.py \
  --name command-name \
  --description "Brief description" \
  --prompt "What Claude should do"
```

---

## Usage Modes

### 1. Interactive Mode

Best for:
- First-time users
- Complex commands with many options
- Exploratory command design

Features:
- Clear prompts with helpful hints
- Multi-line prompt input (Ctrl+D/Ctrl+Z to finish)
- Validation and error messages
- Confirmation before overwriting

**Example Session:**
```
Command name: review
Scope: [1] Project / [2] Personal: 1
Description: Code review for quality and security
Argument hint: [file]
Allowed tools: Read, Grep
Model: [press ENTER to inherit]
Subdirectory: [press ENTER for root]
Command prompt:
Review the code in $ARGUMENTS for:
- Security vulnerabilities
- Performance issues
- Best practices
[Ctrl+D]
```

### 2. Command-Line Mode

Best for:
- Automation and scripting
- Batch command creation
- CI/CD integration
- Quick simple commands

**Minimal Example:**
```bash
python create-claude-slash-commands.py \
  --name status \
  --prompt "Show git status and branch info"
```

**Full Example:**
```bash
python create-claude-slash-commands.py \
  --name review \
  --description "Code review command" \
  --argument-hint "[file]" \
  --tools "Read, Grep, Glob" \
  --model "claude-3-5-sonnet-20241022" \
  --subdirectory "code" \
  --prompt "Review code in \$ARGUMENTS for quality and security"
```

---

## Command Scopes

### Project Commands (`.claude/commands/`)

**When to use:**
- Team-wide workflows
- Project-specific standards
- Shared best practices
- Onboarding new team members

**Benefits:**
- Version controlled with Git
- Shared across entire team
- Consistent workflows
- Discoverable by all team members

**Location:** `.claude/commands/`

**Example:**
```bash
# Create project command
python create-claude-slash-commands.py \
  --name commit \
  --description "Create conventional commit" \
  --prompt "Review changes and create a conventional commit message"
```

### Personal Commands (`~/.claude/commands/`)

**When to use:**
- Personal productivity shortcuts
- Individual preferences
- Experimental commands
- Commands not relevant to team

**Benefits:**
- Available across all projects
- Private to you only
- No version control conflicts
- Quick personal automation

**Location:** `~/.claude/commands/`

**Example:**
```bash
# Create personal command
python create-claude-slash-commands.py \
  --name note \
  --personal \
  --prompt "Create a quick note: \$ARGUMENTS"
```

---

## Configuration Options

### Required Fields

#### 1. name (required)
- Unique identifier for the command
- Becomes the command invocation (`/name`)
- Must be lowercase-with-hyphens
- Minimum 2 characters
- Example: `review`, `git-commit`, `test-api`

#### 2. prompt (required)
- What Claude should do when command is invoked
- Can be multi-line
- Supports variables: `$ARGUMENTS`, `$1`, `$2`, `$3`
- Example: `"Review code in $ARGUMENTS for security"`

### Optional Fields

#### 3. description
- Brief explanation of the command
- Shown in command auto-completion
- Defaults to first line of prompt if omitted
- Example: `"Code review for quality and security"`

#### 4. argument-hint
- Shows expected argument format
- Displayed during auto-completion
- Helpful for users invoking the command
- Examples: `"[file]"`, `"<issue-number>"`, `"[source] [target]"`

#### 5. allowed-tools
- Comma-separated list of tools
- Restricts what tools the command can use
- Defaults to inherit from conversation (recommended)
- Examples: `"Bash, Read"`, `"Read, Edit, Grep"`

#### 6. model
- Specific Claude model to use
- Defaults to inherit from conversation
- Examples:
  - `"claude-3-5-sonnet-20241022"`
  - `"claude-3-5-haiku-20241022"`
  - `"claude-opus-4-20250514"`

#### 7. subdirectory
- Organize commands in subdirectories
- Does NOT affect command name
- Helps with organization
- Examples: `"git"`, `"frontend"`, `"testing"`

#### 8. scope (--personal flag)
- Project: `.claude/commands/` (default)
- Personal: `~/.claude/commands/` (with --personal)

---

## Argument Handling

### 1. All Arguments: $ARGUMENTS

Captures everything the user provides.

**Command:**
```markdown
---
description: Code review command
argument-hint: [file]
---

Review the code in $ARGUMENTS for quality and security.
```

**Usage:**
```
/review src/auth.py
/review "src/auth.py src/utils.py"
/review *.py
```

### 2. Positional Arguments: $1, $2, $3

Individual argument access (shell-style).

**Command:**
```markdown
---
description: Fix GitHub issue
argument-hint: <issue-number>
---

Fix issue #$1. Follow these steps:
1. Understand the issue
2. Locate relevant code
3. Implement solution
4. Add tests
```

**Usage:**
```
/fix-issue 123
```

### 3. Combined Usage

**Command:**
```markdown
Move file from $1 to $2. Analyze impact on $ARGUMENTS.
```

**Usage:**
```
/move-analyze src/old.py src/new.py tests/*.py
```

- `$1` = "src/old.py"
- `$2` = "src/new.py"
- `$ARGUMENTS` = "src/old.py src/new.py tests/*.py"

### 4. No Arguments

Static commands that don't need parameters.

**Command:**
```markdown
---
description: Show project status
---

Run git status and provide a summary of:
- Modified files
- Untracked files
- Current branch
```

**Usage:**
```
/status
```

---

## Examples

### Example 1: Git Commit Command

**Create:**
```bash
python create-claude-slash-commands.py \
  --name commit \
  --description "Create conventional git commit" \
  --tools "Bash" \
  --subdirectory "git" \
  --prompt "Review changes with git status and git diff, then create a conventional commit message and commit the changes."
```

**Generated File** (`.claude/commands/git/commit.md`):
```markdown
---
description: Create conventional git commit
allowed-tools: [Bash]
---

Review changes with git status and git diff, then create a
conventional commit message and commit the changes.
```

**Usage:**
```
/commit
```

### Example 2: Code Review with Arguments

**Create:**
```bash
python create-claude-slash-commands.py \
  --name review \
  --description "Review code for quality and security" \
  --argument-hint "[file]" \
  --tools "Read, Grep, Glob" \
  --prompt "Review the code in \$ARGUMENTS for security vulnerabilities, performance issues, and best practices. Provide actionable feedback."
```

**Usage:**
```
/review src/auth.py
/review "src/*.py"
```

### Example 3: Test Generator

**Create:**
```bash
python create-claude-slash-commands.py \
  --name gen-tests \
  --description "Generate unit tests for a file" \
  --argument-hint "<file>" \
  --tools "Read, Write" \
  --prompt "Read \$1 and generate comprehensive unit tests with edge cases and mocks. Save to tests/test_\$1."
```

**Usage:**
```
/gen-tests auth.py
```

### Example 4: Quick Note (Personal)

**Create:**
```bash
python create-claude-slash-commands.py \
  --name note \
  --personal \
  --prompt "Create a quick markdown note with timestamp: \$ARGUMENTS"
```

**Usage:**
```
/note Remember to update the deployment docs
```

### Example 5: API Documentation

**Create:**
```bash
python create-claude-slash-commands.py \
  --name api-docs \
  --description "Generate API documentation" \
  --argument-hint "[endpoint-file]" \
  --tools "Read, Write" \
  --subdirectory "docs" \
  --prompt "Read the API endpoint definitions in \$ARGUMENTS and generate comprehensive OpenAPI/Swagger documentation."
```

**Usage:**
```
/api-docs src/api/endpoints.py
```

---

## File Format

### Basic Command (No Frontmatter)

```markdown
Review code for security and performance issues.
```

### Command with Description

```markdown
---
description: Code review for security and performance
---

Review code for security and performance issues.
```

### Full Configuration

```markdown
---
description: Review code with comprehensive analysis
allowed-tools: [Read, Grep, Glob, Bash]
argument-hint: [file-pattern]
model: claude-3-5-sonnet-20241022
---

Review all files matching $ARGUMENTS for:
- Security vulnerabilities (SQL injection, XSS, etc.)
- Performance bottlenecks
- Code quality and maintainability
- Test coverage gaps

Provide specific, actionable recommendations.
```

---

## Best Practices

### 1. Clear Names
- Use descriptive, action-oriented names
- `review` instead of `r`
- `commit` instead of `c`
- `gen-tests` instead of `gt`

### 2. Helpful Descriptions
- Explain when/why to use the command
- "Code review for security" vs just "Review"
- Helps team members discover and use commands

### 3. Argument Hints
- Show expected argument format
- `[file]`, `<issue-number>`, `[source] [target]`
- Makes commands self-documenting

### 4. Tool Restrictions
- Only grant necessary tools for security
- Git commands: `allowed-tools: [Bash]`
- Read-only review: `allowed-tools: [Read, Grep]`

### 5. Organization
- Use subdirectories for related commands
- `git/`, `frontend/`, `backend/`, `testing/`
- Keeps commands directory clean

### 6. Team Standards
- Create project commands for team workflows
- Document in project README
- Review and iterate with team

### 7. Model Selection
- Use Haiku for simple tasks (faster, cheaper)
- Use Sonnet for complex analysis
- Default to inherit for flexibility

---

## Advanced Features

### Bash Command Execution

Include bash operations with `!` prefix:

```markdown
---
allowed-tools: [Bash]
---

Run !git status and !git branch to analyze the repository state.
```

### File References

Use `@` prefix for file contents:

```markdown
Review the code in @$ARGUMENTS and compare with @src/best-practices.md.
```

### Subdirectory Organization

```bash
# Create in subdirectory
python create-claude-slash-commands.py \
  --name commit \
  --subdirectory "git" \
  --prompt "..."
```

Structure:
```
.claude/commands/
├── git/
│   ├── commit.md
│   ├── push.md
│   └── rebase.md
├── frontend/
│   └── component.md
└── backend/
    └── api.md
```

Command remains `/commit` (not `/git/commit`), but subdirectory shows in description.

---

## Troubleshooting

### Command Not Appearing

**Issue**: Created command doesn't show up

**Solutions**:
- Check file is in `.claude/commands/` or `~/.claude/commands/`
- Verify filename matches: `command-name.md`
- Restart Claude Code if needed
- Check for YAML syntax errors

### Invalid Command Name

**Error**: "Command name can only contain lowercase letters..."

**Solutions**:
- Use only lowercase letters, numbers, hyphens
- Examples: `review`, `git-commit`, `api-test`
- Avoid: `Review`, `git_commit`, `api.test`

### Tools Not Working

**Issue**: Command can't access certain tools

**Solutions**:
- Add tools to `allowed-tools` in frontmatter
- Or omit `allowed-tools` to inherit all tools
- Check tool names match exactly: `Bash`, not `bash`

### Arguments Not Replaced

**Issue**: `$ARGUMENTS` appears literally in output

**Solutions**:
- Ensure you're providing arguments when invoking
- Use backslash escape in command creation: `\$ARGUMENTS`
- Check command file has correct format

### Overwrite Confirmation

**Issue**: Want to update existing command

**Solutions**:
- Respond 'y' to overwrite prompt
- Or delete old command first: `rm .claude/commands/old.md`
- Or use different name

---

## Dependencies

None - uses Python standard library only.

## See Also

- [Claude Code Slash Commands Documentation](https://code.claude.com/docs/en/slash-commands#custom-slash-commands)
- [Common Workflows Guide](https://code.claude.com/docs/en/common-workflows#create-custom-slash-commands)
- Project's existing commands in `.claude/commands/`
