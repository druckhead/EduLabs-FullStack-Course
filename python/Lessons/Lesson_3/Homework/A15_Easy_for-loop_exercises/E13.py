# Write a program that receives a number from a user and constructs the following pattern,
# using a nested loop. For example, for n=9:
# Expected Output:
#
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()
