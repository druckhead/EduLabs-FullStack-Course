########
# 4
########

a_list = [[1, 2, 3, 4, 5, [10, 20, 30, 40, 50, [100, 200, 300, 400, 500]]]]
b_list = a_list[0][-1][-1]
b_list[0] = 11111
b_list[1] = [22, 222, 2222]
c_list = b_list[1]
num_c = c_list[0]
num_x = num_c
print(a_list)
print(num_x is a_list[-1][-1][-1][1][0])

num_y = b_list[0]
b_list[0] = 555555

print(b_list[0] == num_y)