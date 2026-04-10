import requests
import logging
from src.config import API_URL, CITIES

logging.basicConfig(level=logging.INFO)

def extract():
    all_data = []

    for city in CITIES:
        try:
            name, coords = city.split(":")
            lat, lon = map(float, coords.split(","))

            logging.info(f"Fetching data for {name}")

            params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
            }

            response = requests.get(API_URL, params=params)
            response.raise_for_status()

            data = response.json()
            data["city"] = name

            all_data.append(data)

        except Exception as e:
            logging.error(f"Error for {city}: {e}")

    logging.info("All data fetched successfully")
    return all_data