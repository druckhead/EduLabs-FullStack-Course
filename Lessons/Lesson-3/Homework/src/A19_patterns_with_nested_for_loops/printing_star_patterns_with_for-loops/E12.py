n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n):
        if ((j == 1 or j == n - 2) and i != 0) or ((i == 0 or i == n // 2) and (1 < j < n - 2)):
            print("*", end="")
        else:
            print(" ", end="")
    print()