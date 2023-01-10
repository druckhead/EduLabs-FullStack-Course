# Write a program that receives an integer number from a user
# and appends squares of the numbers
# starting from 1 up to the number inserted by a user to a new list.
# Print the new list with the squares.

number = int(input("Enter a number: "))
new_list = []

for i in range(1, number + 1):
    new_list.append(i ** 2)

print(new_list)