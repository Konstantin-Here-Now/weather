#!/usr/bin/env python3.10
import sys

from weather_api import get_weather
from weather_formatter import format_weather
from exceptions import APIServiceError, StatusCodeError


def main(city: str):
    try:
        weather = get_weather(city)
        print(format_weather(weather))
    except APIServiceError as err:
        print(err)
        exit(1)
    except StatusCodeError as err:
        print("Error occurred. Check city name. Status code:", err)
        exit(1)


if __name__ == "__main__":
    # default city name
    city_name = "Moscow"
    if len(sys.argv) > 1:
        city_name = sys.argv[1]
    main(city_name)
