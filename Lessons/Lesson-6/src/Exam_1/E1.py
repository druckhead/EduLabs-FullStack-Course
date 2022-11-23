from random import randint
# Implement a function second_largest that receives a list of numbers
# and returns the second-largest number in the list.
# You can assume that there are no non-numeric values in the list.

def second_largest(__list: list[float]) -> int:
    __sorted_len = len(__list)
    if __sorted_len == 0:
        return None
    __sorted_list = sorted(__list)
    __max = __sorted_list[__sorted_len - 1]
    __second_largest = __sorted_list[__sorted_len - 1]

    for i in range(__sorted_len):
        if __sorted_list[i] < __max:
            __second_largest = __sorted_list[i]
        elif __sorted_list[i] == __max:
            return __second_largest

    return __second_largest


if __name__ == "__main__":

    for i in range(15):
        __list = []
        len_list = randint(1, 12)
        for j in range(len_list):
            random_num = randint(1, 9999)
            __list.append(random_num)

        print(__list, end=" => ")
        print(second_largest(__list))
        print()





