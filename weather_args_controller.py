import sys

from settings import DEFAULT_CITY


def get_city_name() -> str:
    if len(sys.argv) == 1:
        city = DEFAULT_CITY
    else:
        city = " ".join(sys.argv[1:])
    return city
