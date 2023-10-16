from RoomClass import *

# Firstly creating a deluxe room
try:
    super_single_bed = Bed("Super", 12.99, "Room with super single bed")
    deluxe_room = Room("Deluxe", super_single_bed, 19.99)
    deluxe_room.addAmenity(InRoomAmenity(
        "FRIDGE", "Mini Fridge (50L)", 4.59, 0.25))
    deluxe_room.addAmenity(InRoomAmenity(
        "CHAIR", "Foldable Chair (42cm x 38cm)", 2.59, 0.16))
    deluxe_room.addAmenity(InRoomAmenity(
        "DESK-W", "Writing desk (80cm x 55cm)", 3.99, 0.44))
    deluxe_room.addAmenity(InRoomAmenity(
        "IRON-B", "Iron and ironing board (128cm x 30cm)", 2.99, 0.4))

except (BookingException, MinFloorAreaException) as e:
    print(e)

try:
    single_bed = Bed("Single", 10.99, "Room with single bed")
    standard_room = Room("Standard", single_bed, 16.99)
    standard_room.addAmenity(SharedAmenity(
        "GYM-PEP", "Per entry pass to gym (Level 4-01)", 1.00))
    standard_room.addAmenity(InRoomAmenity(
        "FRIDGE", "Mini Fridge (50L)", 4.59, 0.25))
    standard_room.addAmenity(SharedAmenity(
        "WI-FI", "One-day Wi-Fi access", 1.00))
    standard_room.addAmenity(SharedAmenity(
        "GYM-PEP", "Per entry pass to gym (Level 4-01)", 1.00))
except (BookingException, MinFloorAreaException) as e:
    print(e)

print(deluxe_room)
print(standard_room)


try:
    deluxe_room.removeAmenity("FRIDGE")
    deluxe_room.removeAmenity("GYM-PEP")
except (BookingException, MinFloorAreaException) as e:
    print(e)
    print("\n")

try:
    standard_room.removeAmenity("GYM-PEP")
    standard_room.removeAmenity("GYM-PEP")
except (BookingException, MinFloorAreaException) as e:
    print(e)
    print("\n")

print(deluxe_room)
print(standard_room)
