# Implement a function that receives a list of strings, and returns a new list of strings
# with all the original strings sorted by the string length.

def sort_by_len(strings: list[str]) -> list[str]:
    return sorted(strings, key=lambda a: len(a))


if __name__ == '__main__':
    s = sort_by_len(["Hello", "Dog", "Cat", "Mother", "Shame on you", "Me", "Too"])
    print(s)