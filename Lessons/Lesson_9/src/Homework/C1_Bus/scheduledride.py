from datetime import datetime, timedelta
from uuid import uuid4


class ScheduledRide:
    def __init__(self, origin_time: datetime, destination_time: datetime, driver_name: str):
        self._ride_id = uuid4()
        self._origin_time = origin_time
        self._destination_time = destination_time
        self._driver_name = driver_name
        self._delay: timedelta | None = None

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
    def delay(self) -> timedelta | None:
        return self._delay

    @delay.setter
    def delay(self, delay: timedelta):
        self._delay = delay

    def __str__(self):
        return f"Ride ID: {self.ride_id}\n" \
               f"Origin Time: {self.origin_time}\n" \
               f"Destination Time: {self.destination_time}\n" \
               f"Driver Name: {self.driver_name}" \
               f"Delay: {self.delay}"

    def __repr__(self):
        return f"<Ride Id: {self.ride_id} Origin Time: {self.origin_time.time()}, " \
               f"Destination Time: {self.destination_time.time()}, Delay: {self.delay}>"
