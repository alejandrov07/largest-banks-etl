import sqlite3
from datetime import datetime as dt

import pandas as pd
import requests
from bs4 import BeautifulSoup


def log_progress(message):
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("code_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{timestamp}: {message}\n")


def extract(url, table_attribs=None):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    tables = soup.find_all("table")
    bank_table = tables[0]
    rows = bank_table.find_all("tr")
    data = []

    if table_attribs is None:
        table_attribs = ["Name", "MC_USD_Billion"]

    for row in rows[1:]:
        columns = row.find_all("td")
        if len(columns) < 3:
            continue

        bank_name = columns[1].find_all("a")[1]["title"]
        market_cap = columns[2].get_text(strip=True)
        market_cap = market_cap.replace(",", "").replace("$", "")

        data.append({
            table_attribs[0]: bank_name,
            table_attribs[1]: float(market_cap)
        })

    return pd.DataFrame(data, columns=table_attribs)


def transform(df, csv_path):
    exchange_rates = pd.read_csv(csv_path)

    gbp_rate = exchange_rates.loc[
        exchange_rates["Currency"] == "GBP", "Rate"
    ].item()
    eur_rate = exchange_rates.loc[
        exchange_rates["Currency"] == "EUR", "Rate"
    ].item()
    inr_rate = exchange_rates.loc[
        exchange_rates["Currency"] == "INR", "Rate"
    ].item()

    df["MC_GBP_Billion"] = (
        df["MC_USD_Billion"] * gbp_rate
    ).round(2)
    df["MC_EUR_Billion"] = (
        df["MC_USD_Billion"] * eur_rate
    ).round(2)
    df["MC_INR_Billion"] = (
        df["MC_USD_Billion"] * inr_rate
    ).round(2)

    return df


def load_to_csv(df, output_path):
    df.to_csv(output_path, index=False)
    log_progress("Data loading process to CSV complete")


def load_to_db(df, sql_connection, table_name):
    df.to_sql(
        table_name,
        sql_connection,
        if_exists="replace",
        index=False
    )
    log_progress("Transformed dataframe loaded to SQL database Banks.db")


def run_query(query_statement, sql_connection):
    result = pd.read_sql_query(query_statement, sql_connection)
    print(result)
    log_progress(f"Query executed: {query_statement}")


if __name__ == "__main__":
    url = (
        "https://web.archive.org/web/20230908091635/"
        "https://en.wikipedia.org/wiki/List_of_largest_banks"
    )
    csv_path = (
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
        "IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
    )
    output_path = "./Largest_banks_data.csv"

    log_progress("Preliminaries complete. Initiating ETL process")

    df_banks = extract(url)
    print(df_banks)
    log_progress("Data extraction complete. Initiating transformation process")

    df_transformed = transform(df_banks, csv_path)
    log_progress("Data transformation complete. Initiating loading process")

    load_to_csv(df_transformed, output_path)

    connection = sqlite3.connect("Banks.db")
    log_progress("Connection made to Banks.db")

    load_to_db(df_transformed, connection, "Largest_banks")

    run_query(
        "SELECT Name, MC_GBP_Billion FROM Largest_banks",
        connection
    )
    run_query(
        "SELECT Name, MC_EUR_Billion FROM Largest_banks",
        connection
    )
    run_query(
        "SELECT Name, MC_INR_Billion FROM Largest_banks",
        connection
    )

    log_progress("Queries executed successfully")
    connection.close()
    log_progress("Database connection closed")

