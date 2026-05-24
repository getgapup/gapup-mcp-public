# Gapup MCP — Data sources

> The hosted server pulls from public APIs, government registries, and open
> data sets to ground every tool's response in citable evidence. This page
> is a snapshot of the sources that are wired in production. Live tools
> always reflect the current set — see `tools/list` for what's available.

For each source we note:

- **Type** — what kind of data it returns
- **Auth** — keyless (no auth required), API key (server-side, transparent to you), or partner (contractual)
- **Used by** — example tools that cite it

Auth is server-side; you never need to provide credentials for any source.
You pay a single x402 micro-payment per tool call.

---

## Sanctions, watchlists, PEP & adverse media

Powers `sanctions_screener_multi`, `kyc_screener` (+ batch variants),
`sharia_compliance_screener`, `fraud_detector`.

| Source | Type | Auth | Notes |
|--------|------|------|-------|
| **OFAC SDN + Consolidated** (`treasury.gov/ofac`) | US sanctions, SDN list, Consolidated list | keyless | Refreshed daily via cron |
| **EU consolidated sanctions** (EEAS) | EU restrictive measures | keyless | XML feed, parsed in-house |
| **UK HMT consolidated list** | UK sanctions | keyless | Daily mirror |
| **UN Security Council Consolidated** | UN sanctions | keyless | XML/JSON feed |
| **Switzerland SECO** | Swiss sanctions | keyless | Federal council list |
| **Canada SEMA** | Canadian sanctions | keyless | Justice Canada feed |
| **Australia DFAT** | Australian sanctions | keyless | DFAT consolidated list |
| **OpenSanctions** (opensanctions.org) | PEP, RCA, enforcement databases | API key | Aggregated 200+ data sources |
| **Adverse media** (multi-source web search) | News/regulatory mentions | mixed | GDELT + curated press feeds |

## Corporate registries & legal entities

Powers `corporate_registry_lookup`, `legal_entity_identifier`,
`account_expansion_mapper`, `due_diligence_dossier`.

| Source | Type | Auth |
|--------|------|------|
| **GLEIF** (`api.gleif.org`) | Legal Entity Identifier (LEI) global | keyless |
| **OpenCorporates** (`api.opencorporates.com`) | 200M+ companies, 130+ jurisdictions | API key |
| **Companies House UK** (`api.company-information.service.gov.uk`) | UK companies | API key |
| **KVK Netherlands** (`api.kvk.nl`) | Dutch chamber of commerce | API key |
| **Recherche-Entreprises (FR)** (`recherche-entreprises.api.gouv.fr`) | French SIRENE registry | keyless |
| **SAM.gov** (`api.sam.gov`) | US federal contractor entities + exclusions | API key |
| **MCA India** (`mca.gov.in`) | Indian corporate filings | scraped |
| **Brazilian Planalto registries** (`planalto.gov.br`) | Brazilian official gazette references | keyless |

## Securities, filings, market data

Powers `sec_filing_decoder`, `earnings_reviewer`,
`earnings_transcript_signals`, `historical_price_series`,
`monte_carlo_portfolio`, `ma_deal_screener`, `re_deal_screener`.

| Source | Type | Auth |
|--------|------|------|
| **SEC EDGAR** (`data.sec.gov`, `efts.sec.gov`) | US filings (10-K, 10-Q, 8-K, 13F, S-1) | keyless |
| **HKEXnews** (`www1.hkexnews.hk`) | Hong Kong exchange filings | keyless |
| **BSE India** (`api.bseindia.com`) | Bombay Stock Exchange | keyless |
| **NSE India** (`www.nseindia.com`) | National Stock Exchange India | keyless |
| **Twelve Data** (`api.twelvedata.com`) | Equities, FX, crypto OHLC | API key |
| **Nasdaq Data Link** (`api.nasdaq.com`) | Reference data, quotes | API key |
| **World Bank** (`api.worldbank.org`) | Country macro indicators | keyless |
| **FRED St. Louis Fed** (`api.stlouisfed.org`) | US macro time-series | API key |
| **Frankfurter** (`api.frankfurter.app`) | ECB FX reference rates | keyless |
| **Exchange-Rate Host** (`api.exchangerate.host`) | Cross-rate FX history | keyless |

## Crypto, on-chain, x402 settlement

Powers `crypto_wallet_intel`, `usdc_x402_payments_intel`,
`historical_price_series` (crypto symbols).

| Source | Type | Auth |
|--------|------|------|
| **CoinGecko** (`api.coingecko.com`) | Spot, market cap, history | keyless / pro |
| **Coinbase Exchange** (`api.exchange.coinbase.com`) | Order book, trades | keyless |
| **Coinbase CDP** (`api.cdp.coinbase.com`) | Wallet, on-chain (Base, OP) | API key |
| **Etherscan** (`api.etherscan.io`) | Ethereum L1 explorer | API key |
| **Routescan** (`api.routescan.io`) | Multi-chain explorer (Base, OP, Avax) | API key |
| **Binance** (`api.binance.com`) | Spot/futures market data | keyless |
| **Kraken** (`api.kraken.com`) | Spot market data | keyless |
| **OKX** (`www.okx.com`) | Spot/derivatives market data | keyless |
| **DefiLlama** (`api.llama.fi`) | TVL, protocols, chains | keyless |

## Patents, scientific & academic literature

Powers `patent_landscape`, `clinical_evidence_briefer`,
`clinical_pharma_intel`, `research_paper_qa`, `sci_literature_search`,
`ip_protection_pilot`.

| Source | Type | Auth |
|--------|------|------|
| **Lens.org** (`api.lens.org`) | Patents + scholarly | API key |
| **PatentsView USPTO** (`api.patentsview.org`) | US patents | keyless |
| **OpenAlex** (`api.openalex.org`) | Scholarly works (200M+) | keyless |
| **Semantic Scholar** (`api.semanticscholar.org`) | Papers, citations, authors | keyless / key |
| **Crossref** (`api.crossref.org`) | DOI metadata | keyless |
| **Core.ac.uk** (`api.core.ac.uk`) | Open-access fulltexts | API key |
| **PubMed eutils** (`eutils.ncbi.nlm.nih.gov`) | Biomedical literature | keyless |
| **ClinicalTrials.gov** | Trial protocols + results | keyless |
| **FDA OpenFDA** (`open.fda.gov`, `api.fda.gov`) | Drug labels, adverse events, devices | keyless |

## Security, vulnerabilities, CVE

Powers `cve_security_lookup`, `dependency_vulnerability_scan`,
`attack_surface_monitor`, `pentest_scope_estimator`, `cyber_risk_auditor`.

| Source | Type | Auth |
|--------|------|------|
| **NVD NIST** (`services.nvd.nist.gov`, `nvd.nist.gov`) | CVE catalog + CVSS | API key |
| **OSV** (`api.osv.dev`) | OSS package vuln database | keyless |
| **FIRST.org CVSS** (`api.first.org`) | CVSS scoring service | keyless |
| **NIST CSRC** (`csrc.nist.gov`) | Frameworks (CSF, 800-53, 800-171) | keyless |
| **CISA** (`www.cisa.gov`) | KEV, advisories, ICS | keyless |
| **Spamhaus** (`www.spamhaus.org`) | Email/IP reputation | keyless |

## Government procurement & tenders

Powers `gov_procurement_multi`, `rfp_tender_architect`.

| Source | Type | Auth |
|--------|------|------|
| **SAM.gov** (`sam.gov`, `api.sam.gov`) | US federal opportunities | API key |
| **TED Europa** (`api.ted.europa.eu`) | EU-wide tenders | keyless |
| **UK Contracts Finder** (`contractsfinder.service.gov.uk`) | UK procurement | keyless |

## Court filings, regulatory text, case law

Powers `court_filings_multi`, `arbitration_awards_lookup`,
`contract_risk_scanner`, `legal_clause_extractor`,
`privacy_compliance_audit`, `ai_governance_pilot`.

| Source | Type | Auth |
|--------|------|------|
| **CourtListener** (RECAP, opinions) | US federal + state case law | API key |
| **Caselaw — UK National Archives** (`caselaw.nationalarchives.gov.uk`) | UK case law | keyless |
| **Legifrance FR** (`www.legifrance.gouv.fr`) | French statutes, case law | keyless |
| **UK Legislation** (`www.legislation.gov.uk`) | UK statutes | keyless |
| **HMRC** (`api.service.hmrc.gov.uk`) | UK tax reference | API key |
| **EEOC** (`www.eeoc.gov`) | US employment regulation | keyless |
| **OAG California** (`oag.ca.gov`) | CCPA enforcement | keyless |
| **NIST AI RMF / EU AI Act** | Compliance frameworks | keyless |

## Labor market, jobs, talent

Powers `job_postings_intelligence`, `talent_intelligence`,
`comp_plan_architect`, `recruiting_architect`.

| Source | Type | Auth |
|--------|------|------|
| **Adzuna** (`api.adzuna.com`) | Job postings, salary | API key |
| **ONET** (`services.onetcenter.org`) | Occupation taxonomy + skills | keyless |
| **BLS** (`www.bls.gov`) | US Bureau of Labor Statistics | API key |

## Real estate (France) & climate / hazards

Powers `re_deal_screener`, `real_estate_intel`, `weather_climate_intel`,
`climate_scenario_rcp`, `geo_logistics_intel`.

| Source | Type | Auth |
|--------|------|------|
| **DVF Etalab** (`app.dvf.etalab.gouv.fr`) | French real estate transactions | keyless |
| **Cerema** (`apidf-preprod.cerema.fr`) | French zoning & DVF+ | keyless |
| **Géorisques** | French natural hazards | keyless |
| **Open-Meteo** (`api.open-meteo.com`) | Weather + climate reanalysis | keyless |
| **NOAA tides** (`tidesandcurrents.noaa.gov`) | Coastal | keyless |
| **FEMA hazards** (`hazards.fema.gov`) | US natural hazards | keyless |
| **Open-Elevation** (`api.open-elevation.com`) | Elevation queries | keyless |
| **Postcodes.io** (`api.postcodes.io`) | UK postcode geocoding | keyless |
| **api-adresse.data.gouv.fr** | French BAN geocoder | keyless |

## Shipping, trade, supply chain

Powers `geo_logistics_intel`, `supplier_esg_audit`,
`agoa_eba_intelligence` (trade preference programs).

| Source | Type | Auth |
|--------|------|------|
| **AISStream** (`api.aisstream.io`) | Live AIS vessel positions | API key |
| **AGOA Info** (`agoa.info`) | US trade preference for Africa | keyless |
| **MarineTraffic** (`www.marinetraffic.com`) | Cited reference, not fetched | — |

## News, social signals, web research

Powers research backbones across `competitive_deep_dive`,
`market_research_brief`, `sentiment_news_pulse`, `signal_hunter`,
`press_influencer`, `trend_watcher`.

| Source | Type | Auth |
|--------|------|------|
| **GDELT** (`api.gdeltproject.org`) | Global news event database | keyless |
| **Wikipedia** | Article fulltext + revision metadata | keyless |
| **Wikidata** (`www.wikidata.org`) | Structured entity facts | keyless |
| **Reddit** (`www.reddit.com`) | Subreddit threads | keyless |
| **YouTube** | Captions for transcribe/chapterize | API key |
| **Mojeek** (`www.mojeek.com`) | Independent web index | partner |
| **Wayback Machine** | Snapshot recovery for stale URLs | keyless |

## LLM cascade & embeddings (internal)

| Provider | Use |
|----------|-----|
| **Mistral** (`api.mistral.ai`) | Gold-standard pipeline (`audience: human`) |
| **Cerebras** (`api.cerebras.ai`) | Fast pipeline qwen-3-235b (`audience: agent`) |
| **Groq** (`api.groq.com`) | Tag-extraction fallback |
| **OpenAI** | Embeddings, fallback |
| **Anthropic** (`api.anthropic.com`) | Reasoning fallback |
| **DeepSeek** (`api.deepseek.com`) | Compute-bound fallback |

These are internal — agents never see provider-specific output. The same
JSON contract is returned regardless of which LLM served the request.

---

## How sources are cited

Every output that depends on an external source includes a `sources[]`
array with `{ name, url, fetched_at }` entries. If a source went stale
mid-request (rate-limited, 5xx, schema drift), the tool emits a
`degraded: true` flag and lists the affected sources rather than
silently substituting.

## Data freshness

| Cadence | Examples |
|---------|----------|
| Real-time (on request) | Market data, FX, news search, web search, on-chain |
| Daily | Sanctions lists, SEC filings, NVD, CISA KEV |
| Weekly | Patent landscapes, OpenAlex, scientific lit |
| Monthly | Macro indicators (BLS, FRED, World Bank), labour market datasets |

## Adding a source

If a tool needs a source that isn't here, open a [feature request](../CONTRIBUTING.md)
describing the source, the access path, and the tool that would cite it.
We add ~3-5 sources per month.
