"""Tests for the CLI module."""
import pytest

from quickstart.cli import setup_parser


def test_cli_parser():
    """Test CLI argument parser setup."""
    parser = setup_parser()

    # Test create command
    args = parser.parse_args(["create", "test-project"])
    assert args.command == "create"
    assert args.project_name == "test-project"

    # Test create command with options
    args = parser.parse_args(
        [
            "create",
            "test-project",
            "--language",
            "python",
            "--path",
            "/tmp",
            "--description",
            "Test project",
        ]
    )
    assert args.command == "create"
    assert args.project_name == "test-project"
    assert args.language == "python"
    assert args.path == "/tmp"
    assert args.description == "Test project"

    # Test config command
    args = parser.parse_args(["config", "--show"])
    assert args.command == "config"
    assert args.show is True

    # Test config reset
    args = parser.parse_args(["config", "--reset"])
    assert args.command == "config"
    assert args.reset is True

def test_cli_commands() -> None:
    """Test CLI command setup."""
    cli = setup_parser()
    assert cli.name == "cli"
    assert "create" in [cmd.name for cmd in cli.commands.values()]
