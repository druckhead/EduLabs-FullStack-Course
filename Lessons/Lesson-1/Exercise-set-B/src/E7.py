day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if month == 5:
    if day == 31:
        print("it's summer")
    else:
        print("it's spring")
elif 6 <= month <= 9:
    if month == 9 and day > 22:
        print("it's fall")
    else:
        print("it's summer")
elif 10 <= month <= 12:
    if month == 12 and day > 7:
        print("it's winter")
    else:
        print("its fall")
elif 1 <= month <= 3:
    if month > 30:
        print("it's spring")
    else:
        print("it's winter")
else:
    print("it's spring")

is_divisible_by_four = year % 4 == 0
is_end_of_century = year % 100 == 0
is_divisible_by_four_hundred = year % 400 == 0

is_leap_year = (not is_end_of_century and is_divisible_by_four) or is_divisible_by_four_hundred

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("this month has 31 days")
elif month == 2:
    if is_leap_year:
        print("this month has 29 days")
    else:
        print("this month has 28 days")
else:
    print("this month has 30 days")
