# Find the sum of the series up to n terms.
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become:
# 2 + 22 + 222 + 2222 + 22222 = 24690

number = input("Enter a digit: ")
n = int(input("Enter the length of the series: "))

sum = 0
for i in range(1, n + 1):
    num = int(number * i)
    print(num, end=' ')
    if i < n:
        print("+", end=' ')
    sum += num
print(f"= {sum}")