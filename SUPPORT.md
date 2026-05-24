# Support

This repository hosts the **public manifests, docs, and client examples** for
the hosted Gapup MCP server (`https://mcp.gapup.io/mcp`). The server
implementation itself is proprietary and not in this repo.

## Quick checks before reporting

1. **Endpoint health** — `https://mcp.gapup.io/health` (uptime, tool count, latency).
2. **Status page** — https://status.gapup.io (incidents, scheduled maintenance).
3. **Tool list** — `curl https://mcp.gapup.io/mcp` with a JSON-RPC `tools/list` request.
4. **Onboarding** — free tier (100 calls/month, no card) at https://hub.gapup.io/agents-api/onboard.

## Where to ask what

| Topic | Best channel |
|-------|--------------|
| Bug or unexpected behavior in a tool | [Open an issue](https://github.com/getgapup/gapup-mcp-public/issues) — pick the **Bug report** template |
| Tool gives wrong / stale data | [Open an issue](https://github.com/getgapup/gapup-mcp-public/issues) with the tool name, input, and a sample of the output |
| Feature request / new expertise | [Open an issue](https://github.com/getgapup/gapup-mcp-public/issues) with the **Feature request** template |
| Pricing, x402 settlement, USDC/EURC | `agents@gapup.io` |
| Billing, invoicing, refunds | `agents@gapup.io` |
| Security vulnerability | `agents@gapup.io` — see [SECURITY.md](SECURITY.md) |
| Press, partnership, design partner | `agents@gapup.io` |
| Documentation question | [docs/](docs/) — start with `docs/API.md` and `docs/CLIENTS.md` |

## Response times (target)

- **Hosted endpoint outage**: acknowledged < 1h, status page updated.
- **Security report**: acknowledged < 24h.
- **Bug report (non-blocking)**: triaged < 3 business days.
- **Feature request**: triaged on a weekly cadence.

These are targets, not guarantees — there is no paid SLA outside of the
Enterprise tier described in [docs/PRICING.md](docs/PRICING.md).

## What we cannot help with

- Self-hosting the server (the implementation is not open source).
- Building a custom fork of an expertise tool — file a feature request
  instead and we will fold it into the hosted version.
- Wallet recovery (we never hold your keys; x402 payments go directly to
  the address you control).
