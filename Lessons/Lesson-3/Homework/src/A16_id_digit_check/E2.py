# Bonus - Valid ID number generator application
# There are a lot of places in Israel that are requesting your ID number, however one not always can trust the data security process of certain services.
# So, for educational purposes only, you are going to develop an application that generates random valid israeli ID number.
# f
# The application:
# Shows the instructions on how to use it.
# The application will randomly fit the remaining numbers
# 0 digits entered = application will generate all numbers
# 1-8 digits entered by user = application will generate the remaining digits
# More than 8 digits entered = application will reference only first 8
# Interesting use case:
# Use your birth date: March 2, 1993 => 02031993 -application returns 020319933
# Random number generator info:
# https://docs.python.org/3/library/random.html
# https://www.programiz.com/python-programming/examples/random-number
#
# id_len = 9
#
# id_input = input(“Enter id: ”)
# len_id_input = len(id_input)
#
# if len_id_input == 0:
#         generate_id()
#         generate_check_digit()
# elif len <= 8
#         generate_rest()
# else:
#        cut_len()
#
#

import random


def sum_second_last_digits(_id: str) -> int:
    _sum = 0
    for digit in range(len(_id) - 1, -1, -2):
        multiplier = str(2 * int(_id[digit]))
        if len(multiplier) >= 2:
            for _digit in multiplier:
                _sum += int(_digit)
        else:
            _sum += 2 * int(_id[digit])
    return _sum


def other_sum(_id: str) -> int:
    _sum = 0
    for digit in range(len(_id) - 2, -1, -2):
        _sum += int(_id[digit])
    return _sum


def get_check_digit(_sum: int) -> int:
    return (10 - (_sum % 10)) % 10


def is_valid_id(_id: str) -> bool:
    first_eight = _id[0:8]
    if len(_id) != 9:
        return False
    total_sum = sum_second_last_digits(first_eight) + other_sum(first_eight)
    check_digit = get_check_digit(total_sum)

    return True if check_digit == int(_id[-1]) else False


def print_instructions() -> None:
    print(f"  Enter a sequence of Numbers.\n"
          f"• If no digits are entered then then all 9 digits of ID number will be generated.\n"
          f"• If between 1 and 8 digits are entered then the rest will be generated for you,"
          f"including the check digit.\n"
          f"• If more than 8 are entered, only the first 8 will be referenced"
          f"and a valid 9th check digit will be generated.\n\n")
    return


def generate() -> str:
    print_instructions()

    # Read input from user
    user_input = input("Number: ")
    # get the length of the input
    len_input = len(user_input)

    # empty string for concatenating the generated
    # digits for ID
    _generated_id = ""

    if len_input == 0:
        for i in range(8):
            random_number = random.randint(0, 9)
            _generated_id += str(random_number)
    elif 1 <= len_input <= 8:
        generate_len = 8 - len_input

        _generated_id += str(user_input)

        for i in range(generate_len):
            random_number = random.randint(0, 9)
            _generated_id += str(random_number)
    else:
        _generated_id = user_input[0:8]

    total_sum = sum_second_last_digits(_generated_id) + other_sum(_generated_id)
    check_digit = get_check_digit(total_sum)

    _generated_id += str(check_digit)

    return _generated_id


if __name__ == "__main__":
    while True:
        generated_id = generate()

        print()
        print(f"the ID that was generated is: {generated_id}")

        print(f"The ID is valid? : {is_valid_id(generated_id)}")
        print()

        prompt = input("Would you like to generate another ID? (Y/N): ").lower().strip()
        while prompt != 'y' and prompt != 'n':
            print("Invalid answer. Please enter 'Y' or 'N'\n")
            prompt = input("Would you like to generate another ID? (Y/N): ").lower().strip()
        if prompt == 'n':
            break
        print()