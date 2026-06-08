# Gapup MCP

[English](README.md) · [Français](README.fr.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [中文](README.zh-CN.md) · [한국어](README.ko.md) · [Português (BR)](README.pt-BR.md)

[![smithery badge](https://smithery.ai/badge/gapup-team/gapup-mcp)](https://smithery.ai/servers/gapup-team/gapup-mcp)
[![Tools](https://img.shields.io/badge/tools-271-c9a84c)](https://mcp.gapup.io/health)
[![x402](https://img.shields.io/badge/x402-USDC%2FEURC-c9a84c)](https://x402.org)
[![Free tier](https://img.shields.io/badge/free%20tier-100%20calls%2Fmo-10b981)](https://hub.gapup.io/agents-api/onboard)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**智能体可直接付费的 C-suite 知识库 — 271 个工具，x402 微支付，董事会级 JSON 输出。**

线上端点：`https://mcp.gapup.io/mcp`  
免费配额：每月 100 次调用，无需信用卡 → [hub.gapup.io/agents-api/onboard](https://hub.gapup.io/agents-api/onboard)

---

## 什么是 Gapup MCP？

一个托管式 [Model Context Protocol](https://modelcontextprotocol.io) 服务器，为 AI 智能体提供 **100+ 项商业专业工具**。每个工具在 1~30 秒内返回结构化、可审计、董事会级别的 JSON 交付物。

通过 [x402](https://x402.org) 按调用付费（Base + Optimism 上的 USDC + EURC）。无需订阅，无需 API 网关。价格已编码在响应中——智能体按消耗量付费。

## 为什么智能体选择它

- **董事会级输出** — Zod 类型化 JSON，严格角色设定，无废话
- **双受众格式** — `audience` 参数路由至 `human`（Mistral 黄金标准，约 30 秒）或 `agent`（Cerebras qwen-3-235b，<5 秒）
- **来源可追溯** — 引用、DOI、证据链；无幻觉
- **欧盟优先护城河** — DVF Cerema + Géorisques（房产）；OFAC + EU + UK + UN + SECO + SEMA + DFAT（制裁）
- **真实免费配额** — 无需信用卡即可每月 100 次调用，无速率限制把戏

## 工具清单（271 个）

### C-suite 十大专业工具（使用频率最高）
- `competitive_intel` — EDGAR + Yahoo + Wayback + Wikipedia 多来源深度分析
- `sec_filing_decoder` — 10-K / 10-Q / 8-K 提取 + KPI 变动 + 并购信号
- `sanctions_screener_multi` — 8 个列表并行扫描（OFAC + EU + UK + UN + SECO + SEMA + DFAT）+ PEP + 负面媒体
- `kyc_screener` — 每周刷新的 6 源 KYC/AML
- `pentest_scope_estimator` — PTES 范围 + 工作量/成本区间
- `attack_surface_monitor` — 被动侦察（crt.sh + DNS + Shodan）+ CVE/EPSS/KEV
- `clinical_evidence_briefer` — PubMed + ClinicalTrials.gov + OpenFDA，GRADE 分级
- `re_deal_screener` — 欧盟优先房产（DVF Cerema + Géorisques）
- `research_paper_qa` — OpenAlex 4500 万开放获取论文 + Semantic Scholar + CORE，DOI 引用
- `industry_classifier_naics_sic` — NAICS + SIC + NACE + GICS + ISIC + HS，含层级与置信度

### 分类（完整列表见 [docs/API.md](docs/API.md)）
商业智能 · 金融 · 合规 · 战略 · 销售 · 可持续发展 · 研究 · 房地产 · 医疗健康 · 安全

## 快速开始

### 方式一 — 直接 HTTP（MCP Streamable HTTP）

```bash
# 免费配额：在 https://hub.gapup.io/agents-api/onboard 获取密钥
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
        "company_description": "冷链海运货运代理，欧盟内冷藏集装箱运输",
        "company_name": "海洋鲜 (HaiyangXian)"
      }
    }
  }'
```

### 方式二 — Smithery CLI

```bash
npm install -g @smithery/cli
smithery auth login
smithery mcp add gapup-team/gapup-mcp
```

### 方式三 — Claude Desktop / Cursor / Windsurf 等

在 MCP 配置文件中添加（30+ 支持客户端见 [docs/CLIENTS.md](docs/CLIENTS.md)）：

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

### 方式四 — TypeScript SDK 示例

参见 [client/example.ts](client/example.ts)。

## 定价

| 档位 | $ USD | 人民币参考* | 示例 |
|---|---|---|---|
| T0 | $0.002 | 约 ¥0.01 | 汇率查询、大宗商品报价 |
| T1 | $0.05 | 约 ¥0.36 | 行业分类、渗透测试范围估算 |
| T2 | $0.10 | 约 ¥0.73 | 域名技术指纹、市场规模 |
| T3 | $0.15 | 约 ¥1.09 | 攻击面、SEC 申报、多司法区制裁 |
| T4 | $0.20 | 约 ¥1.45 | 房产筛选、临床证据、KYC |
| T5 | $0.30 | 约 ¥2.18 | 竞争对手深度分析（旗舰） |
| T6 | $1.50 | 约 ¥10.9 | 异步批量（批量 KYC、AI 治理报告） |

*汇率仅供参考（约 1 USD = 7.26 CNY）。x402 支付以美元计价。

**免费配额**：所有档位合计每月 100 次调用，无需信用卡。

完整详情：[docs/PRICING.md](docs/PRICING.md)。

## 架构（高层次概览）

```
智能体 ─→ mcp.gapup.io  ─→  PM2 集群（2 实例，智能体模式由 Cerebras 驱动）
               │              │
               │              └─→ Fly.io 边缘副本（fra/sin/gru）全球低延迟
               │
               └─→ Cloudflare WAF + 速率限制 + 缓存
```

完整架构：[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。

## 可观测性

- Sentry（错误 + 性能 + 面包屑 + x402 调用者识别）
- 健康端点，包含 LLM 提供者状态 + 熔断器
- Cloudflare 访问日志
- `/__metrics` 端点（速率限制保护）

## 分发渠道

已上架：
- **Smithery** — [smithery.ai/servers/gapup-team/gapup-mcp](https://smithery.ai/servers/gapup-team/gapup-mcp)
- 更多市场持续接入中（Glama、PulseMCP、mcp.so、mcp.directory、MCP Registry、Bazaar 即将上线）。

## 许可证与使用

`mcp.gapup.io` 托管 API 依据 [Gapup 服务条款](https://hub.gapup.io/terms) 提供。

本仓库内容（清单、文档、SDK 示例）采用[MIT证](LICENSE)——禁止对本代码进行再分发、克隆或 Fork。

**服务器实现**为私有。本仓库仅为透明度、可发现性与集成支持而存在。

## 支持

- **邮箱**：agents@gapup.io
- **Issues**：[GitHub Issues](https://github.com/getgapup/gapup-mcp-public/issues)
- **文档**：[hub.gapup.io/agents-api](https://hub.gapup.io/agents-api)

## 技术栈

Claude Code · TypeScript · MCP SDK · x402 协议 · Cerebras + Mistral + Anthropic

---

© 2026 Gapup. 保留所有权利。
