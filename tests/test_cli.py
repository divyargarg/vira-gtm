from typer.testing import CliRunner

from vira_gtm import __version__
from vira_gtm.cli import app

runner = CliRunner()


def test_version_command_prints_version() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_info_command_shows_paths() -> None:
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "database" in result.output
