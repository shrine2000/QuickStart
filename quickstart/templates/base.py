"""Base classes for project templates."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional, Type


class ProjectTemplate(ABC):
    """Base class for project templates."""

    def __init__(
        self,
        project_name: str,
        project_path: str,
        config: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize the template.

        Args:
            project_name: Name of the project
            project_path: Path where the project should be created
            config: Optional configuration dictionary
        """
        self.project_name = project_name
        self.project_path = project_path
        self.config = config or {}

    @abstractmethod
    def create_project_structure(self) -> None:
        """Create the basic project structure."""
        pass

    @abstractmethod
    def initialize_dependencies(self) -> None:
        """Initialize project dependencies."""
        pass

    @abstractmethod
    def create_config_files(self) -> None:
        """Create configuration files for the project."""
        pass

    def create_directory(self, path: Path) -> None:
        """Create a directory if it doesn't exist.

        Args:
            path: Path to create
        """
        path.mkdir(parents=True, exist_ok=True)

    def create_file(self, path: Path, content: str) -> None:
        """Create a file with the given content.

        Args:
            path: Path to create
            content: Content to write to the file
        """
        path.write_text(content)


class TemplateRegistry:
    """Registry for project templates."""

    _templates: Dict[str, Type[ProjectTemplate]] = {}

    @classmethod
    def register(cls, name: str, template_class: Type[ProjectTemplate]) -> None:
        """Register a template class.

        Args:
            name: Name of the template
            template_class: Template class to register
        """
        cls._templates[name] = template_class

    @classmethod
    def get_template(cls, name: str) -> Optional[Type[ProjectTemplate]]:
        """Get a template class by name.

        Args:
            name: Name of the template

        Returns:
            Template class if found, None otherwise
        """
        return cls._templates.get(name)

    @classmethod
    def list_templates(cls) -> List[str]:
        """List all registered template names.

        Returns:
            List of template names
        """
        return list(cls._templates.keys())
