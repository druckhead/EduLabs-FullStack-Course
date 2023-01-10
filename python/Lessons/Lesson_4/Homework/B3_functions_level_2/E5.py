# Write a Python function that checks whether a passed string is palindrome or not

def is_palindrome(string: str):
    return string == string[-1::-1]

print(is_palindrome("racecar"))

print(is_palindrome("sportscar"))

print(is_palindrome("12321"))

print(is_palindrome("1"))

print(is_palindrome(""))