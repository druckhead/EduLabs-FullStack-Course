# Write a function that receives a list of numbers as a parameter.
# The function returns the sum of numbers in the list.
# Arguments types: list
# Return value type: float

def sum_nums(_nums: list) -> float:
    _sum = 0.0
    for num in _nums:
        _sum += float(num)
    return _sum

print(sum_nums([1.2,2.05,3.5,4,5.7]))