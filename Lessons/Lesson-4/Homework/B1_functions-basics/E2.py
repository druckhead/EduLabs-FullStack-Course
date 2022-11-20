# Write a Python function to multiply all the numbers in a tuple.
# Arguments types: tuple
# Return value type: float

def mul_tup(tup: tuple) -> float:
    prod = 1.0
    for num in tup:
        prod *= num
    return prod

print(mul_tup((1,2,3,4,5)))