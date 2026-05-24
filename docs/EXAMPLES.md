# Gapup MCP — Examples

> Copy-pasteable snippets for the 10 most-used tools, in **curl**,
> **TypeScript** (official MCP SDK), and **Python** (official MCP SDK).
> All inputs use fictional lambda companies — never plug client data in
> a public example.

The hosted endpoint is `https://mcp.gapup.io/mcp`. The first 100 calls
per month are free; afterwards each call settles via x402 (USDC / EURC
on Base or Optimism). The price is encoded in the response — you only
pay what you consume.

Get a free API key (no card required):
**https://hub.gapup.io/agents-api/onboard**

---

## Conventions used below

- `<GAPUP_API_KEY>` — your free-tier key (header `Authorization: Bearer …`)
- `tools/call` is the MCP method; arguments live under `params.arguments`
- The response is Server-Sent Events (SSE); parse with `Accept: application/json, text/event-stream`
- Every example sets `audience: "agent"` — the fast pipeline (Cerebras qwen-3-235b, <5s, JSON-only). Pass `audience: "human"` for the gold-standard Mistral pipeline (~30s, presenter-script included)

---

## Setup — install the SDK

```bash
# TypeScript
npm install @modelcontextprotocol/sdk

# Python
pip install mcp
```

```ts
// client-setup.ts
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const client = new Client({ name: "my-agent", version: "1.0.0" });
const transport = new StreamableHTTPClientTransport(
  new URL("https://mcp.gapup.io/mcp"),
  { requestInit: { headers: { Authorization: `Bearer ${process.env.GAPUP_API_KEY}` } } },
);
await client.connect(transport);
```

```python
# client_setup.py
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import os

async def make_client():
    headers = {"Authorization": f"Bearer {os.environ['GAPUP_API_KEY']}"}
    async with streamablehttp_client(
        "https://mcp.gapup.io/mcp", headers=headers
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            return session
```

---

## 1. `industry_classifier_naics_sic` — fast company classifier

**Price:** $0.05 · **Latency:** ~210ms p50 · **Use it when:** you need
NAICS / SIC / NACE codes for a company description.

### curl

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
        "company_description": "Maritime freight forwarder specialized in reefer containers, intra-EU corridors, 120 employees, €45M revenue",
        "primary_revenue_source": "Freight forwarding fees",
        "focus_classifications": ["naics", "sic", "nace"]
      }
    }
  }' | grep -E '^data:' | sed 's/^data: //' | jq '.result'
```

### TypeScript

```ts
const result = await client.callTool({
  name: "industry_classifier_naics_sic",
  arguments: {
    audience: "agent",
    company_name: "Helios Cold Chain",
    company_description: "Maritime freight forwarder, reefer containers, intra-EU, 120 FTE, €45M",
    primary_revenue_source: "Freight forwarding fees",
    focus_classifications: ["naics", "sic", "nace"],
  },
});
console.log(result.content[0].text);
```

### Python

```python
result = await session.call_tool(
    "industry_classifier_naics_sic",
    {
        "audience": "agent",
        "company_name": "Helios Cold Chain",
        "company_description": "Maritime freight forwarder, reefer containers, intra-EU, 120 FTE, €45M",
        "primary_revenue_source": "Freight forwarding fees",
        "focus_classifications": ["naics", "sic", "nace"],
    },
)
print(result.content[0].text)
```

---

## 2. `competitor_intel` — full competitor briefing

**Price:** $0.10 · **Latency:** ~25-30s (agent) / ~60s (human) ·
**Use it when:** you need the full picture across 2-5 competitors.

If you only need pricing moves or recent product moves, use the
granular variants (cheaper, faster — see §3).

### curl

```bash
curl -sS -X POST https://mcp.gapup.io/mcp \
  -H "Authorization: Bearer $GAPUP_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {
      "name": "competitor_intel",
      "arguments": {
        "audience": "agent",
        "selfCompany": {
          "name": "Aurora Notes",
          "url": "https://example-aurora.notes",
          "pitch": "Block-based workspace for distributed product teams."
        },
        "competitors": [
          { "name": "Lattice Docs", "url": "https://example-lattice.docs" },
          { "name": "Vela Workspace", "url": "https://example-vela.io" }
        ],
        "focus": "AI-feature moves + pricing shifts threatening our Plus tier in 2026."
      }
    }
  }' | grep -E '^data:' | sed 's/^data: //' | jq '.result.structuredContent.executiveSummary'
```

### TypeScript

```ts
const intel = await client.callTool({
  name: "competitor_intel",
  arguments: {
    audience: "agent",
    selfCompany: {
      name: "Aurora Notes",
      url: "https://example-aurora.notes",
      pitch: "Block-based workspace for distributed product teams.",
    },
    competitors: [
      { name: "Lattice Docs", url: "https://example-lattice.docs" },
      { name: "Vela Workspace", url: "https://example-vela.io" },
    ],
    focus: "AI-feature moves + pricing shifts threatening our Plus tier in 2026.",
  },
});
```

### Python

```python
intel = await session.call_tool("competitor_intel", {
    "audience": "agent",
    "selfCompany": {
        "name": "Aurora Notes",
        "url": "https://example-aurora.notes",
        "pitch": "Block-based workspace for distributed product teams.",
    },
    "competitors": [
        {"name": "Lattice Docs", "url": "https://example-lattice.docs"},
        {"name": "Vela Workspace", "url": "https://example-vela.io"},
    ],
    "focus": "AI-feature moves + pricing shifts threatening our Plus tier in 2026.",
})
```

---

## 3. `competitor_moves` — recent product launches only

**Price:** $0.05 · **Latency:** ~8s · **Use it when:** you only need
the launches/announcements without the full deck.

Same input shape as `competitor_intel`; returns only the `prioritySignals[]`
and a short summary. Three other granular variants exist:
`competitor_pricing_radar` ($0.04), `competitor_profiles` ($0.05),
`competitor_recommendations` ($0.06). Pick the one that matches the
question your agent is actually answering — cheaper, faster, easier to
chain.

```bash
curl -sS -X POST https://mcp.gapup.io/mcp \
  -H "Authorization: Bearer $GAPUP_API_KEY" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{
    "name":"competitor_moves",
    "arguments":{
      "audience":"agent",
      "selfCompany":{"name":"Aurora Notes","url":"https://example-aurora.notes","pitch":"Block-based workspace"},
      "competitors":[{"name":"Lattice Docs","url":"https://example-lattice.docs"}],
      "focus":"AI feature launches in the last 90 days"
    }
  }}' | grep -E '^data:' | sed 's/^data: //' | jq '.result.structuredContent.prioritySignals'
```

---

## 4. `sec_filing_decoder` — extract signals from 10-K / 10-Q / 8-K

**Price:** $0.15 · **Latency:** ~20s · **Source:** SEC EDGAR (live).

```bash
curl -sS -X POST https://mcp.gapup.io/mcp \
  -H "Authorization: Bearer $GAPUP_API_KEY" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{
    "name":"sec_filing_decoder",
    "arguments":{
      "audience":"agent",
      "ticker":"SHOP",
      "filing_types":["10-K"],
      "lookback_months":18,
      "focus":"all"
    }
  }}' | grep -E '^data:' | sed 's/^data: //' | jq '.result.structuredContent'
```

```python
filings = await session.call_tool("sec_filing_decoder", {
    "audience": "agent",
    "ticker": "SHOP",
    "filing_types": ["10-K"],
    "lookback_months": 18,
    "focus": "all",
})
```

---

## 5. `sanctions_screener_multi` — 7 lists + PEP + adverse media

**Price:** $0.15 · **Latency:** ~18s · **Sources:** OFAC SDN +
Consolidated, EU EEAS, UK HMT, UN SC, Switzerland SECO, Canada SEMA +
OpenSanctions PEP + curated adverse media. Composite risk score with
evidence trail.

```bash
curl -sS -X POST https://mcp.gapup.io/mcp \
  -H "Authorization: Bearer $GAPUP_API_KEY" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{
    "name":"sanctions_screener_multi",
    "arguments":{
      "audience":"agent",
      "entity_type":"company",
      "entity_name":"Veridian Trading Co. LLC",
      "aliases":["Veridian Trading","VTC Holdings"],
      "country_of_registration":"CY",
      "address":"Limassol, Cyprus",
      "jurisdiction_focus":"all",
      "adverse_media_lookback_days":730,
      "context_note":"Potential supplier — synthetic textile import €4.2M/yr."
    }
  }}' | grep -E '^data:' | sed 's/^data: //' | jq '.result.structuredContent.composite_risk'
```

```ts
const screening = await client.callTool({
  name: "sanctions_screener_multi",
  arguments: {
    audience: "agent",
    entity_type: "company",
    entity_name: "Veridian Trading Co. LLC",
    aliases: ["Veridian Trading", "VTC Holdings"],
    country_of_registration: "CY",
    jurisdiction_focus: "all",
    adverse_media_lookback_days: 730,
  },
});
```

---

## 6. `kyc_screener` — full onboarding packet review

**Price:** $0.20 · **Latency:** ~25s · **Use it when:** you have an
onboarding packet with multiple entities + UBOs and need a single
composite verdict.

```python
verdict = await session.call_tool("kyc_screener", {
    "audience": "agent",
    "onboardingPacket": {
        "requestId": "KYC-2026-Q4-1147",
        "submittedBy": "Sophie Martinez · Compliance Analyst",
        "submittedAt": "2026-12-08T14:22:00Z",
        "accountType": "private-banking",
        "jurisdiction": "Switzerland (Geneva)",
    },
    "entities": [
        {
            "legalName": "Aldebaran Holdings Ltd.",
            "entityType": "Ltd",
            "jurisdiction": "British Virgin Islands",
            "registrationNumber": "BVI-2018-104782",
            "incorporationDate": "2018-03-15",
            "uboNames": ["Viktor Sokolov", "Elena Sokolova", "Marcus Reinhardt"],
        }
    ],
})
```

Batch variant: `kyc_screener_batch` (async — returns a `job_id`, poll
with `kyc_screener_batch_result`). Use for >5 entities in one call.

---

## 7. `ai_governance_pilot` — EU AI Act readiness brief

**Price:** $0.20 · **Latency:** ~28s · **Use it when:** you need a
deployment-ready governance package across multiple AI use-cases.

The asynchronous variants `ai_governance_full_report_async` +
`_result` give the longer-form report (~3 min) for board-level
deliverables.

```ts
const report = await client.callTool({
  name: "ai_governance_pilot",
  arguments: {
    audience: "agent",
    company: {
      name: "TalentScope SAS",
      sector: "HR SaaS",
      fte: 280,
      revenueEur: 38_000_000,
      country: "France",
      jurisdictions: ["FR", "EU", "UK"],
    },
    aiUseCases: [
      {
        name: "CV scoring",
        description: "Gradient boosting + NLP model scoring CVs 0-100 per role.",
        dataTypes: ["CV text", "experience", "education", "skills"],
        impactedUsers: "280k applicants/yr",
      },
    ],
  },
});
```

---

## 8. `cyber_risk_auditor` — attack surface + CVE exposure brief

**Price:** $0.20 · **Sources:** NVD, OSV, CISA KEV, FIRST.org CVSS.

```bash
curl -sS -X POST https://mcp.gapup.io/mcp \
  -H "Authorization: Bearer $GAPUP_API_KEY" -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{
    "name":"cyber_risk_auditor",
    "arguments":{
      "audience":"agent",
      "company_name":"Nordwind Hydrogen GmbH",
      "primary_stack":["Kubernetes 1.29","PostgreSQL 15","Node 20"],
      "exposure":["public REST API","customer portal","S3 buckets"],
      "compliance_focus":["ISO 27001","NIS2"]
    }
  }}' | grep -E '^data:' | sed 's/^data: //' | jq '.result.structuredContent.priorityCves'
```

---

## 9. `trend_watcher` — what's moving in a niche

**Price:** $0.08 · **Sources:** GDELT, Wikipedia revisions, Reddit,
curated industry press.

```ts
const trends = await client.callTool({
  name: "trend_watcher",
  arguments: {
    audience: "agent",
    domain: "B2B procurement automation",
    lookback_days: 30,
    region: "EU",
    angle: "Macro forces affecting SMB buying behaviour",
  },
});
```

---

## 10. `pitch_deck_storyline` — investor narrative outline

**Price:** $0.25 · **Use it when:** you have a one-pager and need a
12-slide narrative with arguments + counter-objections per slide.

This one is heavier. Default audience is `human` (gold-standard, ~30s)
because deck output is read by humans. Force `agent` only if a
downstream agent reformats it.

```python
deck = await session.call_tool("pitch_deck_storyline", {
    "audience": "human",
    "company": {
        "name": "Atlas Maritime Bunkering",
        "stage": "Series A",
        "askEur": 8_000_000,
        "useOfFunds": "Fleet electrification + 4 new ports of presence",
    },
    "onePager": "Atlas operates green-fuel barges in 6 EU ports...",
    "audience_for_deck": "Climate-focused Series A funds (€50-200M)",
})
```

---

## Error handling

Every tool returns `isError: true` on the response if validation
failed. Inspect `content[0].text` for the structured error.

```ts
const r = await client.callTool({ name: "industry_classifier_naics_sic", arguments: {} });
if (r.isError) {
  const err = JSON.parse(r.content[0].text);
  console.error(err.code, err.message); // e.g. "VALIDATION_ERROR" + Zod issues
}
```

Rate-limit headers always present:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1735689600
```

If `X-RateLimit-Remaining: 0`, the next call returns HTTP 429 with a
`Retry-After` header (seconds).

## Async pattern (heavy tools)

Three tools currently have async variants:
`competitive_deep_dive_async` / `_result`,
`patent_landscape_async` / `_result`,
`ai_governance_full_report_async` / `_result`.

Pattern:

```ts
// 1. Start the job
const start = await client.callTool({
  name: "competitive_deep_dive_async",
  arguments: { audience: "agent", selfCompany: {...}, competitors: [...] },
});
const { job_id } = JSON.parse(start.content[0].text);

// 2. Poll every 5s until status === "complete"
let result;
while (true) {
  const r = await client.callTool({
    name: "competitive_deep_dive_result",
    arguments: { job_id },
  });
  result = JSON.parse(r.content[0].text);
  if (result.status === "complete") break;
  if (result.status === "failed") throw new Error(result.error);
  await new Promise(r => setTimeout(r, 5000));
}
```

## Where next

- Full per-tool prices: [`docs/PRICING.md`](PRICING.md)
- Underlying data sources: [`docs/CONNECTORS.md`](CONNECTORS.md)
- Client install matrix (Claude Code, Cursor, …): [`docs/CLIENTS.md`](CLIENTS.md)
- Architecture overview: [`docs/ARCHITECTURE.md`](ARCHITECTURE.md)
