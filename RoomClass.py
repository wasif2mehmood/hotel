from ExceptionsClasses import *
from AmenityClasses import SharedAmenity, InRoomAmenity, Amenity
from GuestClass import Guest
from BedClass import Bed


class Room:
    _MIN_EXIT_SPACE = 1.84
    _TYPE_SIZE = {"Standard": 4.2, "Deluxe": 4.83}

    def __init__(self, room_type, bed, price):
        if room_type not in ["Standard", "Deluxe"]:
            raise BookingException("Room type must be 'Standard' or 'Deluxe'")
        self._type = room_type
        self._bed = bed
        self._amenities = []
        self._roomPrice = price

    @property
    def type(self):
        return self._type

    @property
    def roomPrice(self):
        return self._roomPrice

    @property
    def fullprice(self):
        return self._roomPrice + self._bed.price + sum([a.price for a in self._amenities])

    def addAmenity(self, amenity: Amenity):
        amentity_size = amenity.getFloorArea()
        if sum([a.getFloorArea() for a in self._amenities]) + amentity_size - self._TYPE_SIZE[self._type] > self._MIN_EXIT_SPACE:
            raise MinFloorAreaException("Not enough space for this amenity")
        if amenity.itemCode in [a.itemCode for a in self._amenities]:
            raise BookingException(f"Duplicate item code for {amenity} ")
        self._amenities.append(amenity)

    def removeAmenity(self, itemCode: str):
        for amenity in self._amenities:
            if amenity.itemCode == itemCode:
                self._amenities.remove(amenity)
                return
        raise BookingException(
            f"{itemCode}: Item code not found for room {self._type}")

    def __str__(self) -> str:
        room_details = f"{self._type} room, ${self._roomPrice:.2f}"
        bed_details = str(self._bed)
        amenities_details = "\n".join(
            [str(amenity) for amenity in self._amenities])
        amenities_details = amenities_details[:-1]
        full_price = f"Full Price: ${self.fullprice:.2f}"
        return f"{room_details}\n{bed_details}\n{amenities_details}\n{full_price}\n"
