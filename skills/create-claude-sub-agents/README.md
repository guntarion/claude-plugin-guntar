# Create Claude Code Sub-Agents - Implementation Notes

## Overview

This skill generates project sub-agents for Claude Code. Sub-agents are specialized assistants stored as Markdown files with YAML frontmatter in `.claude/agents/` directory.

## Implementation Details

### Core Functionality

The script provides two modes:
1. **Interactive Mode**: Step-by-step prompts for easy agent creation
2. **Command-Line Mode**: Scriptable for automation and batch creation

### Smart Defaults

Based on Claude Code documentation and best practices:
- **Model**: Haiku (efficient, cost-effective, sufficient for most tasks)
- **Tools**: All tools (maximum flexibility, recommended by docs)
- **Permission Mode**: Default (inherits from main conversation)

### File Format

Generated files use YAML frontmatter with Markdown body:

```markdown
---
name: agent-name
description: When and why to use this agent
tools: Read, Edit, Bash    # Optional - omit for all tools
model: haiku               # sonnet, opus, haiku, or inherit
---

System prompt defining the agent's role, capabilities,
and behavioral constraints...
```

### Validation

The script validates:
- Agent name format (lowercase-with-hyphens, minimum 3 chars)
- Required fields presence (name, description, prompt)
- Model selection (valid options only)
- Prevents accidental overwrites with confirmation

### Directory Management

Automatically creates `.claude/agents/` directory if it doesn't exist, following Claude Code's expected project structure.

## Usage Modes

### Interactive Mode

Best for:
- First-time users
- Complex multi-line prompts
- Exploratory agent design

Features:
- Clear prompts with validation
- Multi-line prompt input (Ctrl+D/Ctrl+Z to finish)
- Helpful defaults and suggestions
- Confirmation before overwriting

### Command-Line Mode

Best for:
- Automation and scripting
- Batch agent creation
- CI/CD integration
- Team standardization

Features:
- All options via flags
- Scriptable and repeatable
- No interactive prompts
- Exit codes for error handling

## Design Decisions

### Why Haiku as Default?

1. **Efficiency**: Most sub-agent tasks don't require Sonnet/Opus capability
2. **Cost**: Significantly lower token costs
3. **Speed**: Faster response times
4. **Sufficiency**: Haiku handles 80%+ of specialized tasks well

Users can override for complex tasks requiring higher reasoning.

### Why All Tools as Default?

1. **Flexibility**: Agents can adapt to various situations
2. **Documentation Recommendation**: Claude Code docs suggest omitting tools field
3. **Simplicity**: No need to predict exact tool requirements
4. **Safety**: Tool usage is still governed by permissions system

Users can restrict for security-sensitive agents.

### Name Validation Rules

- **Lowercase**: Consistent with Claude Code conventions
- **Hyphens**: Standard separator for multi-word names
- **No special chars**: Prevents file system issues
- **Minimum length**: Ensures meaningful names

## File Structure

```
.claude/skills/create-claude-sub-agents/
├── SKILL.md                      # Skill activation file (~50 tokens)
├── README.md                     # This file (implementation notes)
├── reference.md                  # Comprehensive user guide
└── create-claude-sub-agents.py   # Main Python script
```

## Dependencies

None - uses Python standard library only:
- `argparse` - Command-line parsing
- `pathlib` - File path handling
- `sys` - System operations

## Error Handling

The script handles:
- Invalid agent names (validation with clear error messages)
- Missing required fields (prompts for re-entry)
- Existing agent files (confirmation before overwrite)
- Invalid model names (validation against allowed list)
- Directory creation failures (creates parent directories as needed)

## Testing

Test the skill with:

```bash
# Interactive test
python create-claude-sub-agents.py

# Command-line test
python create-claude-sub-agents.py \
  --name test-agent \
  --description "Test agent for validation" \
  --prompt "You are a test agent."

# Verify output
cat .claude/agents/test-agent.md
```

## Future Enhancements

Potential improvements:
- Template system for common agent types
- Batch creation from JSON/YAML config file
- Agent validation (check prompt quality)
- Integration with skill system for agent-specific skills
- Permission mode configuration
- Skills field support

## See Also

- [Claude Code Sub-Agents Documentation](https://code.claude.com/docs/en/sub-agents)
- [CLI Reference](https://code.claude.com/docs/en/cli-reference#agents-flag-format)
- Project's create-claude-skill guide at `.claude/skills/create-claude-skill/`
