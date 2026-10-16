# Deployment and Execution

## Local requirements

- Python 3.9 or newer
- Internet access for the archived webpage and exchange-rate CSV

## Installation

```bash
git clone https://github.com/alejandrov07/largest-banks-etl.git
cd largest-banks-etl
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
```

## Run

```bash
python src/banks_project.py
```

The script creates or replaces the CSV and SQLite outputs and appends progress entries to `code_log.txt`.

## Verify outputs

```bash
python -c "import pandas as pd; print(pd.read_csv('Largest_banks_data.csv').shape)"
```

The expected shape is `(10, 5)`. The SQLite table is named `Largest_banks` in `Banks.db`.

