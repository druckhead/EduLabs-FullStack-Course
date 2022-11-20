n = int(input("Enter a number: "))

k = 2*n - 2

# loop rows
for i in range(n):
    # for the spaces before *
    for j in range(k):
        print(end=" ")

    # update k to have one less space in the next iteration
    k -= 2

    # print the *
    for j in range(i + 1):
        print("* ", end="")
    print()
