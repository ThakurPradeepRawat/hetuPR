# Contributing to HetuPR

Thanks for your interest in contributing! This guide explains how to get involved.

By participating, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to Contribute

- Report bugs or false positives/negatives in reviews
- Suggest features or improvements
- Improve documentation
- Add tests or evaluation datasets
- Fix issues labeled `good first issue` or `help wanted`

## Before You Start

- Search existing [issues](https://github.com/ThakurPradeepRawat/hetuPR/issues) and PRs to avoid duplicates.
- For significant changes, open an issue to discuss the approach first.
- **Security vulnerabilities:** do not open a public issue. See [SECURITY.md](SECURITY.md).

## Development Setup

```bash
git clone https://github.com/ThakurPradeepRawat/hetuPR.git
cd hetupr
cp .env.example .env          # fill in your own values
docker compose -f infra/docker-compose.prod.yml up --build -d
docker compose exec backend alembic upgrade head
```

For backend-only work:

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Workflow

1. Fork the repository and create a branch: `git checkout -b feat/short-description`
2. Make focused changes with clear commits.
3. Add or update tests for behavior changes.
4. Run checks:
   ```bash
   ruff check backend/
   pytest backend/tests/ -v
   ```
5. Push and open a Pull Request describing **what changed, why, and how you verified it**.

## Commit Messages

We recommend [Conventional Commits](https://www.conventionalcommits.org/):
`feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`

## Code Style

- Python: formatted and linted with Ruff; type hints encouraged.
- Keep functions small and async-safe (no blocking I/O in async paths).
- Never log secrets, tokens, or raw source code.

## Reporting AI Review Issues

Include a **minimal, sanitized** code example, the expected finding, the actual finding, and steps to reproduce. Do not post credentials or proprietary code.

## Pull Request Checklist

- [ ] Tests added/updated and passing
- [ ] `ruff check` passes
- [ ] Docs updated if behavior or config changed
- [ ] No secrets or private keys committed
- [ ] PR description explains the change and verification

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
