from src.Homework.C1_Bus.scheduledride import ScheduledRide


class BusRoute:
    def __init__(self, line_number: str, origin: str, destination: str, stops: list[str]) -> None:
        if not line_number.isnumeric():
            raise ValueError(f"Invalid input of: {line_number}. Expected numeric line number")
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