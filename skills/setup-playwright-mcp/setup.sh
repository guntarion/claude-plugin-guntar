#!/bin/bash
# Playwright MCP Setup Script
# Automates installation and verification of Playwright MCP

set -e

echo "🎭 Setting up Playwright MCP for Claude Code..."
echo ""

# Check Node.js
echo "📋 Checking Node.js installation..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js v16 or higher."
    exit 1
fi

NODE_VERSION=$(node -v)
echo "✅ Found Node.js: $NODE_VERSION"
echo ""

# Install Playwright MCP
echo "📦 Installing Playwright MCP server..."
if command -v claude &> /dev/null; then
    claude mcp add playwright npx @playwright/mcp@latest
    echo "✅ Playwright MCP added to Claude Code configuration"
else
    echo "⚠️  Claude Code CLI not found in PATH"
    echo "   You can manually add Playwright MCP to ~/.claude.json:"
    echo "   {\"mcpServers\": {\"playwright\": {\"command\": \"npx\", \"args\": [\"@playwright/mcp@latest\"]}}}"
fi
echo ""

# Install browsers
echo "📥 Installing Playwright browsers..."
npx playwright install
echo "✅ Playwright browsers installed"
echo ""

# Verify installation
echo "🔍 Verifying Playwright MCP installation..."
if npx @playwright/mcp@latest --help &> /dev/null; then
    echo "✅ Playwright MCP is ready to use"
else
    echo "⚠️  Could not verify Playwright MCP, but installation may still be valid"
fi
echo ""

echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Verify installation: npx @playwright/mcp@latest --help"
echo "2. Check configuration: cat ~/.claude.json"
echo "3. Use Playwright in Claude Code for browser automation"
echo ""
echo "For troubleshooting, see reference.md in this skill"
