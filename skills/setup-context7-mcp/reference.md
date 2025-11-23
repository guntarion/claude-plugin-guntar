# Context7 MCP Setup - Complete Reference

## Table of Contents
1. [Overview](#overview)
2. [Installation Methods](#installation-methods)
3. [Authentication](#authentication)
4. [Verification & Configuration](#verification--configuration)
5. [Available Features](#available-features)
6. [Troubleshooting](#troubleshooting)
7. [API Endpoints](#api-endpoints)

## Overview

Context7 MCP is a Model Context Protocol server that provides access to comprehensive, up-to-date documentation and code examples for thousands of libraries and frameworks. It enables:
- Real-time library documentation retrieval
- Code snippet examples and patterns
- Library version compatibility information
- Framework-specific best practices
- Cross-library knowledge integration

**Source:** [Context7 MCP Server](https://mcp.context7.com)

## Installation Methods

### Method 1: Claude Code CLI with HTTP Transport (Recommended)
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_API_KEY"
```
Replace `YOUR_API_KEY` with your actual Context7 API key.

### Method 2: Manual Configuration
Edit `~/.claude.json` and add:
```json
{
  "mcpServers": {
    "context7": {
      "transport": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

### Method 3: Using Environment Variables
Store your API key in `~/.bashrc` or `~/.zshrc`:
```bash
export CONTEXT7_API_KEY="your-api-key-here"
```
Then use in configuration:
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: $CONTEXT7_API_KEY"
```

## Authentication

### Getting Your API Key
1. Visit [Context7 Dashboard](https://context7.com)
2. Navigate to API Keys section
3. Generate a new API key or use existing one
4. Store securely (never commit to version control)

### API Key Format
Context7 API keys typically follow the format: `ctx7sk-` followed by a UUID
Example: `ctx7sk-0701e9f0-2123-4911-a09e-16c751f1044a`

### Secure Key Storage
**⚠️ IMPORTANT:** Never commit API keys to version control.

**Best practices:**
1. Store in `~/.claude.json` (local only)
2. Use environment variables for CI/CD
3. Rotate keys regularly
4. Use separate keys for development vs. production

## Verification & Configuration

### Check Installation Status
```bash
cat ~/.claude.json | grep context7
```

### Test Server Connectivity
```bash
# The MCP server will be tested automatically when you use Context7 functions
# Look for successful responses from library documentation queries
```

### Verify API Key
```bash
# Your API key is validated on first use
# Check Claude Code output for authentication errors
```

## Available Features

### Resolve Library ID
Converts human-readable library names to Context7-compatible library IDs.
```
Input: "playwright"
Output: "/microsoft/playwright" or version-specific like "/microsoft/playwright/v1.51.0"
```

### Get Library Documentation
Retrieves comprehensive documentation for any library, including:
- API references
- Code examples
- Installation instructions
- Best practices
- Version-specific information

### Code Snippets
Access real-world code examples for:
- Common usage patterns
- Integration examples
- Configuration templates
- Testing approaches

### Library Search
Find libraries by:
- Name matching
- Description relevance
- Feature keywords
- Popularity and benchmarks

## Troubleshooting

### Authentication Failed
**Error:** "Invalid API key" or "Unauthorized"
**Solution:**
1. Verify API key is correct: `cat ~/.claude.json | grep CONTEXT7_API_KEY`
2. Ensure key hasn't expired in Context7 dashboard
3. Check for leading/trailing whitespace in key
4. Try re-adding the MCP server with correct key

### Connection Refused
**Error:** "Cannot connect to https://mcp.context7.com/mcp"
**Possible Causes:**
1. Network connectivity issues
2. Context7 service temporarily down
3. Firewall/proxy blocking HTTPS

**Solutions:**
```bash
# Test network connectivity
curl -I https://mcp.context7.com/mcp

# Check DNS resolution
nslookup mcp.context7.com

# Verify firewall allows HTTPS
netstat -an | grep 443
```

### Header Format Issues
**Error:** "Invalid header format"
**Common Mistakes:**
- Missing quotes around header value
- Incorrect header name (should be `CONTEXT7_API_KEY`)
- Missing colon between key and value

**Correct Format:**
```bash
--header "CONTEXT7_API_KEY: ctx7sk-..."
```

### MCP Server Not Responding
**Error:** "MCP server not responding"
**Solutions:**
1. Verify installation: `cat ~/.claude.json`
2. Check API key validity
3. Restart Claude Code
4. Check Context7 service status page

### SSL Certificate Issues
**Error:** "SSL certificate verification failed"
**Solutions:**
```bash
# Update CA certificates
# macOS:
/Applications/Python\ 3.x/Install\ Certificates.command

# Linux:
sudo apt-get install ca-certificates

# Windows:
# Run Python installer with "Install certificates" option
```

## API Endpoints

Context7 MCP provides the following endpoints through the standard MCP protocol:

### resolve-library-id
Resolves human-readable library names to Context7-compatible IDs.
- **Input:** Library name (string)
- **Output:** Library ID, metadata, and available versions

### get-library-docs
Retrieves comprehensive documentation for a library.
- **Input:** Library ID, optional topic filter, pagination
- **Output:** Documentation content, code examples, references

### search-libraries
Searches available libraries by keyword.
- **Input:** Search query, filters
- **Output:** Matching libraries with ratings and snippet counts

## Configuration Examples

### Basic Setup
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: ctx7sk-your-key"
```

### Multiple MCP Servers
If you have other MCP servers configured:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "context7": {
      "transport": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "ctx7sk-..."
      }
    }
  }
}
```

## Usage in Claude Code

Once installed, you can use Context7 to:

1. **Look up library documentation:**
   ```
   "Can you help me use the React hooks API with Context7?"
   ```

2. **Get code examples:**
   ```
   "Show me examples of using Next.js with Context7"
   ```

3. **Find libraries:**
   ```
   "What testing libraries does Context7 recommend?"
   ```

## Next Steps

1. **Get API Key:** Visit [Context7 Dashboard](https://context7.com)
2. **Run Setup:** Use the installation command with your API key
3. **Verify:** Check `~/.claude.json` contains context7 entry
4. **Test:** Ask Claude about any library to verify it works
5. **Reference:** See [Context7 Documentation](https://context7.com/docs)

## Resources

- [Context7 Website](https://context7.com)
- [Context7 Dashboard](https://context7.com/dashboard)
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Claude Code Documentation](/help)
