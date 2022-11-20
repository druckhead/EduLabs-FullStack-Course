# Write a function that receives the string as a parameter and return the string in reverse order.


def rev_str(s: str) -> str:
    return s[-1::-1]


string = "Hello, World!"

print(rev_str(string))