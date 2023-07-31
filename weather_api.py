from datetime import datetime
from typing import NamedTuple
from enum import Enum

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
    pass
