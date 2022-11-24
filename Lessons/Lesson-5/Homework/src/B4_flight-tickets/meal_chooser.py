from utils import pretty_dict

__BUSINESS_MEAL_OPTIONS = {
    '1': 'Included Business Class Meal',
    '2': 'Upgrade to First Class Meal',
}

__ECONOMY_MEAL_OPTIONS = {
    '1': "Economy Class meal",
    '2': 'Upgrade to Business Class meal',
    '3': 'Upgrade to First Class meal',
}


def __meal_validator(__class: str, __meal) -> bool:
    __max_option = None
    if __class == "economy_class":
        __max_option = 3
    elif __class == "business_class":
        __max_option = 2

    if len(__meal) == 0:
        print("\nError: You must choose a class.\n")
        return False
    if __meal.isnumeric() is not True:
        print(f"\nError: {__meal} is not a valid choice. Enter only 1 to 3")
        return False
    if (1 <= int(__meal) <= __max_option) is not True:
        print(f"\nError: {__meal} is not a valid choice. Enter only 1 to 3")
        return False
    return True


def choose_meal(__class: str) -> str:
    __choice = ""
    match __class:
        case 'first_class':
            __choice = "first_class_meal"
        case 'business_class':
            print("\nChoose a meal.")
            print(pretty_dict(__BUSINESS_MEAL_OPTIONS, sep=")"))
            __choice = input(">>> ")
            while __meal_validator(__class, __choice) is not True:
                print("\nChoose a meal.")
                print(pretty_dict(__BUSINESS_MEAL_OPTIONS, sep=")"))
                __choice = input(">>> ")
            match __choice:
                case '1':
                    return "business_class_meal"
                case '2':
                    return "first_class_meal"
        case 'economy_class':
            print("\nChoose a meal.")
            print(pretty_dict(__ECONOMY_MEAL_OPTIONS, sep=")"))
            __choice = input(">>> ")
            while __meal_validator(__class, __choice) is not True:
                print("\nChoose a meal.")
                print(pretty_dict(__ECONOMY_MEAL_OPTIONS, sep=")"))
                __choice = input(">>> ")
            match __choice:
                case '1':
                    return "economy_class_meal"
                case '2':
                    return "business_class_meal"
                case '3':
                    return "first_class_meal"

    return __choice
