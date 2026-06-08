---
title: Gapup MCP — 271+ Agent-Payable C-Suite Tools
emoji: 🏛️
colorFrom: yellow
colorTo: indigo
sdk: gradio
sdk_version: 5.7.1
app_file: app.py
pinned: false
license: mit
short_description: 271+ agent-payable C-suite tools — x402 USDC pay-per-call
tags:
  - mcp
  - agent-payable
  - x402
  - business-intelligence
  - compliance
  - sec-filings
  - sanctions
  - kyc
  - eu-ai-act
---

# Gapup MCP — 271+ agent-payable C-suite expertise tools

This HF Space is a live browser for the hosted MCP server at
**[mcp.gapup.io/mcp](https://mcp.gapup.io/mcp)**.

- Fetches the live tool list from the production endpoint
- Lets you preview tool descriptions, prices (x402), and example inputs
- Shows the install snippet for Claude / Cursor / Windsurf / VS Code

## Want to use Gapup MCP in your agent ?

1. Get a free key (100 calls/month, no card) → https://hub.gapup.io/agents-api/onboard
2. Add to your MCP client config :
   ```json
   {
     "mcpServers": {
       "gapup": {
         "command": "npx",
         "args": ["-y", "mcp-remote", "https://mcp.gapup.io/mcp",
                  "--header", "Authorization: Bearer ${GAPUP_API_KEY}"]
       }
     }
   }
   ```
3. Call any tool from your agent.

## Docs

- Examples (curl / TS / Python) — https://github.com/getgapup/gapup-mcp-public/blob/main/docs/EXAMPLES.md
- Quickstart 5 min — https://github.com/getgapup/gapup-mcp-public/blob/main/docs/QUICKSTART.md
- Pricing T0 → T5 — https://github.com/getgapup/gapup-mcp-public/blob/main/docs/PRICING.md
- 60+ data sources — https://github.com/getgapup/gapup-mcp-public/blob/main/docs/CONNECTORS.md

## Contact

`agents@gapup.io` · [hub.gapup.io/agents-api](https://hub.gapup.io/agents-api)
