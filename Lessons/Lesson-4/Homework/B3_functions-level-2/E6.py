# Write a Python function to create and print a list where the values
# are square of numbers between 1 and 30 (both included)

def squares_to_30() -> list:
    f = (lambda x: x ** 2)
    return [f(x) for x in range(1, 30 + 1)]

    # return [x * x for x in range(1, 30 + 1)]

l = squares_to_30()
print(l)
