from .weather_api import Weather


def format_weather(weather: Weather) -> str:
    return (f"\n{weather.city}\n"
            f"{weather.weather_type.value}\n"
            f"Температура: {weather.temperature} °C\n"
            f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')}\n")
