import os
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("WEATHER_API_KEY") or 'a8dcdeb52a416a328ebb14052e606431'
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPEN_WEATHER_URL_TEMPLATE = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid=" + OPEN_WEATHER_API_KEY
