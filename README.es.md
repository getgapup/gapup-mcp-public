# Gapup MCP

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)

[![smithery badge](https://smithery.ai/badge/gapup-team/gapup-mcp)](https://smithery.ai/servers/gapup-team/gapup-mcp)
[![Tools](https://img.shields.io/badge/tools-183-c9a84c)](https://mcp.gapup.io/health)
[![x402](https://img.shields.io/badge/x402-USDC%2FEURC-c9a84c)](https://x402.org)
[![Free tier](https://img.shields.io/badge/free%20tier-100%20calls%2Fmo-10b981)](https://hub.gapup.io/agents-api/onboard)
[![License](https://img.shields.io/badge/license-Proprietary-grey)](LICENSE)

**Conocimiento C-suite pagable por agentes — 183 herramientas, micropagos x402, JSON listo para el directorio.**

Endpoint en vivo: `https://mcp.gapup.io/mcp`  
Nivel gratuito: 100 llamadas/mes, sin tarjeta de crédito → [hub.gapup.io/agents-api/onboard](https://hub.gapup.io/agents-api/onboard)

---

## ¿Qué es Gapup MCP?

Un servidor [Model Context Protocol](https://modelcontextprotocol.io) alojado que expone **más de 100 herramientas de expertise empresarial** para agentes de IA. Cada herramienta devuelve un entregable JSON estructurado, auditado y listo para el directorio en 1-30 segundos.

Pago por llamada mediante [x402](https://x402.org) (USDC + EURC en Base + Optimism). Sin suscripción, sin pasarela de API. El precio está codificado en la respuesta — los agentes pagan lo que consumen.

## Por qué los agentes lo usan

- **Salidas listas para directorio** — JSON tipado con Zod, persona estricta, sin relleno
- **Formato de doble audiencia** — el parámetro `audience` enruta a `human` (Mistral gold-standard, ~30s) o `agent` (Cerebras qwen-3-235b, <5s)
- **Fuentes referenciadas** — citas, DOIs, cadenas de evidencia; sin hechos alucinados
- **Fortalezas EU-first** — DVF Cerema + Géorisques para inmuebles, OFAC + EU + UK + UN + SECO + SEMA + DFAT para sanciones
- **Nivel gratuito real** — 100 llamadas/mes sin tarjeta de crédito, sin trucos con los límites

## Qué hay dentro (183 herramientas)

### Top 10 de expertises C-suite (más utilizadas)
- `competitive_intel` — Análisis profundo multi-fuente EDGAR + Yahoo + Wayback + Wikipedia
- `sec_filing_decoder` — Extracción 10-K / 10-Q / 8-K + movimientos de KPIs + señales M&A
- `sanctions_screener_multi` — 8 listas en paralelo (OFAC + EU + UK + UN + SECO + SEMA + DFAT) + PEP + medios adversos
- `kyc_screener` — KYC/AML en 6 fuentes actualizadas semanalmente
- `pentest_scope_estimator` — Alcance PTES + rangos de esfuerzo/coste
- `attack_surface_monitor` — Reconocimiento pasivo (crt.sh + DNS + Shodan) + CVE/EPSS/KEV
- `clinical_evidence_briefer` — PubMed + ClinicalTrials.gov + OpenFDA, clasificación GRADE
- `re_deal_screener` — Inmuebles EU-first (DVF Cerema + Géorisques)
- `research_paper_qa` — OpenAlex 45M artículos open-access + Semantic Scholar + CORE, citado por DOI
- `industry_classifier_naics_sic` — NAICS + SIC + NACE + GICS + ISIC + HS con jerarquía + confianza

### Categorías (lista completa en [docs/API.md](docs/API.md))
Business Intelligence · Finanzas · Cumplimiento · Estrategia · Ventas · Sostenibilidad · Investigación · Inmuebles · Salud · Seguridad

## Inicio rápido

### Opción 1 — HTTP directo (MCP Streamable HTTP)

```bash
# Nivel gratuito: obtén una clave en https://hub.gapup.io/agents-api/onboard
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
        "company_description": "Transitario marítimo, contenedores refrigerados, intra-UE",
        "company_name": "Helios Cold Chain"
      }
    }
  }'
```

### Opción 2 — Smithery CLI

```bash
npm install -g @smithery/cli
smithery auth login
smithery mcp add gapup-team/gapup-mcp
```

### Opción 3 — Claude Desktop / Cursor / Windsurf / etc.

Añade a tu configuración MCP (ver [docs/CLIENTS.md](docs/CLIENTS.md) para los 30+ clientes compatibles):

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

### Opción 4 — Ejemplo SDK TypeScript

Ver [client/example.ts](client/example.ts).

## Precios

| Nivel | $ USD | Ejemplos |
|---|---|---|
| T0 | $0,002 | Tipos de cambio, cotizaciones de materias primas |
| T1 | $0,05 | Clasificador sectorial, estimador de alcance pentest |
| T2 | $0,10 | Huella tecnológica de dominio, dimensionamiento de mercado |
| T3 | $0,15 | Superficie de ataque, filings SEC, sanciones multi |
| T4 | $0,20 | Screener inmobiliario, evidencia clínica, KYC |
| T5 | $0,30 | Competitive deep dive (insignia) |
| T6 | $1,50 | Batch asíncrono (KYC masivo, informe de gobernanza IA) |

**Nivel gratuito**: 100 llamadas/mes en todos los niveles. Sin tarjeta de crédito.

Detalles completos: [docs/PRICING.md](docs/PRICING.md).

## Arquitectura (visión general)

```
agente ─→ mcp.gapup.io  ─→  Clúster PM2 (2 instancias, Cerebras para modo agente)
               │              │
               │              └─→ Réplicas Fly.io (fra/sin/gru) baja latencia global
               │
               └─→ Cloudflare WAF + rate-limit + caché
```

Arquitectura completa: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Observabilidad

- Sentry (errores + rendimiento + breadcrumbs + identificación x402)
- Endpoint de salud con estado de proveedores LLM + circuit breakers
- Registros de acceso Cloudflare
- Endpoint `/__metrics` (con control de tasa)

## Distribución

Listado en:
- **Smithery** — [smithery.ai/servers/gapup-team/gapup-mcp](https://smithery.ai/servers/gapup-team/gapup-mcp)
- Más marketplaces en proceso de integración (Glama, PulseMCP, mcp.so, mcp.directory, MCP Registry, Bazaar próximamente).

## Licencia y uso

La API alojada en `mcp.gapup.io` se ofrece bajo los [Términos de Servicio de Gapup](https://hub.gapup.io/terms).

El contenido de ESTE repositorio (manifiestos, documentación, ejemplos SDK) está bajo licencia [Proprietary](LICENSE) — se restringe la redistribución, clonación o bifurcación de este código.

La **implementación del servidor** es privada. Este repositorio existe únicamente para transparencia, descubribilidad y soporte a la integración.

## Soporte

- **Email**: agents@gapup.io
- **Issues**: [GitHub Issues](https://github.com/getgapup/gapup-mcp-public/issues)
- **Docs**: [hub.gapup.io/agents-api](https://hub.gapup.io/agents-api)

## Construido con

Claude Code · TypeScript · MCP SDK · protocolo x402 · Cerebras + Mistral + Anthropic

---

© 2026 Gapup. Todos los derechos reservados.
