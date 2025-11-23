# Create Claude Code Slash Commands - Implementation Notes

## Overview

This skill generates custom slash commands for Claude Code. Commands are quick shortcuts for executing specific prompts or tasks, stored as Markdown files with optional YAML frontmatter.

## Implementation Details

### Core Functionality

The script provides two modes:
1. **Interactive Mode**: Step-by-step prompts with validation
2. **Command-Line Mode**: Scriptable for automation

### Command Scopes

**Project Commands** (`.claude/commands/`):
- Shared with entire team via Git
- Available only in the specific project
- Best for team workflows and standards

**Personal Commands** (`~/.claude/commands/`):
- Available across all projects
- Individual use only (not shared)
- Best for personal productivity shortcuts

### File Format

Commands use Markdown with optional YAML frontmatter:

```markdown
---
description: Brief command description
allowed-tools: [Bash, Read, Edit]
argument-hint: [file]
model: claude-3-5-haiku-20241022
---

Command prompt here. Use $ARGUMENTS for user input.
Use $1, $2, $3 for positional arguments.
```

### Frontmatter Options

All fields are optional:

- **description**: Brief explanation (defaults to first line of prompt)
- **allowed-tools**: List of tools the command can use (defaults to inherit from conversation)
- **argument-hint**: Shows expected arguments during auto-completion
- **model**: Specific Claude model (defaults to inherit from conversation)
- **disable-model-invocation**: Prevents SlashCommand tool from invoking (rarely used)

### Argument Handling

The script supports three argument mechanisms:

1. **$ARGUMENTS**: Captures all user input
   - Example: `/review $ARGUMENTS` → `/review myfile.py`

2. **Positional $1, $2, $3**: Individual arguments
   - Example: `/fix $1 in $2` → `/fix bug123 in backend`

3. **No arguments**: Static commands
   - Example: `/status` (no parameters needed)

### Validation

The script validates:
- Command name format (lowercase-with-hyphens, minimum 2 chars)
- Required fields presence (name, prompt)
- Prevents accidental overwrites with confirmation

### Directory Management

Automatically creates:
- `.claude/commands/` for project commands
- `~/.claude/commands/` for personal commands
- Subdirectories for organization (optional)

## Design Decisions

### Why Two Scopes?

**Project Commands:**
- Standardize team workflows
- Share best practices
- Ensure consistency across team members

**Personal Commands:**
- Individual productivity
- Experimental commands
- Personal preferences

### Why Optional Frontmatter?

- Simpler commands don't need metadata
- Most commands inherit conversation settings
- Progressive complexity (start simple, add features as needed)

### Name Validation Rules

- **Lowercase**: Consistent with CLI conventions
- **Hyphens**: Standard separator for multi-word commands
- **No spaces**: Ensures command invocation works
- **Minimum length**: Prevents accidental single-letter commands

## File Structure

```
.claude/skills/create-claude-slash-commands/
├── SKILL.md                           # Skill activation file
├── README.md                          # This file (implementation notes)
├── reference.md                       # Comprehensive user guide
└── create-claude-slash-commands.py   # Main Python script
```

## Dependencies

None - uses Python standard library only:
- `argparse` - Command-line parsing
- `pathlib` - File path handling
- `sys` - System operations

## Error Handling

The script handles:
- Invalid command names (validation with clear errors)
- Missing required fields (prompts for re-entry)
- Existing command files (confirmation before overwrite)
- Directory creation (creates parent directories as needed)

## Testing

Test the skill with:

```bash
# Interactive test
python create-claude-slash-commands.py

# Command-line test
python create-claude-slash-commands.py \
  --name test \
  --description "Test command" \
  --prompt "This is a test."

# Verify output
cat .claude/commands/test.md
```

## Examples Generated

**Git commit command:**
```markdown
---
description: Create git commit with conventional message
allowed-tools: [Bash]
---

Review changes with git status and git diff, then create a
conventional commit message and commit the changes.
```

**Code review with arguments:**
```markdown
---
description: Review code for quality and security
argument-hint: [file]
---

Review the code in $ARGUMENTS for:
- Security vulnerabilities
- Performance issues
- Best practices adherence

Provide actionable feedback.
```

## Advanced Features

### Subdirectory Organization

Commands can be organized in subdirectories:
```
.claude/commands/
├── git/
│   ├── commit.md
│   └── push.md
├── frontend/
│   └── component.md
└── backend/
    └── api.md
```

Command name remains the same (`/commit`, not `/git/commit`), but subdirectory appears in descriptions.

### Bash Command Execution

Commands can include bash operations with `!` prefix (requires allowed-tools: [Bash]):

```markdown
---
allowed-tools: [Bash]
---

Run !git status and analyze the changes.
```

### File References

Use `@` prefix to reference files:
```markdown
Review the code in @$ARGUMENTS for security issues.
```

## Future Enhancements

Potential improvements:
- Template system for common command types
- Batch creation from YAML config
- Command validation (check prompt quality)
- Argument type validation
- Integration with MCP servers

## See Also

- [Claude Code Slash Commands Docs](https://code.claude.com/docs/en/slash-commands#custom-slash-commands)
- [Common Workflows](https://code.claude.com/docs/en/common-workflows#create-custom-slash-commands)
- Project's /commit and /commit-push commands in `.claude/commands/`
