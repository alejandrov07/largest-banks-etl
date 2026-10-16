# Largest Banks ETL

**Status:** ETL pipeline completed | CSV and SQLite outputs implemented | Progress logging implemented | Documentation added

This project extracts the ten largest banks in the world by market capitalization, converts their values from USD to GBP, EUR, and INR, and stores the transformed data in CSV and SQLite formats.

## Project Overview

The pipeline uses an archived Wikipedia table as its source and an exchange-rate CSV provided by IBM Skills Network. It demonstrates a complete small-scale ETL workflow suitable for recurring financial reporting.

### Project objectives

- Extract the required bank information from an HTML table.
- Clean market capitalization values and convert them to numeric data.
- Add market capitalization values in GBP, EUR, and INR.
- Save the final dataset to a CSV file and a SQLite database table.
- Run SQL queries against the stored data.
- Record the progress of each major stage in a timestamped log.

## Professional Objective

This repository is part of my technical portfolio and demonstrates introductory competencies in:

- Python data extraction
- Pandas transformations
- ETL pipeline design
- SQLite database loading
- SQL querying
- Data cleaning
- Process logging and documentation

## Tech Stack

| Component | Technology |
|---|---|
| Extraction | Python, Requests, BeautifulSoup |
| Transformation | Python, Pandas |
| Storage | CSV, SQLite |
| Querying | SQL through Pandas and SQLite |
| Documentation | Markdown |
| Version Control | Git / GitHub |

## Key Features

### 1. Extraction

`extract(url, table_attribs=None)` reads the archived **By market capitalization** table and returns the bank name and USD market capitalization.

### 2. Transformation

`transform(df, csv_path)` reads the exchange rates and creates these columns:

- `MC_GBP_Billion`
- `MC_EUR_Billion`
- `MC_INR_Billion`

All converted values are rounded to two decimal places.

### 3. Loading

The transformed DataFrame is saved to:

- `Largest_banks_data.csv`
- `Banks.db`, table `Largest_banks`

### 4. SQL queries

`run_query()` executes queries that retrieve the bank names and market capitalization values for each target currency.

### 5. Logging

`log_progress()` appends timestamped messages to `code_log.txt`. The log records extraction, transformation, CSV loading, database loading, query execution, and connection closure.

## Data Lineage

```text
Archived Wikipedia table + exchange-rate CSV
                    |
                    v
             Extract and clean
                    |
                    v
              Transform values
                    |
          +---------+---------+
          v                   v
        CSV              SQLite table
          |                   |
          +---------+---------+
                    v
                 SQL queries
```

Detailed lineage is available in [`docs/lineage.md`](docs/lineage.md).

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/alejandrov07/largest-banks-etl.git
cd largest-banks-etl
```

### 2. Create the environment and install dependencies

```bash
python -m venv .venv
```

On Windows:

```bash
.\\.venv\\Scripts\\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Then install the requirements:

```bash
pip install -r requirements.txt
```

### 3. Run the pipeline

```bash
python src/banks_project.py
```

The script creates or replaces the CSV and SQLite outputs and appends progress entries to `code_log.txt`.

### 4. Verify the output

```bash
python -c "import pandas as pd; print(pd.read_csv('Largest_banks_data.csv').shape)"
```

Expected shape:

```text
(10, 5)
```

See [`docs/deployment.md`](docs/deployment.md) and [`docs/testing.md`](docs/testing.md) for the complete execution and verification procedures.

## Project Structure

```text
largest-banks-etl/
├── docs/
│   ├── data_dictionary.md
│   ├── deployment.md
│   ├── lineage.md
│   ├── project_charter.md
│   └── testing.md
├── src/
│   └── banks_project.py
├── tests/
│   └── README.md
├── .gitignore
├── README.md
├── requirements.txt
├── Banks.db                 # generated locally, ignored by Git
├── Largest_banks_data.csv   # generated locally, ignored by Git
└── code_log.txt             # generated locally, ignored by Git
```

## Documentation

- [`docs/project_charter.md`](docs/project_charter.md): purpose, scope, inputs, outputs, and success criteria.
- [`docs/data_dictionary.md`](docs/data_dictionary.md): definitions and data types for the final table.
- [`docs/lineage.md`](docs/lineage.md): source-to-output flow and transformations.
- [`docs/deployment.md`](docs/deployment.md): installation and execution instructions.
- [`docs/testing.md`](docs/testing.md): verification evidence and manual checks.

## Limitations and Future Enhancements

- The source is an archived webpage and may not reflect current market values.
- The pipeline currently depends on a fixed table position in the HTML page.
- Automated unit tests and a CI workflow can be added in a future iteration.
- Error handling and retry logic can be expanded for network failures.
- The pipeline can later be scheduled for recurring quarterly execution.

## Contact

**Alejandro Velazquez**

[GitHub](https://github.com/alejandrov07) · [Project repository](https://github.com/alejandrov07/largest-banks-etl)

Built as part of my preparation for Data Engineering and Analytics roles.

