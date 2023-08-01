import json
from datetime import datetime
from json import JSONDecodeError
from typing import NamedTuple, Literal
from enum import Enum

import requests
from requests import RequestException

from settings import OPEN_WEATHER_URL_TEMPLATE
from exceptions import APIServiceError

Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


class Weather(NamedTuple):
    city: str
    weather_type: WeatherType
    temperature: Celsius
    sunrise: datetime
    sunset: datetime


def get_weather(city: str) -> Weather:
    openweather_response = _get_openweather_response(city)
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(city: str) -> str:
    url = OPEN_WEATHER_URL_TEMPLATE.format(city=city)
    try:
        return requests.get(url).text
    except RequestException:
        raise APIServiceError


def _parse_openweather_response(openweather_response: str) -> Weather:
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise APIServiceError
    return Weather(
        city=_parse_city(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        temperature=_parse_temperature(openweather_dict),
        sunrise=_parse_suntime(openweather_dict, "sunrise"),
        sunset=_parse_suntime(openweather_dict, "sunset")
    )


def _parse_city(openweather_dict: dict) -> str:
    return openweather_dict["name"]


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    weather_type_name = openweather_dict["weather"][0]["main"].upper()
    for weather_type in WeatherType:
        if weather_type.name == weather_type_name:
            return weather_type
    else:
        raise APIServiceError


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict["main"]["temp"])


def _parse_suntime(openweather_dict: dict, time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])


if __name__ == "__main__":
    print(get_weather('Moscow'))
