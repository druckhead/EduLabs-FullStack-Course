# Write a Python function that prints out the first _n rows of Pascal's triangle.
from math import sqrt


def fact(_n: int) -> int:
    if _n > 1:
        return _n * fact(_n - 1)
    return 1


def ncr(_n: int, _k: int) -> int:
    return fact(_n) // (fact(_k) * fact(_n - _k))


def print_triangle(_n: int, spaces_format: str = " ", numbers_format: str = "{:^}") -> None:
    for i in range(_n):
        for j in range(_n - i):
            print(spaces_format.format(""), end="")
        for j in range(i + 1):
            print(numbers_format.format(f"{ncr(i, j)}"), end=" ")
        print()


def print_pascal(_n: int) -> None:
    if _n >= 5:
        # if n >= 5, better spacing is needed
        sqrt_n = int(sqrt(_n))

        # define format specifiers
        spc = ['{', ':', '^', f'{sqrt_n + 1}', '}']
        nums = ['{', ':', '^', f'{sqrt_n * 2 + 1}', '}']

        # make the usable as strings
        spacer_spc = ''.join(spc)
        spacer_nums = ''.join(nums)

        print_triangle(_n, spacer_spc, spacer_nums)
    else:
        # print the triangle with regular spacing
        print_triangle(_n)


if __name__ == "__main__":
    n = int(input("Enter a height for Pascal's Triangle: "))
    print_pascal(n)
