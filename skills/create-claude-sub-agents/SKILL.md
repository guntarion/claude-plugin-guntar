---
name: create-claude-sub-agents
description: Create project sub-agents for Claude Code. Generates specialized assistants with focused responsibilities in .claude/agents/ directory. Defaults to Haiku model and all tools access. Supports interactive and command-line modes. Activate when user wants to create custom sub-agents.
---

# Create Claude Code Sub-Agents

Generate project sub-agents with focused responsibilities. Sub-agents are specialized assistants stored in `.claude/agents/` directory.

## Quick Start

```bash
source .venv/bin/activate
python .claude/skills/create-claude-sub-agents/create-claude-sub-agents.py
```

Or command-line mode:
```bash
python .claude/skills/create-claude-sub-agents/create-claude-sub-agents.py \
  --name agent-name \
  --description "When to use this agent" \
  --prompt "System prompt defining behavior"
```

**Defaults:**
- Model: Haiku (efficient and cost-effective)
- Tools: All tools (maximum flexibility)

**For detailed documentation**, see [reference.md](./reference.md)
**For implementation details**, see [README.md](./README.md)
