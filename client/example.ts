/**
 * Gapup MCP — TypeScript client example.
 *
 * Minimal example showing how to call any of the 183 Gapup MCP tools from a
 * Node.js agent using the official MCP SDK.
 *
 * Usage:
 *   GAPUP_API_KEY=gpk_xxx npx tsx client/example.ts
 *
 * Free tier (100 calls/mo, no credit card) :
 *   https://hub.gapup.io/agents-api/onboard
 */

import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const GAPUP_API_KEY = process.env.GAPUP_API_KEY;
if (!GAPUP_API_KEY) {
  console.error("Missing GAPUP_API_KEY — get one at https://hub.gapup.io/agents-api/onboard");
  process.exit(1);
}

// ── Connect ──────────────────────────────────────────────────────────────
const transport = new StreamableHTTPClientTransport(new URL("https://mcp.gapup.io/mcp"), {
  requestInit: {
    headers: { "x-api-key": GAPUP_API_KEY },
  },
});

const client = new Client(
  { name: "gapup-example-client", version: "1.0.0" },
  { capabilities: {} },
);

await client.connect(transport);
console.log(`✓ Connected to Gapup MCP`);

// ── List tools ───────────────────────────────────────────────────────────
const { tools } = await client.listTools();
console.log(`\n${tools.length} tools available. First 5 by name:`);
for (const tool of tools.slice(0, 5)) {
  console.log(`  - ${tool.name} — ${tool.description.slice(0, 80)}…`);
}

// ── Call industry classifier (T1 — $0.05 paid, free on first 100 calls/mo) ─
console.log(`\nCalling industry_classifier_naics_sic...`);
const start = Date.now();
const result = await client.callTool({
  name: "industry_classifier_naics_sic",
  arguments: {
    company_description:
      "Maritime freight forwarder specialized in reefer containers, intra-EU corridors, 120 employees, €45M revenue",
    company_name: "Helios Cold Chain",
    primary_revenue_source: "Freight forwarding fees",
  },
});
const elapsed = Date.now() - start;

const text = (result.content?.[0] as { text?: string } | undefined)?.text;
if (!text) {
  console.error("Empty response");
  process.exit(1);
}

const data = JSON.parse(text);
console.log(`\n✓ Response in ${elapsed}ms`);
console.log(`  NAICS : ${data.classifications?.naics_6digit?.code} — ${data.classifications?.naics_6digit?.label}`);
console.log(`  SIC   : ${data.classifications?.sic_4digit?.code} — ${data.classifications?.sic_4digit?.label}`);
console.log(`  NACE  : ${data.classifications?.nace_eu?.code} — ${data.classifications?.nace_eu?.label}`);
console.log(`  Confidence : ${data.overall_confidence}`);

// ── Clean disconnect ─────────────────────────────────────────────────────
await client.close();
console.log(`\n✓ Done. Check usage at https://hub.gapup.io/agents-api`);
