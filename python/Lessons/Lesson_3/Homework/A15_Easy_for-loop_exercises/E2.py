my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for item in my_list:
    if my_list.index(item) % 2 != 0:
        print(item, end=" ")