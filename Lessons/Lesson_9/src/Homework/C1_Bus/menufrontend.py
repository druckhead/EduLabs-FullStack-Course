from menubackend import Menu
from os import system
from exceptions import *


class MainMenu:
    def __init__(self):
        pass

    @staticmethod
    def present():
        main_menu = Menu()
        try:
            while True:
                system("clear")
                main_menu.display_user_prompt()

                user_choice = input()
                match user_choice:
                    case '1':
                        system("clear")
                        while True:
                            password = input("Enter your password: ")
                            try:
                                main_menu.auth_pass(password)
                                main_menu.sign_in()
                                break
                            except TooManyWrongPasswordAttemptsError as err1:
                                print(err1)
                                break
                            except InvalidPasswordError as err2:
                                print(err2)
                                continue

                        if main_menu.signed_in:
                            main_menu.init_manager_menu()
                            system("clear")
                            main_menu.display_manager_actions()
                            while True:
                                actions_choice = input()
                                match actions_choice:
                                    case '1':
                                        main_menu.user_menu.add_route()
                                    case '2':
                                        main_menu.user_menu.delete_route()
                                    case '3':
                                        main_menu.user_menu.update_route()
                                    case '4':
                                        main_menu.user_menu.add_scheduled_ride()
                                    case '5':
                                        main_menu.sign_out()
                                        break
                    case '2':
                        main_menu.init_passenger_menu()
                        system("clear")
                        main_menu.display_passenger_actions()
                        while True:
                            actions_choice = input()
                            match actions_choice:
                                case '1':
                                    main_menu.user_menu.search_route()
                                case '2':
                                    main_menu.user_menu.report_delay()
                                case '3':
                                    main_menu.sign_out()
                                    break
                    case '3':
                        # main_menu.quit()
                        break
                    case _:
                        continue
        except KeyboardInterrupt:
            # main_menu.quit()
            exit(0)
