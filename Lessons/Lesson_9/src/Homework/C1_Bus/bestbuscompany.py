from datetime import datetime, timedelta
from src.Homework.C1_Bus.busroute import BusRoute
from src.Homework.C1_Bus.scheduledride import ScheduledRide
from exceptions import *


class BestBusCompany:
    def __init__(self):
        self.__routes: dict[str, dict[str, BusRoute | list[BusRoute]] | None] = {
            "line_num": None,
            "origin": None,
            "destination": None,
            "bus_stop": None,
        }

    def _validate_line_number(self, line_number: str):
        if line_number not in self.__routes["line_num"]:
            raise KeyError(f"Invalid line number: {line_number} does not exist"
                           f" in bus routes")

    def add_route(self, line_num: str, origin: str, destination: str, stops: list[str]):
        new_route = BusRoute(line_num, origin, destination, stops)
        self.__routes["line_num"] = {new_route.line_number: new_route}
        if new_route.origin not in self.__routes["origin"]:
            self.__routes["origin"][new_route.origin] = []
        self.__routes["origin"][new_route.origin].append(new_route)
        if new_route.destination not in self.__routes["destination"]:
            self.__routes["destination"][new_route.destination] = []
        self.__routes["destination"][new_route.destination].append(new_route)
        for stop in stops:
            if stop not in self.__routes["bus_stop"]:
                self.__routes["bus_stop"][stop] = []
            self.__routes["bus_stop"][stop].append(new_route)

    def delete_route(self, line_number: str):
        self._validate_line_number(line_number)

        route = self.__routes["line_num"][line_number]
        origin = route.origin
        destination = route.destination
        stops = route.stops

        del self.__routes["line_num"][line_number]
        del self.__routes["origin"][origin]
        del self.__routes["destination"][destination]
        for stop in stops:
            del self.__routes["bus_stop"][stop]

    def update_route(self, line_number: str, origin: str = None, destination: str = None, stops: list[str] = None):
        self._validate_line_number(line_number)
        route = self.__routes["line_number"][line_number]
        if origin is not None:
            route.origin = origin
        if destination is not None:
            route.destination = destination
        if stops is not None:
            route.stops = stops

    def add_scheduled_ride(self, line_number: str, origin_time: datetime, destination_time: datetime, driver_name: str):
        self._validate_line_number(line_number)
        new_ride = ScheduledRide(origin_time, destination_time, driver_name)
        route = self.__routes["line_num"][line_number]
        route.scheduled_rides.append(new_ride)


    def search_route(self, line_num: str = None, origin: str = None, destination: str = None, bus_stop: str = None) -> BusRoute:
        if line_num is not None:
            self._validate_line_number(line_num)
            return self.__routes["line_num"][line_num]
        elif origin is not None:
            if origin not in self.__routes["origin"]:
                raise KeyError()
            return self.__routes["origin"][origin]
        elif destination is not None:
            if destination not in self.__routes["destination"]:
                raise KeyError()
            return self.__routes["destination"][destination]
        elif bus_stop is not None:
            if bus_stop not in self.__routes["bus_stop"]:
                raise KeyError()
            return self.__routes["bus_stop"][bus_stop]

        raise MissingSearchKeyError()



    def report_delay(self, delay: timedelta):
        pass

