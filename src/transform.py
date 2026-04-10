import pandas as pd
import logging

def transform(data_list):
    if not data_list:
        logging.warning("No data to transform")
        return None

    try:
        rows = []

        for data in data_list:
            current = data["current_weather"]

            rows.append({
                "city": data["city"],
                "temperature": current["temperature"],
                "windspeed": current["windspeed"],
                "time": current["time"]
            })

        df = pd.DataFrame(rows)

        logging.info("Data transformed successfully")
        return df

    except Exception as e:
        logging.error(f"Error during transformation: {e}")
        return None