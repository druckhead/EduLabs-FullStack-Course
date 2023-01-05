import sys

print(f"Enter as many numbers as you want, "
      f"this program will print the highest number you entered\n"
      f"Enter q to quit\n")

# solution one
min_number = sys.maxsize
max_number = -sys.maxsize - 1
num = None
while num != 'q':
    if num is not None:
        num = int(num)
        max_number = max(num, max_number)
        min_number = min(num, min_number)
    num = input()

print(f"\nMax number: {max_number}\n"
      f"Min number: {min_number}\n")

# terminate prog after first solution
exit(0)

# solution two
min_number = sys.maxsize
max_number = -sys.maxsize - 1
num = None
while num != 'q':
    if num is not None:
        num = int(num)
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num
    num = input()

print(f"Max number: {max_number}"
      f"Min number: {min_number}")
