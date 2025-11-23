#!/usr/bin/env python3
"""
Session Start Hook
=============================================
Runs when Claude Code starts or resumes a session.
"""

import sys
import json


def main():
    """Handle SessionStart event."""
    try:
        # Read hook data from stdin
        hook_data = json.load(sys.stdin)

        # Extract session information
        session_id = hook_data.get("session_id", "unknown")

        print(f"✓ Session started: {session_id}", file=sys.stderr)

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(f"SessionStart hook error: {e}", file=sys.stderr)
        sys.exit(0)  # Don't block session start on error


if __name__ == "__main__":
    main()
