from datetime import datetime, timedelta
from uuid import uuid4
from busroute import BusRoute
from scheduledride import ScheduledRide
from exceptions import *


class BestBusCompany:
    def __init__(self):
        self.__routes: dict[str, dict[str, BusRoute | list[BusRoute]]] = {
            "line_num": {},
            "origin": {},
            "destination": {},
            "bus_stop": {},
        }

    def _validate_line_number(self, line_number: str):
        if line_number not in self.__routes["line_num"]:
            raise LineDoesntExistError(line_number)

    def add_route(self, line_num: str, origin: str, destination: str, stops: list[str]):
        self._validate_line_number(line_num)

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

    def search_route(self, line_num: str = None, origin: str = None, destination: str = None,
                     bus_stop: str = None) -> BusRoute:
        if line_num is not None:
            self._validate_line_number(line_num)
            return self.__routes["line_num"][line_num]
        elif origin is not None:
            if origin not in self.__routes["origin"]:
                raise OriginDoesntExistError(origin)
            return self.__routes["origin"][origin]
        elif destination is not None:
            if destination not in self.__routes["destination"]:
                raise DestinationDoesntExistError(destination)
            return self.__routes["destination"][destination]
        elif bus_stop is not None:
            if bus_stop not in self.__routes["bus_stop"]:
                raise BusStopDoesntExistError(bus_stop)
            return self.__routes["bus_stop"][bus_stop]

        raise MissingSearchKeyError()

    def report_delay(self, line_number: str, ride_id: uuid4, delay: timedelta) -> None:
        self._validate_line_number(line_number)
        rides = self.__routes["line_num"][line_number].scheduled_rides
        for ride in rides:
            if ride.ride_id == ride_id:
                ride.delay = delay
                return
        raise RideIDDoesntExistError(ride_id)
