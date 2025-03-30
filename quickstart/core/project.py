"""Project management functionality for QuickStart."""

import logging
import os
import subprocess
from pathlib import Path
from typing import Dict, Any

from .config import ConfigManager
from ..templates import TemplateRegistry

logger = logging.getLogger(__name__)

class ProjectManager:
    """Manages project creation and initialization."""

    def __init__(
        self,
        project_name: str,
        template: str,
        config_path: str = None,
    ) -> None:
        """Initialize the project manager.

        Args:
            project_name: Name of the project to create.
            template: Template to use for project creation.
            config_path: Optional path to configuration file.
        """
        self.project_name = project_name
        self.template = template
        self.config = ConfigManager(config_path)
        self.project_path = Path.cwd() / project_name

    def create(self) -> None:
        """Create a new project using the specified template."""
        try:
            # Get template class
            template_class = TemplateRegistry.get_template(self.template)
            if not template_class:
                raise ValueError(f"Template '{self.template}' not found")

            # Create project directory
            self.project_path.mkdir(parents=True, exist_ok=True)

            # Initialize template
            template_instance = template_class(
                project_name=self.project_name,
                project_path=str(self.project_path),
                config=self.config.config,
            )

            # Create project structure
            template_instance.create_project_structure()
            template_instance.initialize_dependencies()
            template_instance.create_config_files()

            logger.info(f"Successfully created project: {self.project_name}")
        except Exception as e:
            logger.error(f"Failed to create project: {str(e)}")
            raise

    def create_project(self) -> None:
        """Create the project structure."""
        self._create_directories()
        self._initialize_git()

    def _create_directories(self) -> None:
        """Create project directories."""
        self.project_path.mkdir(parents=True, exist_ok=True)

    def _initialize_git(self) -> None:
        """Initialize git repository."""
        try:
            subprocess.run(["git", "init"], cwd=self.project_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error initializing git repository: {str(e)}")

    def open_in_vscode(self) -> None:
        """Open project in VS Code."""
        try:
            subprocess.run(["code", str(self.project_path)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error opening VS Code: {str(e)}")

    def create_file(self, filename: str, content: str) -> None:
        """Create a file with the given content."""
        file_path = self.project_path / filename
        file_path.write_text(content)
