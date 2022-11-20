# Write
# a
# program
# that
# asks
# the
# user
# what is the
# temperature
# outside and whether
# there is a
# sun / rain / snow
# outside, and prints
# out

# not clear instructions #

temperature = float(input("What is the temparature outside?: "))
outside = input("Is it raining? Snowing? Or Sunny?: ").lower().strip()

if outside == "raining":
    print(f"It is {temperature}deg and {outside} outside")
elif outside == "sunny":
    print(f"It is {temperature}deg and {outside} outside")
elif outside == "snowing":
    print(f"It is {temperature}deg and {outside} outside")
else:
    print(f"It is {temperature}deg and cloudy outside")