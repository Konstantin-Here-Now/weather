from pathlib import Path

from exceptions import APIServiceError, StatusCodeError
from history import PlainFileWeatherStorage, save_weather
from settings import ENABLE_HISTORY
from weather_api import get_weather
from weather_args_controller import get_city_name
from weather_formatter import format_weather


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
