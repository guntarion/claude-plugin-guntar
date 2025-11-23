#!/usr/bin/env python3
"""
Agent Stop Hook
=============================================
Runs when Claude (main agent) finishes processing and stops.
Captures Claude's responses from the transcript and logs them to the conversation file.

Key Features:
- Automatically captures all Claude responses (no manual /log-summary needed)
- Parses transcript_path (JSONL format) to extract assistant messages
- Appends responses to existing session markdown file
- Updates session JSON with response data
- Enables complete conversation logging (prompts + responses)

This hook is crucial for achieving fully automatic logging of conversations.
"""

import sys
import json
import os
from pathlib import Path
from session_manager import get_session_manager
from conversation_logger import get_logger


def main():
    """Handle Stop (agent stop) event."""
    try:
        # Read hook data from stdin
        hook_data = json.load(sys.stdin)

        # Extract session ID and transcript path
        session_id = hook_data.get("session_id", "unknown")
        transcript_path = hook_data.get("transcript_path", "")

        if session_id == "unknown":
            print("Warning: No valid session_id in Stop hook", file=sys.stderr)
            sys.exit(0)

        if not transcript_path or not os.path.exists(transcript_path):
            print(f"Warning: Transcript path not found: {transcript_path}", file=sys.stderr)
            sys.exit(0)

        # Initialize session manager
        session_manager = get_session_manager()

        # Verify session exists
        if not session_manager.session_exists(session_id):
            print(f"Warning: Session {session_id} not found in Stop hook", file=sys.stderr)
            sys.exit(0)

        # Get logger instance
        logger = get_logger(session_id)

        # Parse transcript to extract messages
        messages = logger.parse_transcript(transcript_path)

        # Extract Claude's responses (role == "assistant")
        claude_responses = logger.extract_claude_responses(messages)

        if not claude_responses:
            # No responses to log
            sys.exit(0)

        # Get session data to check if we've already logged these responses
        session_data = session_manager.load_session(session_id)
        existing_response_count = len(session_data.get("responses", []))

        # Log only new responses (not already in session)
        # Note: This is a simple heuristic - we assume responses are added sequentially
        new_responses = claude_responses[existing_response_count:]

        for response in new_responses:
            # Log response to markdown file
            logger.log_claude_response(response, session_id, response_type="agent")

            # Update session JSON
            session_manager.add_response(session_id, response, response_type="agent")

        if new_responses:
            print(f"✓ Logged {len(new_responses)} Claude response(s) to session {session_id}", file=sys.stderr)

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(f"Stop hook error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(0)  # Don't block on error


if __name__ == "__main__":
    main()
