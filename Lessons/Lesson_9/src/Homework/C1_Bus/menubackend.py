import os.path
import pickle
from enum import Enum, auto
from exceptions import *
from bestbuscompany import BestBusCompany
from usermenu import PassengerMenu, ManagerMenu
from time import sleep


class UserType(Enum):
    MANAGER = auto()
    PASSENGER = auto()


class Menu:
    __PASSWORD = "RideWithUs!"
    __MAX_WRONG_PASSWORD = 3

    def __init__(self):
        if not os.path.exists("bus_company.pickle"):
            self._bus_company = BestBusCompany()
        else:
            self._load()

        self._signed_in = False
        self._wrong_password_count = 0
        self._user_type: UserType | None = None
        self._user_menu: PassengerMenu | ManagerMenu | None = None

    @property
    def signed_in(self):
        return self._signed_in

    @property
    def max_password_attempts(self):
        return self.__MAX_WRONG_PASSWORD

    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, user: UserType):
        if user == UserType.MANAGER:
            self._user_type = UserType.MANAGER
        else:
            self._user_type = UserType.PASSENGER

    @property
    def user_menu(self):
        return self._user_menu

    @staticmethod
    def display_user_prompt():
        print("Are you a passenger or manager?\n"
              "1. manager\n"
              "2. passenger\n"
              "3. quit\n"
              ">>> ", end="")

    @staticmethod
    def display_manager_actions():
        print("Actions for Manager\n"
              "1. Add Route\n"
              "2. Delete Route\n"
              "3. Update Route\n"
              "4. Add Scheduled Ride\n"
              "5. Sign Out\n"
              ">>> ", end="")

    @staticmethod
    def display_passenger_actions():
        print("Actions for Passenger\n"
              "1. Search Route\n"
              "2. Report Delay\n"
              "3. Sign Out\n"
              ">>> ", end="")

    def init_manager_menu(self):
        self._user_menu = ManagerMenu()

    def init_passenger_menu(self):
        self._user_menu = PassengerMenu()

    def auth_pass(self, password: str):
        if self.__PASSWORD != password:
            self._wrong_password_count += 1
            if self._wrong_password_count == self.__MAX_WRONG_PASSWORD:
                self._wrong_password_count = 0
                raise TooManyWrongPasswordAttemptsError()
            raise InvalidPasswordError()

    def quit(self):
        self._save()

    def sign_in(self):
        self._wrong_password_count = 0
        print("Signing In")
        self._signed_in = True
        sleep(1)
        print("Signed In")
        sleep(1)

    def sign_out(self):
        print("Signing Out")
        self._signed_in = False
        sleep(1)
        print("Signed Out")
        sleep(1)

    def _load(self):
        try:
            with open("bus_company.pickle", 'rb') as fh:
                self._bus_company = pickle.load(fh)
        except FileNotFoundError as err:
            print(err)

    def _save(self):
        try:
            with open("bus_company.pickle", 'wb') as fh:
                pickle.dump(self._bus_company, fh)
        except FileNotFoundError as err:
            print(err)
