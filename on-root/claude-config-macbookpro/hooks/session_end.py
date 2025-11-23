#!/usr/bin/env python3
"""
Session End Hook
=============================================
Runs when Claude Code session ends.
"""

import sys
import json


def main():
    """Handle SessionEnd event."""
    try:
        # Read hook data from stdin
        hook_data = json.load(sys.stdin)

        # Extract session information
        session_id = hook_data.get("session_id", "unknown")
        reason = hook_data.get("reason", "other")

        print(f"✓ Session ended: {session_id} (reason: {reason})", file=sys.stderr)

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(f"SessionEnd hook error: {e}", file=sys.stderr)
        sys.exit(0)  # Don't block session end


if __name__ == "__main__":
    main()
