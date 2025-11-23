# Playwright MCP Setup - Complete Reference

## Table of Contents
1. [Overview](#overview)
2. [Installation Methods](#installation-methods)
3. [Verification & Configuration](#verification--configuration)
4. [Browser Setup](#browser-setup)
5. [Troubleshooting](#troubleshooting)
6. [Available Endpoints](#available-endpoints)

## Overview

Playwright MCP is a Model Context Protocol server that enables Claude to interact with web pages through browser automation. It provides:
- Cross-browser support (Chromium, Firefox, WebKit)
- Accessibility snapshots for element identification
- Programmatic page interaction
- Network inspection and debugging

**Source:** [Microsoft Playwright MCP GitHub](https://github.com/microsoft/playwright-mcp)

## Installation Methods

### Method 1: Claude Code CLI (Recommended)
```bash
claude mcp add playwright npx @playwright/mcp@latest
```
This is the fastest way to get started. It automatically adds the server to your Claude Code configuration.

### Method 2: Manual Configuration
Edit `~/.claude.json` and add:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

### Method 3: With Custom Configuration
If you need custom browser settings:
```bash
npx @playwright/mcp@latest --config path/to/playwright.config.json
```

## Verification & Configuration

### Check Installation Status
```bash
npx @playwright/mcp@latest --help
```

### View Claude Code MCP Configuration
```bash
cat ~/.claude.json
```

### Test Server Connectivity
The MCP server will be automatically tested when you use it in Claude Code. Look for successful responses from endpoints like `/browser_snapshot`.

## Browser Setup

### Install Browser Binaries
Playwright requires browser binaries for automation. Install them with:
```bash
npx playwright install
```

Install specific browsers:
```bash
npx playwright install chromium firefox webkit
```

### Install System Dependencies (Linux/macOS)
```bash
npx playwright install-deps
```

### Browser Installation via MCP
Once configured, you can trigger browser installation directly through the MCP:
- Endpoint: `POST /browser_install`
- This is useful if browsers aren't already installed

## Troubleshooting

### Browser Not Found
**Error:** "Browser not found"
**Solution:**
```bash
npx playwright install
```

### Missing System Dependencies (Linux)
**Error:** "GLIBC version or dependencies missing"
**Solution:**
```bash
npx playwright install-deps
```

### MCP Server Not Starting
**Error:** "Failed to start MCP server"
**Possible Causes:**
1. Node.js not installed or outdated (need v16+)
2. npx not available in PATH
3. Network issues preventing npm package download

**Solutions:**
```bash
# Verify Node.js version
node --version  # Should be v16 or higher

# Clear npm cache
npm cache clean --force

# Try installation again
claude mcp add playwright npx @playwright/mcp@latest
```

### Outdated MCP Version
**Solution:** Force update
```bash
npm install -g @playwright/mcp@latest
claude mcp add playwright npx @playwright/mcp@latest
```

## Available Endpoints

Once installed, Playwright MCP provides these endpoints for use in Claude Code:

### GET /browser_snapshot
Captures an accessibility snapshot of the current page.
```json
{
  "snapshot": {
    "name": "document",
    "role": "WebArea",
    "children": [...]
  }
}
```

### POST /browser_install
Initiates browser binary installation.
```json
{
  "status": "success",
  "message": "Browser installation initiated/completed."
}
```

### Additional Endpoints
For complete API documentation, see the [official Playwright MCP repository](https://github.com/microsoft/playwright-mcp).

## Next Steps

1. **Verify Installation:** Run `npx @playwright/mcp@latest --help`
2. **Install Browsers:** Run `npx playwright install`
3. **Use in Claude Code:** Ask Claude to automate web tasks
4. **Reference Documentation:** Visit [Playwright MCP GitHub](https://github.com/microsoft/playwright-mcp)

## Resources

- [Playwright MCP GitHub Repository](https://github.com/microsoft/playwright-mcp)
- [Playwright Documentation](https://playwright.dev)
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Claude Code Documentation](/help)
