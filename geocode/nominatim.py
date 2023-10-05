from geopy.geocoders import Nominatim


async def geocode(address, attempt=1, max_attempts=5):
    try:
        with Nominatim(
                user_agent="Felix' Wohnungsbot",
        ) as geolocator:
            location = geolocator.geocode(address, exactly_one=True, timeout=60)
            return [location.latitude, location.longitude]
    except Exception as e:
        if attempt <= max_attempts:
            return await geocode(address, attempt=attempt + 1)
        raise e
