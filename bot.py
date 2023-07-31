import os
import datetime
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&units=metric&appid={WEATHER_API_KEY}")
        data = response.json()
        print(data)
    except:
        await message.reply("Проверьте название города!")


if __name__ == "__main__":
    # С помощью метода executor.start_polling опрашиваем
    # Dispatcher: ожидаем команду /start
    executor.start_polling(dp)
