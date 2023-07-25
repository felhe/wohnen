from typing import TypedDict, List


class Apartment(TypedDict):
    addr: str
    floor: str
    price: float
    rooms: float
    sqm: float
    timeframe: str
    wbs: str
    year: str
    link: str
    image: str
    coords: List[float]

