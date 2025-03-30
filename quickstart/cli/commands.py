"""Command implementations for the QuickStart CLI."""

import argparse
import json
import sys
from pathlib import Path

from ..core.config import ConfigManager
from ..core.project import ProjectManager
from ..templates.base import TemplateRegistry
from ..utils.logging import setup_logging

logger = setup_logging()


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
