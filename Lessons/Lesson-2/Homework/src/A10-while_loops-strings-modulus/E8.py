# Reverse a given integer number. Solve the exercise in two ways:
# a) By converting received number to string and operating on string
# b) Do not convert the number to string, and use modulus operator

string = input("Enter a number: ")

# a
rev_string = string[-1::-1]
print(f"The string reversed is: {rev_string}")

# b
int_string = int(string)
rev_num = 0

while int_string > 0:
    rev_num *= 10
    rev_num += int_string % 10
    int_string //= 10

print(f"The int reversed is: {rev_num}")