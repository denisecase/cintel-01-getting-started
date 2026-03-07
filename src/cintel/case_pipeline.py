"""
case_pipeline.py - Project script (starter).

Author: Your Name
Date: 2026-03-

Purpose:
  Confirm your project environment is set up correctly.
  Run this script to see a log message in the terminal.

Run as a Module:
  uv run python -m cintel.case_pipeline
"""

# === DECLARE IMPORTS ===

import logging
from pathlib import Path

from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("CI", level="DEBUG")

# === DEFINE GLOBAL PATHS ===

ROOT_PATH: Path = Path.cwd()
DOCS_PATH: Path = ROOT_PATH / "docs"

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CI Pipeline")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "DOCS_PATH", DOCS_PATH)

    LOG.info("========================")
    LOG.info("Pipeline executed successfully.")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
