import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime as dt


def log_progress(mensaje):
    momento = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("code_log.txt", "a") as archivo:
        archivo.write(f"{momento}: {mensaje}\n")


def extract(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    tablas = soup.find_all("table")
    tabla_bancos = tablas[0]

    filas = tabla_bancos.find_all("tr")
    datos = []

    for banco in filas[1:]:
        celda = banco.find_all("td")
        nombre = celda[1].get_text(strip=True)
        capitalizacion = float(celda[2].get_text(strip=True))
        datos.append({"Name" : nombre, "MC_USD_Billion" : capitalizacion})

    df = pd.DataFrame(datos)
    return df


def transform(df, ruta_tasas):
    tabla = pd.read_csv(ruta_tasas)

    tasa_gbp = tabla.loc[tabla["Currency"] == "GBP", "Rate"]
    tasa_gbp = tasa_gbp.item()

    tasa_eur = tabla.loc[tabla["Currency"] == "EUR", "Rate"]
    tasa_eur = tasa_eur.item()

    tasa_inr = tabla.loc[tabla["Currency"] == "INR", "Rate"]
    tasa_inr = tasa_inr.item()

    df["MC_GBP_Billion"] = (
        df["MC_USD_Billion"] * tasa_gbp
    ).round(2)

    df["MC_EUR_Billion"] = (
        df["MC_USD_Billion"] * tasa_eur
    ).round(2)

    df["MC_INR_Billion"] = (
        df["MC_USD_Billion"] * tasa_inr
    ).round(2)

    return df


def load_to_csv(df, ruta_salida):
    df.to_csv(ruta_salida, index=False)


def load_to_db(df, conexion, nombre_tabla):
    df.to_sql(
        nombre_tabla,
        conexion,
        if_exists = "replace",
        index=False
    )


def run_queries(consulta, conexion):
    resultado = pd.read_sql_query(consulta, conexion)
    print(resultado)


url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'

ruta_tasas = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"

df_bancos = extract(url)
log_progress("Data extraction complete. Initiating transformation process")

df_transformado = transform(df_bancos, ruta_tasas)
log_progress("Data transformation complete")

load_to_csv(df_transformado,"./Largest_banks_data.csv")
log_progress("Data loading process to CSV complete")

conexion = sqlite3.connect("Banks.db")
log_progress("Connection made to Banks.db")

load_to_db(df_transformado, conexion, "Largest_banks")
log_progress("Transformed dataframe loaded to sql database Banks.db")

run_queries("SELECT name, MC_GBP_Billion FROM Largest_Banks", conexion)
run_queries("SELECT name, MC_EUR_Billion FROM Largest_Banks", conexion)
run_queries("SELECT name, MC_INR_Billion FROM Largest_Banks", conexion)
log_progress("Queries executed successfully")

conexion.close()
log_progress("Database connection closed")
