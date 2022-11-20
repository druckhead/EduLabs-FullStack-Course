nums = []
temp = input("Enter numbers separated by a space: ").strip().split()

for num in temp:
    nums.append(int(num))

target = int(input("Enter a target number: "))

dict_nums = {}

# create dict with:
# key: value in list
# val: index in list
for i in range(len(nums)):
    dict_nums[nums[i]] = i

# iterate keys in dict_nums
for num in dict_nums:
    # find the pair that's sums equal the target
    # if target - num is in dict_names => dict_names + num == target
    if target - num in dict_nums:
        # print index of value found and it's complement
        print([dict_nums[num], dict_nums[target - num]])
        break

# num2_index, num1_index = None, None
# len_nums = len(nums)
# for i in range(len_nums):
#     for j in range(i+1, len_nums):
#         if nums[i] + nums[j] == target:
#             num1_index = i
#             num2_index = j
#             break

# print(list((num1_index, num2_index)))