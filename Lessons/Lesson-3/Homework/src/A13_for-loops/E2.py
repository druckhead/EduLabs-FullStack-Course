# def receive_num_list(*numbers_list):
#     ls = []
#     for number in numbers_list:
#         ls.append(number)
#     return ls


def find_min_num(num_list: [int]):
    min_number = num_list[0]
    for num in num_list:
        min_number = min(min_number, num)
    return min_number


# numbers = receive_num_list(12, 4, 6, 19, 53, 28)
numbers = [1, 6, 8, 92, 42, 0]
print(numbers)
print()
min_num = find_min_num(numbers)
print(f"min_num = {min_num}")
