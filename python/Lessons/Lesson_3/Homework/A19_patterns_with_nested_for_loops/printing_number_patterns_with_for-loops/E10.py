n = int(input("Enter a number: "))

k = 1
for i in range(n - 1):
    for j in range(i):
        print(" ", end="")
    for j in range(n - i):
        print(j + k, end=" ")
    k += 1
    print()

k = n
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print(j + k, end=" ")
    k -= 1
    print()
