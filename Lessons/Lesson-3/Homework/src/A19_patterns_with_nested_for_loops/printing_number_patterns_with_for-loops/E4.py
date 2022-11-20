n = int(input("Enter a number: "))
# TODO write code

for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

for i in range(n - 2, -1, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
