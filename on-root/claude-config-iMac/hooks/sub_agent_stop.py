#!/usr/bin/env python3
"""
SubAgent Stop Hook
=============================================
Runs when a sub-agent (e.g., Task tool agents) finishes processing and stops.
Captures sub-agent activities and logs them inline in the conversation file.

Key Features:
- Captures sub-agent responses from transcript
- Logs inline with clear **[Sub-Agent]** markers
- Parses transcript_path to extract sub-agent messages
- Appends to existing session markdown file
- Updates session JSON with sub-agent response data

Examples of sub-agents:
- Task tool agents (Explore, Plan, generator-*, associator-*, etc.)
- Other specialized agents launched during conversation

This enables complete tracking of all agent activities in one log file.
"""

import sys
import json
import os
from pathlib import Path
from session_manager import get_session_manager
from conversation_logger import get_logger


def main():
    """Handle SubagentStop event."""
    try:
        # Read hook data from stdin
        hook_data = json.load(sys.stdin)

        # Extract session ID, transcript path, and subagent info
        session_id = hook_data.get("session_id", "unknown")
        transcript_path = hook_data.get("transcript_path", "")
        subagent_type = hook_data.get("subagent_type", "unknown")
        subagent_description = hook_data.get("description", "")

        if session_id == "unknown":
            print("Warning: No valid session_id in SubagentStop hook", file=sys.stderr)
            sys.exit(0)

        if not transcript_path or not os.path.exists(transcript_path):
            print(f"Warning: Transcript path not found: {transcript_path}", file=sys.stderr)
            sys.exit(0)

        # Initialize session manager
        session_manager = get_session_manager()

        # Verify session exists
        if not session_manager.session_exists(session_id):
            print(f"Warning: Session {session_id} not found in SubagentStop hook", file=sys.stderr)
            sys.exit(0)

        # Get logger instance
        logger = get_logger(session_id)

        # Parse transcript to extract messages
        messages = logger.parse_transcript(transcript_path)

        # Extract sub-agent responses
        subagent_responses = logger.extract_claude_responses(messages)

        if not subagent_responses:
            # No responses to log
            sys.exit(0)

        # Create a summary of sub-agent activity
        subagent_header = f"Sub-Agent: {subagent_type}"
        if subagent_description:
            subagent_header += f" - {subagent_description}"

        # Combine all responses with header
        combined_response = f"**{subagent_header}**\n\n"

        # For sub-agents, we typically want the final response or a summary
        # You can customize this logic based on your needs
        if len(subagent_responses) == 1:
            combined_response += subagent_responses[0]
        else:
            # Multiple responses - include all or just the last one
            # For now, include all for completeness
            for i, response in enumerate(subagent_responses, 1):
                if len(subagent_responses) > 1:
                    combined_response += f"\n**Response {i}:**\n{response}\n"
                else:
                    combined_response += response

        # Log sub-agent response to markdown file (inline with [Sub-Agent] marker)
        logger.log_claude_response(combined_response, session_id, response_type="subagent")

        # Update session JSON
        session_manager.add_response(session_id, combined_response, response_type="subagent")

        print(f"✓ Logged sub-agent ({subagent_type}) activity to session {session_id}", file=sys.stderr)

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(f"SubagentStop hook error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(0)  # Don't block on error


if __name__ == "__main__":
    main()
