# SEDA

SEDA is a Python fitness tracking project with both a command-line interface and a graphical interface. The current codebase focuses on user data, water logs, weight logs, and a small SQLite-backed persistence layer.

## Current Features

- start either the CLI or GUI from `main.py`
- manage one user profile
- store water intake entries
- store weight entries
- calculate values such as daily water intake and BMI
- persist data in SQLite
- cover core behavior with automated tests

## Project Layout

- `main.py` starts the application
- `model/` contains classes, database code, and CLI control flow
- `ui/` contains the Flet GUI, CLI view helpers, and tutorial examples
- `data/` stores the main SQLite database
- `tests/` contains automated tests
- `docs/` contains German and English project structure notes
- `legacy/` keeps older code for reference
- `utils/` contains helper and experimental files

For a more detailed overview, see [docs/de_struktur.md](/home/vaeterchen_frost/Code/Python/seda/docs/de_struktur.md) and [docs/en_structur.md](/home/vaeterchen_frost/Code/Python/seda/docs/en_structur.md).

## Requirements

The project currently stores its dependencies in `requirement.txt`.

Typical setup:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirement.txt
```

## Running the Project

Start the application with:

```bash
python main.py
```

You will then be asked whether to launch:

- the GUI
- the CLI

## Running Tests

Run the test suite with:

```bash
pytest
```

## Notes

- The project currently mixes active code, utilities, and older experiments.
- `bug_tracker.py` documents known issues and technical debt.
- Some filenames still reflect earlier project phases, for example `requirement.txt`.
