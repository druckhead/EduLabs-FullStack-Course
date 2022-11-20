# Write a program that receives as input 2 numbers - rows and columns,
# and prints a rectangle of $ with received dimensions.
# For example, for the following input:
# Rows: 5, Columns: 3
# The expected output is:
# $$$
# $$$
# $$$
# $$$
# $$$

rows = int(input("Rows: "))
cols = int(input("Columns: "))

for i in range(rows):
    for j in range(cols):
        print("$", end="")
    print()

