from src.Homework.C2_Classes_flat.room import Room, Bathroom, Balcony, Kitchen


class Flat:
    def __init__(self, flat_floor: int, flat_num: int, kitchen: Kitchen, rooms: list[Room] = None,
                 bathrooms: list[Bathroom] = None, balconies: list[Balcony] = None):
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.balconies = balconies
        self.kitchen = kitchen
        self.flat_floor = flat_floor
        self.flat_num = flat_num

    @property
    def get_floor(self) -> int:
        """
        Returns the floor number of the Flat
        :return: int
        """
        return self.flat_floor

    @property
    def get_room_num(self) -> int:
        """
        Returns the room number of the Flat
        :return: int
        """
        return self.flat_num

    def get_mum_rooms(self) -> int:
        """
        Calculate and return the number of rooms in the flat
        :return: int
        """
        return len(self.rooms)

    def get_num_bathrooms(self) -> int:
        """
        Calculate and return the number of bathrooms in the flat
        :return: int
        """
        return len(self.bathrooms)

    def get_total_living_space_size(self) -> float:
        """
        Calculate the living space area in sqm.\n
        (Not including Kitchen, Bathrooms nor Balconies)\n
        :return: float
        """
        size_sqm: float = 0
        for room in self.rooms:
            size_sqm += room.get_size_sqm
        return size_sqm

    def get_bathrooms_area(self) -> float:
        """
        Calculate the bathrooms area in sqm.\n
        :return: float
        """
        size_sqm = 0
        for bathroom in self.bathrooms:
            size_sqm += bathroom.get_size_sqm
        return size_sqm

    def get_balconies_area(self) -> float:
        """
        Calculate the balconies area in sqm.\n
        :return: float
        """
        size_sqm: float = 0
        for balcony in self.balconies:
            size_sqm += balcony.get_size_sqm
        return size_sqm

    def total_area_exclude_balconies(self) -> float:
        """
        Calculate the total area of the flat excluding the balconies
        :return: float
        """
        size_sqm = 0
        size_sqm += self.get_total_living_space_size()
        size_sqm += self.get_bathrooms_area()
        size_sqm += self.kitchen.get_size_sqm
        return size_sqm

    def calc_arnona(self, base_tariff: float):
        """
        Calculate the monthly arnona tariff
        :param base_tariff:
        :return: float
        """
        return base_tariff * (self.total_area_exclude_balconies()) + base_tariff * 0.75 * self.get_balconies_area()
