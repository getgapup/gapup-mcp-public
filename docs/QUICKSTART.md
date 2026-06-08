# Gapup MCP — Quickstart

> 5 minutes from zero to your first agent-payable tool call. No card needed.

```
┌─ Step 1 ──────────  Get a free API key (60s)
├─ Step 2 ──────────  Wire it into your MCP client (90s)
├─ Step 3 ──────────  Call your first tool (60s)
└─ Step 4 ──────────  (Optional) Verify x402 micro-payment path (90s)
```

## Step 1 — Free API key

Visit **https://hub.gapup.io/agents-api/onboard** and click "Get a key".

- No credit card.
- 100 calls per month, free.
- Key format: `gp_live_...` (40 chars).

Save it where your agent can read it:

```bash
export GAPUP_API_KEY="gp_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## Step 2 — Wire it into your client

Pick the matching block.

### Claude Code / Claude Desktop

`~/.config/claude/claude_desktop_config.json` (Mac/Linux) or
`%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "gapup": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://mcp.gapup.io/mcp"],
      "env": { "GAPUP_API_KEY": "gp_live_..." }
    }
  }
}
```

> Or one-click from Smithery — https://smithery.ai/servers/gapup-team/gapup-mcp

### Cursor

`.cursor-plugin/plugin.json` of this repo is the canonical manifest. Cursor users:

1. Open Cursor → Settings → Plugins → Install from URL
2. Paste `https://github.com/getgapup/gapup-mcp-public`
3. Set `GAPUP_API_KEY` env when prompted

### Windsurf / VS Code / Cherry Studio

All MCP-compliant clients support the Streamable HTTP transport. Point them
at `https://mcp.gapup.io/mcp` with the `Authorization: Bearer <key>` header.

### Raw curl (no SDK)

```bash
curl -sS -X POST https://mcp.gapup.io/mcp \
  -H "Authorization: Bearer $GAPUP_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' \
  | grep -E '^data:' | sed 's/^data: //' \
  | jq '.result.tools | length'
# → 271
```

## Step 3 — Your first tool call

Pick the lightest tool to confirm the chain works end-to-end (NAICS classifier,
$0.05, ~210ms):

```bash
curl -sS -X POST https://mcp.gapup.io/mcp \
  -H "Authorization: Bearer $GAPUP_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0", "id": 1,
    "method": "tools/call",
    "params": {
      "name": "industry_classifier_naics_sic",
      "arguments": {
        "audience": "agent",
        "company_name": "Helios Cold Chain",
        "company_description": "Maritime reefer freight forwarder, intra-EU, 120 FTE.",
        "primary_revenue_source": "Freight forwarding fees"
      }
    }
  }' \
  | grep -E '^data:' | sed 's/^data: //' \
  | jq '.result.structuredContent | {summary, naics_6digit: .classifications.naics_6digit.code}'
```

Expected output (~210 ms):

```json
{
  "summary": "Helios Cold Chain operates in freight forwarding arrangement, transportation services sector (NAICS 488510).",
  "naics_6digit": "488510"
}
```

Your free-tier counter is now at 99/100 for the month.

## Step 4 — (Optional) x402 micro-payment path

When you exhaust the 100 free calls, the next call returns a `402 Payment Required`
with the price and the receiving address. Pay with USDC or EURC on Base or Optimism,
then re-call with an `X-Payment-Proof` header containing the tx hash.

If you use the official x402 SDK or Coinbase CDP wallets, this is handled
transparently. See [docs/EXAMPLES.md](EXAMPLES.md#async-pattern-heavy-tools) for the
full pattern.

## Common gotchas

- **400 — missing `audience`**: every expertise tool requires `audience` to be
  either `"human"` or `"agent"`. Default to `"agent"` for programmatic flows.
- **429 — rate-limit**: per-key burst is 10 RPS. Inspect `X-RateLimit-Reset` for the
  reset time.
- **5xx — upstream source degraded**: the response will include `degraded: true` and
  list the affected source. We never silently substitute data.

## Next reads

- [`docs/EXAMPLES.md`](EXAMPLES.md) — 10 flagship tools in curl/TS/Python
- [`docs/CONNECTORS.md`](CONNECTORS.md) — 60+ data sources that power the tools
- [`docs/PRICING.md`](PRICING.md) — full per-tool price grid (T0 → T5)
- [`docs/ARCHITECTURE.md`](ARCHITECTURE.md) — server architecture overview
- [`docs/API.md`](API.md) — JSON-RPC schema, error codes, paging
