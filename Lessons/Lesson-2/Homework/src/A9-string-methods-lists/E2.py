# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards)

str_input = input("Enter a string: ")
is_palindrome = str_input[::] == str_input[-1::-1]

if is_palindrome:
    print(f"{str_input} is palindrom")
else:
    print(f"{str_input} is not palindrom")
