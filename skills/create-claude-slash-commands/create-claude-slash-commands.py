#!/usr/bin/env python3
"""
Create Claude Code Slash Commands

This script generates custom slash commands for Claude Code, stored in
.claude/commands/ (project) or ~/.claude/commands/ (personal).

Slash commands are quick shortcuts for executing specific prompts or tasks.
They're defined as Markdown files with optional YAML frontmatter.

Usage:
    python 09-create-claude-slash-commands.py
    python 09-create-claude-slash-commands.py --name review --description "..." --prompt "..."
"""

import sys
import argparse
from pathlib import Path
from typing import Optional, List


def create_commands_directory(is_personal: bool = False) -> Path:
    """
    Create .claude/commands/ directory if it doesn't exist.

    Args:
        is_personal: If True, use ~/.claude/commands/ instead

    Returns:
        Path: Commands directory path
    """
    if is_personal:
        commands_dir = Path.home() / '.claude' / 'commands'
    else:
        commands_dir = Path('.claude/commands')

    commands_dir.mkdir(parents=True, exist_ok=True)
    return commands_dir


def validate_command_name(name: str) -> bool:
    """
    Validate command name follows conventions.

    Rules:
    - Lowercase letters, numbers, hyphens only
    - Cannot start or end with hyphen
    - Minimum 2 characters
    - No spaces or special characters

    Args:
        name: Proposed command name

    Returns:
        bool: True if valid
    """
    if len(name) < 2:
        print(f"✗ Error: Command name must be at least 2 characters (got: {name})")
        return False

    if not name.replace('-', '').replace('_', '').isalnum():
        print(f"✗ Error: Command name can only contain lowercase letters, numbers, and hyphens")
        return False

    if name.startswith('-') or name.endswith('-'):
        print(f"✗ Error: Command name cannot start or end with hyphen")
        return False

    if name != name.lower():
        print(f"✗ Error: Command name must be lowercase")
        return False

    return True


def get_user_input_interactive() -> dict:
    """Get command configuration through interactive prompts."""
    print("=" * 60)
    print("Create New Claude Code Slash Command")
    print("=" * 60)
    print()

    # Get command name
    while True:
        name = input("Command name (lowercase-with-hyphens): ").strip()
        if validate_command_name(name):
            break

    # Get scope
    print("\nScope:")
    print("  1. Project (shared with team, stored in .claude/commands/)")
    print("  2. Personal (only for you, stored in ~/.claude/commands/)")
    scope_input = input("Choose [1/2] (default: 1): ").strip() or "1"
    is_personal = scope_input == "2"

    # Get description
    print("\nDescription (brief explanation of what this command does):")
    description = input("> ").strip()
    # Description is optional - will default to first line of prompt

    # Get argument hint
    print("\nArgument hint (shown during auto-completion, e.g., '[file]' or '<issue-number>'):")
    print("  Press ENTER to skip")
    argument_hint = input("> ").strip() or None

    # Get allowed tools
    print("\nAllowed tools (comma-separated, e.g., 'Bash, Read, Edit'):")
    print("  - Press ENTER to inherit from conversation (recommended)")
    print("  - Or specify: Bash, Read, Edit, Grep, Glob, Write, etc.")
    tools_input = input("> ").strip()
    allowed_tools = None if not tools_input else [t.strip() for t in tools_input.split(',')]

    # Get model
    print("\nModel preference:")
    print("  - Press ENTER to inherit from conversation (recommended)")
    print("  - Or specify: claude-3-5-sonnet-20241022, claude-3-5-haiku-20241022, claude-opus-4-20250514")
    model = input("> ").strip() or None

    # Get subdirectory
    print("\nSubdirectory (optional, for organization):")
    print("  e.g., 'git', 'frontend', 'backend'")
    print("  Press ENTER for root directory")
    subdirectory = input("> ").strip() or None

    # Get prompt
    print("\nCommand prompt (what Claude should do when this command is invoked):")
    print("  - Use $ARGUMENTS for all user arguments")
    print("  - Use $1, $2, $3 for positional arguments")
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
        print("✗ Error: Command prompt is required")
        sys.exit(1)

    return {
        'name': name,
        'description': description,
        'argument_hint': argument_hint,
        'allowed_tools': allowed_tools,
        'model': model,
        'subdirectory': subdirectory,
        'is_personal': is_personal,
        'prompt': prompt
    }


def generate_command_file(config: dict) -> str:
    """
    Generate command file content with optional YAML frontmatter.

    Args:
        config: Command configuration dict

    Returns:
        str: File content
    """
    # Build frontmatter if needed
    has_frontmatter = any([
        config.get('description'),
        config.get('allowed_tools'),
        config.get('argument_hint'),
        config.get('model')
    ])

    if has_frontmatter:
        frontmatter = ["---"]

        if config.get('description'):
            frontmatter.append(f"description: {config['description']}")

        if config.get('allowed_tools'):
            tools_str = ', '.join(config['allowed_tools'])
            frontmatter.append(f"allowed-tools: [{tools_str}]")

        if config.get('argument_hint'):
            frontmatter.append(f"argument-hint: {config['argument_hint']}")

        if config.get('model'):
            frontmatter.append(f"model: {config['model']}")

        frontmatter.append("---")

        content = '\n'.join(frontmatter)
        content += '\n\n'
        content += config['prompt']
        content += '\n'
    else:
        # No frontmatter - just prompt
        content = config['prompt'] + '\n'

    return content


def save_command_file(config: dict, commands_dir: Path) -> Path:
    """
    Save command file to .claude/commands/ directory.

    Args:
        config: Command configuration
        commands_dir: Path to commands directory

    Returns:
        Path: Saved file path
    """
    # Handle subdirectory if specified
    if config.get('subdirectory'):
        target_dir = commands_dir / config['subdirectory']
        target_dir.mkdir(parents=True, exist_ok=True)
    else:
        target_dir = commands_dir

    filename = f"{config['name']}.md"
    filepath = target_dir / filename

    # Check if file exists
    if filepath.exists():
        overwrite = input(f"\n⚠ Command '/{config['name']}' already exists. Overwrite? (y/N): ")
        if overwrite.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)

    # Generate and save content
    content = generate_command_file(config)
    filepath.write_text(content, encoding='utf-8')

    return filepath


def display_summary(config: dict, filepath: Path):
    """Display creation summary."""
    print("\n" + "=" * 60)
    print("✓ Slash Command Created Successfully!")
    print("=" * 60)
    print(f"Name: /{config['name']}")

    if config.get('description'):
        print(f"Description: {config['description']}")

    if config.get('argument_hint'):
        print(f"Arguments: {config['argument_hint']}")

    if config.get('allowed_tools'):
        print(f"Tools: {', '.join(config['allowed_tools'])}")
    else:
        print("Tools: Inherited from conversation")

    if config.get('model'):
        print(f"Model: {config['model']}")
    else:
        print("Model: Inherited from conversation")

    scope = "Personal" if config.get('is_personal') else "Project"
    print(f"Scope: {scope}")

    print(f"\nFile: {filepath}")
    print("\nUsage in Claude Code:")
    print(f"  /{config['name']}", end="")
    if config.get('argument_hint'):
        print(f" {config['argument_hint']}")
    else:
        print()

    if '$ARGUMENTS' in config['prompt']:
        print(f"  Example: /{config['name']} your-argument-here")

    print("=" * 60)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Create Claude Code slash commands in .claude/commands/",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python 09-create-claude-slash-commands.py

  # Create git commit command
  python 09-create-claude-slash-commands.py \\
    --name commit \\
    --description "Create git commit with conventional message" \\
    --tools "Bash" \\
    --prompt "Review changes with git status and git diff, then create a conventional commit message."

  # Create code review command with arguments
  python 09-create-claude-slash-commands.py \\
    --name review \\
    --description "Review code for quality and security" \\
    --argument-hint "[file]" \\
    --prompt "Review the code in \\$ARGUMENTS for security, performance, and best practices."

  # Personal command (available across all projects)
  python 09-create-claude-slash-commands.py \\
    --name note \\
    --personal \\
    --prompt "Create a quick note: \\$ARGUMENTS"

Notes:
  - Use $ARGUMENTS to capture all user input
  - Use $1, $2, $3 for positional arguments
  - Project commands (.claude/commands/) are shared with team
  - Personal commands (~/.claude/commands/) are individual-only
        """
    )

    parser.add_argument('--name', help='Command name (lowercase-with-hyphens)')
    parser.add_argument('--description', help='Brief explanation of the command')
    parser.add_argument('--argument-hint', help='Argument format hint (e.g., [file] or <issue>)')
    parser.add_argument('--tools', help='Comma-separated allowed tools')
    parser.add_argument('--model', help='Specific Claude model to use')
    parser.add_argument('--subdirectory', help='Subdirectory for organization')
    parser.add_argument('--personal', action='store_true', help='Create personal command (~/.claude/commands/)')
    parser.add_argument('--prompt', help='Command prompt (what Claude should do)')

    args = parser.parse_args()

    # Determine scope
    is_personal = args.personal

    # Create commands directory
    commands_dir = create_commands_directory(is_personal)

    # Get configuration
    if args.name and args.prompt:
        # Command-line mode
        if not validate_command_name(args.name):
            sys.exit(1)

        config = {
            'name': args.name,
            'description': args.description,
            'argument_hint': args.argument_hint,
            'allowed_tools': [t.strip() for t in args.tools.split(',')] if args.tools else None,
            'model': args.model,
            'subdirectory': args.subdirectory,
            'is_personal': is_personal,
            'prompt': args.prompt
        }
    else:
        # Interactive mode
        config = get_user_input_interactive()
        commands_dir = create_commands_directory(config['is_personal'])

    # Save command file
    filepath = save_command_file(config, commands_dir)

    # Display summary
    display_summary(config, filepath)


if __name__ == '__main__':
    main()
