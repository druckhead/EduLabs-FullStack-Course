from random import randint


# Implement a function second_largest that receives a list of numbers
# and returns the second-largest number in the list.
# You can assume that there are no non-numeric values in the list.


def second_largest(num_list: list[float]) -> float:
    first_max = max(num_list[0], num_list[1])
    second_biggest = min(num_list[0], num_list[1])

    for i in range(2, len(num_list)):
        if num_list[i] > first_max:
            second_biggest = first_max
            first_max = num_list[i]
        elif second_biggest < num_list[i] != first_max:
            second_biggest = num_list[i]
        elif first_max == second_biggest != num_list[i]:
            second_biggest = num_list[i]

    return second_biggest


if __name__ == "__main__":

    for k in range(15):
        __list = []
        len_list = randint(2, 12)
        for j in range(len_list):
            random_num = randint(1, 9999)
            __list.append(random_num)

        print(__list, end=" => ")
        print(second_largest(__list))
        print()
