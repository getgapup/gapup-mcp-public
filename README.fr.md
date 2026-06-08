# Gapup MCP

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)

[![smithery badge](https://smithery.ai/badge/gapup-team/gapup-mcp)](https://smithery.ai/servers/gapup-team/gapup-mcp)
[![Tools](https://img.shields.io/badge/tools-271-c9a84c)](https://mcp.gapup.io/health)
[![x402](https://img.shields.io/badge/x402-USDC%2FEURC-c9a84c)](https://x402.org)
[![Free tier](https://img.shields.io/badge/free%20tier-100%20calls%2Fmo-10b981)](https://hub.gapup.io/agents-api/onboard)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Expertise C-suite payable par les agents — 271 outils, micro-paiements x402, JSON prêt pour le board.**

Endpoint live : `https://mcp.gapup.io/mcp`  
Accès gratuit : 100 appels/mois, sans carte bancaire → [hub.gapup.io/agents-api/onboard](https://hub.gapup.io/agents-api/onboard)

---

## Qu'est-ce que Gapup MCP ?

Un serveur [Model Context Protocol](https://modelcontextprotocol.io) hébergé exposant **plus de 100 outils d'expertise business** pour les agents IA. Chaque outil retourne un livrable JSON structuré, auditable et prêt pour le board en 1 à 30 secondes.

Paiement à l'appel via [x402](https://x402.org) (USDC + EURC sur Base + Optimism). Pas d'abonnement, pas de passerelle API. Le prix est encodé dans la réponse — les agents ne paient que ce qu'ils consomment.

## Pourquoi les agents l'utilisent

- **Sorties board-ready** — JSON typé Zod, persona stricte, sans bavardage
- **Format dual audience** — le paramètre `audience` route vers `human` (Mistral gold-standard, ~30s) ou `agent` (Cerebras qwen-3-235b, <5s)
- **Sources citées** — citations, DOIs, pistes de preuve ; aucun fait halluciné
- **Fortifications EU-first** — DVF Cerema + Géorisques pour l'immobilier, OFAC + EU + UK + UN + SECO + SEMA + DFAT pour les sanctions
- **Tier gratuit réel** — 100 appels/mois sans carte bancaire, sans jeux sur les limites

## Ce qu'il contient (271 outils)

### Top 10 des expertises C-suite (les plus utilisées)
- `competitive_intel` — Plongée multi-sources EDGAR + Yahoo + Wayback + Wikipedia
- `sec_filing_decoder` — Extraction 10-K / 10-Q / 8-K + mouvements de KPIs + signaux M&A
- `sanctions_screener_multi` — 8 listes en parallèle (OFAC + EU + UK + UN + SECO + SEMA + DFAT) + PEP + médias adverses
- `kyc_screener` — KYC/AML sur 6 sources actualisées chaque semaine
- `pentest_scope_estimator` — Périmètre PTES + fourchettes d'effort et de coût
- `attack_surface_monitor` — Reconnaissance passive (crt.sh + DNS + Shodan) + CVE/EPSS/KEV
- `clinical_evidence_briefer` — PubMed + ClinicalTrials.gov + OpenFDA, notation GRADE
- `re_deal_screener` — Immobilier EU-first (DVF Cerema + Géorisques)
- `research_paper_qa` — OpenAlex 45 M articles open-access + Semantic Scholar + CORE, cité par DOI
- `industry_classifier_naics_sic` — NAICS + SIC + NACE + GICS + ISIC + HS avec hiérarchie + score de confiance

### Catégories (liste complète dans [docs/API.md](docs/API.md))
Business Intelligence · Finance · Conformité · Stratégie · Ventes · Développement durable · Recherche · Immobilier · Santé · Cybersécurité

## Démarrage rapide

### Option 1 — HTTP direct (MCP Streamable HTTP)

```bash
# Tier gratuit : obtenez une clé sur https://hub.gapup.io/agents-api/onboard
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
        "company_description": "Transitaire maritime, conteneurs réfrigérés, intra-EU",
        "company_name": "Helios EU"
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

Ajoutez dans votre config MCP (voir [docs/CLIENTS.md](docs/CLIENTS.md) pour les 30+ clients supportés) :

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

### Option 4 — Exemple SDK TypeScript

Voir [client/example.ts](client/example.ts).

## Tarification

| Palier | $ USD | Indication EUR* | Exemples |
|---|---|---|---|
| T0 | $0,002 | ~€0,002 | Taux de change, cours de matières premières |
| T1 | $0,05 | ~€0,046 | Classificateur sectoriel, estimation périmètre pentest |
| T2 | $0,10 | ~€0,092 | Empreinte technologique domaine, sizing marché |
| T3 | $0,15 | ~€0,138 | Surface d'attaque, filings SEC, sanctions multi |
| T4 | $0,20 | ~€0,184 | Screener immobilier, preuve clinique, KYC |
| T5 | $0,30 | ~€0,276 | Competitive deep dive (flagship) |
| T6 | $1,50 | ~€1,38 | Batch asynchrone (KYC en masse, rapport gouvernance IA) |

*Taux indicatif 1 USD ≈ 0,92 EUR. Les paiements x402 s'effectuent en USD.

**Tier gratuit** : 100 appels/mois sur tous les paliers. Sans carte bancaire.

Détails complets : [docs/PRICING.md](docs/PRICING.md).

## Architecture (vue d'ensemble)

```
agent ─→ mcp.gapup.io  ─→  Cluster PM2 (2 instances, Cerebras pour mode agent)
              │              │
              │              └─→ Réplicas Fly.io (fra/sin/gru) faible latence globale
              │
              └─→ Cloudflare WAF + rate-limit + cache
```

Architecture complète : [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Observabilité

- Sentry (erreurs + perf + breadcrumbs + identification x402)
- Endpoint santé avec statut fournisseurs LLM + circuit breakers
- Journaux d'accès Cloudflare
- Endpoint `/__metrics` (avec contrôle de débit)

## Distribution

Référencé sur :
- **Smithery** — [smithery.ai/servers/gapup-team/gapup-mcp](https://smithery.ai/servers/gapup-team/gapup-mcp)
- D'autres places de marché en cours d'intégration (Glama, PulseMCP, mcp.so, mcp.directory, MCP Registry, Bazaar à venir).

## Licence & usage

L'API hébergée sur `mcp.gapup.io` est soumise aux [Conditions d'utilisation Gapup](https://hub.gapup.io/terms).

Le contenu de CE dépôt (manifestes, docs, exemples SDK) est sous licence [Proprietary](LICENSE) — redistribution, clonage ou fork de ce code sont restreints.

Le **code source du serveur** est privé. Ce dépôt existe uniquement pour la transparence, la découvrabilité et le support à l'intégration.

## Support

- **Email** : agents@gapup.io
- **Issues** : [GitHub Issues](https://github.com/getgapup/gapup-mcp-public/issues)
- **Docs** : [hub.gapup.io/agents-api](https://hub.gapup.io/agents-api)

## Construit avec

Claude Code · TypeScript · MCP SDK · protocole x402 · Cerebras + Mistral + Anthropic

---

© 2026 Gapup. Tous droits réservés.
