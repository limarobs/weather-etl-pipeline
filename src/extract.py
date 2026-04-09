import requests

def extract():
    print("Extracting data from API")

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": -29.19,
        "longitude": -54.87,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("API request failed with status code {}".format(response.status_code))

    return response.json()