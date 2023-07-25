from geopy.geocoders import Nominatim


async def geocode(address):
    with Nominatim(
            user_agent="Felix' Wohnungsbot",
    ) as geolocator:
        location = geolocator.geocode(address, exactly_one=True)
        return [location.latitude, location.longitude]
