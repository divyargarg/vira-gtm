"""Command-line entry point: `uv run vira --help`."""

from __future__ import annotations

import typer

from vira_gtm import __version__
from vira_gtm.config import load_settings

app = typer.Typer(help="VIRA Home GTM pipeline.", no_args_is_help=True)


@app.command()
def version() -> None:
    """Print the package version."""
    typer.echo(f"vira-gtm {__version__}")


@app.command()
def info() -> None:
    """Show the resolved configuration (database and raw-data paths)."""
    settings = load_settings()
    typer.echo(f"database : {settings.db_path}")
    typer.echo(f"raw data : {settings.raw_dir}")


if __name__ == "__main__":
    app()
