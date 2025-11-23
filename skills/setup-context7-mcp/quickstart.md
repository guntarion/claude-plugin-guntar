# Context7 MCP Quick Start

Get Context7 MCP running in 2 minutes.

## Prerequisites
- Claude Code CLI installed
- Context7 API key (get from https://context7.com/dashboard)

## One-Liner Installation
Replace `YOUR_API_KEY` with your actual Context7 API key:
```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_API_KEY"
```

## Verify It Works
```bash
cat ~/.claude.json | grep context7
```

You should see:
```json
{
  "mcpServers": {
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

## Test It
Ask Claude Code:
```
Can you help me with React documentation using Context7?
```

## Use Cases
- **Library documentation:** Get latest docs for any library
- **Code examples:** Find best practice code snippets
- **Version information:** Discover compatible versions
- **Integration patterns:** Learn how libraries work together
- **Framework guides:** Get comprehensive framework documentation

## Common Commands
```bash
# View configuration
cat ~/.claude.json

# Update API key (if needed)
# Edit ~/.claude.json manually and update CONTEXT7_API_KEY

# Remove and reinstall (if having issues)
# Edit ~/.claude.json and remove context7 section, then re-add
```

## Troubleshooting
- **"Unauthorized" error** → Check API key is correct in ~/.claude.json
- **"Connection refused"** → Check internet connection and firewall
- **No response from Claude** → Restart Claude Code after setup

See [reference.md](./reference.md) for detailed troubleshooting.
