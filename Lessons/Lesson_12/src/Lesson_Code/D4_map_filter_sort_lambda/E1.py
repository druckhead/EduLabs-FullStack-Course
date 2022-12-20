import string


def is_str(item) -> bool:
    return isinstance(item, str)


def letter_index(letter: str) -> int:
    if letter not in string.ascii_letters:
        raise ValueError("Not a Letter")

    return string.ascii_lowercase.find(letter) + 1


def letter_indices(letters: [str]) -> list[int]:
    if not all(list(map(is_str, letters))):
        raise ValueError("One or more of items in the list is not of type str")
    return list(map(letter_index, map(str.lower, letters)))


if __name__ == '__main__':
    while True:
        try:
            print("Enter values split by spaces (-1 to quit)")
            letters = input()
            if letters == "-1":
                exit(0)
            letters_list = letters.split()
            print(letter_indices(letters_list))
        except ValueError as err:
            print(err)
