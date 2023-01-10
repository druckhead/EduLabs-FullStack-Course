num = int(input("Enter a number: "))
orig_num = num

digits = 0

while num != 0:
    digits += 1
    num //= 10

print(f"{orig_num} has {digits} digits")
