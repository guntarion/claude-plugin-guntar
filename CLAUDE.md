### Work Keywords

- **"commit my changes"** or **"save my work"**: Execute `/commit` command
- **"commit and push"** or **"ship it"**: Execute `/commit-push` command
- **"log summary"** or **"save log"**: Execute `/log-summary` command
- **"log finalize"** or **"end session"**: Execute `/log-finalize` command
- **"log status"** or **"check log"**: Execute `/log-status` command

### Conversation Logging

This project includes an **automatic conversation logging system** that tracks all development sessions.

#### How It Works

- **Location**: All logs are stored in `dev-logs/YYYY-MM-DD/` folders
- **Format**: Each conversation creates a timestamped markdown file: `YYYY-MM-DD-HHmmss-conversation.md`
- **Content**: Logs capture:
  - User prompts (all messages)
  - Claude's task summaries (not full responses)
  - File changes with timestamps
  - Git status and diff summaries
  - Session metadata (duration, modified files)

#### Automatic Logging

The hook system (`hook_handler.py`) automatically tracks:
- File modifications via tool events (Edit, Write, Read)
- Tool usage patterns
- Git repository status

#### Logging Commands

**Slash Commands (Recommended):**

```bash
# Log Claude's summary of completed work
/log-summary [optional: summary text]

# Finalize the current session (adds session summary)
/log-finalize

# Check current session status
/log-status
```

**Direct Python Commands (Alternative):**

```bash
# Log a user message/prompt
python .claude/hooks/log_conversation.py user "Your prompt text here"

# Log Claude's summary of completed work
python .claude/hooks/log_conversation.py summary "Summary of what was accomplished"

# Finalize the current session (adds session summary)
python .claude/hooks/log_conversation.py finalize

# Check current session status
python .claude/hooks/log_conversation.py status
```

#### When to Log Summaries

Log Claude's summaries at key milestones:
- After completing a major feature
- Before and after refactoring
- When fixing critical bugs
- At the end of a work session

**Examples:**

Using slash commands:
```bash
/log-summary Implemented user authentication with Google OAuth and LDAP. Created 5 new API routes and updated database schema. All tests passing.
```

Or simply say: "log summary" and provide the details when prompted.

Using direct command:
```bash
python .claude/hooks/log_conversation.py summary "Implemented user authentication with Google OAuth and LDAP. Created 5 new API routes and updated database schema. All tests passing."
```

#### Benefits

- **Development History**: Track your thought process and decision-making
- **Project Documentation**: Auto-generated chronological record of changes
- **Knowledge Transfer**: New team members can review conversation logs
- **Debugging**: Trace when and why changes were made
- **Progress Tracking**: See what was accomplished each day

#### File Structure

```
dev-logs/
├── 2025-11-02/
│   ├── 2025-11-02-140530-conversation.md
│   ├── 2025-11-02-163245-conversation.md
│   └── 2025-11-02-183853-conversation.md
└── 2025-11-03/
    └── 2025-11-03-090120-conversation.md
```

Each file contains:
1. Session header with start time and project name
2. Timestamped user prompts
3. Timestamped Claude summaries with metadata
4. Session footer with end time, duration, and file changes
