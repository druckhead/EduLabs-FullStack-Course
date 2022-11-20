num = int(input("Enter a number: "))
str = ""

if num % 2 == 0:
    str = "even"
else :
    str = "odd"

print(f"{num} is {str}")