# vira-gtm

A go-to-market engineering system for **VIRA Home**, a B2B importer of home textiles made in India, and sold to US buyers.

The system is built in six stages:

**Find buyers → Enrich → Score → Personalize → Review & send → Track & learn**

It is both a working tool for a real business and a public portfolio project, so the reasoning behind each choice is documented alongside the code (see [docs/](docs/index.md)).

## Status

| Stage | State |
|---|---|
| 1. Find buyers | 🚧 In progress — project scaffold done |
| 2–6 | Not started |

## What Stage 1 does (when complete)

Collects potential buyers from multiple sources (CSV exports in v1) into one clean, deduplicated SQLite table, across three segments:

1. US importers of Indian home textiles (HS 6301, 6302, 6304)
2. Boutique hotels and hospitality groups
3. Independent home décor retailers and interior designers

## Setup

Requires [uv](https://docs.astral.sh/uv/) (it installs Python 3.12 for you).

```bash
git clone https://github.com/divyargarg/vira-gtm.git
cd vira-gtm
uv sync                  # creates .venv and installs dependencies
cp .env.example .env     # then edit if you want non-default paths
```

## Usage

```bash
uv run vira --help       # list commands
uv run vira info         # show resolved database and raw-data paths
```

Ingestion commands (`vira ingest`, `vira summary`, `vira review`) arrive later in Stage 1.

## Development

```bash
uv run pytest            # tests
uv run ruff check .      # lint
uv run ruff format .     # format
```

Conventions for contributors (human or AI) are in [CLAUDE.md](CLAUDE.md).

## Data and privacy

Real buyer data never enters this repository. Source exports and the database live in `data/`, which is gitignored; tests use synthetic fixtures. See [ADR-0001](docs/decisions/0001-sqlite-local-first.md).

## Documentation

`docs/` is an Obsidian vault. Start at [docs/index.md](docs/index.md).
