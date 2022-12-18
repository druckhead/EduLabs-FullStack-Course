from datetime import datetime, timedelta
from busroute import BusRoute
from scheduledride import ScheduledRide
from exceptions import *


class BestBusCompany:
    def __init__(self) -> None:
        self.__routes: dict[str, dict[str, BusRoute | list[BusRoute]]] = {
            "line_num": {},
            "origin": {},
            "destination": {},
            "bus_stop": {},
        }

    def _validate_line_number(self, line_number: str) -> None:
        if line_number not in self.__routes["line_num"]:
            raise LineDoesntExistError(line_number)

    def add_route(self, line_num: str, origin: str, destination: str, stops: list[str]) -> None:
        num_stops = len(stops)
        if num_stops == 0:
            raise NotEnoughStopsError(num_stops)

        new_route = BusRoute(line_num, origin, destination, stops)
        self.__routes["line_num"][new_route.line_number] = new_route
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

    def delete_route(self, line_number: str) -> None:
        self._validate_line_number(line_number)

        route = self.__routes["line_num"][line_number]
        origin = route.origin
        destination = route.destination
        stops = route.stops

        poproute = None

        route_id_address = id(route)

        self.__routes["line_num"].pop(line_number)

        for o in self.__routes["origin"][origin]:
            if id(o) == route_id_address:
                poproute = self.__routes["origin"][origin].index(o)
                break
        self.__routes["origin"][origin].pop(poproute)
        if len(self.__routes["origin"][origin]) == 0:
            self.__routes["origin"].pop(origin)

        for d in self.__routes["destination"][destination]:
            if id(d) == route_id_address:
                poproute = self.__routes["destination"][destination].index(d)
                break
        self.__routes["destination"][destination].pop(poproute)
        if len(self.__routes["destination"][destination]) == 0:
            self.__routes["destination"].pop(destination)

        for stop in stops:
            for s in self.__routes["bus_stop"][stop]:
                if id(s) == route_id_address:
                    poproute = self.__routes["bus_stop"][stop].index(s)
                    break
            self.__routes["bus_stop"][stop].pop(poproute)
            if len(self.__routes["bus_stop"][stop]) == 0:
                self.__routes["bus_stop"].pop(stop)

    def update_route(self, line_number: str, origin: str = None, destination: str = None,
                     stops: list[str] = None) -> None:
        self._validate_line_number(line_number)

        route = self.__routes["line_num"][line_number]
        self.delete_route(line_number)
        if origin is not None:
            route.origin = origin
        if destination is not None:
            route.destination = destination
        if stops is not None:
            route.stops = stops

        self.add_route(line_number, route.origin, route.destination, route.stops)

    def add_scheduled_ride(self, line_number: str, origin_time: datetime, destination_time: datetime,
                           driver_name: str) -> None:
        self._validate_line_number(line_number)

        new_ride = ScheduledRide(origin_time, destination_time, driver_name)
        route = self.__routes["line_num"][line_number]
        route.scheduled_rides.append(new_ride)

    def search_route(self, line_num: str = None, origin: str = None, destination: str = None,
                     bus_stop: str = None) -> BusRoute | list[BusRoute]:
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

    def report_delay(self, line_number: str, ride_id: str, delay: timedelta) -> None:
        self._validate_line_number(line_number)
        rides = self.__routes["line_num"][line_number].scheduled_rides
        for ride in rides:
            if str(ride.ride_id) == ride_id:
                ride.delay = delay
                return
        raise RideIDDoesntExistError(ride_id)
