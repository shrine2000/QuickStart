"""Tests for project management functionality."""

from pathlib import Path
from typing import Generator

import pytest

from quickstart.core.project import ProjectManager


@pytest.fixture
def project_manager() -> Generator[ProjectManager, None, None]:
    """Create a project manager instance for testing."""
    manager = ProjectManager("test_project", "python")
    yield manager
    # Cleanup
    if Path("test_project").exists():
        import shutil

        shutil.rmtree("test_project")


def test_create_project(project_manager: ProjectManager) -> None:
    """Test project creation."""
    project_manager.create()
    assert Path("test_project").exists()
    assert (Path("test_project") / "test_project").exists()
    assert (Path("test_project") / "tests").exists()
    assert (Path("test_project") / "docs").exists()
