def get_luggage_weight() -> float:
    __input_string = "Enter your luggage weight in KGs.\n" \
                     "'0' if you have no luggage\n" \
                     ">>> "
    print()
    __weight = input(__input_string)
    while __weight_validator(__weight) is not True:
        __weight = input("Enter your luggage weight in KGs.\n"
                         "'0' if you have no luggage\n"
                         ">>> ")

    return float(__weight)


def __weight_validator(__weight: str) -> bool:
    if '.' in __weight:
        __split_weight = __weight.split('.')
        for item in __split_weight:
            if item.isnumeric() is not True:
                return False
        return True
    if __weight.isnumeric() is not True:
        print("\nError: Invalid input. Only Positive Numbers supported\n")
        return False
    return True
