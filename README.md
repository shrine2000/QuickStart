# QuickStart

A powerful CLI tool for quickly scaffolding new project structures with best practices.

## Features

- Create new projects with predefined templates
- Configurable project structure
- Git integration
- IDE setup (VS Code)
- Virtual environment setup for Python projects
- Extensible template system


## Usage

### Basic Usage

```bash
# Create a new Python project
qs create my-project

# Create a project with specific language
qs create -l python my-project

# Create a project with description
qs create -d "My awesome project" my-project

# Create a project in a specific directory
qs create -p /path/to/projects my-project
```

### Configuration

```bash
# Show current configuration
qs config --show

# Reset configuration to defaults
qs config --reset
```

## Available Templates

### Python Template
- Standard Python package structure
- Virtual environment setup
- Test directory with pytest configuration
- Development tools (black, flake8)
- Git configuration
- VS Code integration

## Configuration

The configuration file is stored at `~/.quickstart/config.json` and includes:

- Default project path
- Default programming language
- Git user settings
- IDE preferences

## Development

### Using Make

The project includes a Makefile for common development tasks:

```bash
# Show available commands
make help

# Set up development environment
make dev-setup

# Run tests
make test

# Run linters
make lint

# Format code
make format

# Clean build artifacts
make clean

# Build package
make build

# Run all checks
make check
```

### Development Workflow

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quickstart.git
   cd quickstart
   ```

2. Set up development environment:
   ```bash
   make dev-setup
   ```

3. Run initial checks:
   ```bash
   make check
   ```

4. Start development!

### Code Style

The project uses several tools to maintain code quality:

- `black` for code formatting
- `flake8` for linting
- `mypy` for type checking
- `pytest` for testing

Run all checks with:
```bash
make check
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
