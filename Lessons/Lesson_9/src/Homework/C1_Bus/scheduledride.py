from datetime import datetime, timedelta
from uuid import uuid4


class ScheduledRide:
    def __init__(self, origin_time: datetime, destination_time: datetime, driver_name: str):
        self._ride_id = uuid4()
        self._origin_time = origin_time
        self._destination_time = destination_time
        self._driver_name = driver_name
        self._delays: timedelta | None = None

    @property
    def ride_id(self) -> uuid4:
        return self._ride_id

    @property
    def origin_time(self) -> datetime:
        return self._origin_time

    @origin_time.setter
    def origin_time(self, new_time: datetime):
        self._origin_time = new_time

    @property
    def destination_time(self) -> datetime:
        return self._destination_time

    @destination_time.setter
    def destination_time(self, new_time: datetime):
        self._destination_time = new_time

    @property
    def driver_name(self) -> str:
        return self._driver_name

    @property
    def delays(self) -> timedelta | None:
        return self._delays

    @delays.setter
    def delays(self, delay: timedelta):
        self.delays = delay
