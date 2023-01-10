
# coffee_time.py
#
# author: Daniel Raz (@druckhead)
# date: 12/11/2022
#
# A simple coffee order management system for you and your friends in your Hi-Tech offices
# It accepts:
#     A time of day
#     The number of drinkers
#     Option to offset the starting point for coffee choice
#     Option to filter Coffee types to your satisfaction
#
# It outputs:
#     The type of coffee each office worker will get according to the provided inputs


# **************************************************************
#                       FUNCTIONS START
# **************************************************************


def remove_coffee(_all_coffee: list, _coffee_index_to_exclude: int) -> None:
    """
        Remove the index from the list
    """
    remove_item = _all_coffee[_coffee_index_to_exclude - 1]
    if remove_item in _all_coffee:
        _all_coffee.remove(remove_item)
    return


def time_input() -> tuple:
    """
        Read a time from standard input.

        Parse and validate input.

        Returns a tuple of the hours, minutes.
    """
    _hours, _minutes = None, None
    is_valid_time = None
    while is_valid_time is not True:
        time = input("Enter the current time (24-hour format): ")
        formatted_time = time.split(':')
        # validate that time is split with semicolon
        if len(formatted_time) == 2:
            # validate time is NOT negative
            if '-' in formatted_time[0] or '-' in formatted_time[1]:
                print(f"OverFlow Error: Invalid Time given.\n"
                      f"Hours and Minutes MUST be positive numbers\n")
                continue
            # validate Hours and Minutes do not contain any non-numeric characters
            if formatted_time[0].isnumeric() is not True or formatted_time[1].isnumeric() is not True:
                print("ValueError: This isn't a time!\n")
                continue
            _hours = int(formatted_time[0])
            # validate hours are not over 24
            if _hours > 24:
                print(f"OverFlow Error: Invalid Hour given.\n"
                      f"Hours Must be between 0 and 24\n")
                continue
            _minutes = int(formatted_time[1])
            # validate minutes are not above 59
            if _minutes > 59:
                print(f"OverFlow Error: Invalid Minutes given.\n"
                      f"Minutes Must be between 0 and 59\n")
                continue
            # passed all validations
            is_valid_time = True
        else:
            print("ValueError: This isn't a time!\n")
            continue
    return _hours, _minutes


def num_drinkers_input() -> int:
    """
        Read a drinker count from standard input.

        Validate input.

        Returns the number of drinkers as an int.
    """
    _number_of_drinkers = None
    is_valid_number_of_drinkers = None
    while is_valid_number_of_drinkers is not True:
        _number_of_drinkers = input("Enter the number of drinkers: ")
        # validate input isn't empty
        if len(_number_of_drinkers) == 0:
            print(f"Error: Input can NOT be empty!\n")
            continue
        # validate number of drinkers isn't negative
        if _number_of_drinkers[0] == '-':
            if _number_of_drinkers[1:].isnumeric() is not True:
                print(f"TypeError: Invalid Input! "
                      f"Please only enter a number\n")
                continue
            else:
                print(f"ValueError: Invalid Input! "
                      f"Please only enter a positive number\n")
                continue
        # validate that the number of drinkers is actually a number
        if _number_of_drinkers.isnumeric() is not True:
            print(f"TypeError: Invalid Input! "
                  f"Please only enter a number\n")
            continue
        # validation passed
        # convert number_of_drinkers to int
        _number_of_drinkers = int(_number_of_drinkers)
        # make sure number of drinkers is at least 1
        if _number_of_drinkers < 1:
            print("ValueError: Number of drinkers can NOT be zero!\n")
            continue
        # passed all validations
        is_valid_number_of_drinkers = True
    return _number_of_drinkers


def offset_input() -> int:
    """
        Read an offset number from standard input.

        Validate input.

        Returns the offset as an int.
    """
    _offset = None
    valid_offset = None
    while valid_offset is not True:
        _offset = input("Enter an offset: ")
        # handle empty offset
        if len(_offset) == 0:
            print(f"MissingValueError: offset can NOT be empty.\n"
                  f"Enter '0' to not have an offset\n")
            continue
        # handle negative offset
        if _offset[0] == '-':
            # validate that the part after the minus sign is a number
            if _offset[1::].isnumeric() is not True:
                print(f"ValueError: offset MUST be a number\n")
                continue
        # handle positive offset
        # validate that the input is a number
        elif _offset.isnumeric() is not True:
            print(f"ValueError: offset MUST be a number\n")
            continue
        # all validations passed
        # convert offset to int
        valid_offset = True
        _offset = int(_offset)
    return _offset


def should_exclude_input() -> bool:
    """
        Prompt user for Y/N answer from standard input.

        Validate input.

        Returns the answer as a bool value.
    """
    _should_exclude = None
    while True:
        _should_exclude = input(
            "Would you like to exclude any Coffee types from this Coffee run? (Y/N): ").strip().lower()
        # handle incompatible answer
        if _should_exclude != 'y' and _should_exclude != 'n':
            print(f"ValueError: Expected 'Y' or 'N'\n")
            continue
        # validation passed
        # get bool value of input answer
        _should_exclude = True if _should_exclude == 'y' else False
        break
    return _should_exclude


def type_exclude_input(_filtered_coffee_types: list) -> None:
    """
        Prompt user for items to exclude from the list until '$' is entered.

        Remove the prompted items from the list.
    """
    print(f"Enter Coffee numbers one by one to exclude them from this Coffee run.\n"
          f"When you are finished, enter '$'.\n")
    _excluded_coffee_type = None
    while True:
        # make sure a value exists
        if _excluded_coffee_type is not None:
            # convert excluded_coffee_type to int
            _excluded_coffee_type = int(_excluded_coffee_type)
            # validate that excluded_coffee_type is not index overflowing
            if (1 <= _excluded_coffee_type <= 28) is not True:
                print(f"ValueError: Excluded Coffee type MUST be a number between 1 and 28\n")
                _excluded_coffee_type = None
                continue
            # all validations passed
            # remove the coffee type that was given in this iteration
            remove_coffee(_filtered_coffee_types, _excluded_coffee_type)
        # get input from user
        _excluded_coffee_type = input("Enter a Coffee number to exclude: ")
        # handle empty input
        if len(_excluded_coffee_type) == 0:
            print(f"Error: if you would like to continue to the next step, enter '$'\n")
            continue
        # handle exit character for continuing with the program
        if _excluded_coffee_type == '$':
            break
        # handle negative input
        if _excluded_coffee_type[0] == '-':
            if _excluded_coffee_type[1:].isnumeric():
                print(f"ValueError: Excluded Coffee type MUST be a number between 1 and 28\n")
                _excluded_coffee_type = None
                continue
        # validate the input is a number
        if _excluded_coffee_type.isnumeric() is not True:
            print(f"TypeError: received {_excluded_coffee_type}\n"
                  f"Expected positive number between 1 and 28 or '$'\n")
            _excluded_coffee_type = None
            continue
    return


def print_order(_filtered_coffee_types: list, _hours: int, _minutes: int,
                _number_of_drinkers: int, _offset: int) -> None:
    """
        Prints the order accordingly.
    """
    # the new length of the Coffee types
    len_filter = len(_filtered_coffee_types)

    # calculate the coffee number for customer presentation
    coffee_number = (_hours + _offset) % len_filter
    # zero-index handling
    coffee_type = _filtered_coffee_types[coffee_number - 1]

    print()
    print(f"******************************\n",
          f'{"ORDER": ^30}')
    print(f"******************************\n"
          f"User #1\n"
          f"Coffee #{coffee_types.index(coffee_type) + 1}: {coffee_type}")

    # store the previous users coffee number to calculate other friends coffee number
    previous_user_coffee = coffee_number

    # iterate the rest of the drinkers
    user = 2
    while user <= _number_of_drinkers:
        # calculate the coffee number for customer presentation
        coffee_number = (previous_user_coffee + _minutes) % len_filter
        # zero-index handling
        coffee_type = _filtered_coffee_types[coffee_number - 1]
        print(f"******************************\n"
              f"User #{user}\n"
              f"Coffee #{coffee_types.index(coffee_type) + 1}: {coffee_type}"
              )
        user += 1
        # update the previous coffee number
        previous_user_coffee = coffee_number
    print("******************************")
    return


def main():
    print("""
    .-. . .-..----..-.    .---.  .----. .-.   .-..----.
    | |/ \\| || {_  | |   /  ___}/  {}  \\|  `.'  || {_  
    |  .'.  || {__ | `--.\\     }\\      /| |\\ /| || {__ 
    `-'   `-'`----'`----' `---'  `----' `-' ` `-'`----'
                    .---.  .----.                      
                   {_   _}/  {}  \\                     
                     | |  \\      /                     
                     `-'   `----'                      
           .---.  .----. .----..----..----.            
          /  ___}/  {}  \\| {_  | {_  | {_              
          \\     }\\      /| |   | |   | {__             
           `---'  `----' `-'   `-'   `----'            
              .---. .-..-.   .-..----.                 
             {_   _}| ||  `.'  || {_                   
               | |  | || |\\ /| || {__                  
               `-'  `-'`-' ` `-'`----' 
    """)

    # get the time from user
    hours, minutes = time_input()
    print()

    # get the number of drinkers from user
    number_of_drinkers = num_drinkers_input()
    print()

    # get the offset amount from user
    offset = offset_input()
    print()

    # create a (mutable) list containing all coffee types to use as a filter
    _filtered_coffee_types = list(coffee_types)

    # prompt user if they want to filter coffee types
    should_exclude = should_exclude_input()
    print()

    if should_exclude is True:
        # prompt for coffee types to filter
        type_exclude_input(_filtered_coffee_types)

    print_order(_filtered_coffee_types, hours, minutes, number_of_drinkers, offset)

    print("""
     .---. .-. .-.  .--.  .-. .-..-. .-.   .-.  .-. .----. .-. .-.    
    {_   _}| {_} | / {} \\ |  `| || |/ /     \\ \\/ / /  {}  \\| { } |    
      | |  | { } |/  /\\  \\| |\\  || |\\ \\      }  {  \\      /| {_} |    
      `-'  `-' `-'`-'  `-'`-' `-'`-' `-'     `--'   `----' `-----'    
             .----. .-.   .----.  .--.   .----..----.                 
             | {}  }| |   | {_   / {} \\ { {__  | {_                   
             | .--' | `--.| {__ /  /\\  \\.-._} }| {__                  
             `-'    `----'`----'`-'  `-'`----' `----'                 
     .---.  .----. .-.   .-..----.     .--.   .---.   .--.  .-..-. .-.
    /  ___}/  {}  \\|  `.'  || {_      / {} \\ /   __} / {} \\ | ||  `| |
    \\     }\\      /| |\\ /| || {__    /  /\\  \\  {_ }/  /\\  \\| || |\\  |
     `---'  `----' `-' ` `-'`----'   `-'  `-' `---' `-'  `-'`-'`-' `-'
    """)


# **************************************************************
#                       FUNCTIONS END
# **************************************************************

# **************************************************************
#                       MAIN START
# **************************************************************

if __name__ == "__main__":
    # tuple of coffee types to ensure immutability
    coffee_types = ('Espresso', 'Doppio', 'Lungo', 'Ristretto',
                    'Macchiato', 'Corretto', 'Con Panna', 'Romano',
                    'Cappuccino', 'Americano', 'Café Late', 'Flat White',
                    'Marocchino', 'Mocha', 'Bicerin', 'Breve',
                    'Raf Coffee', 'Mead Raf', 'Vienna Coffee', 'Chocolate Milk',
                    'Latte Macchiato', 'Glace', 'Freddo', 'Irish Coffee',
                    'Frappe', 'Cappuccino Freddo', 'Caramel Frappe', 'Espresso Laccino'
                    )
    main()

# **************************************************************
#                       MAIN END
# **************************************************************
