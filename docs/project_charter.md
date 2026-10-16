# Project Charter

## Project

Largest Banks ETL

## Purpose

Build a repeatable Python ETL pipeline that extracts the ten largest banks by market capitalization, transforms the values into GBP, EUR, and INR, and loads the results into CSV and SQLite outputs.

## Scope

The project covers web extraction, basic data cleaning, currency conversion, file loading, database loading, SQL queries, and progress logging. It is an academic project based on the IBM Data Engineering Professional Certificate final project.

## Inputs

- Archived Wikipedia page containing the market-capitalization table.
- IBM Skills Network exchange-rate CSV.

## Outputs

- `Largest_banks_data.csv`
- `Banks.db`, table `Largest_banks`
- `code_log.txt`

## Success criteria

- Ten banks are extracted with numeric USD market capitalization.
- GBP, EUR, and INR columns are calculated and rounded to two decimals.
- The transformed data is available in both output formats.
- SQL queries return the expected currency-specific values.
- The major ETL stages are recorded in the log.

