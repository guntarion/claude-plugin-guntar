#!/bin/bash

# Read JSON input
input=$(cat)

# Extract current directory from JSON
cwd=$(echo "$input" | jq -r '.workspace.current_dir')
cd "$cwd" 2>/dev/null || cd ~

# Function to get git info
get_git_info() {
    if git rev-parse --git-dir > /dev/null 2>&1; then
        # Get branch name
        branch=$(git symbolic-ref --short HEAD 2>/dev/null || git rev-parse --short HEAD 2>/dev/null)

        # Get git status counts (skip optional locks for speed)
        untracked=$(git status --porcelain 2>/dev/null | grep -c '^??')
        modified=$(git status --porcelain 2>/dev/null | grep -c '^ M')
        staged=$(git status --porcelain 2>/dev/null | grep -c '^[MARC]')
        deleted=$(git status --porcelain 2>/dev/null | grep -c '^ D')

        # Build status string
        status_parts=()
        [ "$staged" -gt 0 ] && status_parts+="+${staged}"
        [ "$modified" -gt 0 ] && status_parts+="!${modified}"
        [ "$untracked" -gt 0 ] && status_parts+="?${untracked}"
        [ "$deleted" -gt 0 ] && status_parts+="x${deleted}"

        # Join status parts
        status_str=""
        if [ ${#status_parts[@]} -gt 0 ]; then
            status_str=" [$(IFS=' '; echo "${status_parts[*]}")]"
        fi

        printf " on \033[35m🌱 %s\033[0m\033[33m%s\033[0m" "$branch" "$status_str"
    fi
}

# Function to get python info
get_python_info() {
    if [ -n "$VIRTUAL_ENV" ]; then
        venv_name=$(basename "$VIRTUAL_ENV")
        printf " via \033[32m🐍 %s\033[0m" "$venv_name"
    elif [ -n "$CONDA_DEFAULT_ENV" ] && [ "$CONDA_DEFAULT_ENV" != "base" ]; then
        printf " via \033[32m🐍 %s\033[0m" "$CONDA_DEFAULT_ENV"
    fi
}

# Function to get node info
get_node_info() {
    if [ -f "package.json" ] && command -v node >/dev/null 2>&1; then
        node_version=$(node --version 2>/dev/null | sed 's/v//')
        printf " via \033[32m⬢ %s\033[0m" "$node_version"
    fi
}

# Build the status line
printf "\033[36m%s\033[0m" "$(basename "$cwd")"
get_git_info
get_python_info
get_node_info
