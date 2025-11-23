#!/usr/bin/env python3
"""
Agent Stop Hook
=============================================
Runs when Claude (main agent) finishes processing and stops.
"""

import sys
import json


def main():
    """Handle Stop (agent stop) event."""
    try:
        # Read hook data from stdin
        hook_data = json.load(sys.stdin)

        # Extract session ID
        session_id = hook_data.get("session_id", "unknown")

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(f"Stop hook error: {e}", file=sys.stderr)
        sys.exit(0)  # Don't block on error


if __name__ == "__main__":
    main()
