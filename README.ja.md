# Gapup MCP

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)

[![smithery badge](https://smithery.ai/badge/gapup-team/gapup-mcp)](https://smithery.ai/servers/gapup-team/gapup-mcp)
[![Tools](https://img.shields.io/badge/tools-271-c9a84c)](https://mcp.gapup.io/health)
[![x402](https://img.shields.io/badge/x402-USDC%2FEURC-c9a84c)](https://x402.org)
[![Free tier](https://img.shields.io/badge/free%20tier-100%20calls%2Fmo-10b981)](https://hub.gapup.io/agents-api/onboard)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**エージェントが支払えるC-suiteナレッジ — 271ツール、x402マイクロ決済、取締役会向けJSON。**

ライブエンドポイント: `https://mcp.gapup.io/mcp`  
無料枠: 100コール/月、クレジットカード不要 → [hub.gapup.io/agents-api/onboard](https://hub.gapup.io/agents-api/onboard)

---

## Gapup MCPとは？

AIエージェント向けに**100以上のビジネス専門ツール**を提供するホスト型[Model Context Protocol](https://modelcontextprotocol.io)サーバーです。各ツールは1〜30秒で、構造化・監査可能・取締役会向けのJSONアウトプットを返します。

[x402](https://x402.org)（Base + Optimism上のUSDC + EURC）によるコール課金。サブスクリプション不要、APIゲートウェイ不要。価格はレスポンスにエンコードされており、エージェントは消費分だけ支払います。

## エージェントが使う理由

- **取締役会向けアウトプット** — Zod型付きJSON、厳格なペルソナ、無駄なチャットなし
- **デュアルオーディエンス形式** — `audience`パラメーターで`human`（Mistralゴールドスタンダード、〜30秒）または`agent`（Cerebras qwen-3-235b、5秒未満）へルーティング
- **ソース明示** — 引用、DOI、エビデンストレイル；ハルシネーションなし
- **EU-firstの強み** — 不動産向けDVF Cerema + Géorisques、制裁向けOFAC + EU + UK + UN + SECO + SEMA + DFAT
- **本物の無料枠** — クレジットカードなしで月100コール、レート制限の裏技なし

## 内容（271ツール）

### C-suiteトップ10専門ツール（最多利用）
- `competitive_intel` — EDGAR + Yahoo + Wayback + Wikipediaのマルチソース詳細分析
- `sec_filing_decoder` — 10-K / 10-Q / 8-K抽出 + KPI変動 + M&Aシグナル
- `sanctions_screener_multi` — 8リスト並列（OFAC + EU + UK + UN + SECO + SEMA + DFAT）+ PEP + 否定的メディア
- `kyc_screener` — 週次更新の6ソースKYC/AML
- `pentest_scope_estimator` — PTESスコープ + 工数・コスト見積り
- `attack_surface_monitor` — パッシブ偵察（crt.sh + DNS + Shodan）+ CVE/EPSS/KEV
- `clinical_evidence_briefer` — PubMed + ClinicalTrials.gov + OpenFDA、GRADEグレード
- `re_deal_screener` — EU-first不動産（DVF Cerema + Géorisques）
- `research_paper_qa` — OpenAlex 4,500万オープンアクセス論文 + Semantic Scholar + CORE、DOI引用
- `industry_classifier_naics_sic` — NAICS + SIC + NACE + GICS + ISIC + HS、階層 + 信頼スコア付き

### カテゴリー（全リストは[docs/API.md](docs/API.md)）
ビジネスインテリジェンス · 金融 · コンプライアンス · 戦略 · 営業 · サステナビリティ · 研究 · 不動産 · ヘルスケア · セキュリティ

## クイックスタート

### オプション1 — ダイレクトHTTP（MCP Streamable HTTP）

```bash
# 無料枠: https://hub.gapup.io/agents-api/onboard でキーを取得
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
        "company_description": "冷凍コンテナを使った海上貨物フォワーダー、EU域内輸送",
        "company_name": "海運フレッシュ"
      }
    }
  }'
```

### オプション2 — Smithery CLI

```bash
npm install -g @smithery/cli
smithery auth login
smithery mcp add gapup-team/gapup-mcp
```

### オプション3 — Claude Desktop / Cursor / Windsurf など

MCPコンフィグに追加（30以上の対応クライアントは[docs/CLIENTS.md](docs/CLIENTS.md)参照）：

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

### オプション4 — TypeScript SDKサンプル

[client/example.ts](client/example.ts)を参照。

## 料金

| ティア | $ USD | 円換算（目安）* | 例 |
|---|---|---|---|
| T0 | $0.002 | 約¥0.3 | FXレート、商品価格の簡易照会 |
| T1 | $0.05 | 約¥7 | 業種分類、ペンテスト範囲見積もり |
| T2 | $0.10 | 約¥15 | ドメインTechフィンガープリント、市場規模 |
| T3 | $0.15 | 約¥22 | アタックサーフェス、SECファイリング、多国籍制裁 |
| T4 | $0.20 | 約¥30 | 不動産スクリーナー、臨床エビデンス、KYC |
| T5 | $0.30 | 約¥45 | 競合詳細分析（フラッグシップ） |
| T6 | $1.50 | 約¥225 | 非同期バッチ（大量KYC、AIガバナンスレポート） |

*1 USD ≈ ¥150 の目安レート。x402決済はUSD建てです。

**無料枠**: 全ティア合計で月100コール。クレジットカード不要。

詳細: [docs/PRICING.md](docs/PRICING.md).

## アーキテクチャ（概要）

```
エージェント ─→ mcp.gapup.io  ─→  PM2クラスター（2インスタンス、エージェントモードはCerebras）
                    │              │
                    │              └─→ Fly.ioエッジ（fra/sin/gru）グローバル低レイテンシ
                    │
                    └─→ Cloudflare WAF + レート制限 + キャッシュ
```

アーキテクチャ詳細: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## オブザーバビリティ

- Sentry（エラー + パフォーマンス + ブレッドクラム + x402識別）
- LLMプロバイダーステータス + サーキットブレーカーを含むヘルスエンドポイント
- Cloudflareアクセスログ
- `/__metrics`エンドポイント（レート制限対応）

## 配信先

- **Smithery** — [smithery.ai/servers/gapup-team/gapup-mcp](https://smithery.ai/servers/gapup-team/gapup-mcp)
- 追加マーケットプレイスも順次掲載予定（Glama、PulseMCP、mcp.so、mcp.directory、MCP Registry、Bazaar近日公開）。

## ライセンス・利用規約

`mcp.gapup.io`のホストAPIは[Gapup利用規約](https://hub.gapup.io/terms)に基づいて提供されます。

このリポジトリの内容（マニフェスト、ドキュメント、SDKサンプル）は[Proprietary](LICENSE)ライセンスです — コードの再配布・クローン・フォークは禁止されています。

**サーバー実装**はプライベートです。このリポジトリは透明性・発見可能性・インテグレーションサポートのためだけに存在します。

## サポート

- **メール**: agents@gapup.io
- **Issues**: [GitHub Issues](https://github.com/getgapup/gapup-mcp-public/issues)
- **ドキュメント**: [hub.gapup.io/agents-api](https://hub.gapup.io/agents-api)

## 使用技術

Claude Code · TypeScript · MCP SDK · x402プロトコル · Cerebras + Mistral + Anthropic

---

© 2026 Gapup. All rights reserved.
