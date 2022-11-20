year = int(input("Enter a year: "))

is_divisible_by_four = year % 4 == 0
is_end_of_century = year % 100 == 0
is_divisible_by_four_hundred = year % 400 == 0

is_leap_year = (not is_end_of_century and is_divisible_by_four) or is_divisible_by_four_hundred

print(is_leap_year)
