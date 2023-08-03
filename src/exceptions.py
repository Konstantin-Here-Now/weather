class APIServiceError(Exception):
    """Program failed to get weather"""


class StatusCodeError(Exception):
    """OpenWeather Response had error status code (4xx, 5xx), may be wrong city name"""
