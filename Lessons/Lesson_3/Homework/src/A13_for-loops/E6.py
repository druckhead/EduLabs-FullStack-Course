# Find the factorial of a given number.
# Take into account that factorial of 0 is 1, and factorial does not exist for negative numbers

factorial = 1

n = int(input("Enter a number to find the factorial of: "))
if n >= 0:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is: {factorial}")
else:
    print("Negative numbers don't have a factorial")
