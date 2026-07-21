import requests
import json
import os
from logger import logger

cities = {
    "Hyderabad": (17.3850, 78.4867),
    "Bengaluru": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Mumbai": (19.0760, 72.8777),
    "Delhi": (28.6139, 77.2090),
    "Kolkata": (22.5726, 88.3639),
    "Pune": (18.5204, 73.8567),
    "Visakhapatnam": (17.6868, 83.2185)
}

url = "https://api.open-meteo.com/v1/forecast"

try:
    logger.info("Extraction Started")

    weather_data = []

    for city, (lat, lon) in cities.items():

        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:

            data = response.json()

            weather_data.append({
                "city": city,
                "time": data["current"]["time"],
                "temperature": data["current"]["temperature_2m"],
                "humidity": data["current"]["relative_humidity_2m"],
                "wind_speed": data["current"]["wind_speed_10m"]
            })

            print(f"✅ {city}")

    os.makedirs("data/raw", exist_ok=True)

    with open("data/raw/weather.json", "w") as file:
        json.dump(weather_data, file, indent=4)

    logger.info("Extraction Completed")

except Exception as e:
    logger.error(e)
    print(e)