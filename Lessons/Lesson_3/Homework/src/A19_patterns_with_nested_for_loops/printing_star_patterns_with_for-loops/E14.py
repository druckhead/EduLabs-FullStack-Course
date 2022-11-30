n = int(input("Enter a number: "))

for i in range(n - 1, -1, -1):
    for j in range(n, i, -1):
        print(" ", end="")
    print("*", end="")
    if i < n - 1:
        for k in range(1, 2 * i):
            print(" ", end="")
    else:
        for k in range(1, 2 * n - 2):
            print("*", end="")
    if i == 0:
        print()
    else:
        print("*")
