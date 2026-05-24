# Gapup MCP — Client integrations

The Gapup MCP server is reachable via standard MCP Streamable HTTP at `https://mcp.gapup.io/mcp` and is compatible with any MCP-compliant client.

## Tested clients (via Smithery)

Smithery provides a one-click install for 30+ clients:

- Claude Code
- Claude Desktop
- Cursor
- Windsurf
- VS Code
- VS Code Insiders
- Cherry Studio
- LM Studio
- Gemini CLI
- Roo Code
- ChatWise
- Amazon Q
- Dust
- LibreChat
- Zed
- Cline
- Kiro
- ChatGPT (via MCP plugin)
- Goose
- Poke
- Trae
- Raycast
- Witsy
- BoltAI
- Augment
- Highlight
- Qordinate
- OpenClaw
- AgentOne
- Codex
- OpenCode
- Antigravity

See the live install commands at https://smithery.ai/servers/gapup-team/gapup-mcp.

## Manual config (no Smithery)

### Claude Desktop / Claude Code

`~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) or
`%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "gapup": {
      "type": "http",
      "url": "https://mcp.gapup.io/mcp",
      "headers": {
        "x-api-key": "gpk_your_free_key"
      }
    }
  }
}
```

### Cursor

`.cursor/mcp.json` in your workspace:

```json
{
  "mcpServers": {
    "gapup": {
      "type": "http",
      "url": "https://mcp.gapup.io/mcp",
      "headers": {
        "x-api-key": "gpk_your_free_key"
      }
    }
  }
}
```

### Windsurf

`~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "gapup": {
      "url": "https://mcp.gapup.io/mcp",
      "headers": {
        "x-api-key": "gpk_your_free_key"
      }
    }
  }
}
```

### Custom Node.js client (MCP SDK)

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const transport = new StreamableHTTPClientTransport(
  new URL("https://mcp.gapup.io/mcp"),
  {
    requestInit: {
      headers: { "x-api-key": process.env.GAPUP_API_KEY! },
    },
  },
);

const client = new Client({ name: "my-agent", version: "1.0.0" }, { capabilities: {} });
await client.connect(transport);

const tools = await client.listTools();
console.log(`${tools.tools.length} tools available`);

const result = await client.callTool({
  name: "industry_classifier_naics_sic",
  arguments: {
    company_description: "Maritime freight forwarder, reefer containers, intra-EU",
    company_name: "Helios Cold Chain",
  },
});
console.log(JSON.parse(result.content[0].text));
```

## Direct HTTP (no SDK)

```bash
# tools/list
curl -X POST https://mcp.gapup.io/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "x-api-key: gpk_your_free_key" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'

# tools/call
curl -X POST https://mcp.gapup.io/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "x-api-key: gpk_your_free_key" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 2,
    "params": {
      "name": "sec_filing_decoder",
      "arguments": {
        "ticker": "SHOP",
        "filing_types": ["10-K"],
        "lookback_months": 18
      }
    }
  }'
```

Note: the `Accept: application/json, text/event-stream` header is required (Streamable HTTP MCP protocol).

## Free tier key

Get yours at: https://hub.gapup.io/agents-api/onboard
- 100 calls/month
- No credit card
- Instant issuance

## Support

Integration issues: open a [GitHub Issue](https://github.com/getgapup/gapup-mcp-public/issues) or email agents@gapup.io.
