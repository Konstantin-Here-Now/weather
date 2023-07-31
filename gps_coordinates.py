from typing import NamedTuple
from geopy.geocoders import Nominatim


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates(address) -> Coordinates:
    geolocator = Nominatim(user_agent="gps_coordinates_getter")
    location = geolocator.geocode(address)
    return Coordinates(latitude=location.latitude, longitude=location.longitude)
