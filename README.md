# Weather

This is a console application that allows user to get the weather (weather type, temperature),
as well as the time of sunrise and sunset. The weather is obtained using the Open Weather API.


## Contents

- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Technologies](#technologies)
- [File structure](#file-structure)
- [Testing](#testing)


## Requirements

To use the project, you need to get [OpenWeather API key](https://openweathermap.org/appid#signup)
and install [Python 3.10](https://www.python.org/downloads/release/python-3100/).


## Quick start

### Installing virtual environment and libraries

Create virtual environment using bash console:
```bash
python3 -m venv YOUR_VIRTUAL_ENV_NAME
```

Activate virtual environment:
```bash
# Linux
source YOUR_VIRTUAL_ENV_NAME/bin/activate
# Windows
YOUR_VIRTUAL_ENV_NAME/Scripts/activate
```

Install necessary libraries for Python:
```bash
pip install -r requirements.txt
```

### Setting up settings

You need to open file called .env-example. Insert your `OPEN_WEATHER_API_KEY`, 
select `DEFAULT_CITY` (the program without cmd arguments will show the weather in this city).

If you want, you can change `ENABLE_HISTORY` to "True". In this case every run will be stored in `history.txt` file.  

**IMPORTANT:**
Then save the file as `.env` (change the file extension).

### Running program

Run entry point, called "weather" (for Windows - you need to run it through bash console):
```bash
./weather
```

You may use city name to see weather in a particular city:
```bash
./weather Moscow
```

If city name consists of several words, there is no problem:
```bash
./weather New York
```


## Technologies

- [Python](https://www.python.org/)
- [requests](https://github.com/psf/requests/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [pytest](https://github.com/pytest-dev/pytest/)


## File structure


```bash
weather/
├── pytest.ini
├── README.md
├── requirements.txt
├── src
│   ├── exceptions.py
│   ├── history.py
│   ├── __init__.py
│   ├── settings.py
│   ├── weather_api.py
│   ├── weather_args_controller.py
│   └── weather_formatter.py
├── tests
│   ├── test_print_weather.py
│   ├── test_weather_api.py
│   ├── test_weather_args_controller.py
│   └── test_weather_formatter.py
├── weather
└── weather_printer.py
```


## Testing

Make sure you have installed `pytest` package (it is also stated in `requirements.txt`).

To run all the tests use:
```bash
pytest -v
```