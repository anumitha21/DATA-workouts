import os
import json
import pandas as pd

RAW_FILE = "data/raw/weather_raw.json"
PROCESSED_DIR = "data/processed"
PROCESSED_FILE = os.path.join(PROCESSED_DIR, "weather_cleaned.csv")


def load_raw_data(file_path=RAW_FILE):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def transform_weather_data(raw_data):
    """
    Convert raw Open-Meteo JSON into a clean Pandas DataFrame.
    """
    hourly = raw_data.get("hourly", {})

    df = pd.DataFrame({
        "time": hourly.get("time", []),
        "temperature_2m": hourly.get("temperature_2m", []),
        "relative_humidity_2m": hourly.get("relative_humidity_2m", []),
        "wind_speed_10m": hourly.get("wind_speed_10m", [])
    })

    if not df.empty:
        df["time"] = pd.to_datetime(df["time"])
        df["date"] = df["time"].dt.date
        df["hour"] = df["time"].dt.hour

    return df


def save_processed_data(df, file_path=PROCESSED_FILE):
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    df.to_csv(file_path, index=False)


if __name__ == "__main__":
    raw_data = load_raw_data()
    df = transform_weather_data(raw_data)
    save_processed_data(df)
    print(f"Processed weather data saved to {PROCESSED_FILE}")
    print(df.head())