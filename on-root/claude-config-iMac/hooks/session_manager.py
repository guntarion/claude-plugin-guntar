#!/usr/bin/env python3
"""
Session Manager for Conversation Logging
==========================================
Provides file-based session persistence to ensure one session = one log file.

Key Features:
- Persists session state across hook invocations
- Uses session_id to maintain continuity
- Stores session data in .claude/data/sessions/{session_id}.json
- Generates consistent log file paths per session

This solves the problem of creating multiple log files per session by storing
session metadata (log file path, timestamps, prompts, file changes) in a persistent
JSON file that all hooks can read/write to.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List


class SessionManager:
    """Manages session persistence for conversation logging."""

    def __init__(self, project_root: Optional[Path] = None):
        """
        Initialize the session manager.

        Args:
            project_root: Project root directory (defaults to auto-detect)
        """
        self.project_root = project_root or self._get_project_root()
        self.sessions_dir = self.project_root / ".claude" / "data" / "sessions"
        self.sessions_dir.mkdir(parents=True, exist_ok=True)

    def _get_project_root(self) -> Path:
        """Get the project root directory (parent of .claude folder)."""
        return Path(__file__).parent.parent.parent

    def get_session_file_path(self, session_id: str) -> Path:
        """
        Get the path to a session's JSON file.

        Args:
            session_id: Unique session identifier

        Returns:
            Path to session JSON file
        """
        return self.sessions_dir / f"{session_id}.json"

    def session_exists(self, session_id: str) -> bool:
        """
        Check if a session exists.

        Args:
            session_id: Unique session identifier

        Returns:
            True if session file exists, False otherwise
        """
        return self.get_session_file_path(session_id).exists()

    def load_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Load session data from file.

        Args:
            session_id: Unique session identifier

        Returns:
            Session data dictionary or None if session doesn't exist
        """
        session_file = self.get_session_file_path(session_id)

        if not session_file.exists():
            return None

        try:
            with open(session_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load session {session_id}: {e}", file=sys.stderr)
            return None

    def save_session(self, session_id: str, data: Dict[str, Any]) -> bool:
        """
        Save session data to file.

        Args:
            session_id: Unique session identifier
            data: Session data dictionary to save

        Returns:
            True if save successful, False otherwise
        """
        session_file = self.get_session_file_path(session_id)

        try:
            with open(session_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except IOError as e:
            print(f"Error: Failed to save session {session_id}: {e}", file=sys.stderr)
            return False

    def create_session(self, session_id: str, log_file_path: str) -> Dict[str, Any]:
        """
        Create a new session with initial data.

        Args:
            session_id: Unique session identifier
            log_file_path: Path to the markdown log file for this session

        Returns:
            New session data dictionary
        """
        now = datetime.now()

        session_data = {
            "session_id": session_id,
            "start_time": now.isoformat(),
            "log_file": log_file_path,
            "prompts": [],
            "responses": [],
            "file_changes": [],
            "finalized": False,
            "created_at": now.isoformat(),
            "updated_at": now.isoformat()
        }

        self.save_session(session_id, session_data)
        return session_data

    def get_or_create_session(self, session_id: str) -> Dict[str, Any]:
        """
        Get existing session or create a new one.

        Args:
            session_id: Unique session identifier

        Returns:
            Session data dictionary
        """
        # Try to load existing session
        session_data = self.load_session(session_id)

        if session_data is not None:
            return session_data

        # Create new session with log file path
        log_file_path = self.generate_log_file_path()
        return self.create_session(session_id, log_file_path)

    def update_session(self, session_id: str, updates: Dict[str, Any]) -> bool:
        """
        Update specific fields in a session.

        Args:
            session_id: Unique session identifier
            updates: Dictionary of fields to update

        Returns:
            True if update successful, False otherwise
        """
        session_data = self.load_session(session_id)

        if session_data is None:
            print(f"Warning: Cannot update non-existent session {session_id}", file=sys.stderr)
            return False

        # Update fields
        session_data.update(updates)
        session_data["updated_at"] = datetime.now().isoformat()

        return self.save_session(session_id, session_data)

    def add_prompt(self, session_id: str, prompt: str, timestamp: Optional[str] = None) -> bool:
        """
        Add a user prompt to the session.

        Args:
            session_id: Unique session identifier
            prompt: User prompt text
            timestamp: Optional timestamp (defaults to now)

        Returns:
            True if successful, False otherwise
        """
        session_data = self.load_session(session_id)

        if session_data is None:
            return False

        prompt_entry = {
            "timestamp": timestamp or datetime.now().strftime("%H:%M:%S"),
            "content": prompt
        }

        session_data["prompts"].append(prompt_entry)
        session_data["updated_at"] = datetime.now().isoformat()

        return self.save_session(session_id, session_data)

    def add_response(self, session_id: str, response: str, response_type: str = "agent",
                     timestamp: Optional[str] = None) -> bool:
        """
        Add a Claude response to the session.

        Args:
            session_id: Unique session identifier
            response: Response text
            response_type: Type of response ("agent" or "subagent")
            timestamp: Optional timestamp (defaults to now)

        Returns:
            True if successful, False otherwise
        """
        session_data = self.load_session(session_id)

        if session_data is None:
            return False

        response_entry = {
            "timestamp": timestamp or datetime.now().strftime("%H:%M:%S"),
            "content": response,
            "type": response_type
        }

        session_data["responses"].append(response_entry)
        session_data["updated_at"] = datetime.now().isoformat()

        return self.save_session(session_id, session_data)

    def add_file_change(self, session_id: str, file_path: str) -> bool:
        """
        Track a file change in the session.

        Args:
            session_id: Unique session identifier
            file_path: Path to the changed file

        Returns:
            True if successful, False otherwise
        """
        session_data = self.load_session(session_id)

        if session_data is None:
            return False

        # Avoid duplicates
        if file_path not in session_data["file_changes"]:
            session_data["file_changes"].append(file_path)
            session_data["updated_at"] = datetime.now().isoformat()
            return self.save_session(session_id, session_data)

        return True

    def get_log_file_path(self, session_id: str) -> Optional[str]:
        """
        Get the log file path for a session.

        Args:
            session_id: Unique session identifier

        Returns:
            Log file path string or None if session doesn't exist
        """
        session_data = self.load_session(session_id)
        return session_data.get("log_file") if session_data else None

    def generate_log_file_path(self, base_dir: str = "dev-logs") -> str:
        """
        Generate a new log file path for a session.

        Args:
            base_dir: Base directory for logs (default: "dev-logs")

        Returns:
            Relative path to the new log file
        """
        today = datetime.now().strftime("%Y-%m-%d")
        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")

        return f"{base_dir}/{today}/{timestamp}-conversation.md"

    def finalize_session(self, session_id: str) -> bool:
        """
        Mark a session as finalized.

        Args:
            session_id: Unique session identifier

        Returns:
            True if successful, False otherwise
        """
        return self.update_session(session_id, {
            "finalized": True,
            "end_time": datetime.now().isoformat()
        })

    def cleanup_old_sessions(self, days: int = 30) -> int:
        """
        Clean up session files older than specified days.

        Args:
            days: Number of days to keep sessions (default: 30)

        Returns:
            Number of sessions deleted
        """
        cutoff_date = datetime.now().timestamp() - (days * 24 * 60 * 60)
        deleted_count = 0

        for session_file in self.sessions_dir.glob("*.json"):
            if session_file.stat().st_mtime < cutoff_date:
                try:
                    session_file.unlink()
                    deleted_count += 1
                except OSError:
                    pass

        return deleted_count


# Convenience functions for use in hooks
def get_session_manager() -> SessionManager:
    """Get a SessionManager instance."""
    return SessionManager()


def load_session_data(session_id: str) -> Optional[Dict[str, Any]]:
    """
    Load session data (convenience function).

    Args:
        session_id: Unique session identifier

    Returns:
        Session data dictionary or None
    """
    manager = get_session_manager()
    return manager.load_session(session_id)


def save_session_data(session_id: str, data: Dict[str, Any]) -> bool:
    """
    Save session data (convenience function).

    Args:
        session_id: Unique session identifier
        data: Session data dictionary

    Returns:
        True if successful, False otherwise
    """
    manager = get_session_manager()
    return manager.save_session(session_id, data)


if __name__ == "__main__":
    """Test the session manager."""
    import sys

    print("Testing SessionManager...", file=sys.stderr)

    manager = SessionManager()
    test_session_id = "test-session-123"

    # Test creating a session
    session_data = manager.get_or_create_session(test_session_id)
    print(f"Created session: {session_data['session_id']}", file=sys.stderr)
    print(f"Log file: {session_data['log_file']}", file=sys.stderr)

    # Test adding prompts
    manager.add_prompt(test_session_id, "Test prompt 1")
    manager.add_prompt(test_session_id, "Test prompt 2")

    # Test adding responses
    manager.add_response(test_session_id, "Test response 1", "agent")

    # Test adding file changes
    manager.add_file_change(test_session_id, "test/file1.py")
    manager.add_file_change(test_session_id, "test/file2.py")

    # Load and display
    final_data = manager.load_session(test_session_id)
    print("\nFinal session data:", file=sys.stderr)
    print(json.dumps(final_data, indent=2), file=sys.stderr)

    # Cleanup test
    manager.get_session_file_path(test_session_id).unlink()
    print("\nTest session cleaned up.", file=sys.stderr)
