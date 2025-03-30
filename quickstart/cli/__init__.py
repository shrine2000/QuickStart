"""Command-line interface for the QuickStart tool."""

import logging
from typing import Optional

import click
from rich.console import Console
from rich.logging import RichHandler

from ..core.project import ProjectManager
from ..templates import TemplateRegistry
from ..utils.logging import setup_logging

# Set up logging
logger = logging.getLogger(__name__)
console = Console()

def setup_parser() -> click.Group:
    """Set up the command-line argument parser.

    Returns:
        A Click command group that serves as the entry point for the CLI.
    """
    @click.group()
    @click.option(
        "--verbose",
        "-v",
        is_flag=True,
        help="Enable verbose output",
    )
    @click.option(
        "--debug",
        "-d",
        is_flag=True,
        help="Enable debug logging",
    )
    def cli(verbose: bool, debug: bool) -> None:
        """QuickStart - A tool for scaffolding new project structures."""
        setup_logging(verbose, debug)

    @cli.command()
    @click.argument("project_name")
    @click.option(
        "--template",
        "-t",
        type=click.Choice(TemplateRegistry.list_templates()),
        default="python",
        help="Project template to use",
    )
    @click.option(
        "--config",
        "-c",
        type=click.Path(exists=True),
        help="Path to configuration file",
    )
    def create(project_name: str, template: str, config: Optional[str]) -> None:
        """Create a new project using the specified template."""
        try:
            project = ProjectManager(project_name, template, config)
            project.create()
            console.print(f"[green]Successfully created project: {project_name}[/green]")
        except Exception as e:
            console.print(f"[red]Error creating project: {str(e)}[/red]")
            raise click.Abort()

    return cli

def main() -> None:
    """Entry point for the CLI."""
    cli = setup_parser()
    cli()
