.PHONY: install test lint format clean build help

# Python interpreter to use
PYTHON := python3

# Package name
PACKAGE := quickstart

help: ## Show this help message
	@echo 'Usage:'
	@echo '  make <target>'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  %-20s %s\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

install: ## Install the package in development mode
	$(PYTHON) -m pip install -e ".[dev]"

test: ## Run tests
	$(PYTHON) -m pytest tests/ -v

lint: ## Run linters
	$(PYTHON) -m flake8 $(PACKAGE) tests
	$(PYTHON) -m mypy $(PACKAGE)

format: ## Format code using black
	$(PYTHON) -m black $(PACKAGE) tests

clean: ## Clean build artifacts and cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: ## Build the package
	$(PYTHON) -m build

dev-setup: ## Set up development environment
	$(PYTHON) -m venv venv
	. venv/bin/activate && pip install -e ".[dev]"

check: ## Run all checks (lint, format, test)
	make lint
	make format
	make test

# Development workflow
dev: dev-setup ## Set up development environment and run initial checks
	make check
