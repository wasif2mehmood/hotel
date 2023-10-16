from datetime import datetime, timedelta
from RoomClass import *


class Hotel:
    def __init__(self, name, roomFilename):
        self._name = name
        self._guests = self.setupGuests()
        self._amenities = self.setupAmenities()
        self._roomAvailability = self.setupRoomAvailability(roomFilename)
        self._bookings = {}

    @property
    def rooms(self):
        return self._roomAvailability

    @property
    def amenities(self):
        return self._amenities

    @property
    def guests(self):
        return self._guests

    def printGuests(self):
        for guest in self._guests.values():
            print(guest)
        print("\n")

    def printAmenities(self):
        for amenity in self._amenities:
            print(amenity)
        print("\n")

    def printRooms(self):
        for date, roomCount in self._roomAvailability.items():
            print(f"{date}: {roomCount}")

    def printBookings(self):
        for booking in self._bookings.values():
            print(booking)

    def setupGuests(self):
        guests = {}
        infile = open("Guests.txt", "r")
        for line in infile:
            pp, name, country, sami_points = line.split(",")
            guests[pp.strip()] = Guest(
                pp.strip(), name.strip(), country.strip())
        infile.close()
        infile = open("Blacklist.txt", "r")
        for line in infile:
            pp, dateReported, reason = line.split(",")
            g = guests.get(pp.strip())
            if g is not None:
                g.blacklist(datetime.strptime(dateReported.strip(), "%d-%b-%Y").date(),
                            reason.strip())
        infile.close()
        return guests

    def setupAmenities(self):

        amenities = []
        infile = open("SharedAmenity.txt", "r")
        for line in infile:
            itemCode, desc, price = line.split(",")
            amenities.append(SharedAmenity(itemCode, desc, float(price)))
        infile.close()
        infile = open("InRoomAmenity.txt", "r")
        for line in infile:
            itemCode, desc, price, floorArea = line.split(",")
            amenities.append(InRoomAmenity(itemCode, desc, float(price),
                                           float(floorArea)))
        infile.close()
        return amenities

    def setupRoomAvailability(self, filename):

        roomAvailability = {}
        infile = open(filename, "r")
        for line in infile:
            dateString, standardCount, deluxeCount = line.split(",")
            thisDate = datetime.strptime(dateString, "%d-%b-%Y").date()
            roomAvailability[thisDate] = [
                int(standardCount), int(deluxeCount)]
        infile.close()
        return roomAvailability

    def saveRoomAvailability(self, filename):

        outfile = open(filename, "w")
        for k, v in self._roomAvailability.items():
            print("{},{},{}".format(k.strftime(
                "%d-%b-%Y"), v[0], v[1]), file=outfile)
        outfile.close()

    def searchGuest(self, passport):

        for guest in self._guests.values():

            if guest.passport == passport:
                return guest
        raise BookingException("Guest not found")

    def checkRoomAvailability(self, room_type, start, end):
        diff = end - start
        if diff.days < 0:
            raise BookingException("Invalid date range")
        cureent_date = start
        while cureent_date <= end:
            std_count, del_count = self._roomAvailability[cureent_date][
                0], self._roomAvailability[cureent_date][1]
            if room_type == "Standard":
                if std_count == 0:
                    return False
            elif room_type == "Deluxe":
                if del_count == 0:
                    return False
            cureent_date += timedelta(days=1)

    def listAmenity(self):
        amenities = ""
        for amenity in self._amenities:
            amenities += str(amenity) + "\n"
        return amenities

    def getAmenity(self, itemCode):
        for amenity in self._amenities:
            if amenity.itemCode == itemCode:
                return amenity
        return None

    def searchBooking(self, bookingID):
        bookings = []
        for booking in self._bookings.values():
            if booking.bookingID == bookingID:
                bookings.append(booking)
        return bookings

    def searchBookingByPassport(self, passport):
        bookings = []
        for booking in self._bookings.values():
            if booking._guest.passport == passport:
                bookings.append(booking)
        return bookings

    def SubmitBooking(self, booking):
        try:
            if booking.status != "Pending":
                raise BookingException("Booking is not pending")
            room_type = booking.roomType
            check_in_date = booking.checkInDate
            check_out_date = booking.checkOutDate

            availibility = self.checkRoomAvailability(
                room_type, check_in_date, check_out_date)
            if availibility == False:
                raise BookingException("Room are  not available")
            current_date = check_in_date
            while current_date <= check_out_date:
                std_count, del_count = self._roomAvailability[current_date][
                    0], self._roomAvailability[current_date][1]

                if room_type == "Standard":
                    std_count -= 1

                else:
                    del_count -= 1
                self._roomAvailability[current_date] = [std_count, del_count]

                current_date += timedelta(days=1)
            booking.status = "Confirmed"
            self._bookings[booking.bookingID] = booking
        except KeyError as e:
            raise BookingException("No booking found")

    def cancelBooking(self, bookingID):
        booking = self.searchBooking(bookingID)
        booking = booking[0]
        if booking is None:
            raise BookingException("Booking not found")
        if booking.status != "Confirmed":
            raise BookingException(
                "Booking is either cancelled or has been checked in")
        booking.status = "Cancelled"
        room_type = booking.roomType
        check_in_date = booking.checkInDate
        check_out_date = booking.checkOutDate
        current_date = check_in_date
        while current_date <= check_out_date:
            std_count, del_count = self._roomAvailability[current_date][
                0], self._roomAvailability[current_date][1]
            if room_type == "Standard":
                std_count += 1
            else:
                del_count += 1
            self._roomAvailability[current_date] = [std_count, del_count]
            current_date += timedelta(days=1)

    def checkIn(self, bookingID, allocatedRoomNo):
        for booking in self._bookings.values():
            if booking.bookingID == bookingID:
                booking.checkIn(allocatedRoomNo)
                return
