from bestbuscompany import BestBusCompany
from datetime import timedelta, datetime
from time import sleep
from menubackend import Menu
from exceptions import *
from busroute import BusRoute


class PassengerMenu(Menu):
    def __init__(self, bus_company: BestBusCompany) -> None:
        super().__init__(bus_company)

    @staticmethod
    def display_passenger_actions() -> None:
        print("Actions for Passenger\n"
              "1. Search Route\n"
              "2. Report Delay\n"
              "3. Sign Out\n"
              ">>> ", end="")

    def search_route(self) -> BusRoute | list[BusRoute]:
        line_num = origin = destination = bus_stop = None
        print("Search by\n"
              "1. Line Num\n"
              "2. Origin Station\n"
              "3. Destination Station\n"
              "4. Bus Stop")
        while True:
            query_choice = input(">>> ")
            match query_choice:
                case '1':
                    line_num = input("Enter a line number: ")
                    if not line_num.isnumeric():
                        raise NotALineNumberError(line_num)
                    break
                case '2':
                    origin = input("Enter an origin station: ")
                    break
                case '3':
                    destination = input("Enter a destination destination")
                    break
                case '4':
                    bus_stop = input("Enter a bus stop: ")
                    break
                case _:
                    continue

        return self.bus_company.search_route(line_num, origin, destination, bus_stop)

    def report_delay(self) -> None:
        route = self.search_route()
        scheduled_rides = route.scheduled_rides
        for i, ride in enumerate(scheduled_rides):
            print(f"{i + 1}. {ride.ride_id}", sep=",", end="")
        print()
        print("Choose a ride using the ride id above")
        ride_id = input(">>> ")
        print("Enter the delay in minutes")
        delay_str = input(">>> ")
        if not delay_str.isnumeric():
            raise NotAValidDelayError(delay_str)
        delay_int = int(delay_str)
        delay = timedelta(minutes=delay_int)

        self.bus_company.report_delay(route.line_number, ride_id, delay)
        print(f"Delay reported for line #{route.line_number} at route id: {ride_id}")

    @staticmethod
    def sign_out() -> None:
        print("Signing Out")
        sleep(1)
        print("Signed Out")
        sleep(1)


class ManagerMenu(Menu):
    __PASSWORD = "RideWithUs!"
    __MAX_WRONG_PASSWORD = 3

    def __init__(self, bus_company: BestBusCompany) -> None:
        super().__init__(bus_company)
        self._signed_in = False
        self._wrong_password_count = 0

    @property
    def signed_in(self) -> bool:
        return self._signed_in

    @property
    def max_password_attempts(self) -> int:
        return self.__MAX_WRONG_PASSWORD

    @staticmethod
    def display_manager_actions() -> None:
        print("Actions for Manager\n"
              "1. Add Route\n"
              "2. Delete Route\n"
              "3. Update Route\n"
              "4. Add Scheduled Ride\n"
              "5. Sign Out\n"
              ">>> ", end="")

    def add_route(self) -> None:
        line_num = input("Enter a line number: ")
        if not line_num.isnumeric():
            raise NotALineNumberError(line_num)
        origin = input("Enter an origin station")
        destination = input("Enter a destination station")
        stops_un_formatted = input("Enter stops separated by a comma")
        stops = stops_un_formatted.split(',')

        self.bus_company.add_route(line_num, origin, destination, stops)
        print(f"Added route line# {line_num}")

    def delete_route(self) -> None:
        line_num = input("Enter a line number: ")
        if not line_num.isnumeric():
            raise NotALineNumberError(line_num)
        choice = input(f"Are you sure you want to delete line# {line_num}? (Y/N)").lower()
        while choice != 'y' and choice != 'n':
            print("Invalid input")
            choice = input(f"Are you sure you want to delete line# {line_num}? (Y/N)").lower()
        if choice == 'y':
            self.bus_company.delete_route(line_num)
            print(f"Deleted route line# {line_num}")
        else:
            print(f"Did not delete route; line #{line_num}")

    def update_route(self) -> None:
        origin = destination = stops = None
        line_num = input("Enter a line number: ")
        if not line_num.isnumeric():
            raise NotALineNumberError(line_num)
        print("What would you like to update\n"
              "1. Origin\n"
              "2. Destination\n"
              "3. Stops")
        while True:
            choice = input(">>> ")
            match choice:
                case '1':
                    origin = input("Enter an origin station")
                    choice_str = "origin"
                    updated_val = origin
                    break
                case '2':
                    destination = input("Enter a destination station")
                    choice_str = "destination"
                    updated_val = destination
                    break
                case '3':
                    stops_un_formatted = input("Enter stops separated by a comma")
                    stops = stops_un_formatted.split(',')
                    choice_str = "stops"
                    updated_val = stops
                    break
                case _:
                    continue

        self.bus_company.update_route(line_num, origin, destination, stops)
        print(f"Updated {choice_str} for line #{line_num}.")

    def add_scheduled_ride(self) -> None:
        line_num = input("Enter a line number: ")
        if not line_num.isnumeric():
            raise NotALineNumberError(line_num)
        origin_time_str = input("Enter an origin time (DD/MM/YYYY HH:MM:SS): ")
        origin_time = datetime.strptime(origin_time_str, "%d/%m/%Y %H:%M:%S")

        destination_time_str = input("Enter a destination time (DD/MM/YYYY HH:MM:SS): ")
        destination_time = datetime.strptime(destination_time_str, "%d/%m/%Y %H:%M:%S")

        driver_name = input("Enter the driver name")

        self.bus_company.add_scheduled_ride(line_num, origin_time, destination_time, driver_name)
        print(f"Added scheduled ride to route line# {line_num}")

    def auth_pass(self, password: str) -> None:
        if self.__PASSWORD != password:
            self._wrong_password_count += 1
            if self._wrong_password_count == self.__MAX_WRONG_PASSWORD:
                self._wrong_password_count = 0
                raise TooManyWrongPasswordAttemptsError()
            raise InvalidPasswordError()

    def sign_in(self) -> None:
        self._wrong_password_count = 0
        print("Signing In")
        self._signed_in = True
        sleep(1)
        print("Signed In")
        sleep(1)

    def sign_out(self) -> None:
        print("Signing Out")
        self._signed_in = False
        sleep(1)
        print("Signed Out")
        sleep(1)
