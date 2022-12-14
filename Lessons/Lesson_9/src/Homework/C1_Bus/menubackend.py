import os.path
from datetime import datetime
import pickle
from src.Homework.C1_Bus.bestbuscompany import BestBusCompany
from src.Homework.C1_Bus.usermenu import PassengerMenu, ManagerMenu


class MainMenu:
    __PASSWORD = "RideWithUs!"

    def __init__(self):
        self._bus_company = BestBusCompany()
        self._user = None

    def _load(self):
        try:
            with open("bus_company.pickle", 'rb') as fh:
                self._bus_company = pickle.load(fh)
        except FileNotFoundError as err:
            print(err)

    def _save(self):
        try:

    def main(self):
        self._user = ManagerMenu()
        self._user.add_route(self._bus_company, "1", "Tel Aviv", "Jerusalem", ["yaffo", "yahud"])
        self._user.add_scheduled_ride(self._bus_company, "1", datetime(year=2022, month=12, day=14, hour=14, minute=30),
                                      datetime(year=2022, month=12, day=14, hour=16, minute=0),
                                      "Jesus")
        self._user = PassengerMenu()
        route = self._user.search_route(self._bus_company, "1")
        print(route)
        self._user = ManagerMenu()
        self._user.delete_route(self._bus_company, "1")

        self._user = PassengerMenu()
        try:
            route = self._user.search_route(self._bus_company, "1")
        except KeyError as e:
            print()
            print(e)


if __name__ == '__main__':
    mainmenu = MainMenu()
    mainmenu.main()
