def factorial_n(n: int) -> int:
    if n > 1:
        return n * factorial_n(n - 1)
    return 1

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n - 1 - i, -1, -1):
        print(" ", end="")
    for j in range(i + 1):
        ncr = factorial_n(i) // (factorial_n(j) * factorial_n(i - j))
        print(ncr, end=" ")
    print()
