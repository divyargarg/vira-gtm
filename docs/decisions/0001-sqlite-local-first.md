# 0001 — SQLite, local-first, real data never committed

- **Status:** accepted
- **Date:** 2026-10-09

## Context

Stage 1 needs one place to store buyers from several sources. The tool is used by one person,
runs on a laptop, and must cost nothing. The repo is public, but the buyer data is business
data and some sources' terms restrict redistribution.

## Options

1. **SQLite file** — zero setup, one file, SQL for dedup queries and views, ships with Python.
   Single writer only.
2. **Postgres (local or free hosted)** — concurrent access, richer types. Needs a server or an
   account; overkill for one user.
3. **CSV/Parquet files + pandas** — simplest to start, but no constraints, joins get awkward, and
   provenance across sources is hard to keep consistent.

## Decision

SQLite at `data/vira.db`. The whole `data/` folder is gitignored. Tests and demos use synthetic
fixtures only. Secrets live in `.env`, also gitignored.

## Why

SQLite gives real tables, constraints and views with no infrastructure, which fits a one-person
tool. Keeping data out of git protects buyer information and avoids redistributing anything a
source's terms forbid, while the code stays fully public.

Revisit if more than one person or process needs to write at the same time (Stage 5 sync jobs
are the likely trigger), or if the data outgrows a single file.
