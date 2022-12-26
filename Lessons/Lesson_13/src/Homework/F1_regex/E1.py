import re


# Given a word, check whether it's a Capitalized word (starts from upper case, the second char is a lower case)

def is_capitalized(word: str):
    is_cap_regex = re.match("[A-Z][a-z]+?[A-Za-z]*", word)
    return is_cap_regex is not None


if __name__ == '__main__':
    print(is_capitalized("James"))
