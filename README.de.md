# Gapup MCP

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)

[![smithery badge](https://smithery.ai/badge/gapup-team/gapup-mcp)](https://smithery.ai/servers/gapup-team/gapup-mcp)
[![Tools](https://img.shields.io/badge/tools-183-c9a84c)](https://mcp.gapup.io/health)
[![x402](https://img.shields.io/badge/x402-USDC%2FEURC-c9a84c)](https://x402.org)
[![Free tier](https://img.shields.io/badge/free%20tier-100%20calls%2Fmo-10b981)](https://hub.gapup.io/agents-api/onboard)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Agent-zahlbares C-Suite-Wissen — 183 Tools, x402-Mikrozahlungen, boardtaugliches JSON.**

Live-Endpunkt: `https://mcp.gapup.io/mcp`  
Kostenloses Kontingent: 100 Aufrufe/Monat, keine Kreditkarte → [hub.gapup.io/agents-api/onboard](https://hub.gapup.io/agents-api/onboard)

---

## Was ist Gapup MCP?

Ein gehosteter [Model Context Protocol](https://modelcontextprotocol.io)-Server mit **über 100 Business-Expertise-Tools** für KI-Agenten. Jedes Tool liefert in 1–30 Sekunden ein strukturiertes, auditierbares, boardtaugliches JSON-Ergebnis.

Abrechnung per Aufruf über [x402](https://x402.org) (USDC + EURC auf Base + Optimism). Kein Abo, kein API-Gateway. Der Preis ist in der Antwort kodiert — Agenten zahlen nur, was sie verbrauchen.

## Warum Agenten es nutzen

- **Boardtaugliche Ausgaben** — Zod-typisiertes JSON, strenge Persona, kein Chat-Rauschen
- **Dual-Audience-Format** — Parameter `audience` leitet an `human` (Mistral Gold-Standard, ~30 s) oder `agent` (Cerebras qwen-3-235b, <5 s) weiter
- **Quellbasiert** — Zitate, DOIs, Belege; keine halluzinierten Fakten
- **EU-first-Stärken** — DVF Cerema + Géorisques für Immobilien, OFAC + EU + UK + UN + SECO + SEMA + DFAT für Sanktionen
- **Echtes Freikontingent** — 100 Aufrufe/Monat ohne Kreditkarte, ohne Rate-Limit-Tricks

## Inhalt (183 Tools)

### Top 10 C-Suite-Expertisen (meistgenutzt)
- `competitive_intel` — Mehrquellen-Deep-Dive EDGAR + Yahoo + Wayback + Wikipedia
- `sec_filing_decoder` — 10-K / 10-Q / 8-K-Extraktion + KPI-Bewegungen + M&A-Signale
- `sanctions_screener_multi` — 8 Listen parallel (OFAC + EU + UK + UN + SECO + SEMA + DFAT) + PEP + negative Medienberichte
- `kyc_screener` — KYC/AML aus 6 Quellen, wöchentlich aktualisiert
- `pentest_scope_estimator` — PTES-Umfang + Aufwands- und Kostenbereiche
- `attack_surface_monitor` — Passive Aufklärung (crt.sh + DNS + Shodan) + CVE/EPSS/KEV
- `clinical_evidence_briefer` — PubMed + ClinicalTrials.gov + OpenFDA, GRADE-bewertet
- `re_deal_screener` — EU-first-Immobilien (DVF Cerema + Géorisques)
- `research_paper_qa` — OpenAlex 45 Mio. Open-Access-Artikel + Semantic Scholar + CORE, DOI-zitiert
- `industry_classifier_naics_sic` — NAICS + SIC + NACE + GICS + ISIC + HS mit Hierarchie + Konfidenz

### Kategorien (vollständige Liste in [docs/API.md](docs/API.md))
Business Intelligence · Finanzen · Compliance · Strategie · Vertrieb · Nachhaltigkeit · Forschung · Immobilien · Gesundheit · Sicherheit

## Schnellstart

### Option 1 — Direktes HTTP (MCP Streamable HTTP)

```bash
# Freikontingent: Schlüssel erhalten unter https://hub.gapup.io/agents-api/onboard
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
        "company_description": "Seefrachtspediteur, Kühlcontainer, innereuropäisch",
        "company_name": "Helios Cold Chain"
      }
    }
  }'
```

### Option 2 — Smithery CLI

```bash
npm install -g @smithery/cli
smithery auth login
smithery mcp add gapup-team/gapup-mcp
```

### Option 3 — Claude Desktop / Cursor / Windsurf / etc.

In die MCP-Konfiguration einfügen (alle 30+ unterstützten Clients: [docs/CLIENTS.md](docs/CLIENTS.md)):

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

### Option 4 — TypeScript-SDK-Beispiel

Siehe [client/example.ts](client/example.ts).

## Preise

| Stufe | $ USD | Beispiele |
|---|---|---|
| T0 | $0,002 | Wechselkurse, einfache Rohstoffpreise |
| T1 | $0,05 | Branchenklassifizierer, Pentest-Umfangsschätzung |
| T2 | $0,10 | Domain-Tech-Fingerabdruck, Marktgröße |
| T3 | $0,15 | Angriffsfläche, SEC-Einreichungen, Multi-Sanktionen |
| T4 | $0,20 | Immobilien-Screener, klinische Evidenz, KYC |
| T5 | $0,30 | Competitive Deep Dive (Flaggschiff) |
| T6 | $1,50 | Asynchroner Batch (Massen-KYC, KI-Governance-Bericht) |

**Freikontingent**: 100 Aufrufe/Monat über alle Stufen. Keine Kreditkarte.

Vollständige Details: [docs/PRICING.md](docs/PRICING.md).

## Architektur (Überblick)

```
Agent ─→ mcp.gapup.io  ─→  PM2-Cluster (2 Instanzen, Cerebras für Agentenmodus)
               │              │
               │              └─→ Fly.io-Edge-Replikate (fra/sin/gru) globale Niedriglatenz
               │
               └─→ Cloudflare WAF + Rate-Limit + Cache
```

Vollständige Architektur: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Observability

- Sentry (Fehler + Leistung + Breadcrumbs + x402-Identifikation)
- Health-Endpunkt mit LLM-Provider-Status + Circuit Breaker
- Cloudflare-Zugriffsprotokolle
- Endpunkt `/__metrics` (ratenlimitgeschützt)

## Vertrieb

Gelistet auf:
- **Smithery** — [smithery.ai/servers/gapup-team/gapup-mcp](https://smithery.ai/servers/gapup-team/gapup-mcp)
- Weitere Marktplätze folgen (Glama, PulseMCP, mcp.so, mcp.directory, MCP Registry, Bazaar demnächst).

## Lizenz & Nutzung

Die gehostete API unter `mcp.gapup.io` wird gemäß den [Gapup-Nutzungsbedingungen](https://hub.gapup.io/terms) bereitgestellt.

Der Inhalt DIESES Repositorys (Manifeste, Dokumentation, SDK-Beispiele) steht unter der [proprietären Lizenz](LICENSE) — Weiterverbreitung, Klonen oder Forken dieses Codes ist untersagt.

Die **Serverimplementierung** ist privat. Dieses Repository existiert ausschließlich für Transparenz, Auffindbarkeit und Integrationssupport.

## Support

- **E-Mail**: agents@gapup.io
- **Issues**: [GitHub Issues](https://github.com/getgapup/gapup-mcp-public/issues)
- **Docs**: [hub.gapup.io/agents-api](https://hub.gapup.io/agents-api)

## Entwickelt mit

Claude Code · TypeScript · MCP SDK · x402-Protokoll · Cerebras + Mistral + Anthropic

---

© 2026 Gapup. Alle Rechte vorbehalten.
