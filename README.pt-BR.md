# Gapup MCP

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)

[![smithery badge](https://smithery.ai/badge/gapup-team/gapup-mcp)](https://smithery.ai/servers/gapup-team/gapup-mcp)
[![Tools](https://img.shields.io/badge/tools-183-c9a84c)](https://mcp.gapup.io/health)
[![x402](https://img.shields.io/badge/x402-USDC%2FEURC-c9a84c)](https://x402.org)
[![Free tier](https://img.shields.io/badge/free%20tier-100%20calls%2Fmo-10b981)](https://hub.gapup.io/agents-api/onboard)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Conhecimento C-suite pagável por agentes — 183 ferramentas, micropagamentos x402, JSON pronto para o conselho.**

Endpoint ativo: `https://mcp.gapup.io/mcp`  
Plano gratuito: 100 chamadas/mês, sem cartão de crédito → [hub.gapup.io/agents-api/onboard](https://hub.gapup.io/agents-api/onboard)

---

## O que é o Gapup MCP?

Um servidor [Model Context Protocol](https://modelcontextprotocol.io) hospedado que expõe **mais de 100 ferramentas de expertise empresarial** para agentes de IA. Cada ferramenta retorna um entregável JSON estruturado, auditável e pronto para o conselho em 1 a 30 segundos.

Pagamento por chamada via [x402](https://x402.org) (USDC + EURC na Base + Optimism). Sem assinatura, sem gateway de API. O preço está codificado na resposta — agentes pagam apenas o que consomem.

## Por que agentes usam

- **Saídas prontas para o conselho** — JSON tipado com Zod, persona estrita, sem enrolação
- **Formato dual-audience** — parâmetro `audience` roteia para `human` (Mistral padrão ouro, ~30s) ou `agent` (Cerebras qwen-3-235b, <5s)
- **Fontes citadas** — citações, DOIs, cadeias de evidência; sem fatos alucinados
- **Vantagens EU-first** — DVF Cerema + Géorisques para imóveis, OFAC + EU + UK + UN + SECO + SEMA + DFAT para sanções
- **Plano gratuito real** — 100 chamadas/mês sem cartão de crédito, sem truques de limite de taxa

## O que há dentro (183 ferramentas)

### Top 10 expertises C-suite (mais utilizadas)
- `competitive_intel` — Análise profunda multi-fonte EDGAR + Yahoo + Wayback + Wikipedia
- `sec_filing_decoder` — Extração 10-K / 10-Q / 8-K + movimentos de KPIs + sinais de M&A
- `sanctions_screener_multi` — 8 listas em paralelo (OFAC + EU + UK + UN + SECO + SEMA + DFAT) + PEP + mídia adversa
- `kyc_screener` — KYC/AML em 6 fontes atualizadas semanalmente
- `pentest_scope_estimator` — Escopo PTES + faixas de esforço/custo
- `attack_surface_monitor` — Reconhecimento passivo (crt.sh + DNS + Shodan) + CVE/EPSS/KEV
- `clinical_evidence_briefer` — PubMed + ClinicalTrials.gov + OpenFDA, classificação GRADE
- `re_deal_screener` — Imóveis EU-first (DVF Cerema + Géorisques)
- `research_paper_qa` — OpenAlex 45M artigos open-access + Semantic Scholar + CORE, citado por DOI
- `industry_classifier_naics_sic` — NAICS + SIC + NACE + GICS + ISIC + HS com hierarquia + confiança

### Categorias (lista completa em [docs/API.md](docs/API.md))
Business Intelligence · Finanças · Conformidade · Estratégia · Vendas · Sustentabilidade · Pesquisa · Imóveis · Saúde · Segurança

## Início rápido

### Opção 1 — HTTP direto (MCP Streamable HTTP)

```bash
# Plano gratuito: obtenha uma chave em https://hub.gapup.io/agents-api/onboard
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
        "company_description": "Despachante marítimo de contêineres refrigerados, rotas intra-UE",
        "company_name": "Helios Cold Chain"
      }
    }
  }'
```

### Opção 2 — Smithery CLI

```bash
npm install -g @smithery/cli
smithery auth login
smithery mcp add gapup-team/gapup-mcp
```

### Opção 3 — Claude Desktop / Cursor / Windsurf / etc.

Adicione à sua configuração MCP (veja [docs/CLIENTS.md](docs/CLIENTS.md) para os 30+ clientes suportados):

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

### Opção 4 — Exemplo SDK TypeScript

Ver [client/example.ts](client/example.ts).

## Preços

| Nível | $ USD | Exemplos |
|---|---|---|
| T0 | $0,002 | Taxas de câmbio, cotações de commodities |
| T1 | $0,05 | Classificador setorial, estimador de escopo pentest |
| T2 | $0,10 | Impressão digital de tecnologia de domínio, tamanho de mercado |
| T3 | $0,15 | Superfície de ataque, arquivamentos SEC, sanções multi |
| T4 | $0,20 | Triagem imobiliária, evidência clínica, KYC |
| T5 | $0,30 | Análise competitiva aprofundada (carro-chefe) |
| T6 | $1,50 | Lote assíncrono (KYC em massa, relatório de governança IA) |

**Plano gratuito**: 100 chamadas/mês em todos os níveis. Sem cartão de crédito.

Detalhes completos: [docs/PRICING.md](docs/PRICING.md).

## Arquitetura (visão geral)

```
agente ─→ mcp.gapup.io  ─→  Cluster PM2 (2 instâncias, Cerebras para modo agente)
               │              │
               │              └─→ Réplicas Fly.io (fra/sin/gru) baixa latência global
               │
               └─→ Cloudflare WAF + limite de taxa + cache
```

Arquitetura completa: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Observabilidade

- Sentry (erros + performance + breadcrumbs + identificação x402)
- Endpoint de saúde com status de provedores LLM + circuit breakers
- Logs de acesso do Cloudflare
- Endpoint `/__metrics` (com controle de taxa)

## Distribuição

Listado em:
- **Smithery** — [smithery.ai/servers/gapup-team/gapup-mcp](https://smithery.ai/servers/gapup-team/gapup-mcp)
- Mais marketplaces sendo adicionados (Glama, PulseMCP, mcp.so, mcp.directory, MCP Registry, Bazaar em breve).

## Licença e uso

A API hospedada em `mcp.gapup.io` é oferecida sob os [Termos de Serviço da Gapup](https://hub.gapup.io/terms).

O conteúdo DESTE repositório (manifestos, documentação, exemplos SDK) está licenciado sob [Proprietary](LICENSE) — redistribuição, clonagem ou fork deste código é restrito.

A **implementação do servidor** é privada. Este repositório existe exclusivamente para transparência, descoberta e suporte à integração.

## Suporte

- **E-mail**: agents@gapup.io
- **Issues**: [GitHub Issues](https://github.com/getgapup/gapup-mcp-public/issues)
- **Docs**: [hub.gapup.io/agents-api](https://hub.gapup.io/agents-api)

## Construído com

Claude Code · TypeScript · MCP SDK · protocolo x402 · Cerebras + Mistral + Anthropic

---

© 2026 Gapup. Todos os direitos reservados.
