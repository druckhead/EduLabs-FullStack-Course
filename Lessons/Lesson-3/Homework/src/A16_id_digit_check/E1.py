def is_id_valid_length(_id: str) -> bool:
    return len(_id) == 9


def sum_second_last_digits(_id: str) -> int:
    _sum = 0
    _temp_id = _id[:-1]
    for digit in range(len(_temp_id) - 1, -1, -2):
        multiplier = str(2 * int(_temp_id[digit]))
        if len(multiplier) >= 2:
            for _digit in multiplier:
                _sum += int(_digit)
        else:
            _sum += 2 * int(_temp_id[digit])
    return _sum


def other_sum(_id: str) -> int:
    _sum = 0
    _temp_id = _id[:-2]
    for digit in range(len(_temp_id) - 1, -1, -2):
        _sum += int(_temp_id[digit])
    return _sum


def get_check_digit(_sum: int) -> int:
    return (10 - (_sum % 10)) % 10


def is_valid_id(_id: str) -> bool:
    if is_id_valid_length(_id) is not True:
        return False
    total_sum = sum_second_last_digits(_id) + other_sum(_id)
    check_digit = get_check_digit(total_sum)

    return True if check_digit == int(_id[-1]) else False


if __name__ == "__main__":
    id_number = input("Enter an id number: ")
    is_valid = is_valid_id(id_number)

    if is_valid is True:
        print(f"The id number: {id_number} is Valid")
    else:
        print(f"The id number: {id_number} is not Valid")
