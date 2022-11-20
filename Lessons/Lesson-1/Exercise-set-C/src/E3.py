str = input("Enter a string: ")

is_palindrome = str[0:] == str[-1::-1]

if is_palindrome:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")