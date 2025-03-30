"""Tests for command-line interface."""

from click.testing import CliRunner

from quickstart.cli import setup_parser


def test_cli_commands() -> None:
    """Test CLI command setup."""
    cli = setup_parser()
    assert cli.name == "cli"
    assert "create" in [cmd.name for cmd in cli.commands.values()]


def test_create_command() -> None:
    """Test the create command."""
    runner = CliRunner()
    result = runner.invoke(setup_parser(), ["create", "test-project"])
    assert result.exit_code == 0
    assert "Successfully created project: test-project" in result.output
