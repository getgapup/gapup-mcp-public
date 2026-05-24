# Gapup MCP

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)

[![smithery badge](https://smithery.ai/badge/gapup-team/gapup-mcp)](https://smithery.ai/servers/gapup-team/gapup-mcp)
[![Tools](https://img.shields.io/badge/tools-183-c9a84c)](https://mcp.gapup.io/health)
[![x402](https://img.shields.io/badge/x402-USDC%2FEURC-c9a84c)](https://x402.org)
[![Free tier](https://img.shields.io/badge/free%20tier-100%20calls%2Fmo-10b981)](https://hub.gapup.io/agents-api/onboard)
[![License](https://img.shields.io/badge/license-Proprietary-grey)](LICENSE)

**에이전트가 직접 결제하는 C-suite 전문 지식 — 183개 도구, x402 마이크로결제, 이사회 수준 JSON.**

라이브 엔드포인트: `https://mcp.gapup.io/mcp`  
무료 플랜: 월 100회 호출, 신용카드 불필요 → [hub.gapup.io/agents-api/onboard](https://hub.gapup.io/agents-api/onboard)

---

## Gapup MCP란?

AI 에이전트를 위해 **100개 이상의 비즈니스 전문 도구**를 제공하는 호스팅형 [Model Context Protocol](https://modelcontextprotocol.io) 서버입니다. 각 도구는 1~30초 내에 구조화되고 감사 가능한 이사회 수준의 JSON 결과물을 반환합니다.

[x402](https://x402.org)를 통한 호출당 결제 방식(Base + Optimism의 USDC + EURC). 구독 없음, API 게이트웨이 없음. 가격은 응답에 인코딩되어 있으며, 에이전트는 사용한 만큼만 지불합니다.

## 에이전트가 사용하는 이유

- **이사회 수준 출력** — Zod 타입 JSON, 엄격한 페르소나, 불필요한 채팅 없음
- **이중 오디언스 형식** — `audience` 파라미터로 `human`(Mistral 골드 스탠더드, ~30초) 또는 `agent`(Cerebras qwen-3-235b, <5초)로 라우팅
- **출처 명시** — 인용, DOI, 증거 추적; 환각 없음
- **EU-first 강점** — 부동산용 DVF Cerema + Géorisques, 제재용 OFAC + EU + UK + UN + SECO + SEMA + DFAT
- **실질적 무료 플랜** — 신용카드 없이 월 100회 호출, 속도 제한 꼼수 없음

## 구성 내용 (183개 도구)

### C-suite 상위 10개 전문 도구 (가장 많이 사용)
- `competitive_intel` — EDGAR + Yahoo + Wayback + Wikipedia 멀티소스 심층 분석
- `sec_filing_decoder` — 10-K / 10-Q / 8-K 추출 + KPI 변동 + M&A 시그널
- `sanctions_screener_multi` — 8개 목록 병렬 조회(OFAC + EU + UK + UN + SECO + SEMA + DFAT) + PEP + 부정적 미디어
- `kyc_screener` — 주간 업데이트 6개 소스 KYC/AML
- `pentest_scope_estimator` — PTES 범위 + 공수/비용 구간
- `attack_surface_monitor` — 패시브 정찰(crt.sh + DNS + Shodan) + CVE/EPSS/KEV
- `clinical_evidence_briefer` — PubMed + ClinicalTrials.gov + OpenFDA, GRADE 등급
- `re_deal_screener` — EU-first 부동산(DVF Cerema + Géorisques)
- `research_paper_qa` — OpenAlex 4,500만 오픈액세스 논문 + Semantic Scholar + CORE, DOI 인용
- `industry_classifier_naics_sic` — NAICS + SIC + NACE + GICS + ISIC + HS, 계층 구조 + 신뢰도 포함

### 카테고리 (전체 목록은 [docs/API.md](docs/API.md))
비즈니스 인텔리전스 · 금융 · 컴플라이언스 · 전략 · 영업 · 지속가능성 · 연구 · 부동산 · 헬스케어 · 보안

## 빠른 시작

### 옵션 1 — 직접 HTTP (MCP Streamable HTTP)

```bash
# 무료 플랜: https://hub.gapup.io/agents-api/onboard 에서 키 발급
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
        "company_description": "냉동 컨테이너 해상 운송 포워더, EU 역내",
        "company_name": "Helios Cold Chain"
      }
    }
  }'
```

### 옵션 2 — Smithery CLI

```bash
npm install -g @smithery/cli
smithery auth login
smithery mcp add gapup-team/gapup-mcp
```

### 옵션 3 — Claude Desktop / Cursor / Windsurf 등

MCP 설정에 추가(30개 이상 지원 클라이언트는 [docs/CLIENTS.md](docs/CLIENTS.md) 참조):

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

### 옵션 4 — TypeScript SDK 예시

[client/example.ts](client/example.ts) 참조.

## 요금제

| 티어 | $ USD | 예시 |
|---|---|---|
| T0 | $0.002 | FX 환율, 단순 원자재 시세 |
| T1 | $0.05 | 산업 분류기, 펜테스트 범위 추정기 |
| T2 | $0.10 | 도메인 기술 지문, 시장 규모 분석 |
| T3 | $0.15 | 공격 표면, SEC 제출 서류, 다국적 제재 |
| T4 | $0.20 | 부동산 딜 스크리너, 임상 증거, KYC |
| T5 | $0.30 | 경쟁 심층 분석(플래그십) |
| T6 | $1.50 | 비동기 배치(대량 KYC, AI 거버넌스 리포트) |

**무료 플랜**: 전 티어 합산 월 100회. 신용카드 불필요.

전체 세부 사항: [docs/PRICING.md](docs/PRICING.md).

## 아키텍처 (개요)

```
에이전트 ─→ mcp.gapup.io  ─→  PM2 클러스터(2 인스턴스, 에이전트 모드는 Cerebras)
                 │              │
                 │              └─→ Fly.io 엣지 레플리카(fra/sin/gru) 글로벌 저지연
                 │
                 └─→ Cloudflare WAF + 속도 제한 + 캐시
```

전체 아키텍처: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## 관찰 가능성

- Sentry(오류 + 성능 + 브레드크럼 + x402 식별)
- LLM 제공자 상태 + 서킷 브레이커 포함 헬스 엔드포인트
- Cloudflare 액세스 로그
- `/__metrics` 엔드포인트(속도 제한 보호)

## 배포 현황

등록된 마켓플레이스:
- **Smithery** — [smithery.ai/servers/gapup-team/gapup-mcp](https://smithery.ai/servers/gapup-team/gapup-mcp)
- 추가 마켓플레이스 연동 중(Glama, PulseMCP, mcp.so, mcp.directory, MCP Registry, Bazaar 예정).

## 라이선스 및 이용

`mcp.gapup.io` 호스팅 API는 [Gapup 이용약관](https://hub.gapup.io/terms)에 따라 제공됩니다.

이 리포지토리의 내용(매니페스트, 문서, SDK 예시)은 [Proprietary](LICENSE) 라이선스입니다 — 코드 재배포·클론·포크는 금지됩니다.

**서버 구현**은 비공개입니다. 이 리포지토리는 투명성, 검색 가능성, 통합 지원만을 목적으로 합니다.

## 지원

- **이메일**: agents@gapup.io
- **Issues**: [GitHub Issues](https://github.com/getgapup/gapup-mcp-public/issues)
- **문서**: [hub.gapup.io/agents-api](https://hub.gapup.io/agents-api)

## 사용 기술

Claude Code · TypeScript · MCP SDK · x402 프로토콜 · Cerebras + Mistral + Anthropic

---

© 2026 Gapup. All rights reserved.
