from abc import ABC, abstractmethod


class Amenity(ABC):
    def __init__(self, itemCode, description, price):
        self._itemCode = itemCode
        self._description = description
        self._price = price

    @property
    def itemCode(self):
        return self._itemCode

    @property
    def price(self):
        return self._price

    @abstractmethod
    def getFloorArea(self):
        pass

    def __str__(self):
        return "{}, {}, ${:.2f}".format(self._itemCode, self._description, self._price)


class InRoomAmenity(Amenity):
    def __init__(self, itemCode, description, price, floorArea):
        super().__init__(itemCode, description, price)
        self._floorArea = floorArea

    def getFloorArea(self):
        return self._floorArea


class SharedAmenity(Amenity):
    def getFloorArea(self):
        return 0
