#!/usr/bin/env python3
"""
Session End Hook
=============================================
Runs when Claude Code session ends.
Finalizes the conversation log with session statistics.

Key Improvements:
- Uses session_id to load session from session manager
- Reads file changes from session JSON (persistent storage)
- Writes comprehensive session summary to markdown
- Marks session as finalized in session JSON
"""

import sys
import json
from session_manager import get_session_manager
from conversation_logger import get_logger


def main():
    """Handle SessionEnd event."""
    try:
        # Read hook data from stdin
        hook_data = json.load(sys.stdin)

        # Extract session information
        session_id = hook_data.get("session_id", "unknown")
        reason = hook_data.get("reason", "other")

        if session_id == "unknown":
            print("Warning: No valid session_id in SessionEnd hook", file=sys.stderr)
            sys.exit(0)

        # Initialize session manager
        session_manager = get_session_manager()

        # Check if session exists
        if not session_manager.session_exists(session_id):
            print(f"Warning: Session {session_id} not found in SessionEnd hook", file=sys.stderr)
            sys.exit(0)

        # Get logger instance with session ID
        logger = get_logger(session_id)

        # Finalize session (reads file changes from session JSON)
        logger.finalize_session(session_id)

        # Get session summary
        summary = logger.get_session_summary(session_id)
        log_file = summary.get("session_file", "unknown")

        # Write to stderr for visibility
        print(f"✓ Session finalized: {log_file}", file=sys.stderr)
        print(f"  Reason: {reason}", file=sys.stderr)
        print(f"  Prompts logged: {summary.get('prompts_count', 0)}", file=sys.stderr)
        print(f"  Responses logged: {summary.get('responses_count', 0)}", file=sys.stderr)
        print(f"  Files modified: {len(summary.get('files_modified', []))}", file=sys.stderr)

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(f"SessionEnd hook error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(0)  # Don't block session end


if __name__ == "__main__":
    main()
