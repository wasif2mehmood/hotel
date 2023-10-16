from datetime import date, timedelta
from RoomClass import *
from GuestClass import Guest


class Booking:
    _NEXT_ID = 1

    def __init__(self, guest, room, check_in_date, check_out_date):
        self._bookingID = str(Booking._NEXT_ID)
        Booking._NEXT_ID += 1
        self._guest = guest
        self._room = room
        self._checkInDate = check_in_date
        self._checkOutDate = check_out_date
        self._allocatedRoomNo = None
        self._status = "Pending"

        # Ensure the guest is not blacklisted
        if self._guest.isBlacklisted():
            raise BookingException("Guest is blacklisted")

        # Check-out date must be at least 1 day after check-in date
        if self._checkOutDate <= self._checkInDate:
            raise BookingException(
                "Check-out date must be at least 1 day after check-in date")

    @property
    def bookingID(self):
        return self._bookingID

    @property
    def checkInDate(self):
        return self._checkInDate

    @property
    def checkOutDate(self):
        return self._checkOutDate

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def passport(self):
        return self._guest.passport

    @property
    def roomType(self):
        return self._room.type

    @property
    def totalPrice(self):
        return self._room.fullprice * ((self._checkOutDate - self._checkInDate).days)

    def checkIn(self, allocatedRoomNo):
        if self._status != "Confirmed":
            raise BookingException(
                "Booking status must be Confirmed for check-in")
        diff = self._checkOutDate - self._checkInDate
        if diff.days <= 0:
            raise BookingException(
                "Check-in must be greater than the check-in date itself")
        if self._guest.isBlacklisted():
            raise BookingException("Guest is blacklisted")

        self._status = "Checked-In"
        self._allocatedRoomNo = allocatedRoomNo

    def __str__(self):
        room_str = str(self._room)
        total_price_str = f"Total Price: ${self._room.fullprice:.2f} x {(self._checkOutDate - self._checkInDate).days} nights = ${self.totalPrice:.2f}"
        return (f"Booking ID: {self._bookingID}\n"
                f"Passport Number: {self._guest.passport} Name: {self._guest.name}\n"
                f"Check-In/Out dates: {self._checkInDate.strftime('%d-%b-%Y')} / {self._checkOutDate.strftime('%d-%b-%Y')} "
                f"Booking Status: {self._status}\n"
                f"{room_str}\n{total_price_str}")
