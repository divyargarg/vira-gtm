# CLAUDE.md — project conventions

Read this before working on the repo. It keeps every session consistent.

## Project

GTM pipeline for VIRA Home (B2B home textiles, imported from India, sold to US buyers).
Six stages: Find buyers → Enrich → Score → Personalize → Review & send → Track & learn.
Current stage and status: see `docs/architecture.md` and the latest `docs/devlog/` entry.

## Roles

- Divya is the tech lead. Flag trade-offs and let her decide anything significant
  (schema, dependencies, thresholds, data sources, anything touching a third party's terms).
- Explain key design decisions briefly as you go. This is a learning and portfolio project.

## Stack

- Python 3.12, uv, SQLite, pandas, rapidfuzz, typer, pytest, ruff.
- Free tools only. The Claude API is the one planned paid dependency (Stage 4).
- Add a dependency only with a reason, recorded in the commit message or an ADR.

## Code conventions

- `src/` layout, package `vira_gtm`. Small modules, one responsibility each.
- Type hints on all functions. `from __future__ import annotations` at the top of modules.
- Pure functions for normalization and matching so they are easy to test.
- Source-specific code lives only in `sources/<name>.py`. Everything downstream works on the
  canonical `BuyerRecord`.
- Line length 100. `uv run ruff check . && uv run ruff format .` must pass before commit.
- Tests in `tests/`, named `test_<module>.py`. Normalization and dedup logic must have tests.

## Data rules

- Never commit real buyer data, source exports, or the database. `data/` is gitignored.
- Test fixtures are synthetic. Do not paste real company or contact rows into tests or docs.
- Never guess or pattern-generate contact emails. Store only emails a source provides, with
  provenance and an `email_verified` flag.
- Respect each source's terms of service. No scraping in v1. Check a source's terms before
  writing its adapter and record the finding in an ADR.

## Git workflow

- Branch per change: `feat/…`, `fix/…`, `docs/…`, `chore/…`. Never commit directly to `main`.
- Open a PR for each branch. Do not merge — Divya reviews and merges.
- Small commits with clear messages in imperative mood (`Add company name normalizer`).
- Secrets only in `.env` (gitignored). Keep `.env.example` in sync when adding settings.

## Documentation (update as you go, not at the end)

`docs/` is an Obsidian vault: plain markdown, `[[wikilinks]]` between docs.

- `docs/architecture.md` — stages, what is built, mermaid data-flow diagram.
- `docs/decisions/NNNN-title.md` — one ADR per significant choice (copy `_template.md`).
- `docs/data-dictionary.md` — every table and field: meaning and source.
- `docs/devlog/YYYY-MM-DD.md` — per session: what we did, what broke, what's next.
- `docs/posts/` — LinkedIn post drafts about findings or lessons.
- `README.md` — keep setup and usage accurate when commands change.

End every session by updating the devlog and suggesting the next step.
