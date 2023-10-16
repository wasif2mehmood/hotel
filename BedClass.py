from ExceptionsClasses import *


class Bed:
    _TYPE_SIZE = {"Single": 1.73, "Super": 2.03}

    def __init__(self, bed_type: str, price: float, description: str):
        if bed_type not in ["Single", "Super"]:
            raise BookingException("Bed type must be 'Single' or 'Super'")
        self._type = bed_type
        self._price = price
        self._description = description

    @property
    def price(self):
        return self._price

    @property
    def floorArea(self):
        return self._TYPE_SIZE[self._type]

    def __str__(self) -> str:
        return f"{self._description}, ${self._price:.2f}"
