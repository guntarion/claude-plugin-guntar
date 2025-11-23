#!/usr/bin/env python3
"""
Create Claude Code Sub-Agents

This script generates project sub-agents for Claude Code, stored in .claude/agents/
directory. Sub-agents are specialized assistants with focused responsibilities.

Sub-agents are Markdown files with YAML frontmatter that define:
- Unique name and description
- Model selection (defaults to Haiku for efficiency)
- Tool access (defaults to all tools)
- Detailed system prompt for behavior

Usage:
    python 08-create-claude-sub-agents.py
    python 08-create-claude-sub-agents.py --name agent-name --description "..." --prompt "..."
"""

import sys
import argparse
from pathlib import Path


def create_agents_directory():
    """Create .claude/agents/ directory if it doesn't exist."""
    agents_dir = Path('.claude/agents')
    agents_dir.mkdir(parents=True, exist_ok=True)
    return agents_dir


def validate_agent_name(name: str) -> bool:
    """
    Validate agent name follows conventions.

    Rules:
    - Lowercase letters, numbers, hyphens only
    - Cannot start or end with hyphen
    - Minimum 3 characters

    Args:
        name: Proposed agent name

    Returns:
        bool: True if valid
    """
    if len(name) < 3:
        print(f"✗ Error: Agent name must be at least 3 characters (got: {name})")
        return False

    if not name.replace('-', '').replace('_', '').isalnum():
        print(f"✗ Error: Agent name can only contain lowercase letters, numbers, and hyphens")
        return False

    if name.startswith('-') or name.endswith('-'):
        print(f"✗ Error: Agent name cannot start or end with hyphen")
        return False

    if name != name.lower():
        print(f"✗ Error: Agent name must be lowercase")
        return False

    return True


def get_user_input_interactive():
    """Get agent configuration through interactive prompts."""
    print("=" * 60)
    print("Create New Claude Code Sub-Agent")
    print("=" * 60)
    print()

    # Get agent name
    while True:
        name = input("Agent name (lowercase-with-hyphens): ").strip()
        if validate_agent_name(name):
            break

    # Get description
    print("\nDescription (when and why to use this agent):")
    description = input("> ").strip()
    while not description:
        print("✗ Description is required")
        description = input("> ").strip()

    # Get model preference
    print("\nModel (sonnet/opus/haiku/inherit) [default: haiku]:")
    model = input("> ").strip().lower() or "haiku"
    valid_models = ['sonnet', 'opus', 'haiku', 'inherit']
    while model not in valid_models:
        print(f"✗ Invalid model. Choose from: {', '.join(valid_models)}")
        model = input("> ").strip().lower() or "haiku"

    # Get tool access
    print("\nTool access:")
    print("  - Press ENTER for all tools (recommended)")
    print("  - Or specify comma-separated list: Read, Edit, Bash, Grep, Glob, etc.")
    tools_input = input("> ").strip()
    tools = None if not tools_input else [t.strip() for t in tools_input.split(',')]

    # Get system prompt
    print("\nSystem prompt (detailed instructions for the agent):")
    print("(Type or paste multi-line prompt, then press Ctrl+D on Mac/Linux or Ctrl+Z on Windows)")
    prompt_lines = []
    try:
        while True:
            line = input()
            prompt_lines.append(line)
    except EOFError:
        pass

    prompt = '\n'.join(prompt_lines).strip()

    if not prompt:
        print("✗ Error: System prompt is required")
        sys.exit(1)

    return {
        'name': name,
        'description': description,
        'model': model,
        'tools': tools,
        'prompt': prompt
    }


def generate_agent_file(config: dict) -> str:
    """
    Generate agent file content with YAML frontmatter.

    Args:
        config: Agent configuration dict

    Returns:
        str: File content
    """
    frontmatter = ["---"]
    frontmatter.append(f"name: {config['name']}")
    frontmatter.append(f"description: {config['description']}")

    # Add optional fields
    if config.get('tools'):
        tools_str = ', '.join(config['tools'])
        frontmatter.append(f"tools: {tools_str}")
    # If tools not specified, omit field = access to all tools

    frontmatter.append(f"model: {config['model']}")
    frontmatter.append("---")

    # Build complete file
    content = '\n'.join(frontmatter)
    content += '\n\n'
    content += config['prompt']
    content += '\n'

    return content


def save_agent_file(config: dict, agents_dir: Path) -> Path:
    """
    Save agent file to .claude/agents/ directory.

    Args:
        config: Agent configuration
        agents_dir: Path to agents directory

    Returns:
        Path: Saved file path
    """
    filename = f"{config['name']}.md"
    filepath = agents_dir / filename

    # Check if file exists
    if filepath.exists():
        overwrite = input(f"\n⚠ Agent '{config['name']}' already exists. Overwrite? (y/N): ")
        if overwrite.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)

    # Generate and save content
    content = generate_agent_file(config)
    filepath.write_text(content, encoding='utf-8')

    return filepath


def display_summary(config: dict, filepath: Path):
    """Display creation summary."""
    print("\n" + "=" * 60)
    print("✓ Sub-Agent Created Successfully!")
    print("=" * 60)
    print(f"Name: {config['name']}")
    print(f"Description: {config['description']}")
    print(f"Model: {config['model']}")

    if config.get('tools'):
        print(f"Tools: {', '.join(config['tools'])}")
    else:
        print("Tools: All tools (default)")

    print(f"\nFile: {filepath}")
    print("\nUsage in Claude Code:")
    print(f"  - The agent will be available as '{config['name']}'")
    print(f"  - Claude will automatically use it when: {config['description']}")
    print("\nYou can manually invoke it or let Claude choose when appropriate.")
    print("=" * 60)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Create Claude Code sub-agents in .claude/agents/",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python 08-create-claude-sub-agents.py

  # Command-line mode
  python 08-create-claude-sub-agents.py \\
    --name code-reviewer \\
    --description "Expert code reviewer for quality and security" \\
    --model sonnet \\
    --tools "Read, Grep, Glob, Bash" \\
    --prompt "You are a senior code reviewer focusing on..."

  # All tools, Haiku model (defaults)
  python 08-create-claude-sub-agents.py \\
    --name doc-writer \\
    --description "Technical documentation specialist" \\
    --prompt "You write clear, comprehensive technical documentation..."

Notes:
  - Defaults to Haiku model (efficient and cost-effective)
  - Defaults to all tools access (maximum flexibility)
  - Agent names must be lowercase-with-hyphens
  - Files saved to .claude/agents/
        """
    )

    parser.add_argument('--name', help='Agent name (lowercase-with-hyphens)')
    parser.add_argument('--description', help='When and why to use this agent')
    parser.add_argument('--model', default='haiku',
                       choices=['sonnet', 'opus', 'haiku', 'inherit'],
                       help='Model to use (default: haiku)')
    parser.add_argument('--tools', help='Comma-separated tool list (omit for all tools)')
    parser.add_argument('--prompt', help='System prompt for agent behavior')

    args = parser.parse_args()

    # Create agents directory
    agents_dir = create_agents_directory()

    # Get configuration
    if args.name and args.description and args.prompt:
        # Command-line mode
        if not validate_agent_name(args.name):
            sys.exit(1)

        config = {
            'name': args.name,
            'description': args.description,
            'model': args.model,
            'tools': [t.strip() for t in args.tools.split(',')] if args.tools else None,
            'prompt': args.prompt
        }
    else:
        # Interactive mode
        config = get_user_input_interactive()

    # Save agent file
    filepath = save_agent_file(config, agents_dir)

    # Display summary
    display_summary(config, filepath)


if __name__ == '__main__':
    main()
