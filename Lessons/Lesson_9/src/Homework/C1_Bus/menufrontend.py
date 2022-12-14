from menubackend import Menu
from os import system
from exceptions import *
from time import sleep


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
                                sleep(1.5)
                                break
                            except InvalidPasswordError as err2:
                                print(err2)
                                sleep(0.25)
                                continue

                        if main_menu.signed_in:
                            main_menu.init_manager_menu()
                            while True:
                                system("clear")
                                main_menu.display_manager_actions()
                                actions_choice = input()
                                match actions_choice:
                                    case '1':
                                        # todo accept inputs and validate them
                                        #  before sending them as params in the functions
                                        main_menu.user_menu.add_route()
                                    case '2':
                                        # todo accept inputs and validate them before sending them as params in the functions
                                        main_menu.user_menu.delete_route()
                                    case '3':
                                        # todo accept inputs and validate them before sending them as params in the functions
                                        main_menu.user_menu.update_route()
                                    case '4':
                                        # todo accept inputs and validate them before sending them as params in the functions
                                        main_menu.user_menu.add_scheduled_ride()
                                    case '5':
                                        # todo accept inputs and validate them before sending them as params in the functions
                                        main_menu.sign_out()
                                        break
                                    case _:
                                        print("Invalid input. Please Choose from the options provided.")
                                        sleep(1)
                                        continue
                    case '2':
                        main_menu.init_passenger_menu()
                        while True:
                            system("clear")
                            main_menu.display_passenger_actions()
                            actions_choice = input()
                            match actions_choice:
                                case '1':
                                    # todo accept inputs and validate them before sending them as params in the functions
                                    main_menu.user_menu.search_route()
                                case '2':
                                    # todo accept inputs and validate them before sending them as params in the functions
                                    main_menu.user_menu.report_delay()
                                case '3':
                                    # todo accept inputs and validate them before sending them as params in the functions
                                    main_menu.sign_out()
                                    break
                                case _:
                                    print("Invalid input. Please Choose from the options provided.")
                                    sleep(1)
                                    continue
                    case '3':
                        # main_menu.quit()
                        break
                    case _:
                        print("Invalid input. Please Choose from the options provided.")
                        sleep(1)
                        continue
        except KeyboardInterrupt:
            # main_menu.quit()
            exit(0)
