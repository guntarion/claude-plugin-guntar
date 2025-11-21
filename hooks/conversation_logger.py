#!/usr/bin/env python3
"""
Conversation Logger for Claude Code
=============================================
Logs user prompts and Claude's summaries to organized markdown files.

Log Structure:
- dev-logs/YYYY-MM-DD/YYYY-MM-DD-HHmmss-conversation.md
- Captures: user prompts, task summaries, file changes, git status, timestamps

Configuration:
- One file per conversation/session (using session_id for persistence)
- Full automatic logging: all prompts + responses + sub-agent activities
- Metadata: timestamps, file changes, git status

Session Persistence:
- Uses SessionManager for file-based session tracking
- Session state persists across hook invocations
- Ensures one session = one markdown file
"""

import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List

# Import the session manager
from session_manager import SessionManager


class ConversationLogger:
    """Handles logging of Claude Code conversations to markdown files."""

    def __init__(self, base_dir: str = "dev-logs", session_id: Optional[str] = None):
        """
        Initialize the conversation logger.

        Args:
            base_dir: Base directory for all logs (relative to project root)
            session_id: Optional session ID (required for session-aware operations)
        """
        self.base_dir = Path(base_dir)
        self.session_id = session_id
        self.session_manager = SessionManager()

    def _get_project_root(self) -> Path:
        """Get the project root directory (parent of .claude folder)."""
        return Path(__file__).parent.parent.parent

    def _ensure_log_directory(self) -> Path:
        """
        Create and return the log directory for today.

        Returns:
            Path to today's log directory (YYYY-MM-DD format)
        """
        project_root = self._get_project_root()
        today = datetime.now().strftime("%Y-%m-%d")
        log_dir = project_root / self.base_dir / today

        log_dir.mkdir(parents=True, exist_ok=True)
        return log_dir

    def get_session_log_file(self, session_id: Optional[str] = None) -> Optional[Path]:
        """
        Get the log file path for a session from session manager.

        Args:
            session_id: Session ID (uses self.session_id if not provided)

        Returns:
            Path to the session's markdown file or None if session doesn't exist
        """
        sid = session_id or self.session_id
        if not sid:
            return None

        log_file_path = self.session_manager.get_log_file_path(sid)
        if not log_file_path:
            return None

        return self._get_project_root() / log_file_path

    def create_session_file(self, session_id: str, log_file_path: str) -> Path:
        """
        Create a new session markdown file with header.

        Args:
            session_id: Session ID
            log_file_path: Relative path to the log file

        Returns:
            Path to the created file
        """
        project_root = self._get_project_root()
        full_path = project_root / log_file_path

        # Ensure directory exists
        full_path.parent.mkdir(parents=True, exist_ok=True)

        # Write header
        self._write_session_header(full_path)

        return full_path

    def _write_session_header(self, file_path: Path):
        """
        Write the initial header for a new session file.

        Args:
            file_path: Path to the session file
        """
        session_start = datetime.now()

        header = f"""# Claude Code Conversation Log

**Session Started:** {session_start.strftime("%Y-%m-%d %H:%M:%S")}
**Project:** PLN Nusantara Power Learning Path

---

"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(header)

    def _get_git_status(self) -> Optional[str]:
        """
        Get current git status if available.

        Returns:
            Git status string or None if git not available
        """
        try:
            project_root = self._get_project_root()
            result = subprocess.run(
                ["git", "status", "--short"],
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
            return None
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            return None

    def _get_git_diff_summary(self) -> Optional[str]:
        """
        Get a summary of git changes (number of files changed, insertions, deletions).

        Returns:
            Git diff summary or None
        """
        try:
            project_root = self._get_project_root()
            result = subprocess.run(
                ["git", "diff", "--shortstat"],
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
            return None
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            return None

    def _format_timestamp(self) -> str:
        """Get formatted timestamp for log entries."""
        return datetime.now().strftime("%H:%M:%S")

    def _extract_file_changes_from_event(self, hook_data: Dict[str, Any]) -> List[str]:
        """
        Extract file paths from tool events.

        Args:
            hook_data: Hook event data from Claude

        Returns:
            List of file paths that were modified
        """
        files = []
        tool_name = hook_data.get("tool_name", "")
        tool_input = hook_data.get("tool_input", {})

        # Extract file path based on tool type
        if tool_name in ["Edit", "Write", "Read"]:
            file_path = tool_input.get("file_path")
            if file_path:
                files.append(file_path)
        elif tool_name == "Bash":
            # Try to extract files from bash commands (e.g., git add, touch, etc.)
            command = tool_input.get("command", "")
            # Simple heuristic: look for file paths in common commands
            # This is not perfect but covers most cases
            pass  # Could be enhanced if needed

        return files

    def log_user_message(self, message: str, session_id: Optional[str] = None):
        """
        Log a user prompt/message.

        Args:
            message: The user's message/prompt
            session_id: Session ID (uses self.session_id if not provided)
        """
        sid = session_id or self.session_id
        if not sid:
            print("Warning: No session_id provided for logging user message", file=sys.stderr)
            return

        session_file = self.get_session_log_file(sid)
        if not session_file:
            print(f"Warning: No log file found for session {sid}", file=sys.stderr)
            return

        timestamp = self._format_timestamp()

        log_entry = f"""## [{timestamp}] User Prompt

{message}

"""

        self._append_to_file(session_file, log_entry)

    def log_claude_summary(self, summary: str, session_id: Optional[str] = None,
                          metadata: Optional[Dict[str, Any]] = None):
        """
        Log Claude's task summary/completion report.

        Args:
            summary: Claude's summary or report
            session_id: Session ID (uses self.session_id if not provided)
            metadata: Optional metadata (tool usage, files changed, etc.)
        """
        sid = session_id or self.session_id
        if not sid:
            print("Warning: No session_id provided for logging Claude summary", file=sys.stderr)
            return

        session_file = self.get_session_log_file(sid)
        if not session_file:
            print(f"Warning: No log file found for session {sid}", file=sys.stderr)
            return

        timestamp = self._format_timestamp()

        log_entry = f"""## [{timestamp}] Claude Summary

{summary}

"""

        # Add metadata if available
        if metadata:
            log_entry += "**Metadata:**\n"

            if metadata.get("files_changed"):
                log_entry += f"- Files modified: {', '.join(metadata['files_changed'])}\n"

            if metadata.get("tools_used"):
                log_entry += f"- Tools used: {', '.join(metadata['tools_used'])}\n"

            if metadata.get("git_status"):
                log_entry += f"- Git status:\n```\n{metadata['git_status']}\n```\n"

            if metadata.get("git_diff"):
                log_entry += f"- Git changes: {metadata['git_diff']}\n"

            log_entry += "\n"

        log_entry += "---\n\n"

        self._append_to_file(session_file, log_entry)

    def log_claude_response(self, response: str, session_id: Optional[str] = None,
                           response_type: str = "agent"):
        """
        Log Claude's response from transcript.

        Args:
            response: Claude's response text
            session_id: Session ID (uses self.session_id if not provided)
            response_type: Type of response ("agent" or "subagent")
        """
        sid = session_id or self.session_id
        if not sid:
            print("Warning: No session_id provided for logging Claude response", file=sys.stderr)
            return

        session_file = self.get_session_log_file(sid)
        if not session_file:
            print(f"Warning: No log file found for session {sid}", file=sys.stderr)
            return

        timestamp = self._format_timestamp()

        if response_type == "subagent":
            log_entry = f"""## [{timestamp}] Claude Response **[Sub-Agent]**

{response}

---

"""
        else:
            log_entry = f"""## [{timestamp}] Claude Response

{response}

---

"""

        self._append_to_file(session_file, log_entry)

    def _append_to_file(self, file_path: Path, content: str):
        """
        Append content to a file.

        Args:
            file_path: Path to the file
            content: Content to append
        """
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(content)

    def parse_transcript(self, transcript_path: str) -> List[Dict[str, Any]]:
        """
        Parse a JSONL transcript file.

        Args:
            transcript_path: Path to the transcript file

        Returns:
            List of message dictionaries
        """
        messages = []

        try:
            with open(transcript_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            msg = json.loads(line)
                            messages.append(msg)
                        except json.JSONDecodeError as e:
                            print(f"Warning: Failed to parse transcript line: {e}", file=sys.stderr)
        except (IOError, FileNotFoundError) as e:
            print(f"Warning: Failed to read transcript file {transcript_path}: {e}", file=sys.stderr)

        return messages

    def extract_claude_responses(self, messages: List[Dict[str, Any]]) -> List[str]:
        """
        Extract Claude's text responses from transcript messages.

        Args:
            messages: List of message dictionaries from transcript

        Returns:
            List of response text strings
        """
        responses = []

        for msg in messages:
            if msg.get('role') == 'assistant':
                # Extract text content from the message
                content = msg.get('content', [])

                # Handle both string and list content formats
                if isinstance(content, str):
                    responses.append(content)
                elif isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict) and block.get('type') == 'text':
                            text = block.get('text', '')
                            if text:
                                responses.append(text)

        return responses

    def log_event(self, hook_data: Dict[str, Any]):
        """
        Log an event from Claude's hook system.

        This is called on every hook event to track file changes and
        potentially trigger logging.

        Args:
            hook_data: Hook event data from Claude
        """
        # Extract and track file changes
        files = self._extract_file_changes_from_event(hook_data)
        for file_path in files:
            self.files_modified.add(file_path)

        # For "user-prompt-submit" events, we log the user message
        event_name = hook_data.get("hook_event_name", "")

        # Note: The actual user message isn't available in the hook data,
        # so we'll need to handle this differently or document that
        # users should manually trigger logging for summaries

    def get_session_summary(self, session_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get summary of the current session from session manager.

        Args:
            session_id: Session ID (uses self.session_id if not provided)

        Returns:
            Dictionary with session statistics
        """
        sid = session_id or self.session_id
        if not sid:
            return {}

        session_data = self.session_manager.load_session(sid)
        if not session_data:
            return {}

        return {
            "session_id": sid,
            "session_file": session_data.get("log_file"),
            "session_start": session_data.get("start_time"),
            "files_modified": session_data.get("file_changes", []),
            "prompts_count": len(session_data.get("prompts", [])),
            "responses_count": len(session_data.get("responses", [])),
            "git_status": self._get_git_status(),
            "git_diff": self._get_git_diff_summary(),
        }

    def finalize_session(self, session_id: Optional[str] = None):
        """
        Finalize the session by writing session summary.

        Args:
            session_id: Session ID (uses self.session_id if not provided)
        """
        sid = session_id or self.session_id
        if not sid:
            print("Warning: No session_id provided for finalizing session", file=sys.stderr)
            return

        session_data = self.session_manager.load_session(sid)
        if not session_data:
            print(f"Warning: No session data found for session {sid}", file=sys.stderr)
            return

        session_file = self.get_session_log_file(sid)
        if not session_file:
            print(f"Warning: No log file found for session {sid}", file=sys.stderr)
            return

        session_end = datetime.now()
        session_start = datetime.fromisoformat(session_data.get("start_time", session_end.isoformat()))
        duration = session_end - session_start

        files_modified = session_data.get("file_changes", [])

        footer = f"""---

## Session Summary

**Session Ended:** {session_end.strftime("%Y-%m-%d %H:%M:%S")}
**Duration:** {str(duration).split('.')[0]}
**Files Modified:** {len(files_modified)}
**Prompts:** {len(session_data.get("prompts", []))}
**Responses:** {len(session_data.get("responses", []))}

"""

        if files_modified:
            footer += "**Modified Files:**\n"
            for file_path in sorted(files_modified):
                footer += f"- `{file_path}`\n"
            footer += "\n"

        git_status = self._get_git_status()
        if git_status:
            footer += f"**Final Git Status:**\n```\n{git_status}\n```\n\n"

        git_diff = self._get_git_diff_summary()
        if git_diff:
            footer += f"**Git Changes:** {git_diff}\n\n"

        self._append_to_file(session_file, footer)

        # Mark session as finalized in session manager
        self.session_manager.finalize_session(sid)


# Convenience functions for use in hooks
def get_logger(session_id: Optional[str] = None) -> ConversationLogger:
    """
    Get a ConversationLogger instance.

    Args:
        session_id: Optional session ID for session-aware operations

    Returns:
        ConversationLogger instance
    """
    return ConversationLogger(session_id=session_id)


def log_to_markdown(event_type: str, content: str, session_id: str,
                   metadata: Optional[Dict[str, Any]] = None):
    """
    Convenience function to log to markdown.

    Args:
        event_type: Type of event ("user_message", "claude_summary", or "claude_response")
        content: The content to log
        session_id: Session ID
        metadata: Optional metadata dictionary
    """
    logger = get_logger(session_id)

    if event_type == "user_message":
        logger.log_user_message(content, session_id)
    elif event_type == "claude_summary":
        logger.log_claude_summary(content, session_id, metadata)
    elif event_type == "claude_response":
        logger.log_claude_response(content, session_id, metadata.get("response_type", "agent") if metadata else "agent")
    else:
        # Generic event logging
        logger.log_event({"content": content, "metadata": metadata})


if __name__ == "__main__":
    """
    Test the logger when run directly.
    """
    print("Testing Conversation Logger...", file=sys.stderr)

    # Create a test session
    test_session_id = f"test-session-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Initialize session manager and create session
    from session_manager import SessionManager
    session_manager = SessionManager()
    session_data = session_manager.get_or_create_session(test_session_id)
    print(f"Created test session: {test_session_id}", file=sys.stderr)
    print(f"Log file: {session_data['log_file']}", file=sys.stderr)

    # Create logger with session ID
    logger = get_logger(test_session_id)

    # Create the markdown file
    log_file = logger.create_session_file(test_session_id, session_data['log_file'])
    print(f"Created log file: {log_file}", file=sys.stderr)

    # Test logging
    logger.log_user_message("Test user prompt: Implement a new feature", test_session_id)
    session_manager.add_prompt(test_session_id, "Test user prompt: Implement a new feature")

    logger.log_claude_response("I'll help you implement that feature.", test_session_id)
    session_manager.add_response(test_session_id, "I'll help you implement that feature.")

    logger.log_claude_summary(
        "Implemented the feature successfully. Created 3 new files and modified 2 existing files.",
        test_session_id,
        metadata={
            "files_changed": ["src/feature.ts", "src/index.ts"],
            "tools_used": ["Write", "Edit"],
            "git_status": "M  src/feature.ts\nM  src/index.ts",
            "git_diff": "2 files changed, 45 insertions(+), 5 deletions(-)"
        }
    )

    # Track file changes
    session_manager.add_file_change(test_session_id, "src/feature.ts")
    session_manager.add_file_change(test_session_id, "src/index.ts")

    # Finalize
    logger.finalize_session(test_session_id)

    print(f"\nTest log created at: {log_file}", file=sys.stderr)
    print("Session summary:", json.dumps(
        logger.get_session_summary(test_session_id), indent=2), file=sys.stderr)

    # Cleanup test files
    print("\nCleaning up test files...", file=sys.stderr)
    if log_file.exists():
        log_file.unlink()
    session_file = session_manager.get_session_file_path(test_session_id)
    if session_file.exists():
        session_file.unlink()
    print("Test completed successfully!", file=sys.stderr)
