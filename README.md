# Gapup MCP

[![smithery badge](https://smithery.ai/badge/mehdi-sakalypr/gapup-mcp)](https://smithery.ai/servers/mehdi-sakalypr/gapup-mcp)
[![Tools](https://img.shields.io/badge/tools-183-c9a84c)](https://mcp.gapup.io/health)
[![x402](https://img.shields.io/badge/x402-USDC%2FEURC-c9a84c)](https://x402.org)
[![Free tier](https://img.shields.io/badge/free%20tier-100%20calls%2Fmo-10b981)](https://hub.gapup.io/agents-api/onboard)
[![License](https://img.shields.io/badge/license-Proprietary-grey)](LICENSE)

**Agent-payable C-suite knowledge — 183 tools, x402 micro-payments, board-ready JSON.**

Live endpoint: `https://mcp.gapup.io/mcp`
Free tier: 100 calls/month, no credit card → [hub.gapup.io/agents-api/onboard](https://hub.gapup.io/agents-api/onboard)

---

## What is Gapup MCP?

A hosted [Model Context Protocol](https://modelcontextprotocol.io) server exposing **100+ business expertise tools** for AI agents. Each tool returns a structured, audited, board-ready JSON deliverable in 1-30 seconds.

Pay-per-call via [x402](https://x402.org) (USDC + EURC on Base + Optimism). No subscription, no API gateway. The price is encoded in the response — agents pay what they consume.

## Why agents use it

- **Board-ready output** — Zod-typed JSON, persona-stricte, no chat fluff
- **Dual-audience format** — `audience` param routes `human` (Mistral gold-standard, ~30s) vs `agent` (Cerebras qwen-3-235b, <5s)
- **Source-grounded** — citations, DOIs, evidence trails; no hallucinated facts
- **EU-first moats** — DVF Cerema + Géorisques for real estate, OFAC + EU + UK + UN + SECO + SEMA + DFAT for sanctions
- **Free tier real** — 100 calls/mo without credit card, no rate-limit games

## What's inside (183 tools)

### Top 10 C-suite expertises (most used)
- `competitive_intel` — EDGAR + Yahoo + Wayback + Wikipedia multi-source deep-dive
- `sec_filing_decoder` — 10-K / 10-Q / 8-K extraction + KPIs movement + red flags + M&A signals
- `sanctions_screener_multi` — 8 lists parallel (OFAC + EU + UK + UN + SECO + SEMA + DFAT) + PEP + adverse media
- `kyc_screener` — KYC/AML 6 sources refreshed weekly
- `pentest_scope_estimator` — PTES scope + effort/cost ranges
- `attack_surface_monitor` — passive recon (crt.sh + DNS + Shodan) + CVE/EPSS/KEV
- `clinical_evidence_briefer` — PubMed + ClinicalTrials.gov + OpenFDA, GRADE-graded
- `re_deal_screener` — EU-first real estate (DVF Cerema + Géorisques)
- `research_paper_qa` — OpenAlex 45M open-access + Semantic Scholar + CORE, DOI-cited
- `industry_classifier_naics_sic` — NAICS + SIC + NACE + GICS + ISIC + HS with hierarchy + confidence

### Categories (full list in [docs/API.md](docs/API.md))
Business Intelligence · Finance · Compliance · Strategy · Sales · Sustainability · Research · Real Estate · Healthcare · Security

## Quick start

### Option 1 — Direct HTTP (MCP Streamable HTTP)

```bash
# Free tier: get a key at https://hub.gapup.io/agents-api/onboard
export GAPUP_API_KEY=gpk_your_free_key

curl -X POST https://mcp.gapup.io/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "x-api-key: $GAPUP_API_KEY" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 1,
    "params": {
      "name": "industry_classifier_naics_sic",
      "arguments": {
        "company_description": "Maritime freight forwarder, reefer containers, intra-EU",
        "company_name": "Helios Cold Chain"
      }
    }
  }'
```

### Option 2 — Smithery CLI

```bash
npm install -g @smithery/cli
smithery auth login
smithery mcp add mehdi-sakalypr/gapup-mcp
```

### Option 3 — Claude Desktop / Cursor / Windsurf / etc.

Add to your MCP config (see [docs/CLIENTS.md](docs/CLIENTS.md) for all 30+ supported clients):

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

### Option 4 — TypeScript SDK example

See [client/example.ts](client/example.ts).

## Pricing

| Tier | $ USD | Examples |
|---|---|---|
| T0 | $0.002 | FX lookups, simple commodity prices |
| T1 | $0.05 | Industry classifier, pentest scope estimator |
| T2 | $0.10 | Domain tech fingerprint, market sizing |
| T3 | $0.15 | Attack surface, SEC filings, sanctions multi |
| T4 | $0.20 | Real estate deal screener, clinical evidence, KYC, AI Act audit |
| T5 | $0.30 | Competitive deep dive flagship |
| T6 | $1.50 | Async batch (bulk KYC, AI governance full report) |

**Free tier**: 100 calls/month total across all tiers. No credit card.

Full details: [docs/PRICING.md](docs/PRICING.md).

## Architecture (high-level)

```
agent ─→ mcp.gapup.io  ─→  Cluster PM2 (2 instances, Cerebras-backed for agent mode)
              │              │
              │              └─→ Fly.io edges (fra/sin/gru) for global low-latency
              │
              └─→ Cloudflare WAF + rate-limit + cache
```

Full architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Observability

- Sentry (errors + perf + breadcrumbs + x402 caller identification)
- Health endpoint with LLM providers status + circuit breakers
- Cloudflare access logs
- `/__metrics` endpoint (rate-limit-aware)

## Distribution

Listed on:
- **Smithery** — [smithery.ai/servers/mehdi-sakalypr/gapup-mcp](https://smithery.ai/servers/mehdi-sakalypr/gapup-mcp)
- More marketplaces being added (Glama, PulseMCP, mcp.so, mcp.directory, MCP Registry, Bazaar coming soon).

## License & usage

The hosted API at `mcp.gapup.io` is offered under the [Gapup Terms of Service](https://hub.gapup.io/terms).

The contents of THIS repository (manifests, docs, SDK examples) are licensed under [Proprietary](LICENSE) — usage of the API is governed by the ToS; redistribution / cloning / forking of this code is restricted.

The **server implementation** is private. This repository exists solely for transparency, discoverability and integration support.

## Support

- **Email**: agents@gapup.io
- **Issues**: [GitHub Issues](https://github.com/getgapup/gapup-mcp-public/issues)
- **Docs**: [hub.gapup.io/agents-api](https://hub.gapup.io/agents-api)

## Built with

Claude Code · TypeScript · MCP SDK · x402 protocol · Cerebras + Mistral + Anthropic

---

© 2026 Gapup. All rights reserved.
