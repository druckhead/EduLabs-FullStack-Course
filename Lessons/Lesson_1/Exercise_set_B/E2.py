num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))

smallest = None
middle = None
biggest = None

# find the smallest number of the three
if num1 < num2 and num1 < num3:
    smallest = num1
elif num2 < num1 and num2 < num3:
    smallest = num2
else:
    smallest = num3

#  find the biggest number of the three
if num1 > num2 and num1 > num3:
    biggest = num1
elif num2 > num1 and num2 > num3:
    biggest = num2
else:
    biggest = num3

# find the middle number
if num1 > smallest and num1 < biggest:
    middle = num1
elif num2 > smallest and num2 < biggest:
    middle = num2
else:
    middle = num3

# print the result
print(smallest, middle, biggest)
