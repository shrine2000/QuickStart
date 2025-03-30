"""Python project template."""

from pathlib import Path

from .base import ProjectTemplate, TemplateRegistry

class PythonTemplate(ProjectTemplate):
    """Template for Python projects."""

    def create_project_structure(self) -> None:
        """Create the Python project structure."""
        # Create main package directory
        package_dir = Path(self.project_path) / self.project_name
        self.create_directory(package_dir)

        # Create __init__.py
        self.create_file(
            package_dir / "__init__.py",
            f'"""Main package for {self.project_name}."""\n\n__version__ = "0.1.0"\n'
        )

        # Create test directory
        test_dir = Path(self.project_path) / "tests"
        self.create_directory(test_dir)
        self.create_file(
            test_dir / "__init__.py",
            f'"""Tests for {self.project_name}."""\n'
        )

        # Create test_app.py
        test_app_content = (
            f'"""Tests for the main application module."""\n\n'
            f"import pytest\n"
            f"from {self.project_name}.app import main\n\n"
            f"def test_main(capsys):\n"
            f'    """Test the main function."""\n'
            f"    main()\n"
            f"    captured = capsys.readouterr()\n"
            f'    assert captured.out == "Hello from {self.project_name}!\\n"\n'
        )
        self.create_file(
            test_dir / "test_app.py",
            test_app_content
        )

        # Create docs directory
        docs_dir = Path(self.project_path) / "docs"
        self.create_directory(docs_dir)

        # Create app.py in the main package
        app_content = (
            f'"""Main application module for {self.project_name}."""\n\n'
            f"def main():\n"
            f'    """Main entry point for the application."""\n'
            f'    print("Hello from {self.project_name}!")\n\n'
            f'if __name__ == "__main__":\n'
            f"    main()\n"
        )
        self.create_file(
            package_dir / "app.py",
            app_content
        )

    def initialize_dependencies(self) -> None:
        """Initialize Python project dependencies."""
        # Create requirements.txt
        requirements = [
            "# Project dependencies",
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.900",
        ]
        self.create_file(
            Path(self.project_path) / "requirements.txt",
            "\n".join(requirements) + "\n"
        )

        # Create setup.py
        setup_content = (
            f'"""Setup configuration for {self.project_name}."""\n\n'
            f"from setuptools import setup, find_packages\n\n"
            f"setup(\n"
            f'    name="{self.project_name}",\n'
            f"    version=\"0.1.0\",\n"
            f"    packages=find_packages(),\n"
            f"    install_requires=[],\n"
            f'    python_requires=">=3.8",\n'
            f"    entry_points={{\n"
            f"        \"console_scripts\": [\n"
            f'            "{self.project_name}={self.project_name}.app:main",\n'
            f"        ],\n"
            f"    }},\n"
            f")\n"
        )
        self.create_file(
            Path(self.project_path) / "setup.py",
            setup_content
        )

    def create_config_files(self) -> None:
        """Create configuration files for the project."""
        # Create .gitignore
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Testing
.coverage
htmlcov/
.pytest_cache/
"""
        self.create_file(
            Path(self.project_path) / ".gitignore",
            gitignore_content
        )

        # Create README.md
        readme_content = (
            f"# {self.project_name}\n\n"
            f"{self.config.get('description', 'A Python project.')}\n\n"
            f"## Installation\n\n"
            f"```bash\n"
            f"pip install -e .\n"
            f"```\n\n"
            f"## Development\n\n"
            f"```bash\n"
            f"# Install development dependencies\n"
            f"pip install -r requirements.txt\n\n"
            f"# Run tests\n"
            f"pytest\n\n"
            f"# Format code\n"
            f"black .\n"
            f"```\n\n"
            f"## Usage\n\n"
            f"```bash\n"
            f"# Run the application\n"
            f"{self.project_name}\n"
            f"```\n\n"
            f"## License\n\n"
            f"MIT\n"
        )
        self.create_file(
            Path(self.project_path) / "README.md",
            readme_content
        )

# Register the template
TemplateRegistry.register("python", PythonTemplate)
