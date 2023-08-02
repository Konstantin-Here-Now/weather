class APIServiceError(Exception):
    """Program can't get weather"""


class StatusCodeError(Exception):
    """Response had error status code (4xx, 5xx)"""
