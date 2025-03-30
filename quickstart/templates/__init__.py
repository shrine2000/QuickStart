"""Template system for project scaffolding."""

from .base import ProjectTemplate, TemplateRegistry
from .python import PythonTemplate

__all__ = ["ProjectTemplate", "TemplateRegistry", "PythonTemplate"]
