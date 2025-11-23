# Playwright MCP Quick Start

Get Playwright MCP running in 2 minutes.

## One-Liner Installation
```bash
claude mcp add playwright npx @playwright/mcp@latest && npx playwright install
```

## Verify It Works
```bash
npx @playwright/mcp@latest --help
cat ~/.claude.json | grep playwright
```

## Use Cases
- **Web scraping:** Extract data from websites
- **E2E testing:** Automate browser testing
- **Screenshot generation:** Capture pages programmatically
- **Form filling:** Automate data entry
- **API testing:** Interact with JavaScript-heavy apps

## Common Commands
```bash
# Check MCP status
npx @playwright/mcp@latest --help

# Reinstall browsers (if missing)
npx playwright install

# View configuration
cat ~/.claude.json
```

## Troubleshooting
- **"Browser not found"** → Run `npx playwright install`
- **"npx not found"** → Install Node.js and npm
- **"MCP server not responding"** → Restart Claude Code

See [reference.md](./reference.md) for detailed troubleshooting.
