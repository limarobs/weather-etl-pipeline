import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

if API_URL is None:
    raise ValueError("API_URL not found in .env")