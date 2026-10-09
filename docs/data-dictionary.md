# Data dictionary

Every table and field in the SQLite database, with its meaning and where it comes from.

> Status: **planned schema** (agreed 2026-10-09). Tables are created in Stage 1, step 2.
> Fields will be finalized and this page updated when the schema is built.

## Overview

The core buyer schema is stored across three tables, so one company can have several contacts and
several sources. The `buyers` view joins them back into the single flat table from the original
spec. See [[architecture]].

## `companies` (planned)

One row per real-world buyer company after deduplication.

| Field | Meaning | Source |
|---|---|---|
| `company` | Display name as first seen | Source export |
| `company_norm` | Normalized name used for matching | Derived ([[architecture#Module map (Stage 1, planned)\|normalize]]) |
| `segment` | `importer`, `hospitality`, or `retail_design` | Adapter or rules |
| `website` | Homepage domain | Source export |
| `city`, `state` | Location (state as 2-letter code) | Source export, normalized |
| `signal` | Human-readable buying signal, e.g. "imported HS 6302 from India 8x in 2025" | Derived per source |
| `first_seen`, `last_seen` | Dates the company first and most recently appeared in an ingestion | Pipeline |

## `contacts` (planned)

| Field | Meaning | Source |
|---|---|---|
| `contact_name`, `contact_role` | Person at the company | Source export only |
| `contact_email` | Email exactly as provided by a source — never guessed | Source export only |
| `email_verified` | Whether the email has been verified | Pipeline (false by default) |
| `source` | Which source supplied this contact | Pipeline |

## `company_sources` (planned)

Provenance: one row per (company, source) pair, so we always know where a buyer came from.

## Supporting tables (planned)

- `ingest_runs` — one row per ingestion (file, file hash, counts) for idempotent re-runs.
- `merge_candidates` — possible duplicates (score 80–92) waiting for manual review.

## `buyers` view (planned)

Flat view matching the original spec: company, segment, website, city, state, source(s), signal,
contact_name, contact_role, contact_email, first_seen, last_seen.
