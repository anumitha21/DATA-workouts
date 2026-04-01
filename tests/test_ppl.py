import pandas as pd
from src.transform import transform_weather_data


sample_raw_data = {
    "hourly": {
        "time": ["2026-04-01T00:00", "2026-04-01T01:00"],
        "temperature_2m": [28.1, 27.8],
        "relative_humidity_2m": [74, 76],
        "wind_speed_10m": [12.4, 10.8]
    }
}


def test_transform_returns_dataframe():
    df = transform_weather_data(sample_raw_data)
    assert isinstance(df, pd.DataFrame)


def test_dataframe_has_expected_columns():
    df = transform_weather_data(sample_raw_data)
    expected_columns = {
        "time",
        "temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m",
        "date",
        "hour"
    }
    assert expected_columns.issubset(set(df.columns))


def test_row_count_matches_input():
    df = transform_weather_data(sample_raw_data)
    assert len(df) == 2