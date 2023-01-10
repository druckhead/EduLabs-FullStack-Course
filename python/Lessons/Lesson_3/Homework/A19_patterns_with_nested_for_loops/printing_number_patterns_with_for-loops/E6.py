n = int(input("Enter a number: "))

for i in range(n + 1):
    k = n
    for j in range(i):
        print(k - j, end=" ")
    print()