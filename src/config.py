import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
CITIES = os.getenv("CITIES")

if CITIES is None:
    raise ValueError("CITIES not found in .env")

CITIES = CITIES.split(";")