# Contributing

Thanks for taking an interest in the Gapup MCP server. This repository hosts
the **public manifests, docs, and client examples**; the server
implementation itself is proprietary and not in this repo. That changes what
kinds of contributions are useful here — please read this before opening an
issue or PR.

## What contributions we welcome

- **Documentation fixes** — typos, broken links, unclear sections in
  [`README.md`](README.md), `docs/`, the i18n READMEs (`README.fr.md`,
  `README.es.md`, …), `CHANGELOG.md`, `SECURITY.md`, `SUPPORT.md`.
- **Client examples** — usage snippets in `client/` for SDKs you use
  (TypeScript, Python, Go, Rust, ...). Keep them runnable end-to-end.
- **Issue reports** — bugs, unexpected behavior, stale data, regressions
  against `https://mcp.gapup.io/mcp`. Use the issue templates.
- **Feature requests** — new expertise tools or new fields on existing
  tools. We fold them into the hosted version; we will not accept PRs
  that change tool surface, because the implementation is upstream.
- **Translations** — corrections to existing i18n READMEs, or a new
  language we don't ship yet. Keep the structure of `README.md` 1:1.

## What contributions we cannot accept

- **Server implementation changes** — the runtime is closed-source. Open a
  feature request describing the behavior you want; we ship the change.
- **New tools as code** — same reason. Describe the tool you need, we
  scaffold it on our side.
- **Forks of the manifest claiming feature parity** — `server.json` is the
  canonical contract for the hosted endpoint; a forked manifest pointing
  at a different endpoint creates user confusion. Build your own MCP server
  and list it separately instead.

## How to propose a change

1. **Open an issue first** for anything non-trivial. It's cheaper than a
   rejected PR and lets us catch scope mismatches early.
2. **Fork → branch → PR** for docs and examples. One logical change per PR.
3. **Match the existing tone and formatting**. We use sentence case in
   headings, fenced code blocks with explicit languages, and avoid emojis
   in technical docs.
4. **Update the relevant i18n READMEs** when you change `README.md` in a
   way that affects content (not just typos). Linking to the source change
   is acceptable if you don't speak the target language.
5. **Sign your commits** is appreciated but not required.

## Commit messages

We use [Conventional Commits](https://www.conventionalcommits.org/) for the
type prefix. Examples:

```
docs: clarify x402 settlement timing in PRICING.md
fix(readme): typo "agnet" → "agent"
chore(i18n): re-translate hero paragraph in README.de.md
```

Keep the subject line ≤ 72 characters. Wrap the body at 80.

## Security reports

**Do not open a public issue for security vulnerabilities.** See
[SECURITY.md](SECURITY.md) — email `agents@gapup.io` with subject
`[SECURITY] <brief description>`.

## Code of Conduct

Participation in this project is subject to
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Be respectful.

## Questions

For questions that are not bugs and not feature requests, see
[SUPPORT.md](SUPPORT.md) for the right channel.
