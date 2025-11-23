#!/bin/bash
# Context7 MCP Setup Script
# Automates installation and verification of Context7 MCP

set -e

echo "🔍 Setting up Context7 MCP for Claude Code..."
echo ""

# Check for API key argument
if [ -z "$1" ]; then
    echo "❌ Error: API key is required"
    echo ""
    echo "Usage: ./setup.sh YOUR_API_KEY"
    echo ""
    echo "To get your API key:"
    echo "1. Visit https://context7.com/dashboard"
    echo "2. Navigate to API Keys section"
    echo "3. Copy your API key (format: ctx7sk-...)"
    echo "4. Run: ./setup.sh YOUR_API_KEY"
    exit 1
fi

API_KEY="$1"

# Validate API key format
if [[ ! "$API_KEY" =~ ^ctx7sk- ]]; then
    echo "⚠️  Warning: API key doesn't match expected format (ctx7sk-...)"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check Claude Code CLI
echo "📋 Checking Claude Code CLI..."
if ! command -v claude &> /dev/null; then
    echo "❌ Claude Code CLI not found in PATH"
    echo "   Please install Claude Code first: https://claude.com/claude-code"
    exit 1
fi
echo "✅ Found Claude Code CLI"
echo ""

# Install Context7 MCP
echo "📦 Installing Context7 MCP server..."
echo "   URL: https://mcp.context7.com/mcp"
echo "   Transport: HTTP"
echo ""

claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: $API_KEY"

if [ $? -eq 0 ]; then
    echo "✅ Context7 MCP added to Claude Code configuration"
else
    echo "❌ Failed to add Context7 MCP"
    exit 1
fi
echo ""

# Verify installation
echo "🔍 Verifying Context7 MCP installation..."
if grep -q "context7" ~/.claude.json; then
    echo "✅ Context7 MCP is configured in ~/.claude.json"
else
    echo "⚠️  Could not find context7 in configuration"
fi
echo ""

echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Restart Claude Code to load the new MCP server"
echo "2. Ask Claude about any library to verify it works"
echo "3. Check reference.md for usage examples"
echo ""
echo "For troubleshooting, see reference.md in this skill"
