# Calculate the cube of all numbers from 1 to a given number.

n = int(input("Enter a number to cube until: "))
for i in range(1, n + 1):
    print(f"Current Number is : {i}  and the cube is {i ** 3}")
