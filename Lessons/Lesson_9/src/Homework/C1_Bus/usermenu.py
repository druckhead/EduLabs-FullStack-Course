from bestbuscompany import BestBusCompany
from datetime import timedelta, datetime
from uuid import uuid4


class PassengerMenu:
    def __init__(self):
        pass

    @staticmethod
    def search_route(bus_company: BestBusCompany, line_num: str = None, origin: str = None, destination: str = None,
                     bus_stop: str = None):
        return bus_company.search_route(line_num, origin, destination, bus_stop)

    @staticmethod
    def report_delay(bus_company: BestBusCompany, line_num: str, ride_id: uuid4, delay: timedelta):
        bus_company.report_delay(line_num, ride_id, delay)


class ManagerMenu:
    def __init__(self):
        pass

    @staticmethod
    def add_route(bus_company: BestBusCompany, line_num: str, origin: str, destination: str, stops: list[str]):
        bus_company.add_route(line_num, origin, destination, stops)

    @staticmethod
    def delete_route(bus_company: BestBusCompany, line_num: str):
        bus_company.delete_route(line_num)

    @staticmethod
    def update_route(bus_company: BestBusCompany, line_num: str = None, origin: str = None, destination: str = None,
                     stops: list[str] = None):
        bus_company.update_route(line_num, origin, destination, stops)

    @staticmethod
    def add_scheduled_ride(bus_company: BestBusCompany, line_num: str, origin_time: datetime,
                           destination_time: datetime, driver_name: str):
        bus_company.add_scheduled_ride(line_num, origin_time, destination_time, driver_name)
