# Changelog

All notable changes to the Gapup MCP server are documented here.
This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the version numbers in [`server.json`](server.json) /
[`smithery.yaml`](smithery.yaml).

The hosted endpoint is always `https://mcp.gapup.io/mcp`; older versions
are not retained — only the current production deployment is supported.

---

## [Unreleased] — 2026-05-24

### Changed
- **License migrated from Proprietary → MIT** for the public repository contents (manifests, docs, governance, SDK examples, i18n READMEs). The server runtime stays closed-source — only the public surface is now open.
- Updated badge in README + i18n READMEs + `.cursor-plugin/plugin.json`.

### Why
- Cursor Marketplace requires OSI-approved license to list.
- Smithery / Glama / mcpbundles quality scores reward OSI-licensed manifests.
- Public repo contains no proprietary code — MIT is the natural fit.

---

## [0.2.2] — 2026-05-23

### Changed
- Refreshed canonical manifests pushed to the MCP Registry (official `io.github.getgapup/gapup-mcp`).
- Re-broadcast to downstream auto-importers (Glama, PulseMCP, Smithery rescan hook).

### Notes
- No tool surface change vs. 0.2.1 — version bump exists so the Registry pulls the latest description, tags, and capability counts.

## [0.2.1] — 2026-05-22

### Added
- **`audience` parameter** on every expertise tool (Phase 2). `human` keeps the gold-standard Mistral pipeline (~30s, full pedagogy). `agent` switches to Cerebras qwen-3-235b (<5s, JSON-only, no presenter script).
- Granular `competitor-*` decomposition shipped on the hub side (4 new sub-tools — moves, pricing-radar, profiles, recommendations) ahead of agent registration.
- `answersQuestions` field surfaced in tool descriptions so MCP routers can match agent intent without guessing.

### Changed
- Tool count surfaced to listings: **183** (previously 92 → 124 → 155 → 183 as new wrappers were registered).
- Tool wrapper generator now injects `answersQuestions` into the MCP description.

### Fixed
- Smithery scanner mismatch (`/server/` vs `/servers/`) corrected in README + `/agents-api` page.
- Capacity sentinel + circuit-breaker stabilise RAM under the heavier expertise mix.

## [0.2.0] — 2026-05-21

### Added
- Phase 1 async execution + Redis-backed job store for expertise tools (`tool/start` → `tool/poll`).
- Capacity sentinel deployment, per-connector budgets, EU ticker fixes.
- Pricing v3 finalised (T0–T5, T4 PREMIUM $0.08, T5 flagship $0.30) across 130+ tools.
- Telemetry, rate-limit, circuit-breaker and `/health` surface live on `mcp.gapup.io`.

### Changed
- Latency p95 reduced ~50% (60.9s → 30.1s) across heavy tools through per-connector budgets and AICI cache tuning.

## [0.1.0] — 2026-05-14

### Added
- Initial public manifest for `@gapup/mcp-knowledge` scaffold: 5 stdio tools (competitor-intel, trend-watcher, partnership-synergies, pitch-deck-storyline, carbon-footprint-calculator).
- JSON-RPC handshake validated against the MCP reference client.

---

[0.2.2]: https://github.com/getgapup/gapup-mcp-public/releases/tag/v0.2.2
[0.2.1]: https://github.com/getgapup/gapup-mcp-public/releases/tag/v0.2.1
[0.2.0]: https://github.com/getgapup/gapup-mcp-public/releases/tag/v0.2.0
[0.1.0]: https://github.com/getgapup/gapup-mcp-public/releases/tag/v0.1.0
