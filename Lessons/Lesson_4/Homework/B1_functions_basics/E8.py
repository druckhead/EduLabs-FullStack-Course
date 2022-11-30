# Write a Python function to check whether a number is perfect or not.

def is_perfect(num: int) -> bool:
    divisors = [lambda arg=i: arg for i in range(1, num) if num % i == 0]
    _sum = 0
    for divisor in divisors:
        _sum += divisor()
    return _sum == num


perfect_nums = [6, 28, 496, 8128, 33550336]
not_perfect_nums = [1, 24, 99, 1029, 84731]
for num in perfect_nums:
    print(f"{num}: is perfect: {is_perfect(num)}")
print()
for num in not_perfect_nums:
    print(f"{num}: is perfect: {is_perfect(num)}")
