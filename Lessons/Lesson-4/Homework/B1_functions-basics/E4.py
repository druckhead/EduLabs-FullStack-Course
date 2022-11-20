# Write a Python function to calculate the factorial of a number (a non-negative integer).
# Arguments types: int
# Return value type: int

# recursive
def fac_n_rec(n: int) -> int:
    if n > 1:
        return n * fac_n_rec(n - 1)
    return 1


print(fac_n_rec(5))

# iterative
def fac_n_iter(n: int) -> int:
    _prod = 1
    for i in range(2, n + 1):
        _prod *= i
    return _prod

print(fac_n_iter(6))