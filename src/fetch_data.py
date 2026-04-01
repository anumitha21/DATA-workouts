import os
import json
import requests

RAW_DIR = "data/raw"
RAW_FILE = os.path.join(RAW_DIR, "weather_raw.json")


def fetch_weather_data(latitude=13.0827, longitude=80.2707):
    """
    Fetch hourly weather data from Open-Meteo API for Chennai.
    """
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        "&forecast_days=2"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


def save_raw_data(data):
    os.makedirs(RAW_DIR, exist_ok=True)
    with open(RAW_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    weather_data = fetch_weather_data()
    save_raw_data(weather_data)
    print(f"Raw weather data saved to {RAW_FILE}")