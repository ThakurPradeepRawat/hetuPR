# Security Policy

HetuPR handles webhooks, GitHub credentials, and source-code context, so we take security seriously.

## Supported Versions

| Version | Supported |
|---|---|
| `main` (latest) | ✅ |
| Older releases | ❌ |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, either:

- Use GitHub's [private vulnerability reporting](https://github.com/ThakurPradeepRawat/hetuPR/security/advisories/new), or
- Email **p.s.rawat4458@gmail.com** with the subject `HetuPR Security`.

Please include:

- A description of the issue and its impact
- Steps to reproduce (a minimal proof of concept if possible)
- Affected version/commit and configuration
- Any suggested mitigation

## What to Expect

- Acknowledgement within **72 hours**
- An initial assessment within **7 days**
- Coordinated disclosure: we will work with you on a fix and credit you in the release notes unless you prefer to stay anonymous

## Scope Notes

Areas of particular interest: webhook signature verification, GitHub token handling, prompt injection via PR content, secret leakage in logs, SSRF, and SQL injection.

## For Self-Hosters

- Never commit `.env` files or GitHub App private keys.
- Rotate the webhook secret and private key if you suspect exposure.
- Use least-privilege GitHub App permissions and keep dependencies updated.
