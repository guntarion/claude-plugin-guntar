#!/usr/bin/env python3
"""
SubAgent Stop Hook
=============================================
Runs when a sub-agent (e.g., Task tool agents) finishes processing and stops.
"""

import sys
import json


def main():
    """Handle SubagentStop event."""
    try:
        # Read hook data from stdin
        hook_data = json.load(sys.stdin)

        # Extract session ID and subagent info
        session_id = hook_data.get("session_id", "unknown")
        subagent_type = hook_data.get("subagent_type", "unknown")

        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(f"SubagentStop hook error: {e}", file=sys.stderr)
        sys.exit(0)  # Don't block on error


if __name__ == "__main__":
    main()
