import sys
from pathlib import Path

from settings import ENABLE_HISTORY, DEFAULT_CITY
from weather_api import get_weather
from weather_formatter import format_weather
from exceptions import APIServiceError, StatusCodeError
from history import save_weather, PlainFileWeatherStorage


def main(city: str):
    try:
        weather = get_weather(city)
        print(format_weather(weather))
        if ENABLE_HISTORY:
            save_weather(weather, PlainFileWeatherStorage(Path.cwd() / "history.txt"))
    except APIServiceError as err:
        print(err)
        exit(1)
    except StatusCodeError as err:
        print("Error occurred. Check city name. Status code:", err)
        exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        city_name = DEFAULT_CITY
    else:
        city_name = " ".join(sys.argv[1:])

    main(city_name)
