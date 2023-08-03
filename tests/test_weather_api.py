from datetime import datetime

import pytest

import src.exceptions as custom_exceptions
import src.weather_api as weather_api
from src.weather_api import WeatherType

MOCK_OPENWEATHER_DICT = {'coord': {'lon': 37.6156, 'lat': 55.7522},
                         'weather': [
                             {'id': 803, 'main': 'Clouds', 'description': 'облачно с прояснениями', 'icon': '04n'}],
                         'base': 'stations',
                         'main': {'temp': 20.83, 'feels_like': 20.74, 'temp_min': 18.64, 'temp_max': 21.29,
                                  'pressure': 1010, 'humidity': 68, 'sea_level': 1010, 'grnd_level': 993},
                         'visibility': 10000,
                         'wind': {'speed': 2.61, 'deg': 193, 'gust': 7.33},
                         'clouds': {'all': 72},
                         'dt': 1691095647,
                         'sys': {'type': 2, 'id': 47754, 'country': 'RU', 'sunrise': 1691026650,
                                 'sunset': 1691084036},
                         'timezone': 10800,
                         'id': 524901,
                         'name': 'Москва',
                         'cod': 200}


def test_check_response_status_code_no_error():
    assert weather_api._check_response_status_code(200) is None


def test_check_response_status_code_has_error_404():
    with pytest.raises(custom_exceptions.StatusCodeError) as err_info:
        weather_api._check_response_status_code(404)
    assert str(err_info.value) == "404"


def test_parse_city():
    assert weather_api._parse_city(MOCK_OPENWEATHER_DICT) == "Москва"


def test_parse_weather_type_default():
    assert weather_api._parse_weather_type(MOCK_OPENWEATHER_DICT) == WeatherType.CLOUDS


def test_parse_weather_type_with_error():
    dict_with_error = MOCK_OPENWEATHER_DICT
    dict_with_error["weather"][0]["main"] = "no weather type"
    with pytest.raises(custom_exceptions.APIServiceError):
        weather_api._parse_weather_type(dict_with_error)


def test_parse_temperature():
    assert weather_api._parse_temperature(MOCK_OPENWEATHER_DICT) == 21


def test_parse_suntime_sunrise():
    assert weather_api._parse_suntime(MOCK_OPENWEATHER_DICT, "sunrise") == datetime(2023, 8, 3, 4, 37, 30)


def test__parse_suntime_sunset():
    assert weather_api._parse_suntime(MOCK_OPENWEATHER_DICT, "sunset") == datetime(2023, 8, 3, 20, 33, 56)
