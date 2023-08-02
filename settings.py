import os
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
OPEN_WEATHER_URL_TEMPLATE = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid=" + OPEN_WEATHER_API_KEY + \
                            "&units=metric&lang=ru"
ENABLE_HISTORY = (os.getenv("ENABLE_HISTORY") == "True")
DEFAULT_CITY = os.getenv("DEFAULT_CITY")
