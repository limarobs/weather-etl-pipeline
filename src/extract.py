import requests
import logging
import json
from src.config import API_URL

logging.basicConfig(level=logging.INFO)

def load_cities(file_path="data/cities.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def extract():
    all_data = []
    cities = load_cities()

    for city in cities:
        try:
            name = city["name"]
            lat = city["lat"]
            lon = city["lon"]

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
            logging.error(f"Error fetching data for {city['name']}: {e}")

    logging.info("All data fetched successfully")
    return all_data