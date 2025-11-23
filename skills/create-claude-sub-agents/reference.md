# Create Claude Code Sub-Agents

## Purpose

Generate project sub-agents for Claude Code. Sub-agents are specialized assistants with focused responsibilities, stored in `.claude/agents/` directory.

## Features

- **Interactive Mode**: Step-by-step prompts for easy agent creation
- **Command-Line Mode**: Scriptable for automation
- **Smart Defaults**:
  - Haiku model (efficient and cost-effective)
  - All tools access (maximum flexibility)
- **Validation**: Ensures agent names follow conventions
- **Overwrite Protection**: Confirms before replacing existing agents

## Sub-Agent Concepts

### What are Sub-Agents?

Sub-agents are specialized assistants that Claude Code can invoke for specific tasks. They have:
- Focused responsibilities (e.g., code review, documentation, testing)
- Custom system prompts defining their behavior
- Configurable model and tool access
- Higher priority than user-level agents

### When to Use Sub-Agents

Create sub-agents for:
- **Repetitive specialized tasks**: Code review, documentation generation
- **Domain expertise**: Security analysis, performance optimization
- **Workflow automation**: Pre-commit checks, test generation
- **Team collaboration**: Shared best practices across projects

## Usage

### Interactive Mode (Recommended)

```bash
python 08-create-claude-sub-agents.py
```

Follow the prompts:
1. Enter agent name (lowercase-with-hyphens)
2. Describe when to use the agent
3. Choose model (default: haiku)
4. Specify tools (default: all tools)
5. Paste system prompt, then Ctrl+D (Mac/Linux) or Ctrl+Z (Windows)

### Command-Line Mode

```bash
python 08-create-claude-sub-agents.py \
  --name agent-name \
  --description "When and why to use this agent" \
  --model haiku \
  --tools "Read, Edit, Bash" \
  --prompt "Your detailed system prompt here"
```

### Examples

**Example 1: Code Reviewer (Sonnet with limited tools)**
```bash
python 08-create-claude-sub-agents.py \
  --name code-reviewer \
  --description "Expert code reviewer for quality, security, and best practices" \
  --model sonnet \
  --tools "Read, Grep, Glob, Bash" \
  --prompt "You are a senior code reviewer specializing in security and performance..."
```

**Example 2: Documentation Writer (Haiku with all tools)**
```bash
python 08-create-claude-sub-agents.py \
  --name doc-writer \
  --description "Technical documentation specialist" \
  --prompt "You write clear, comprehensive technical documentation..."
```

**Example 3: Test Generator (Inherit model)**
```bash
python 08-create-claude-sub-agents.py \
  --name test-generator \
  --description "Generates comprehensive unit tests" \
  --model inherit \
  --prompt "You generate thorough unit tests with edge cases and mocks..."
```

## Configuration Options

### Required Fields

- **name**: Unique identifier
  - Lowercase letters, numbers, hyphens
  - Minimum 3 characters
  - Cannot start/end with hyphen
  - Example: `code-reviewer`, `doc-writer`

- **description**: When and why to use the agent
  - Natural language description
  - Helps Claude decide when to invoke
  - Example: "Expert code reviewer for security and performance"

- **prompt**: System prompt defining behavior
  - Detailed instructions for the agent
  - Define role, capabilities, constraints
  - Can be multi-line

### Optional Fields

- **model**: Model selection
  - `haiku` (default) - Fast and efficient
  - `sonnet` - Balanced performance
  - `opus` - Maximum capability
  - `inherit` - Match main conversation's model

- **tools**: Tool access
  - Omit for all tools (default, recommended)
  - Specify comma-separated list: `Read, Edit, Bash, Grep, Glob`
  - Available tools: Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch, etc.

## File Structure

Generated files are saved to `.claude/agents/`:

```markdown
---
name: code-reviewer
description: Expert code reviewer for quality and security
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a senior code reviewer focusing on:
- Security vulnerabilities
- Performance optimization
- Code maintainability
- Best practices adherence

Review code thoroughly and provide actionable feedback.
```

## Best Practices

1. **Single Responsibility**: Each agent should have one focused purpose
2. **Detailed Prompts**: Write specific instructions and constraints
3. **Limit Tools**: Only grant access to necessary tools (improves security)
4. **Use Haiku**: Default to Haiku for efficiency unless higher capability needed
5. **Version Control**: Commit agents to Git for team collaboration
6. **Descriptive Names**: Use clear, hyphenated names like `code-reviewer`
7. **Clear Descriptions**: Help Claude decide when to invoke the agent

## Advanced Usage

### Creating Multiple Agents

```bash
# Code reviewer
python 08-create-claude-sub-agents.py --name code-reviewer \
  --description "Reviews code for quality and security" \
  --model sonnet --tools "Read, Grep, Glob" \
  --prompt "Senior code reviewer focusing on security..."

# Doc writer
python 08-create-claude-sub-agents.py --name doc-writer \
  --description "Writes technical documentation" \
  --prompt "Technical writer creating clear docs..."

# Test generator
python 08-create-claude-sub-agents.py --name test-gen \
  --description "Generates comprehensive unit tests" \
  --prompt "Test specialist creating thorough test suites..."
```

### Team Workflows

1. Create shared agents for team standards
2. Commit `.claude/agents/` to version control
3. Team members get consistent behavior
4. Iterate and improve agents collaboratively

## Dependencies

No external dependencies required - uses Python standard library only.

## Troubleshooting

**Invalid agent name**
- Use only lowercase letters, numbers, hyphens
- Minimum 3 characters
- Cannot start/end with hyphen

**Agent not appearing**
- Check file is in `.claude/agents/`
- Ensure proper YAML frontmatter format
- Restart Claude Code if necessary

**Tools not working**
- Verify tool names match available tools
- Check spelling and capitalization
- Try omitting tools field for all access

## See Also

- Claude Code Documentation: https://code.claude.com/docs/en/sub-agents
- CLI Reference: https://code.claude.com/docs/en/cli-reference#agents-flag-format
