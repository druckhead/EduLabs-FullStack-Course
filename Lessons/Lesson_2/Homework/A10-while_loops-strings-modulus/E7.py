number = input("Enter a number: ")
num_len = len(number)

digit_count = 0

i = 0
while i <= num_len - 1:
    if number[i].isnumeric():
        digit_count += 1
    i += 1

print(f"The number of digits entered in {number} is: {digit_count}")