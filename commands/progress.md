---
description: Record progress entry in PROGRESS.md with timestamp
allowed-tools: [bash]
---

# Record Progress Entry

Records a progress note in PROGRESS.md with automatic timestamp. Entries are prepended to the top (most recent first).

## Steps

1. Take the user's progress note from $ARGUMENTS
2. Call the update-progresslog skill to record the entry:
   ```bash
   python ~/.claude/skills/update-progresslog/update-progresslog.py "$ARGUMENTS" "$(date '+%Y-%m-%d %H:%M:%S')"
   ```
3. Confirm the entry was recorded

## Usage Examples

```
/progress "Currently working on LDAP auth. See folder /docs/ldap for detail"
/progress "Completed API integration. Running tests now"
/progress "Blocked on database migration - waiting for DBA approval"
```

## Notes

- Progress entries are added to PROGRESS.md in the project root
- Most recent entries appear at the top
- Each entry includes a timestamp
- PROGRESS.md is created automatically if it doesn't exist
- Great for daily standups, async updates, and progress tracking
