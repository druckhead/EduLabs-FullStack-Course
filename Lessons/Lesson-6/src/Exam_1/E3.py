# Implement a function my_sqrt that receives a non-negative integer x,
# and returns the square root of x rounded down to the nearest integer.
#
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator like x ** 0.5 or math.sqrt()  in python.

def my_sqrt(x: int):
    for i in range(1, x + 1):
        if x // i == i:
            return i
        elif x // i == i - 1:
            return i - 1


if __name__ == "__main__":
    for i in range(1, 100 + 1):
        print(f"sqrt of {i} is: {my_sqrt(i)}")