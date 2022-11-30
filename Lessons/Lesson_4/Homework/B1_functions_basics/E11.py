# Write a Python function to check whether a number falls
# in a given range. (The function receives number and range
# (from/to) as parameters and returns True/False)

def is_in_range(num: int, r: range) -> bool:
    return num in r


n = 101
rng = range(21,100)

print(is_in_range(n, rng))