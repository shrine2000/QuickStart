"""Configuration management for QuickStart."""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional


class ConfigManager:
    """Manages configuration for QuickStart projects."""

    DEFAULT_CONFIG = {
        "default_language": "python",
        "default_project_path": str(Path.home() / "Projects"),
        "git": {
            "user_name": "",
            "user_email": "",
        },
        "ide": {
            "vscode": True,
        },
    }

    def __init__(self, config_path: Optional[str] = None):
        """Initialize the configuration manager.

        Args:
            config_path: Optional path to a configuration file.
        """
        self.config_path = config_path or str(
            Path.home() / ".quickstart" / "config.json"
        )
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default."""
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            if os.path.exists(self.config_path):
                with open(self.config_path, "r") as f:
                    return {**self.DEFAULT_CONFIG, **json.load(f)}
            else:
                self._save_config(self.DEFAULT_CONFIG)
                return self.DEFAULT_CONFIG
        except Exception as e:
            print(f"Error loading config: {str(e)}")
            return self.DEFAULT_CONFIG

    def _save_config(self, config: Dict[str, Any]) -> None:
        """Save configuration to file."""
        try:
            with open(self.config_path, "w") as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {str(e)}")

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value.

        Args:
            key: Configuration key to look up.
            default: Default value if key is not found.

        Returns:
            The configuration value or default.
        """
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value.

        Args:
            key: Configuration key to set.
            value: Value to set for the key.
        """
        self.config[key] = value
        self._save_config(self.config)

    def update(self, updates: Dict[str, Any]) -> None:
        """Update multiple configuration values."""
        self.config.update(updates)
        self._save_config(self.config)

    def reset(self) -> None:
        """Reset configuration to defaults."""
        self.config = self.DEFAULT_CONFIG.copy()
        self._save_config(self.config)

    def load_config(self) -> None:
        """Load configuration from file if it exists."""
        if self.config_path and os.path.exists(self.config_path):
            with open(self.config_path) as f:
                self.config = json.load(f)

    def save(self) -> None:
        """Save configuration to file if path is set."""
        if self.config_path:
            with open(self.config_path, "w") as f:
                json.dump(self.config, f, indent=2)
