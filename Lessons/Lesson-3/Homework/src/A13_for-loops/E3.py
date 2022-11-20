# Write a program that receives a list of numbers,
# and finds the second-largest number

numbers = [13, 4, 3, 24, 5, 16, 8]

# numbers_exclude_max = [x for x in numbers if x < max(numbers)]
# print(max(numbers_exclude_max))

max_num = numbers[0]
second_max_num = numbers[0]
for number in numbers:
    if number > max_num:
        second_max_num = max_num
        max_num = number
    else:
        second_max_num = max(number, second_max_num)
print(second_max_num)
