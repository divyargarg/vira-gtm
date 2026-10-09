"""Runtime settings, loaded from environment variables (and .env if present)."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    db_path: Path
    raw_dir: Path


def _resolve(path_str: str) -> Path:
    """Treat relative paths as relative to the project root, not the shell's cwd."""
    path = Path(path_str)
    return path if path.is_absolute() else PROJECT_ROOT / path


def load_settings() -> Settings:
    load_dotenv(PROJECT_ROOT / ".env")
    return Settings(
        db_path=_resolve(os.getenv("VIRA_DB_PATH", "data/vira.db")),
        raw_dir=_resolve(os.getenv("VIRA_RAW_DIR", "data/raw")),
    )
