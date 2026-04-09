import pandas as pd
from datetime import datetime

def transform(data):
    print("Data transformation in progress")

    weather = data["current_weather"]

    df = pd.DataFrame([weather])

    df = df.rename(columns={
        "temperature": "temp_c",
        "windspeed": "wind_kmh"
    })

    df["temp_category"] = df["temp_c"].apply(
        lambda x: "HOT" if x > 30 else "COLD" if x < 15 else "MILD"
    )

    df["collected_at"] = datetime.now()

    return df