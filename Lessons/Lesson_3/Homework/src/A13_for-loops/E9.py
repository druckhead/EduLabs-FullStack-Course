# Write a program to display all prime numbers within a range provided by the user.
# Note: A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

def is_prime(num: int):
    if num < 2:
        return False
    for index in range(2, num):
        if num % index == 0:
            return False
    return True


start = int(input("Enter a start range: "))
end = int(input("Enter a end range: "))

r = range(start, end + 1)

ls = ['{',
      ':',
      '>',
      str(len(f'{end}')),
      '}'
      ]
# convert specifier list to usable string
string = ''.join(ls)
print(f"Format specifier: {string}\n")

prime_count = 0
for i in r:
    if is_prime(i):
        prime_count += 1
        if prime_count >= 10:
            print()
            prime_count = 0
        print(string.format(f"{i}"), end=" ")
