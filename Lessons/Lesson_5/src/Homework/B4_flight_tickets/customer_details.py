def __is_valid_name(__name: str) -> bool:
    return __name.isalpha()


def __input_name(__name_type: str) -> str:
    if __name_type == "first":
        input_str = f"Enter your {__name_type} name." \
                    "\n>>> "
    elif __name_type == "last":
        input_str = f"Enter your {__name_type} name." \
                    "\n>>> "

    __name = input(f"Enter your {__name_type} name.\n"
                   ">>> ").strip()

    while __is_valid_name(__name) is not True:
        print(f"\n{__name} is not a valid name.\n"
              f"Please only enter letters.\n")
        __name = input(f"Enter your {__name_type} name.\n"
                       ">>> ").strip()
    return __name


def __validate_full_name(__full_name: str) -> None:
    print(f"You entered '{__full_name}' is this your correct name? (Y/N)")
    __choice = input(">>> ").lower().strip()
    while __choice != 'y' and __choice != 'n':
        print("Invalid choice!\n"
              "Only enter 'Y' or 'N'\n")
        __choice = input(">>> ").lower().strip()
    if __choice == 'n':
        print()
        get_name()
    else:
        print()


def get_name() -> tuple[str, str]:
    __f_name = __input_name("first")
    print()
    __l_name = __input_name("last")
    print()

    __full_name = __f_name + " " + __l_name
    __validate_full_name(__full_name)

    return __f_name, __l_name
