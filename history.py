from datetime import datetime
from pathlib import Path

from weather_api import Weather
from weather_formatter import format_weather


class WeatherStorage:
    """Interface for any storage saving weather"""

    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class PlainFileWeatherStorage(WeatherStorage):
    """Store weather in plain text file"""

    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self._file, "a") as f:
            f.write(f"{now}\n{formatted_weather}")


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Saves weather in storage"""
    storage.save(weather)
