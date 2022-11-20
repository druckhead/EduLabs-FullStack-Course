# Write a Python function that receives a string as a parameter and calculates
# the number of upper case letters and lowercase letters.

# (The function should return 2 numbers in a tuple)

def num_upper_lower(string: str):
    count_lower = count_upper = 0
    for char in string:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    return count_lower, count_upper


print(num_upper_lower("The Sun Is Shining"))
print("lower, upper")