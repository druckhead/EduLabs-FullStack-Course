n = int(input("Enter a number: "))

for i in range(n + 1):
    for j in range(n, i, -1):
        print(" ", end="")
    print("*", end="")
    for k in range(1, 2 * i):
        print(" ", end="")
    if i == 0:
        print()
    else:
        print("*")

for i in range(n - 1, -1, -1):
    for j in range(n, i, -1):
        print(" ", end="")
    print("*", end="")
    for k in range(1, 2 * i):
        print(" ", end="")
    if i == 0:
        print()
    else:
        print("*")
