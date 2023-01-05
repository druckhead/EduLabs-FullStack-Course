salary = int(input("Enter Bob's salary: "))
percentage = 0.14
to_donate = salary * percentage

# print("Bob is going to donate: $", "%.2f" % to_donate)
print(f"Bob is going to donate: $", "{:.2f}".format(to_donate))