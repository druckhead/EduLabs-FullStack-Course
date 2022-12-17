import os.path
import pickle
from menubackend import Menu
from bestbuscompany import BestBusCompany
from usermenu import PassengerMenu, ManagerMenu
from os import system
from exceptions import *
from time import sleep


class MainMenu:
    def __init__(self):
        if os.path.exists("bus_company.pickle"):
            self._bus_company = self._load()
        else:
            self._bus_company = BestBusCompany()

    @staticmethod
    def display_user_prompt():
        print("Are you a passenger or manager?\n"
              "1. manager\n"
              "2. passenger\n"
              "3. quit\n"
              ">>> ", end="")

    def present(self):
        main_menu = Menu(self._bus_company)
        try:
            while True:
                system("clear")
                self.display_user_prompt()

                user_choice = input()
                match user_choice:
                    case '1':
                        system("clear")
                        manager_menu = ManagerMenu(self._bus_company)
                        while True:
                            password = input("Enter your password: ")
                            try:
                                manager_menu.auth_pass(password)
                                manager_menu.sign_in()
                                break
                            except TooManyWrongPasswordAttemptsError as err1:
                                print(err1)
                                sleep(1.5)
                                break
                            except InvalidPasswordError as err2:
                                print(err2)
                                sleep(0.25)
                                continue

                        if manager_menu.signed_in:
                            while True:
                                system("clear")
                                manager_menu.display_manager_actions()
                                actions_choice = input()
                                try:
                                    match actions_choice:
                                        case '1':
                                            manager_menu.add_route()
                                            pass
                                        case '2':
                                            manager_menu.delete_route()
                                            pass
                                        case '3':
                                            manager_menu.update_route()
                                        case '4':
                                            while True:
                                                try:
                                                    manager_menu.add_scheduled_ride()
                                                    break
                                                except ValueError:
                                                    print("Invalid Time")
                                                    sleep(1)
                                            pass
                                        case '5':
                                            manager_menu.sign_out()
                                            break
                                        case _:
                                            print("Invalid input. Please Choose from the options provided.")
                                            sleep(1)
                                            continue
                                except BaseKeyError as inputErr1:
                                    print(inputErr1)
                    case '2':
                        passenger_menu = PassengerMenu(self._bus_company)
                        while True:
                            system("clear")
                            passenger_menu.display_passenger_actions()
                            actions_choice = input()
                            try:
                                match actions_choice:
                                    case '1':
                                        route = passenger_menu.search_route()
                                        if type(route) is list:
                                            for r in route:
                                                print(r)
                                        else:
                                            print(route)
                                    case '2':
                                        # todo accept inputs and validate them before sending them as params in the functions
                                        passenger_menu.report_delay()
                                        pass
                                    case '3':
                                        passenger_menu.sign_out()
                                        break
                                    case _:
                                        print("Invalid input. Please Choose from the options provided.")
                                        sleep(1)
                                        continue
                            except BaseKeyError as inputErr2:
                                print(inputErr2)
                    case '3':
                        main_menu.quit()
                        break
                    case _:
                        print("Invalid input. Please Choose from the options provided.")
                        sleep(1)
                        continue
        except KeyboardInterrupt:
            main_menu.quit()
            exit(0)

    @staticmethod
    def _load():
        with open("bus_company.pickle", 'rb') as fh:
            bus_company = pickle.load(fh)

        return bus_company
