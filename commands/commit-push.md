---
description: Create a meaningful git commit and push to remote
allowed-tools: [bash]
---

# Git Commit and Push with Meaningful Message

Create a conventional commit message for all current changes and push to remote.

## Steps

### Phase 1: Review Changes
1. Run `git status` to see all changes
2. Run `git diff --stat` to review the changes summary
3. Run `git branch --show-current` to confirm the current branch
4. Run `git remote` to get the remote name (use the first remote found)

### Phase 2: Create Commit Message
5. Analyze the changes and determine:
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
6. Create a clear, descriptive commit message that:
   - Starts with the conventional commit type
   - Summarizes the changes in 50-72 characters
   - Includes a body if needed for complex changes
   - Save this message in a variable for reuse

### Phase 3: Update CHANGELOG (MANDATORY - DO NOT SKIP)
7. **CRITICAL STEP - MUST BE DONE BEFORE STAGING**:
   Update CHANGELOG.md by running this command with the EXACT commit message from step 6:
   ```bash
   python ~/.claude/skills/update-changelog/update-changelog.py "<exact-commit-message-from-step-6>" "$(date '+%Y-%m-%d %H:%M:%S')"
   ```
   **YOU MUST EXECUTE THIS COMMAND. DO NOT SKIP THIS STEP.**

### Phase 4: Stage, Commit, and Push
8. Stage ALL changes INCLUDING the newly updated CHANGELOG.md:
   ```bash
   git add -A
   ```
9. Create the commit using a HEREDOC to properly handle special characters:
   ```bash
   git commit -m "$(cat <<'EOF'
   <exact-commit-message-from-step-6>

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude <noreply@anthropic.com>
   EOF
   )"
   ```
10. Push to remote with `git push <remote-name> HEAD` where <remote-name> is from step 4
11. Verify final status with `git status` to ensure working tree is clean

**Important**: Do NOT hardcode "origin" as the remote name. Always use `git remote` to dynamically detect the actual remote name for this repository.

Remember: Write the commit message in imperative mood ("Add feature" not "Added feature")
