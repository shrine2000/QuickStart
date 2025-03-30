# flake8: noqa: F401
# mypy: no-warn-return-any
"""Command implementations for the QuickStart CLI."""

import argparse
import json
import sys
from pathlib import Path

import click
from rich.console import Console

from ..core.config import ConfigManager
from ..core.project import ProjectManager
from ..templates import TemplateRegistry
from ..utils.logging import setup_logging

logger = setup_logging()
console = Console()


def create_project(args: argparse.Namespace, config: ConfigManager) -> None:
    """Create a new project."""
    try:
        # Determine project path
        project_path = args.path or config.get("default_project_path")
        project_path = Path(project_path) / args.project_name

        # Determine language
        language = args.language or config.get("default_language")
        template_class = TemplateRegistry.get_template(language)

        if not template_class:
            logger.error(f"Template not found for language: {language}")
            sys.exit(1)

        # Create project configuration
        project_config = {
            "description": args.description or "",
            "language": language,
        }

        # Initialize template
        template = template_class(
            project_name=args.project_name,
            project_path=str(project_path),
            config=project_config,
        )

        # Create project structure
        logger.info(f"Creating {language} project: {args.project_name}")
        template.create_project_structure()
        template.initialize_dependencies()
        template.create_config_files()

        logger.info(f"Project created successfully at: {project_path}")

    except Exception as e:
        logger.error(f"Failed to create project: {str(e)}")
        sys.exit(1)


def handle_config(args: argparse.Namespace, config: ConfigManager) -> None:
    """Handle configuration commands."""
    if args.show:
        print(json.dumps(config.config, indent=4))
    elif args.reset:
        config.reset()
        print("Configuration reset to defaults")


@click.command()
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
def create(project_name: str, template: str, config: str) -> None:
    """Create a new project using the specified template."""
    try:
        # Create project using template
        template_class = TemplateRegistry.get_template(template)
        if not template_class:
            raise click.ClickException(f"Template '{template}' not found")

        # Initialize template
        template_instance = template_class(
            project_name=project_name,
            project_path=project_name,
            config={"description": f"A {template} project named {project_name}"},
        )

        # Create project structure
        template_instance.create_project_structure()
        template_instance.initialize_dependencies()
        template_instance.create_config_files()

        console.print(f"[green]Successfully created project: {project_name}[/green]")
    except Exception as e:
        console.print(f"[red]Error creating project: {str(e)}[/red]")
        raise click.Abort()
