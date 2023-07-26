from geopy.geocoders import Nominatim


def get_coordinates(address):
    geolocator = Nominatim(user_agent="myapplication")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude


latitude, longitude = get_coordinates({'city': 'Moscow'})
print(latitude, longitude)
