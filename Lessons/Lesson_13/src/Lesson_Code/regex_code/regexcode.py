import re

user_email = input("Insert email: ")

pattern = "[a-z]+@[a-z]+\.[a-z]+"

result = re.match(pattern, user_email)

print(type(result))

print(result)