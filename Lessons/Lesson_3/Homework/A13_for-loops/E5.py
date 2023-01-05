# Get 10 dates from the user. The date is in the following format: dd.mm.yyyy
# (no need to check.
# After you get all the 10 dates, print the amount of dates
# in winter, autumn, sprint, summer, and print the dates themselves.
# The output should look something like:
#
# You entered 2 dates in winter:
# 11.12.2013
# 05.01.1999
#
# You entered 8 dates in summer:
# 16.08.2012
# 05.07.1999
#
all_dates = []

dates_summer_count = 0
dates_winter_count = 0
dates_spring_count = 0
dates_fall_count = 0

dates_summer = []
dates_winter = []
dates_spring = []
dates_fall = []

i = 0
while i < 10:
    date = input("Enter date (dd.mm.yyyy): ")
    date_format = date.split('.')
    day = int(date_format[0])
    month = int(date_format[1])
    year = int(date_format[2])

    if month == 5:
        if day == 31:
            dates_summer.append(date)
            dates_summer_count += 1
            # print("it's summer")
        else:
            dates_spring.append(date)
            dates_spring_count += 1
            # print("it's spring")
    elif 6 <= month <= 9:
        if month == 9 and day > 22:
            dates_fall.append(date)
            dates_fall_count += 1
            # print("it's fall")
        else:
            dates_summer.append(date)
            dates_summer_count += 1
            # print("it's summer")
    elif 10 <= month <= 12:
        if month == 12 and day > 7:
            # print("it's winter")
            dates_winter.append(date)
            dates_winter_count += 1
        else:
            dates_fall.append(date)
            dates_fall_count += 1
            # print("its fall")
    elif 1 <= month <= 3:
        if month > 30:
            # print("it's spring")
            dates_spring.append(date)
            dates_spring_count += 1
        else:
            # print("it's winter")
            dates_winter.append(date)
            dates_winter_count += 1
    else:
        # print("it's spring")
        dates_spring.append(date)
        dates_spring_count += 1
    i += 1

print()

print(f"The number of dates in Summer: {dates_summer_count}")
for date in dates_summer:
    print(date)
print()

print(f"The number of dates in Winter: {dates_winter_count}")
for date in dates_winter:
    print(date)
print()

print(f"The number of dates in Spring: {dates_spring_count}")
for date in dates_spring:
    print(date)
print()

print(f"The number of dates in Fall: {dates_fall_count}")
for date in dates_fall:
    print(date)
print()
