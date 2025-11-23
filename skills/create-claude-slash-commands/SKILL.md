---
name: create-claude-slash-commands
description: Create custom slash commands for Claude Code. Generates quick shortcuts for common tasks stored in .claude/commands/ (project) or ~/.claude/commands/ (personal). Supports YAML frontmatter for tools, models, and arguments. Activate when user wants to create slash commands.
---

# Create Claude Code Slash Commands

Generate custom slash commands for quick task execution. Commands are Markdown files with optional YAML frontmatter configuration.

## Quick Start

```bash
source .venv/bin/activate
python .claude/skills/create-claude-slash-commands/create-claude-slash-commands.py
```

Or command-line mode:
```bash
python .claude/skills/create-claude-slash-commands/create-claude-slash-commands.py \
  --name review \
  --description "Code review command" \
  --prompt "Review code in \$ARGUMENTS for quality and security"
```

**Features:**
- Project commands (shared with team)
- Personal commands (individual use)
- $ARGUMENTS and $1, $2, $3 for parameters
- Optional tool and model configuration

**For detailed documentation**, see [reference.md](./reference.md)
**For implementation details**, see [README.md](./README.md)
