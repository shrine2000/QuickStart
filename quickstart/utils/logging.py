"""Logging configuration for QuickStart."""

import logging

from rich.logging import RichHandler


def setup_logging(verbose: bool = False, debug: bool = False) -> logging.Logger:
    """Set up logging configuration.

    Args:
        verbose: Whether to enable verbose output.
        debug: Whether to enable debug logging.

    Returns:
        The configured logger instance.
    """
    level = logging.DEBUG if debug else (logging.INFO if verbose else logging.WARNING)

    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )

    return logging.getLogger(__name__)
