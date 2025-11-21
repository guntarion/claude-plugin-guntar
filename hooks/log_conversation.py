#!/usr/bin/env python3
"""
Manual Conversation Logger Script
=============================================
This script allows manual logging of conversation summaries.

Usage:
    python log_conversation.py user "Your prompt text here"
    python log_conversation.py summary "Claude's summary text here"
    python log_conversation.py finalize

You can also use it from Claude Code by invoking it via Bash:
    python .claude/hooks/log_conversation.py summary "Task completed successfully"
"""

import sys
import json
from pathlib import Path
from conversation_logger import get_logger


def main():
    """Main entry point for manual logging."""
    if len(sys.argv) < 2:
        print("Usage: log_conversation.py <command> [text]", file=sys.stderr)
        print("Commands: user, summary, finalize, status", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1].lower()
    logger = get_logger()

    if command == "user":
        if len(sys.argv) < 3:
            print("Error: 'user' command requires message text", file=sys.stderr)
            sys.exit(1)
        message = " ".join(sys.argv[2:])
        logger.log_user_message(message)
        print(f"✓ Logged user message to {logger.session_file}", file=sys.stderr)

    elif command == "summary":
        if len(sys.argv) < 3:
            print("Error: 'summary' command requires summary text", file=sys.stderr)
            sys.exit(1)
        summary = " ".join(sys.argv[2:])

        # Get current session metadata
        session_data = logger.get_session_summary()
        metadata = {
            "files_changed": session_data.get("files_modified", []),
            "git_status": session_data.get("git_status"),
            "git_diff": session_data.get("git_diff"),
        }

        logger.log_claude_summary(summary, metadata)
        print(f"✓ Logged Claude summary to {logger.session_file}", file=sys.stderr)

    elif command == "finalize":
        logger.finalize_session()
        print(f"✓ Finalized session in {logger.session_file}", file=sys.stderr)

    elif command == "status":
        session_data = logger.get_session_summary()
        print(json.dumps(session_data, indent=2))

    else:
        print(f"Error: Unknown command '{command}'", file=sys.stderr)
        print("Valid commands: user, summary, finalize, status", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
