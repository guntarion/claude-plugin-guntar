#!/bin/bash

# Read JSON input from stdin
input=$(cat)

# Extract basic information
model=$(echo "$input" | jq -r '.model.display_name // .model.id')
cwd=$(echo "$input" | jq -r '.workspace.current_dir')
exit_code=$(echo "$input" | jq -r '.exit_code // null')

# Current directory (replace home with ~)
current_dir="${cwd/#$HOME/~}"

# Colors
BLUE='\033[34m'
YELLOW='\033[33m'
RED='\033[31m'
GREEN='\033[32m'
CYAN='\033[36m'
RESET='\033[0m'
BOLD='\033[1m'

# Virtual environment indicator
venv_info=""
if [[ -n "$VIRTUAL_ENV" ]]; then
    venv_name=$(basename "$VIRTUAL_ENV")
    venv_info="${RED}(${venv_name})${RESET} "
fi

# Current directory (bold blue)
dir_info="${BOLD}${BLUE}${current_dir}${RESET}"

# Git branch and modified files (yellow with brackets)
git_info=""
if git -C "$cwd" rev-parse --git-dir > /dev/null 2>&1; then
    branch=$(git -C "$cwd" -c core.filemode=false branch --show-current 2>/dev/null)
    if [[ -n "$branch" ]]; then
        # Count unstaged changes
        git_status=$(git -C "$cwd" -c core.filemode=false status --porcelain 2>/dev/null | wc -l | tr -d ' ')
        if [[ "$git_status" -gt 0 ]]; then
            git_info=" ${YELLOW}‹${branch}*${RED}${git_status}${YELLOW}›${RESET}"
        else
            git_info=" ${YELLOW}‹${branch}›${RESET}"
        fi
    fi
fi

# Exit status indicator
exit_status=""
if [[ "$exit_code" != "null" && "$exit_code" != "" ]]; then
    if [[ "$exit_code" == "0" ]]; then
        exit_status=" ${GREEN}✓${RESET}"
    else
        exit_status=" ${RED}✗${RESET}"
    fi
fi

# Time indicator (current time in HH:MM format)
time_info=" ${CYAN}$(date +%H:%M)${RESET}"

# Model indicator (using model name directly)
model_display="${model}"

# Output the statusline
# Format: [venv] model dir [git_branch] [exit_status] time
printf "${venv_info}${model_display} ${dir_info}${git_info}${exit_status}${time_info}"
