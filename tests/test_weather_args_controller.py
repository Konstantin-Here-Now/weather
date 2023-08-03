import sys
from unittest.mock import patch

import src.weather_args_controller as weather_args_controller
from src.settings import DEFAULT_CITY


def test_get_city_name_without_city_name():
    test_args = ['weather']
    with patch.object(sys, 'argv', test_args):
        assert weather_args_controller.get_city_name() == DEFAULT_CITY


def test_get_city_name_with_city_name_consisting_of_two_words():
    test_args = ['weather', 'New York']
    with patch.object(sys, 'argv', test_args):
        assert weather_args_controller.get_city_name() == "New York"


def test_get_city_name_with_city_name_consisting_of_one_word():
    test_args = ['weather', 'London']
    with patch.object(sys, 'argv', test_args):
        assert weather_args_controller.get_city_name() == "London"
