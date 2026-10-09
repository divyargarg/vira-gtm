# data/

Local-only working data. Everything in this folder except this README is gitignored.

- `raw/` — source exports you drop in for ingestion (one subfolder per source is fine).
- `vira.db` — the SQLite database the pipeline builds.

Real buyer data never goes into the public repo. Tests use synthetic fixtures in `tests/fixtures/`.
