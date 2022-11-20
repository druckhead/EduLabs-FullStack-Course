# Write a Python program to execute a string containing Python code.
# Hint: search for exec() function in Python

exec(f"""
print()
print('Hello, World!')
print(f'The sum of 1 to 5 is: {sum([1,2,3,4,5])}')
print('I am running Python3 code as a string')
ls =[5, 6, 7, 8, 9, 10]
print(ls)
ls.append(11)
print(ls)
""")
