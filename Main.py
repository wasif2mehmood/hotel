from HotelClass import Hotel
from datetime import datetime
from BookingClass import *


try:
    room_name = input("Enter the room name: ")
    MyHotel = Hotel("Shining Star", room_name)
except FileNotFoundError:
    print("File not found")
    room_name = input("Enter the (correct) room name: ")
    MyHotel = Hotel("Shining Star", room_name)


def add_aminities(Room):
    try:
        MyHotel.printAmenities
        user_option = input("Enter the Amenity ID , you want to add:").upper()
        current_Amenity = MyHotel.getAmenity(user_option)
        if (current_Amenity == None):
            raise BookingException("There exists such no item code ")
        else:
            Room.addAmenity(current_Amenity)
    except BookingException as e:
        print(e)
        add_aminities(Room)


def search_booking():
    try:
        option = input(
            "Do you want to search by (I)D or (P)assport: or press e to exit: ")
        if option.upper() == "E":
            return
        if option.upper() == "I":
            booking_id = input("Enter booking ID: ")
            booking = MyHotel.searchBooking(booking_id)
        else:
            passport = input("Enter passport number: ")
            booking = MyHotel.searchBookingByPassport(passport)
        if booking == None:
            raise BookingException("No booking found")
        print("Booking found:\n")
        for bookings in booking:
            print(bookings)
    except ValueError:
        print("Invalid booking ID")
        print("\n")
        search_booking()
    except BookingException as e:
        print(e)
        print("\n")
    except IndexError:
        print("No booking found")
        print("\n")


def checkin_hotel():
    try:
        booking_id = input("Enter booking ID: ")
        Booking = MyHotel.searchBooking(booking_id)
        if Booking == None:
            raise BookingException("No booking found")
        print(Booking[0])
        room = input("Enter room number:  or e to exit:")
        if room.upper() == "E":
            print("Check in cancelled")
            return
        MyHotel.checkIn(booking_id, room)
        print("Check in successful")
    except ValueError:
        print("Invalid booking ID")
        checkin_hotel()
    except BookingException as e:
        print(e)
        checkin_hotel()
    except IndexError:
        print("Invalid booking ID")
        checkin_hotel()


def cancel_booking():
    try:
        selected_id = input("Enter booking ID: or e to exit to main menu: ")
        if selected_id.upper() == "E":
            return
        booking = MyHotel.searchBooking(selected_id)
        if booking == None:
            raise BookingException("No booking found")
        booking = booking[0]
        if booking == None:
            raise BookingException("No booking found")
        MyHotel.cancelBooking(selected_id)
        print("Booking cancelled")
    except BookingException as e:
        print(e)
        print("\n")
        cancel_booking()
    except ValueError:
        print("Invalid booking ID")
        print("\n")
        cancel_booking()
    except IndexError:
        print("Invalid booking ID")
        print("\n")
        cancel_booking()


def select_room():
    try:
        room_type = input(
            "Enter room type: (S) for Standard, (D) for Deluxe: ")
        if room_type.upper() == "S":
            room_type = "Standard"
            room_price = 23
        elif room_type.upper() == "D":
            room_type = "Deluxe"
            room_price = 19
        else:
            raise BookingException("Please enter S or D , To select room type")
        return room_type, room_price
    except BookingException as e:
        print(e)
        print("\n")
        select_room()


def select_bed():
    try:
        bed_type = input(
            "Enter bed type: (S) for Single, (D) for Super Single Bed: ")
        if bed_type.upper() == "S":
            bed_type = "Single"
            price = 4.73
            description = "Single bed"

        elif bed_type.upper() == "D":
            bed_type = "Super"
            price = 3.33
            description = "Super Single Bed"
        else:
            raise BookingException(
                "Please enter S or D to select the Bed of your choice")
        return bed_type, price, description
    except BookingException as e:
        print(e)
        print("\n")
        select_bed()


def select_guest():
    try:
        guest_id = (input("Enter PassPort Number: or e to exit to main menu: "))
        if guest_id.upper() == "E":
            return
        guest = MyHotel.searchGuest((guest_id))
        print("Guest selected:")
        print(guest)
        return guest
    except ValueError:
        print("Invalid guest ID")
        print("\n")
        select_guest()
    except BookingException as e:
        print(e)
        print("\n")
        select_guest()


def doBooking(MyHotel):

    guest = select_guest()
    if guest == None:
        return
    try:
        room_type, room_price = select_room()
        bed_type, bed_price, bed_description = select_bed()
        current_bed = Bed(bed_type, bed_price, bed_description)
        current_room = Room(room_type, current_bed, room_price)
        print("Room selected:")
        print(current_room)
        input("Press enter to continue")
        op = input("Do you want to add amenities? (Y/N): ")
        if op.upper() == "N":
            pass
        else:
            while True:
                print("Amenities available:")
                MyHotel.printAmenities()
                add_aminities(current_room)
                user_option = input(
                    "Do you want to add more amenities? (Y/N): ")
                if user_option.upper() == "N":
                    break

        check_in_date = input("\nEnter check-in date DD-MON-YY: ")
        check_out_date = input("Enter check-out date DD-MON-YY: ")
        check_in_date = datetime.strptime(check_in_date, "%d-%b-%Y").date()
        check_out_date = datetime.strptime(check_out_date, "%d-%b-%Y").date()
        CurrentBooking = Booking(
            guest, current_room, check_in_date, check_out_date)

        confirm_booking = input("Confirm booking? (Y/N): ")
        if confirm_booking.upper() == "N":
            print("Booking cancelled")
            return
        else:
            MyHotel.SubmitBooking(CurrentBooking)
            print("Booking successful")

    except BookingException as e:
        print(e)
        print("Booking failed")
        print("\n")
        doBooking(MyHotel)


def MainMenu():
    print("@@SAMI HOTEL MANAGEMENT SYSTEM@@")
    print("1. Submit Booking")
    print("2. Cancel Booking")
    print("3. Search Booking")
    print("4. Check-in")
    print("5. Exit")
    option = input("Enter option: ")
    if option == "1":
        doBooking(MyHotel)
    elif option == "2":
        cancel_booking()
    elif option == "3":
        search_booking()
    elif option == "4":
        checkin_hotel()
    elif option == "5":
        MyHotel.saveRoomAvailability("availablerooms.txt")
        print("Thank you for using the system")
        return
    else:
        print("Invalid option")
        MainMenu()
    if option != "5":
        print("\n")
        input("Press enter to continue\n")
        MainMenu()


MainMenu()
