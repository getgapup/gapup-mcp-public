# Security Policy

## Supported Versions

Only the currently deployed version of the Gapup MCP server is actively supported.

| Version | Supported |
|---------|-----------|
| 0.2.x (latest) | Yes |
| < 0.2.0 | No |

The server implementation is hosted and managed by Gapup. There is no self-hosted option for the server. This repository contains manifests, documentation, and SDK examples only.

## Reporting a Vulnerability

**Please do not open a public GitHub issue for security vulnerabilities.**

Report security issues by emailing **agents@gapup.io** with the subject line:

```
[SECURITY] <brief description>
```

If you believe the issue is critical or involves active exploitation, please mark the subject as `[SECURITY CRITICAL]`.

### What to include

- Description of the vulnerability and its potential impact
- Steps to reproduce (curl commands, tool names, payloads)
- Whether you believe the issue is exploitable in the current production environment (`mcp.gapup.io`)
- Any suggested mitigation

### Response timeline

| Severity | Initial acknowledgement | Fix or workaround | Public disclosure |
|----------|------------------------|-------------------|-------------------|
| Critical | < 8 hours | < 7 days | 90 days after fix |
| High | < 24 hours | < 14 days | 90 days after fix |
| Medium | < 48 hours | < 30 days | 90 days after fix |
| Low | < 5 business days | Next release cycle | At our discretion |

We follow responsible disclosure. If you need more than 90 days to coordinate disclosure on your end, reach out and we will work with you.

## Scope

In scope:
- Authentication bypass or API key leakage
- x402 payment flow manipulation (double-spend, price tampering)
- Data exfiltration from tool outputs (PII leaks, OFAC list content injection)
- Rate-limit bypass or denial-of-service at the application layer
- Prompt injection leading to unexpected data disclosure
- WAF bypass leading to internal endpoint access

Out of scope:
- Vulnerabilities in third-party services (Cloudflare, Fly.io, Supabase, Sentry) — report those to the respective vendors
- Social engineering attacks on Gapup team members
- Physical security
- Denial of service via volumetric traffic (contact Cloudflare)
- Issues requiring physical access to infrastructure

## Hall of Fame

We gratefully acknowledge security researchers who responsibly disclose vulnerabilities. Confirmed valid reports will be credited here (with your permission).

*No reports yet — be the first.*

## PGP Key

A PGP key for encrypted communication will be published at [keys.openpgp.org](https://keys.openpgp.org) by Q1 2027. Until then, use the email address above; TLS in transit provides baseline confidentiality for non-critical reports.

## Bug Bounty

We do not currently operate a formal bug bounty program. Researchers who identify significant vulnerabilities may be recognized publicly and/or offered complimentary API credits at our discretion.
