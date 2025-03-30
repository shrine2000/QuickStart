"""Tests for configuration management."""

import json
from pathlib import Path
from typing import Generator

import pytest

from quickstart.core.config import ConfigManager


@pytest.fixture
def config_manager(tmp_path: Path) -> Generator[ConfigManager, None, None]:
    """Create a config manager instance for testing."""
    config_path = tmp_path / "config.json"
    manager = ConfigManager(str(config_path))
    yield manager
    # Cleanup
    if config_path.exists():
        config_path.unlink()


def test_config_creation(tmp_path):
    """Test config creation and default values."""
    config_path = tmp_path / "config.json"
    config = ConfigManager(config_path=str(config_path))

    assert config.get("default_language") == "python"
    assert "default_project_path" in config.config
    assert "git" in config.config
    assert "ide" in config.config


def test_config_save_load(tmp_path):
    """Test config save and load functionality."""
    config_path = tmp_path / "config.json"
    config = ConfigManager(config_path=str(config_path))

    # Set some values
    config.set("test_key", "test_value")

    # Create new config instance to test loading
    new_config = ConfigManager(config_path=str(config_path))
    assert new_config.get("test_key") == "test_value"


def test_config_reset(tmp_path):
    """Test config reset functionality."""
    config_path = tmp_path / "config.json"
    config = ConfigManager(config_path=str(config_path))

    # Set some values
    config.set("test_key", "test_value")

    # Reset config
    config.reset()
    assert config.get("test_key") is None
    assert config.get("default_language") == "python"


def test_load_config(config_manager: ConfigManager) -> None:
    """Test loading configuration from file."""
    test_config = {"test_key": "test_value"}
    with open(config_manager.config_path, "w") as f:
        json.dump(test_config, f)

    config_manager.load_config()
    assert config_manager.get("test_key") == "test_value"


def test_set_config(config_manager: ConfigManager) -> None:
    """Test setting configuration values."""
    config_manager.set("test_key", "test_value")
    assert config_manager.get("test_key") == "test_value"


def test_save_config(config_manager: ConfigManager) -> None:
    """Test saving configuration to file."""
    config_manager.set("test_key", "test_value")
    config_manager.save()

    with open(config_manager.config_path) as f:
        saved_config = json.load(f)
    assert saved_config["test_key"] == "test_value"
