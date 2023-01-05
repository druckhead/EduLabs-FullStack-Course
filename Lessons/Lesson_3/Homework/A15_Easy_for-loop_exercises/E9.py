# Write a program to count the number of even and odd numbers from a given list of numbers.
import random

numbers = []

size = int(input("Enter the size of the list: "))
for i in range(0, size):
    numbers.append(random.randint(0, 100))
print(numbers)

even_count, odd_count = 0, 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even Count: {even_count}\n"
      f"Odd Count: {odd_count}")