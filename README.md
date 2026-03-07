# cintel-01-getting-started

[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://denisecase.github.io/cintel-01-getting-started/)
[![CI Status](https://github.com/denisecase/cintel-01-getting-started/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/denisecase/cintel-01-getting-started/actions/workflows/ci-python-zensical.yml)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project for continuous intelligence.

Continuous intelligence systems monitor data streams, detect change, and respond in real time.
This course builds those capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows the structure of professional Python projects.
We learn by doing.

## This Project

This is the **getting started** project.
The goal is to copy this repository, set up your environment, run the example pipeline, and push your work to GitHub.
You'll change the authorship to make it yours and explore the project without making major code changes.

You will only work with these files:

- **src/cintel/case_pipeline.py** - where the logic happens
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. Start & Run
2. Phase 2. Change Authorship
3. Phase 3. Read & Understand

The guide walks through each phase in detail.
Follow the instructions to create your own working copy and use YOUR GitHub account in the `git clone` command below.

Commands are listed for convenience only - you will need the full instructions from the workflow guide linked above.

## Command Summary

You will need the detailed instructions the first few times you run this process.
These are core skills and setting a good foundation will pay off many times over.

In a machine Terminal (open in Repos folder):

```shell
# **IMPORTANT**: In the git clone command below,
# replace username with YOUR GitHub username
# as described in the instructions above.

git clone https://github.com/username/cintel-01-getting-started
cd cintel-01-getting-started
code .
```

In a VS Code Terminal:

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uv run python -m cintel.case_pipeline

uv run ruff format .
uv run ruff check . --fix
uv run zensical build

git add -A
git commit -m "update"
git push -u origin main
```

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
