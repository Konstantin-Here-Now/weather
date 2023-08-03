from datetime import datetime

import src.weather_formatter as weather_formatter
from src.weather_api import Weather, WeatherType


def test_format_weather():
    mock_weather = Weather(
        city='Москва',
        weather_type=WeatherType.CLEAR,
        temperature=20,
        sunrise=datetime.fromisoformat("2022-08-02 04:00:00"),
        sunset=datetime.fromisoformat("2022-08-02 21:45:00"),
    )
    assert weather_formatter.format_weather(mock_weather) == ("\nМосква\n"
                                                              "Ясно\n"
                                                              "Температура: 20 °C\n"
                                                              "Восход: 04:00\n"
                                                              "Закат: 21:45\n")
