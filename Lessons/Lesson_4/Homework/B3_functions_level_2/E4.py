# Write a Python function to check whether a string is a pangram or not.
# Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def is_panagram(string: str) -> bool:
    abc = "abcdefghijklmnopqrstuvwxyz"
    for letter in abc:
        if letter not in string.lower():
            return False
    return True

print(is_panagram("the quick brown fox jumps over the lazy dog".upper()))

print(is_panagram('brown fox jumps'.upper()))