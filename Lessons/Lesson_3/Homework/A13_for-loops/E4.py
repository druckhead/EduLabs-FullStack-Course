# Print list in reverse order using a for loop

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("[", end="")
for i in range(len(list) - 1, -1, -1):
    end = None
    if i > 0:
        end = ", "
    else:
        end = ""
    print(list[i], end=end)
print("]")
