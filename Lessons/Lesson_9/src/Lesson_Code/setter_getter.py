class Age:
    def __init__(self, years: int, months: int, days: int):
        self.__years = years
        self.__months = months
        self.__days = days

    @property
    def get_years(self):
        return self.__years

    @get_years.setter
    def get_years(self, value):
        if value < 0:
            raise ValueError
        self.__years = value

    @property
    def get_month(self):
        return self.__months

    @get_month.setter
    def get_month(self, value):
        if value < 0:
            raise ValueError
        self.__months = value

    @property
    def get_day(self):
        return self.__days

    @get_day.setter
    def get_day(self, value):
        if value < 0:
            raise ValueError
        self.__days = value

    def __str__(self):
        return f"<Age>: Y={self.__years}, M={self.__months}, D={self.__days}"

    def __repr__(self):
        return f"<Age>: Y={self.__years}"


class Person:
    def __init__(self, name: str, age: Age):
        self.__name = name
        self.__age = age

    @property
    def get_name(self):
        return self.__name

    @property
    def get_age(self):
        return self.__age
