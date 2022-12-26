import re
from string import whitespace


# Write a regular expression to look for 3 digits, possibly separated by whitespace.

def three_digits(string: str):
    # print(re.search(f"([0-9][{whitespace}]*?){3}", string))
    return re.search(f"([0-9][{whitespace}]*?){3}", string) is not None


if __name__ == '__main__':
    print(three_digits("333"))
    print(three_digits("3 23"))
    print(three_digits("32 3"))
    print(three_digits("3 3 3"))
    print(three_digits("3\n3\t3\t"))
    print(three_digits("3\n3\t3"))

    print(three_digits("6 a 6"))

    print(three_digits("aaa"))
    print(three_digits("aa a"))
    print(three_digits("aaa"))
    print(three_digits("a a a"))
