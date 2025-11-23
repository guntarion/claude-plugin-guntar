#!/usr/bin/env python3
"""
Session Start Hook
=============================================
Runs when Claude Code starts or resumes a session.
Initializes the conversation logger and session persistence for a new session.

Key Improvements:
- Uses SessionManager for file-based session persistence
- Creates or loads existing session based on session_id
- Creates markdown log file only once per session (not per prompt)
- Enables one session = one log file
"""

import sys
import json
from pathlib import Path
from session_manager import SessionManager, get_session_manager
from conversation_logger import get_logger


def main():
    """Handle SessionStart event."""
    try:
        # Read hook data from stdin
        hook_data = json.load(sys.stdin)

        # Extract session information
        session_id = hook_data.get("session_id", "unknown")
        source = hook_data.get("source", "unknown")

        if session_id == "unknown":
            print("Warning: No valid session_id in SessionStart hook", file=sys.stderr)
            sys.exit(0)

        # Initialize session manager
        session_manager = get_session_manager()

        # Check if session already exists (resume case)
        session_exists = session_manager.session_exists(session_id)

        if session_exists:
            # Load existing session
            session_data = session_manager.load_session(session_id)
            log_file = session_data.get("log_file", "unknown") if session_data else "unknown"

            print(f"📝 Conversation logging resumed: {log_file}", file=sys.stderr)
            print(f"   Session ID: {session_id}", file=sys.stderr)
        else:
            # Create new session
            session_data = session_manager.get_or_create_session(session_id)
            log_file_path = session_data.get("log_file")

            # Create logger and markdown file
            logger = get_logger(session_id)
            log_file = logger.create_session_file(session_id, log_file_path)

            print(f"📝 Conversation logging started: {log_file_path}", file=sys.stderr)
            print(f"   Session ID: {session_id}", file=sys.stderr)
            print(f"   Session file: {session_manager.get_session_file_path(session_id)}", file=sys.stderr)

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(f"SessionStart hook error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(0)  # Don't block session start on error


if __name__ == "__main__":
    main()
