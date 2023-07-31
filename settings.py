import os
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")


