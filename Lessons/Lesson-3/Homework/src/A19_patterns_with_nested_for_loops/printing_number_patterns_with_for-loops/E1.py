n = int(input("Enter a number: "))

for i in range(n, -1, -1):
    for j in range(1, n - i + 1):
        print(j, "", end="")
    print()