from pathlib import Path

from src.exceptions import APIServiceError, StatusCodeError
from src.history import PlainFileWeatherStorage, save_weather
from src.settings import ENABLE_HISTORY
from src.weather_api import get_weather
from src.weather_args_controller import get_city_name
from src.weather_formatter import format_weather


def main(city: str) -> None:
    try:
        weather = get_weather(city)
        print(format_weather(weather))
        if ENABLE_HISTORY:
            save_weather(weather, PlainFileWeatherStorage(Path.cwd() / "history.txt"))
    except APIServiceError as err:
        print(err)
        exit(1)
    except StatusCodeError as err:
        print("Error occurred. Check city name or OpenWeatherAPI key. Status code:", err)
        exit(1)


if __name__ == "__main__":
    city_name = get_city_name()
    main(city_name)
