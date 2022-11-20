# Write a Python function to find the Max of three numbers.
# The function receives 3 floats as parameters and returns a float.

def find_max_three(num1: float, num2: float, num3: float) -> float:
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    elif num2 >= num1:
        if num2 >= num3:
            return num2
        else:
            return num3
    elif num3 >= num1:
        if num3 >= num2:
            return num3
        else:
            return num2


print(find_max_three(4.99213, 4.9922, 4.9923))
