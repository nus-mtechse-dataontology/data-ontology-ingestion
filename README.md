# data-ontology-ingestion

This repository provides a flexible **data ingestion framework** that pulls information from
external APIs or local files and loads it into a relational database.  It is used for the
DataOntology project and is driven by YAML configuration files located in the `datasets/`
directory.

## 📦 Installation

You can install the project and its dependencies in two ways:

1. **Using `uv` (uvicorn runner)**
   ```bash
   # first make sure you have uv installed
   pip install uv

   # install requirements
   pip install -r requirements.txt
   ```

2. **Using `pip`/virtual environment directly**
   ```bash
   python -m venv .venv            # create virtual environment
   source .venv/bin/activate       # activate (macOS/Linux)
   source .venv/Scripts/activate   # activate Windows
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

> ⚠️ Ensure the `PROJECT_PATH` environment variable is set when running the CLI (handled by
> the examples below).

## 🚀 Running the ingestion

The main entry point is `src/main.py`, which uses [Typer](https://typer.tiangolo.com/) for
command-line argument parsing.  You must specify the dataset name (`--ingestion-type`) and the
working directory (`--project-path`).

### 🧪 Running the test suite

A small pytest-based test suite lives under `tests/`.  The tests mirror the project
package structure, e.g. `tests/services`, `tests/gateway`, `tests/sessions`, and
`tests/ingestion`.  After installing the requirements (`pip install -r requirements.txt`),
execute:

```bash
pytest -q
```

Tests exercise the DAO/service layers, file ingestion logic, API gateway, and utility
functions.

```bash
# example using uv
uv run src/main.py --ingestion-type="airport" --project-path="$(pwd)"

# or with python directly
python src/main.py --ingestion-type="airport" --project-path="$(pwd)"
```

The `--ingestion-type` must correspond to one of the YAML files under `datasets/`.

### 🔍 Available datasets for API ingestion

- `airport`
- `city`
- `country`
- `airline_coverage`

### 📁 File ingestion example

- `airline`
- `currency_rate`
- `fact_flight_info`

These configurations uses a CSV source.  To execute it:

```bash
python src/main.py --ingestion-type="fact_flight_info" --project-path="$(pwd)"
```

## 🗂️ Configuration

* All ingestion definitions live in `datasets/`.
* Vault files containing API keys/secrets are stored in `vault/` and referenced by the
  YAML using simple names (e.g. `destination.apiKey`).

## 🛠️ Extending the project

To add a new dataset, create a new YAML file alongside the existing ones and implement the
corresponding `service`, `dao`, and `ingestion` classes if necessary.  The system will dynamically
load whatever modules you specify in the YAML.
