from weather_api import Weather


def format_weather(weather: Weather) -> str:
    return (f"\n{weather.city}\n"
            f"{weather.weather_type.value}\n"
            f"Температура: {weather.temperature} °C\n"
            f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')}\n")


if __name__ == "__main__":
    from datetime import datetime
    from weather_api import WeatherType

    print(format_weather(Weather(
        city='Москва',
        weather_type=WeatherType.CLEAR,
        temperature=20,
        sunrise=datetime.fromisoformat("2022-08-02 04:00:00"),
        sunset=datetime.fromisoformat("2022-08-02 21:45:00"),
    )))
