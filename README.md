# ETL Project: World's Largest Banks

This project extracts the ten largest banks by market capitalization, converts their values from USD to GBP, EUR, and INR, and loads the resulting dataset into a CSV file and a SQLite database.

## Project workflow

1. Extract the table headed **By market capitalization** from the archived Wikipedia page.
2. Clean and convert market capitalization values to numeric data.
3. Add market capitalization columns in GBP, EUR, and INR using the provided exchange-rate CSV.
4. Save the transformed data to `Largest_banks_data.csv`.
5. Save the data to the `Largest_banks` table in `Banks.db`.
6. Run SQL queries for each currency and record progress in `code_log.txt`.

## Technologies

- Python
- pandas
- requests
- BeautifulSoup
- SQLite

## Requirements

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Run the project

```bash
python banks_project.py
```

The script creates or updates these files:

- `Largest_banks_data.csv`
- `Banks.db`
- `code_log.txt`

## Main functions

- `log_progress(message)`: appends a timestamped message to the log file.
- `extract(url, table_attribs=None)`: extracts and cleans bank data into a DataFrame.
- `transform(df, csv_path)`: adds GBP, EUR, and INR market capitalization columns.
- `load_to_csv(df, output_path)`: writes the transformed DataFrame to CSV.
- `load_to_db(df, sql_connection, table_name)`: writes the DataFrame to SQLite.
- `run_query(query_statement, sql_connection)`: executes and prints a SQL query result.

This is an academic ETL project created as part of the IBM Data Engineering Professional Certificate.

