# Write a program that receives rows number  and prints the following number pattern:
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#   1 2 3 4 5
n = int(input("Enter a number of rows: "))
for i in range(n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()