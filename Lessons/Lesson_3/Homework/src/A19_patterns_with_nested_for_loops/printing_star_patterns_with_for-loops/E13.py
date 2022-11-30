n = int(input("Enter a number: "))


for i in range(n):
    for j in range(n, i, -1):
        print(" ", end="")
    print("*", end="")
    if i < n - 1:
        for k in range(1, 2 * i):
            print(" ", end="")
    if i == 0:
        print()
    elif i == n - 1:
        for k in range(1, 2 * n - 1):
            print("*", end="")
    else:
        print("*")
