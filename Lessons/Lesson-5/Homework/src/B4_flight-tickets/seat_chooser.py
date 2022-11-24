from utils import pretty_layout
import pricing


def print_pricing(__class: str) -> None:
    match __class:
        case "first_class":
            print(pricing.__FIRST)
        case "business_class":
            print(pricing.__BUSINESS)
        case "economy_class":
            print(pricing.__ECONOMY)
    return


def __is_near_window(__class: str, __seat: str) -> bool:
    match __class:
        case 'economy_class':
            return __seat == 'A' or __seat == "F"
        case _:
            return __seat == 'A' or __seat == "D"


def __row_validator(__row: str, __min_row: int, __max_row: int) -> bool:
    if len(__row) == 0:
        print("\nThis field is required. Please fill it out!")
        print()
        return False
    if __row.isnumeric():
        if __min_row <= int(__row) <= __max_row:
            return True
        else:
            print(f"\nError: Only numbers between {__min_row} and {__max_row} are available.")
            print()
            return False
    elif ' ' in __row:
        print("Error: spaces not supported.")
        print()
        return False
    elif __row.isalpha():
        print(f"\nError: Only numbers between {__min_row} and {__max_row} are available.")
        print()
        return False
    elif len(__row) > 1 and __row[0] == '-':
        print("\nRows do NOT negative numbers.")
        print()
        return False
    else:
        print("\nSpecial characters are not supported for Row number.")
        print()
        return False


def __row_input(__min_seat: int, __max_seat: int) -> int:
    __input_string = "Where would you like to to sit?\n" \
                     f"Choose: Rows {__min_seat} - {__max_seat}\n" \
                     ">>> "

    __choice = input(__input_string)
    while __row_validator(__choice, __min_seat, __max_seat) is False:
        __choice = input(__input_string)

    return int(__choice)


def choose_row(__class: str) -> int:
    print()
    __choice: int = 0
    match __class:
        case "first_class":
            min_seat = 1
            max_seat = 4
            print_pricing(__class)
            print()
            __choice = __row_input(min_seat, max_seat)
        case "business_class":
            min_seat = 5
            max_seat = 10
            print_pricing(__class)
            print()
            __choice = __row_input(min_seat, max_seat)
        case "economy_class":
            min_seat = 11
            max_seat = 60
            print_pricing(__class)
            print()
            __choice = __row_input(min_seat, max_seat)

    return int(__choice)


def __seat_validator(__seat: str,
                     __available_seats: tuple[str, str, str, str] | tuple[str, str, str, str, str, str]) -> bool:
    if __seat not in __available_seats:
        print(f"\n{__seat} is not in the available seats")
        return False
    return True
    pass


def __seat_input(__available_seats: tuple[str, str, str, str] | tuple[str, str, str, str, str, str]) -> str:
    __input_str = "Where would you like to to sit?\n" \
                  f"The layout is: {pretty_layout(__available_seats)}\n" \
                  f"Choose: Seat {__available_seats}\n" \
                  ">>> "
    print()
    __choice = input(__input_str).upper().strip()
    while __seat_validator(__choice, __available_seats) is False:
        print()
        __choice = input(__input_str).upper().strip()

    return __choice


def choose_seat(__class: str) -> str:
    __choice = ""
    match __class:
        case "first_class":
            available_seats = ('A', 'B', 'C', 'D')
            __choice = __seat_input(available_seats)
        case "business_class":
            available_seats = ('A', 'B', 'C', 'D')
            __choice = __seat_input(available_seats)
        case "economy_class":
            available_seats = ('A', 'B', 'C', 'D', 'E', 'F')
            __choice = __seat_input(available_seats)

    return __choice
