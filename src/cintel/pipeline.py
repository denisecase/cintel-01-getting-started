"""pipeline.py - Project script (example).

Author: Your Name Here
Date: 2026-mm-dd

Purpose:
  Confirm your project environment is set up correctly.
  Run this script to see a log message in the terminal.

Run as a Module:
  uv run python -m cintel.pipeline

DESIGN:

Use this file to first learn and then apply your skills.

Reusable functions that do the work are kept in a external files.
We import functions and pass in what they need through their parentheses.
Shared utility functions can be imported into a Python
module or a reactive marimo notebook app.

SKILLS:

- Setting up a professional Python project.
- Managing a project environment using uv.
- Editing project code using VS Code editor.
- Tracking project source code using git version control system.
- Storing and sharing projects using GitHub.
- Writing a professional Python file, often called a script.
- Providing this opening docstring with your name and date.
- Providing an opening docstring with important information about the file.
- Importing freely available code into a Python file.
- Configuring a logger to record information as the file runs.
- Declaring and using global constants for folder paths.
- Defining a main function that "orchestrates" the project logic.
- Using a conditional execution block to trigger main().
"""

# === DECLARE IMPORTS ===

# First from the Python standard library (no installation needed)
import logging
from pathlib import Path

# Then, external dependencies (must be listed in pyproject.toml)
from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P1", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS FOR FOLDER PATHS (directories) ===

# ANALYST: Use the VS Code "Explorer" to navigate the project folder structure.
# Above, we imported Path from the pathlib module to work with filesystem paths.
# Every Path object represents a filesystem path and can be combined with other paths using the "/" operator.
# Every Path object has a method called `cwd` that returns the current working directory as a Path object.
ROOT_DIR: Path = Path.cwd()
DOCS_DIR: Path = ROOT_DIR / "docs"
SOURCE_DIR: Path = ROOT_DIR / "src"
CINTEL_DIR: Path = SOURCE_DIR / "cintel"

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """This function is where the execution begins.

    In this course, we will use this function to "orchestrate"
    the main steps of the project.

    In this first module, this function demonstrates logging
    (a way of recording what the project is doing) and
    path management.

    Both are important and will be used throughout the course.

    The first function we call is the log_header() function
    which we imported up above.

    Can you tell what package it comes from?

    It comes from the `datafun_toolkit.logger` package.

    You can find it listed in `pyproject.toml`
    in the `[dependencies]` section.
    That's where we list free code packages
    that others write and maintain.
    We use them for free.
    Knowing how to use free code packages is a valuable skill.

    Once we have imported the log_header function above,
    we can call it here in main.

    Calling log_header() logs an opening.
    Call it at the beginning of the main function
    to provide a clear visual separation of pipeline runs.
    When calling the function, we must provide 2 arguments
    that we "pass in" through the parentheses:
    - the logger instance (LOG) and
    - a string with a project name, e.g., "CINTEL".

    We'll also call log_path().
    Calling log_path() logs a path to a file or folder in the project
    without revealing sensitive information.
    When calling the function, we must provide 3 arguments
    that we "pass in" through the parentheses:
    - the logger instance,
    - a descriptive name for the path, and
    - the path itself.
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    # Always use the the imported log_path() function
    # It will log only relative paths and not reveal sensitive information.
    # First, log the root project folder (ROOT_DIR)
    # Then, log other interesting paths to explore.
    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DOCS_DIR", DOCS_DIR)
    log_path(LOG, "SOURCE_DIR", SOURCE_DIR)
    log_path(LOG, "CINTEL_DIR", CINTEL_DIR)

    # Log a custom message (change this to something meaningful for your project)
    LOG.info("Hello World from Dr. Case!")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

# Python has some Python-controlled variables that it manages.
# These are typically named with dunders or "double underscores".
# The variable __name__ is one such Python-controlled variable.
# When this file is run directly, Python sets __name__
# for this file to a string equal to "__main__".
#
# The conditional execution guard checks if __name__ is "__main__"
# and if so, it will then call the main function by
# using the function name followed by parentheses.
# In this case the parentheses are empty,
# since this main function does not need any arguments
# (additional information) calls main().
if __name__ == "__main__":
    main()
