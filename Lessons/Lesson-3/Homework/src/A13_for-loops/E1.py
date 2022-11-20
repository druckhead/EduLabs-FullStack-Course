# Write a program that receives a number from a user and calculates the sum of all numbers
# from 1 to a given number

n = input("Enter a number: ")
while not n.isdigit():
    print("Invalid input!")
    n = input("Enter a number: ")
n = int(n)

sum_digits = 0
for i in range(1, n + 1):
    sum_digits += i
print(f"the sum of all digits from one to num is: {sum_digits}")
