from AmenityClasses import SharedAmenity, InRoomAmenity

if __name__ == "__main__":
    Amenities = []
    Amenities.append(SharedAmenity(
        "BIZ-PEP", "Per entry pass to business centre (Level 3-03)", 2.00))
    Amenities.append(SharedAmenity(
        "HI-TEA", "Hi-Tea buffet at Sun café (Level 1-01 2pm to 4pm)", 11.99))
    Amenities.append(InRoomAmenity(
        "DESK-W", "Writing desk(80cm x 55cm)", 3.99, 0.44))
    Amenities.append(InRoomAmenity(
        "IRON-B", "Iron and ironing board (128cm x 30cm)", 2.99, 0.4))
    total_price = 0
    total_floor_area = 0
    for amenity in Amenities:
        print(amenity)
        total_price += amenity.price
        total_floor_area += amenity.getFloorArea()
    print("Total price: ${:.2f}".format(total_price))
    print("Total floor area: {:.2f} sqm".format(total_floor_area))
