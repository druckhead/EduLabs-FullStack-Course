from datetime import datetime
from enum import Enum


class RideType(Enum):
    short = 15
    medium = 40
    long = -1


class RidePrice(Enum):
    short = 5.5
    medium = 12
    long = 23


class RavKav:
    def __init__(self, holder_id: str, holder_name: str, balance: float = 0):
        self.__holder_id = holder_id
        self.__holder_name = holder_name
        self.__balance = balance

        self.__dates_log: dict[datetime, int] = {}
        self.__ride_type_log: dict[RideType, int] = {}

    @property
    def get_holder_id(self) -> str:
        return self.__holder_id

    @property
    def get_holder_name(self) -> str:
        return self.__holder_name

    @property
    def get_balance(self) -> float:
        return self.__balance

    @get_balance.setter
    def get_balance(self, value) -> None:
        if value < 0:
            raise ValueError
        self.__balance = value

    def top_up(self, amount: float) -> None:
        if amount < 0:
            raise ValueError
        self.get_balance = (amount + self.__balance)

    def use_balance(self, amount: float) -> None:
        if self.__balance - amount < 0:
            raise ValueError
        self.get_balance = (self.__balance - amount)

    def ride(self, ride_km: int, date: datetime.date) -> None:
        if ride_km <= RideType.short.value:
            self.use_balance(RidePrice.short.value)
            self.update_num_rides_by_type(RideType.short)
        elif ride_km <= RideType.medium.value:
            self.use_balance(RidePrice.medium.value)
            self.update_num_rides_by_type(RideType.medium)
        else:
            self.use_balance(RidePrice.long.value)
            self.update_num_rides_by_type(RideType.long)
        self.update_num_rides_by_date(date)

    def get_num_rides_by_date(self, date: datetime.date) -> int:
        if date not in self.__dates_log:
            raise KeyError
        return self.__dates_log[date]

    def update_num_rides_by_date(self, date: datetime.date) -> None:
        if date not in self.__dates_log:
            self.__dates_log[date] = 0
        self.__dates_log[date] += 1

    def get_num_rides_by_type(self, ride_type: RideType) -> int:
        if ride_type not in self.__ride_type_log:
            raise KeyError
        return self.__ride_type_log[ride_type]

    def update_num_rides_by_type(self, ride_type: RideType) -> None:
        if ride_type not in self.__ride_type_log:
            self.__ride_type_log[ride_type] = 0
        self.__ride_type_log[ride_type] += 1

    def display_num_rides_by_dates_log(self) -> None:
        print("Rides by Date")
        for k, v in self.__dates_log.items():
            print(f"Date: {k}")
            print(f"\tNumber of rides: {v}")
        return

    def display_num_rides_by_type_log(self) -> None:
        print("Rides by Type")
        for k, v in self.__ride_type_log.items():
            print(f"Type: {k.name}")
            print(f"\tNumber of rides: {v}")
        return

    def __str__(self):
        to_str = f"<RavKav: id={self.__holder_id}>\n" \
                 f"Name: {self.__holder_name}\n" \
                 f"Balance: {self.__balance}"
        return to_str

    def __repr__(self):
        return f"<RavKav: id={self.__holder_id}>"
