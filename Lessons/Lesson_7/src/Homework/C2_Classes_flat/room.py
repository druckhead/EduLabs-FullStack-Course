class Room:
    def __init__(self, size_sqm: float):
        self.size_sqm = size_sqm

    @property
    def get_size_sqm(self):
        """
        Returns the size of the room in sqm
        :return: float
        """
        return self.size_sqm

    @property
    def set_size_sqm(self, size_sqm: float):
        """
        Sets the size of the room in sqm
        :param size_sqm: float
        :return: None
        """
        if size_sqm <= 0:
            raise ValueError
        self.size_sqm = size_sqm


class Bathroom(Room):
    def __init__(self, size_sqm: float, has_toilet: bool, has_sink: bool, has_bath: bool, has_shower: bool):
        super().__init__(size_sqm)
        self.has_toilet = has_toilet
        self.has_sink = has_sink
        self.has_bath = has_bath
        self.has_shower = has_shower


class Balcony(Room):
    def __init__(self, size_sqm):
        self.size_sqm = size_sqm


class Kitchen(Room):
    def __init__(self, size_sqm: float):
        super().__init__(size_sqm)
