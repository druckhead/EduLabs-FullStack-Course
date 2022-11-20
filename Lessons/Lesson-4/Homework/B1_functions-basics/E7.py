# Write a Python program that prints the even numbers from a given list.

# lambada
def print_even_nums(_l: list) -> None:
    is_even_list = [lambda arg=num: arg for num in _l if num % 2 == 0]
    for item in is_even_list:
        print(item(), end=" ")
    return

def print_even_reg(_l: list) -> None:
    for item in _l:
        if item % 2 == 0:
            print(item, end=" ")
    return


l = [1, 9, 492, 495, 34829141, 234792356, 4, 23]
print("lambada: ", end="")
print_even_nums(l)
print()
print("regular: ", end="")
print_even_reg(l)
