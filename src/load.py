import sqlite3
import logging

def load(df):
    if df is None:
        logging.warning("No data to load")
        return

    try:
        conn = sqlite3.connect("data/weather.db")

        df.to_sql("weather", conn, if_exists="append", index=False)
        df.to_csv("data/weather.csv", mode="a", index=False, header=False)

        conn.close()
        logging.info("Data loaded into SQLite")

    except Exception as e:
        logging.error(f"Error during load: {e}")