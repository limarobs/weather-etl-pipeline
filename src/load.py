from db import get_engine

def load(df):
    print("Loading data into the database")

    engine = get_engine()

    df.to_sql(
        "weather_data",
        engine,
        if_exists="append",
        index=False
    )