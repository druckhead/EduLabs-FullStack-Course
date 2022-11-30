# Write a program that prints each item and its corresponding type from the given list.
# For example, given the list:
# ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
# The expected output is something like:
# AAA - string
# [4,5,7] - list
# 5 - string
# 5 - integer
# 3.0 - float
# … and so on…

various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]

for item in various:
    print(f"{item} - {type(item).__name__}")
