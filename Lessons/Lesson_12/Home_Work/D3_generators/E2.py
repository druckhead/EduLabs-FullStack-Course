def batches(n: int, my_list: list):
    start = 0
    end = n
    max_end = len(my_list)
    while start < max_end:
        batch = my_list[start: end]
        start = end
        end += n
        yield batch


if __name__ == '__main__':
    bg = batches(6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    for b in bg:
        print(b)
