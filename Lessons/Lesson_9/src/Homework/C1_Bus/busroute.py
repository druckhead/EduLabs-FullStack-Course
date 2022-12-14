from scheduledride import ScheduledRide
from exceptions import NotALineNumberError


class BusRoute:
    def __init__(self, line_number: str, origin: str, destination: str, stops: list[str]) -> None:
        if not line_number.isnumeric():
            raise NotALineNumberError(line_number)
        self._line_number = line_number
        self._origin = origin
        self._destination = destination
        self._stops = stops
        self._scheduled_rides: list[ScheduledRide] = []

    @property
    def line_number(self) -> str:
        return self._line_number

    @property
    def origin(self) -> str:
        return self._origin

    @origin.setter
    def origin(self, new_origin: str):
        self._origin = new_origin

    @property
    def destination(self) -> str:
        return self._destination

    @destination.setter
    def destination(self, new_destination: str):
        self._destination = new_destination

    @property
    def stops(self) -> list[str]:
        return self._stops

    @property
    def scheduled_rides(self) -> list[ScheduledRide]:
        return self._scheduled_rides

    def __str__(self):
        return f"Line #{self.line_number}\n" \
               f"Origin: {self.origin}\n" \
               f"Destination: {self.destination}\n" \
               f"Stops: {self.stops}\n" \
               f"Scheduled Rides: {self.scheduled_rides}"

    def __repr__(self):
        return f"<BusRoute Line #: {self.line_number}, Origin: {self.origin}, Destination: {self.destination}>"