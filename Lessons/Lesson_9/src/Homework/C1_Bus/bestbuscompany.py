from src.Homework.C1_Bus.busroute import BusRoute


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
        del self.__routes["line_num"][line_number]

    def update_route(self, line_number: str, origin: str = None, destination: str = None, stops: list[str] = None):
        route = self.__routes["line_number"][line_number]
        if origin is not None:
            route.origin = origin
        if destination is not None:
            route.destination = destination
        if stops is not None:
            route.stops = stops

    def add_scheduled_ride(self):
        pass

    def search_route(self):
        pass

    def report_delay(self):
        pass
