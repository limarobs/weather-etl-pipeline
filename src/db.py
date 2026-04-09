import os
from sqlalchemy import create_engine

def get_engine():
    os.makedirs("data", exist_ok=True)
    return create_engine("sqlite:///data/weather.db")