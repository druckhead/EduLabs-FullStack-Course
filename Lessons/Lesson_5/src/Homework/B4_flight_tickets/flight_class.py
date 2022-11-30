from utils import pretty_dict

__FLIGHT_CLASSES: dict[str] = {
    "1": "First Class",
    "2": "Business Class",
    "3": "Economy Class",
}


def __class_validator(__class: str) -> bool:
    if len(__class) == 0:
        print("\nError: You must choose a class.\n")
        return False
    if __class.isnumeric() is not True:
        print(f"\nError: {__class} is not a valid choice. Enter only 1 to 3\n")
        return False
    if (1 <= int(__class) <= 3) is not True:
        print(f"\nError: {__class} is not a valid choice. Enter only 1 to 3\n")
        return False
    return True


def get_customer_class() -> str:
    print(f"Which Class would you like to fly?\n"
          f"{pretty_dict(__FLIGHT_CLASSES, ')')}")
    __choice: str = input(">>> ")
    while __class_validator(__choice) is not True:
        print(f"Which Class would you like to fly?\n"
              f"{pretty_dict(__FLIGHT_CLASSES, ')')}")
        __choice: str = input(">>> ")

    __flight_class: str = __FLIGHT_CLASSES.get(__choice)

    return '_'.join(__flight_class.lower().split())
