from unittest.mock import Mock, patch

import pytest
import src.exceptions as custom_exceptions
import weather_printer

MOCK_FORMATTED_WEATHER = ("\nМосква\n"
                          "Ясно\n"
                          "Температура: 20 °C\n"
                          "Восход: 04:00\n"
                          "Закат: 21:45\n")


@patch('weather_printer.get_weather', Mock(return_value=None))
@patch('weather_printer.format_weather', Mock(return_value=MOCK_FORMATTED_WEATHER))
def test_print_weather_default(capsys):
    weather_printer.main("asdfghjkl")
    captured = capsys.readouterr()
    assert captured.out == f"{MOCK_FORMATTED_WEATHER}\n"


@patch('weather_printer.get_weather', Mock(side_effect=custom_exceptions.APIServiceError))
def test_print_weather_APIServiceError():
    with pytest.raises(SystemExit):
        weather_printer.main("asdfghjkl")


@patch('weather_printer.get_weather', Mock(side_effect=custom_exceptions.StatusCodeError))
def test_print_weather_StatusCodeError():
    with pytest.raises(SystemExit):
        weather_printer.main("asdfghjkl")
