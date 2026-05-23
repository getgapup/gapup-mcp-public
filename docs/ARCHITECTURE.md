# Gapup MCP — Architecture overview

> High-level architecture. Implementation details and source code are private.
> This document exists so integrators understand the contract.

## System diagram

```
                          ┌──────────────────────────┐
                          │  Cloudflare CDN + WAF    │
                          │  - 60 req/min per IP cap │
                          │  - Trusted crawler bypass│
                          │    (Bazaar, Smithery,    │
                          │     MCP Registry, ...)   │
                          │  - WAF inline (path      │
                          │    traversal, /_internal)│
                          │  - Email Routing         │
                          └────────────┬─────────────┘
                                       │
                                       ↓
                          ┌──────────────────────────┐
                          │       mcp.gapup.io       │
                          │   Streamable HTTP MCP    │
                          │  - tools/list (cached)   │
                          │  - tools/call (per-tool) │
                          │  - prompts, resources    │
                          │  - x402 payment headers  │
                          └────────────┬─────────────┘
                                       │
                                       ↓
                          ┌──────────────────────────┐
                          │  PM2 cluster — DO VPS    │
                          │  2 instances, fork mode  │
                          │  Node.js + TypeScript    │
                          │  + 4 fork apps (content, │
                          │    trade, expertise,     │
                          │    custom)               │
                          └──┬──────────────────┬────┘
                             │                  │
              ┌──────────────┘                  └──────────────────┐
              ↓                                                     ↓
   ┌──────────────────────┐                          ┌────────────────────────┐
   │  Fly.io edge replicas │                          │      Internal API     │
   │  fra / sin / gru     │                          │    hub.gapup.io       │
   │  (low-latency global)│                          │    (Next.js Vercel)   │
   └──────────────────────┘                          │  - 102 expertises     │
                                                     │  - Cerebras + Mistral │
                                                     │    + Anthropic        │
                                                     │  - x402 payment       │
                                                     │    facilitator        │
                                                     │  - Resend (outbound)  │
                                                     │  - Supabase           │
                                                     └────────────────────────┘
                                                                  │
                                                                  ↓
                                                     ┌────────────────────────┐
                                                     │   External data sources │
                                                     │  EDGAR, OFAC SDN, EU,  │
                                                     │  UK HMT, UN, SECO,     │
                                                     │  OpenAlex, PubMed,     │
                                                     │  ClinicalTrials.gov,   │
                                                     │  OpenFDA, DVF Cerema,  │
                                                     │  Géorisques, Shodan,   │
                                                     │  crt.sh, GDELT, ...    │
                                                     └────────────────────────┘
```

## Request flow

### Free tier call

```
agent → CF (rate-limit check)
      → mcp.gapup.io (auth: x-api-key)
      → PM2 cluster (route by tool name)
      → Internal API hub.gapup.io
      → LLM provider (Cerebras for agent mode, Mistral for human mode)
      → Structured JSON response
      → Back through PM2 → CF cache → agent
```

Typical latency: 1.5s (industry-classifier) to 30s (clinical-evidence-briefer in human mode).

### Paid x402 call (post-LLC + Coinbase Business activation)

```
agent → mcp.gapup.io/api/agent/<slug>
      → 402 Payment Required + x402 manifest
agent → x402 facilitator (Coinbase x402) → signs payment proof
agent → mcp.gapup.io/api/agent/<slug> + payment proof header
      → Server validates proof via facilitator
      → Tool executes, response returned
```

Currently in `mock-dev` mode (testnet base-sepolia). Production activation requires the Gapup LLC + Coinbase Business KYB.

## Components

### 1. MCP server (`mcp.gapup.io`)

- **Transport**: Streamable HTTP (Server-Sent Events for tool responses)
- **Protocol**: MCP v1
- **183 tools** indexed across 5 server segments (all, content, trade, expertise, custom)
- **Stateless** per-request; no session affinity required between calls

### 2. Hub API (`hub.gapup.io`)

- **Framework**: Next.js 16 on Vercel (Edge runtime where applicable)
- **102 expertises** implemented as serverless functions
- **Dual LLM routing**:
  - `audience: "agent"` → Cerebras qwen-3-235b (~2-5s P50)
  - `audience: "human"` → Mistral Large (~25-50s, board-ready quality)
  - Cascade fallback: Cerebras → Mistral → Groq → Anthropic (configurable per-tool)
- **x402 facilitator integration**: Coinbase x402 / mock-dev

### 3. Resilience

- **Circuit breaker** per upstream data source (last-good cache, graceful degradation)
- **Retry with backoff** on 5xx + network errors (3 attempts, exponential 300ms → 1.5s → 5s)
- **AbortSignal timeout** hard-cap 45s on all external fetches
- **Rate limiting** per-API-key + per-IP (60 req/min standard, 10 req/min for T4+ tools)
- **Trusted crawler bypass** for known MCP indexers (Bazaar, Smithery, MCP Registry, Anthropic, OpenAI)

### 4. Observability

- **Sentry**: errors + transactions + breadcrumbs + user context (x402 wallet / API key prefix, no PII)
- **Health endpoint** (`/health`): JSON with `ok`, `tools`, `llm_providers_status`, `cache_status`, `circuit_breaker_status`, `x402_enabled`
- **Metrics endpoint** (`/__metrics`): rate-limit-aware (auth required)
- **Sourcemaps uploaded** per release to Sentry for readable stack traces

### 5. Discovery / cache

- **Cloudflare cache** on GET endpoints (`/api/v1/tools`, `/docs`, `/api/v1/openapi.json`, `/.well-known/x402`) for crawlers
- **Daily refresh cron** for sanctions sources (OFAC SDN, EU Consolidated, UK HMT, UN Security Council, SECO, SEMA, DFAT)
- **Embeddings refresh** for content-similar / content-discovery (pgvector)

## What's NOT in this public repository

- Tool prompts (`lib/expertises/*/prompt.ts`)
- Tool schemas (Zod definitions for input/output)
- Generation logic (`lib/expertises/*/generate.ts`)
- Data fetchers (EDGAR, OFAC parser, PubMed, ...)
- LLM routing cascade
- Cron schedules
- x402 facilitator integration details
- Internal discovery agent (Hisoka v2)
- Telemetry implementation
- Catalogue building scripts

These are the moat. Integration consumers don't need them — the contract is the MCP tools/list output and the per-tool JSON schemas (exposed via tools/list).
