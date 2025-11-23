---
description: Create a meaningful git commit for all changes
allowed-tools: [bash]
---

# Git Commit with Meaningful Message

Create a conventional commit message for all current changes.

## Steps

### Phase 1: Review Changes
1. Run `git status` to see all changes
2. Run `git diff --stat` to review the changes summary
3. Run `git branch --show-current` to confirm the current branch

### Phase 2: Create Commit Message
4. Analyze the changes and determine:
   - The main purpose of the changes
   - The appropriate conventional commit type:
     - `feat:` for new features
     - `fix:` for bug fixes
     - `docs:` for documentation changes
     - `style:` for formatting/style changes
     - `refactor:` for code refactoring
     - `test:` for test additions/changes
     - `chore:` for maintenance tasks
     - `perf:` for performance improvements
5. Create a clear, descriptive commit message that:
   - Starts with the conventional commit type
   - Summarizes the changes in 50-72 characters
   - Includes a body if needed for complex changes
   - Save this message in a variable for reuse

### Phase 3: Update CHANGELOG (MANDATORY - DO NOT SKIP)
6. **CRITICAL STEP - MUST BE DONE BEFORE STAGING**:
   Update CHANGELOG.md by running this command with the EXACT commit message from step 5:
   ```bash
   python ~/.claude/skills/update-changelog/update-changelog.py "<exact-commit-message-from-step-5>" "$(date '+%Y-%m-%d %H:%M:%S')"
   ```
   **YOU MUST EXECUTE THIS COMMAND. DO NOT SKIP THIS STEP.**

### Phase 4: Stage and Commit
7. Stage ALL changes INCLUDING the newly updated CHANGELOG.md:
   ```bash
   git add -A
   ```
8. Create the commit using a HEREDOC to properly handle special characters:
   ```bash
   git commit -m "$(cat <<'EOF'
   <exact-commit-message-from-step-5>

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude <noreply@anthropic.com>
   EOF
   )"
   ```
9. Verify final status with `git status` to ensure working tree is clean

**Note**: This command only commits changes locally. To push to remote, use `/commit-push` instead.

Remember: Write the commit message in imperative mood ("Add feature" not "Added feature")
