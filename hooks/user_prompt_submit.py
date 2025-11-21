#!/usr/bin/env python3
"""
User Prompt Submit Hook
=============================================
Runs when user submits a prompt, before Claude processes it.
Logs the user's prompt to the conversation log.

Key Improvements:
- Uses session_id to load existing session
- Appends to existing markdown file (doesn't create new file)
- Updates session JSON with prompt data
- Enables one session = one log file
"""

import sys
import json
from session_manager import get_session_manager
from conversation_logger import get_logger


def main():
    """Handle UserPromptSubmit event."""
    try:
        # Read hook data from stdin
        hook_data = json.load(sys.stdin)

        # Extract the user's prompt and session ID
        prompt = hook_data.get("prompt", "")
        session_id = hook_data.get("session_id", "unknown")

        if not prompt.strip():
            sys.exit(0)

        if session_id == "unknown":
            print("Warning: No valid session_id in UserPromptSubmit hook", file=sys.stderr)
            sys.exit(0)

        # Initialize session manager
        session_manager = get_session_manager()

        # Verify session exists (should be created by SessionStart hook)
        if not session_manager.session_exists(session_id):
            print(f"Warning: Session {session_id} not found, creating new session", file=sys.stderr)
            # Create session if it doesn't exist (fallback)
            session_data = session_manager.get_or_create_session(session_id)
            logger = get_logger(session_id)
            logger.create_session_file(session_id, session_data.get("log_file"))

        # Get logger instance with session ID
        logger = get_logger(session_id)

        # Log the user prompt to markdown file (appends to existing file)
        logger.log_user_message(prompt, session_id)

        # Update session JSON with prompt data
        session_manager.add_prompt(session_id, prompt)

        # Write confirmation to stderr (for debugging)
        # print(f"✓ Logged user prompt to session {session_id}", file=sys.stderr)

        # Exit successfully without adding context to Claude
        sys.exit(0)

    except Exception as e:
        print(f"UserPromptSubmit hook error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(0)  # Don't block prompt submission on error


if __name__ == "__main__":
    main()
