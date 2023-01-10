from src.Homework.C2_Classes_flat.flat import Flat
from src.Homework.C2_Classes_flat.address import Address


class Building:
    def __init__(self, address: Address):
        # apartments => dict{ key: floor, value: dict{ flat_num: Flat } }
        self.apartments: dict[int, dict[int, Flat]] = {}
        self.address = address

    def add_apartment(self, flat: Flat) -> None:
        """
        Add a flat to the building if it doesn't already exist in it
        :param flat:
        :return:
        """
        if self.apartments.get(flat.get_floor) is None:
            self.apartments[flat.get_floor] = {}
        self.apartments[flat.get_floor] = {
            flat.flat_num: flat
        }
