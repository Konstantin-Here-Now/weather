#!/usr/bin/env python3.10
import sys

from weather_api import get_weather
from weather_formatter import format_weather


def main(city: str):
    weather = get_weather(city)
    print(format_weather(weather))


if __name__ == "__main__":
    # default city name
    city_name = "Moscow"
    if len(sys.argv) > 1:
        city_name = sys.argv[1]
    main(city_name)
