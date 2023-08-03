import json
from datetime import datetime
from enum import Enum
from json import JSONDecodeError
from typing import Literal, NamedTuple

import requests

from .exceptions import APIServiceError, StatusCodeError
from .settings import OPEN_WEATHER_URL_TEMPLATE

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
    _check_response_status_code(openweather_response.status_code)
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(city: str) -> requests.Response:
    url = OPEN_WEATHER_URL_TEMPLATE.format(city=city)
    try:
        return requests.get(url)
    except requests.RequestException:
        raise APIServiceError


def _check_response_status_code(status_code: int) -> None:
    if 400 <= status_code < 600:
        raise StatusCodeError(status_code)


def _parse_openweather_response(openweather_response: requests.Response) -> Weather:
    try:
        openweather_dict = json.loads(openweather_response.text)
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
