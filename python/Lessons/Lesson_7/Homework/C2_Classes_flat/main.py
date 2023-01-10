from src.Homework.C2_Classes_flat.building import Building
from src.Homework.C2_Classes_flat.address import Address

from src.Homework.C2_Classes_flat.room import Room, Bathroom, Kitchen, Balcony
from src.Homework.C2_Classes_flat.flat import Flat

if __name__ == "__main__":
    address = Address("USA", "San Francisco", "Infinity Loop", "1")
    b1 = Building(address)

    r1 = Room(60)
    k1 = Kitchen(10)
    balconies = [Balcony(4)]
    rooms = [Room(20), Room(40), Room(25)]
    bathrooms = [Bathroom(10, True, True, True, True), Bathroom(5, True, True, True, True)]

    f1 = Flat(1, 12, k1, rooms, bathrooms, balconies)
    b1.add_apartment(f1)
    print(f1.calc_arnona(48))
