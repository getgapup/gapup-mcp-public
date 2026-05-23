# Gapup MCP — Pricing

## Free tier

**100 calls / calendar month** across all tools and tiers.
**No credit card required.**
Issue key at https://hub.gapup.io/agents-api/onboard.

Rate limits on the free tier:
- 60 requests / minute / IP
- 10 requests / minute / IP for T4+ tools
- Trusted MCP indexers (Bazaar, Smithery, MCP Registry, Anthropic, OpenAI) bypass the standard cap

## Paid tier (x402 micro-payments)

| Tier | $ USD | Tool examples |
|---|---|---|
| **T0** | $0.002 | FX rates, commodity quotes, simple lookups |
| **T1** | $0.05 | `industry_classifier_naics_sic`, `pentest_scope_estimator`, atomic enrichments |
| **T2** | $0.10 | `domain_tech_fingerprint`, `market_sizing`, mid-weight synthesis |
| **T3** | $0.15 | `attack_surface_monitor`, `sec_filing_decoder`, `sanctions_screener_multi`, `sentiment_news_pulse`, `competitor_intel`, board-pack analyses |
| **T4** | $0.20 | `re_deal_screener`, `clinical_evidence_briefer`, `kyc_screener`, `ai_governance_pilot`, regulatory audits, premium niche |
| **T5** | $0.30 | `competitive_deep_dive` flagship, complex multi-source synthesis |
| **T6** | $1.50 | Async batch flagships (`kyc_screener_batch`, `ai_governance_full_report_async`), replaces $5-15k cabinet work |

Each tool's tier is declared in its MCP description and in `tools/list`. The exact price is encoded in the 402 response.

## Currencies & networks

- **USDC** on Base (primary) and Optimism
- **EURC** on Base (rate 1 USD = 0.92 EUR, dynamic in v2)

## Payment facilitator

- **Production**: [Coinbase x402](https://x402.coinbase.com) (post-LLC + Coinbase Business KYB activation, ETA mid-June 2026)
- **Currently**: `mock-dev` mode on `base-sepolia` (testnet, free)

## When you'll pay

Free tier covers most exploration and individual usage. Paid x402 kicks in:
- After the 100 calls/month free quota
- For T6 async flagships (always paid)
- For high-volume agent traffic (~thousand+ calls/month)

## Examples

A typical agent session calling 5 tools:

| Tool | Tier | Price |
|---|---|---|
| `competitor_intel` | T3 | $0.15 |
| `sec_filing_decoder` (3 companies) | T3 × 3 | $0.45 |
| `sanctions_screener_multi` (5 entities) | T3 × 5 | $0.75 |
| `re_deal_screener` (1 deal) | T4 | $0.20 |
| `research_paper_qa` (1 query) | T4 | $0.20 |
| **Total session** | | **$1.75** |

For comparison: a typical $5-15k consulting report on equivalent topics = ~1000-2000× the price.

## Compare with similar offers

- **PaperQA2** (research_paper_qa equivalent): self-hosted, requires you to manage Python + corpus → free but operational burden
- **Cobalt pentest scope**: $5k-15k per engagement scope → vs our $0.05 estimate
- **Sanctions screening incumbents** (LexisNexis, ComplyAdvantage): $1-5/check, restricted access → vs our $0.15 multi-jurisdiction
- **SEC filing decoder** (CapIQ, Bloomberg): subscription only → vs our $0.15 per company

The Gapup pricing reflects pay-as-you-go agent economics: an agent making decisions over thousands of micro-queries gets order-of-magnitude cheaper than human-grade subscriptions.

## SLAs (paid tier post-LLC)

To be published with the production x402 activation. Free tier provided on a best-effort basis.

See [Terms of Service](https://hub.gapup.io/terms) for full details.
