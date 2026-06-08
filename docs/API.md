# Gapup MCP — API reference

> Live tools/list always reflects the canonical state. This doc is a snapshot.

## Quick verify (always fresh)

```bash
curl -X POST https://mcp.gapup.io/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' \
  | grep -E '^data:' | head -1 | sed 's/^data: //' \
  | jq '.result.tools | length, (map(.name) | sort | .[:10])'
```

Returns 271+ and the first 10 tool names alphabetically.

## Tool categories (271 total)

### C-suite expertises (102 tools)

#### Finance / Investment (18)
- `competitor_intel`, `competitor_moves`, `competitor_pricing_radar`, `competitor_profiles`, `competitor_recommendations`
- `sec_filing_decoder`, `earnings_reviewer`, `treasury_optimizer`, `working_capital`, `tax_optimization`
- `cap_table_strategist`, `capital_strategy`, `funding_hunter`, `investor_list`, `investor_shortlist`, `term_sheet_negotiation`
- `ma_deal_screener`, `re_deal_screener`

#### Compliance / Risk / Legal (16)
- `sanctions_screener_multi`, `kyc_screener`, `fraud_detector`
- `ai_governance_pilot`, `privacy_compliance_audit`, `contract_risk_scanner`
- `cyber_risk_auditor`, `attack_surface_monitor`, `pentest_scope_estimator`
- `audit_pre_flight`, `qa_pre_flight`, `vendor_risk_assessor`
- `insurance_coverage_analyzer`, `ip_protection_pilot`
- `clinical_evidence_briefer`, `industry_classifier_naics_sic`

#### Sales / GTM (16)
- `abm_architect`, `account_expansion_mapper`, `battle_cards_live`, `battle_plan`
- `champion_mapping`, `cross_sell_reco`, `deal_coach`, `deal_structurer`
- `discovery_prep`, `meddic_scoring`, `outbound_sequencer`, `pricing_in_deal`
- `revops_architect`, `sales_enablement_architect`, `sales_pipeline_forecast`, `upsell_hunter`

#### Marketing / Brand / PR (15)
- `brand_builder`, `content_engine`, `customer_marketing`, `customer_voice_synth`
- `event_marketing`, `lead_magnets`, `marketing_roi_dashboard`, `paid_ads_optimizer`
- `positioning_strategist`, `pricing_strategist`, `press_influencer`, `reputation_engine`
- `proposal_generator`, `domain_tech_fingerprint`, `sentiment_news_pulse`

#### Strategy / Ops (12)
- `bp_narratif`, `geographic_expansion`, `growth_path_architect`, `market_entry_strategist`, `market_sizing`
- `strategic_options_analyzer`, `operational_dashboards`, `process_mapping`, `process_mining`
- `procurement_spend_optim`, `infra_blueprint_designer`, `research_paper_qa`

#### HR / People (10)
- `anti_demissions_hr`, `comp_plan_architect`, `diversity_inclusion_metrics`
- `enps_auto`, `internal_communication`, `knowledge_base_auto`
- `ld_architect`, `onboarding_salaries`, `recruiting_architect`, `qbr_auto`

#### Sustainability / ESG (10)
- `action_plan_esg`, `carbon_footprint_calculator`, `carbon_roadmap`
- `esrs_narrative_builder`, `rse_policy_builder`, `supplier_esg_audit`
- `sustainability_report`, `sustainability_reporting_pilot`
- `partnership_synergies`, `pitch_deck_storyline`

#### Customer Success / Retention (5)
- `churn_defender`, `customer_voice_synth`, `renewal_optimizer`, `save_plays`, `win_loss_decoder`

#### Capacity / Vendor / Margin (4)
- `capacity_planning`, `margin_doctor`, `margin_doctor_finance`, `vendor_management`

#### Other (8 — including `trend_watcher`, `rfp_tender_architect`, etc.)

### Content data layer (~30 tools)

`content_catalog`, `content_enrichment`, `content_discovery`, `content_similar`, `content_taxonomy`, `content_audience_profile`, `content_provenance`, `content_compare`, `content_ranking` + domain-specific (gaming, films, TV, music).

### Trade intelligence (~31 tools)

FTG market gap, production methods, sourcing buyers, opportunity scout, business plans, country studies, Africa corridors, commodity prices, ...

### Data connectors (~20 tools)

Live data: FX rates, equity tickers, commodity prices, weather/climate, court filings, corporate registries, patent search, ...

## tools/list response shape

```typescript
{
  jsonrpc: "2.0",
  id: 1,
  result: {
    tools: Array<{
      name: string;          // snake_case tool slug
      description: string;   // full description with use case + inputs
      inputSchema: {         // JSON Schema for arguments
        type: "object",
        properties: Record<string, JSONSchemaProp>,
        required?: string[],
        additionalProperties: boolean
      };
      annotations?: {
        readOnlyHint?: boolean,
        openWorldHint?: boolean,
        ...
      };
    }>
  }
}
```

## tools/call response shape

```typescript
{
  jsonrpc: "2.0",
  id: <id>,
  result: {
    content: Array<{
      type: "text",
      text: string   // JSON string of the structured deliverable
    }>,
    isError?: boolean
  }
}
```

The `content[0].text` is always a JSON string. Parse it for the deliverable, which follows each tool's documented output schema.

## REST API alternative

For consumers who prefer plain REST over MCP:

```
GET  https://mcp.gapup.io/api/v1/tools              # list all tools
GET  https://mcp.gapup.io/api/v1/tools/:name        # tool metadata + schema
POST https://mcp.gapup.io/api/v1/call/:name         # call a tool
GET  https://mcp.gapup.io/api/v1/openapi.json       # OpenAPI 3.0 spec
GET  https://mcp.gapup.io/api/v1/pricing            # tier pricing
GET  https://mcp.gapup.io/health                    # health + status
GET  https://mcp.gapup.io/.well-known/x402          # x402 manifest
```

## x402 (paid calls)

When a paid endpoint is called without payment proof:

```
HTTP/2 402
Content-Type: application/json

{
  "x402Version": "0.1.0",
  "error": "payment_required",
  "price": 0.15,
  "currency": "USDC",
  "accepts": [
    {
      "scheme": "exact",
      "network": "base",
      "maxAmountRequired": "150000",
      "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
      "payTo": "0x...",
      "resource": "https://mcp.gapup.io/api/agent/<slug>"
    }
  ],
  "protocol": "x402/v0",
  "expertise": "<slug>",
  "facilitator": "https://x402.coinbase.com"
}
```

The agent then obtains a payment proof from the facilitator and resends the request with the `x-payment` header.

Currently in `mock-dev` (testnet base-sepolia) mode pending LLC + Coinbase Business activation.

## Free tier authentication

```
Header: x-api-key: gpk_xxxxxxxx
```

Issue at https://hub.gapup.io/agents-api/onboard — instant, no credit card. 100 calls/month across all tiers.

## Examples

See [docs/examples/](examples/) for sample inputs/outputs per major tool.
