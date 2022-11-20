# Write a program that receives a number from a user
# and prints a multiplication table of a given number.

n = int(input("Enter a number: "))
r = range(1, n + 1)

# build padding number specifier:
# > is right align (push to the right)
# the length of 'n * n'.
# i.e -> len('10 * 10') = 7.
ls = ['{',
      ':',
      '>',
      str(len(f'{n} * {n}')),
      '}'
      ]
# convert specifier list to usable string
string = ''.join(ls)
print(f"Format specifier: {string}\n")
for i in r:
    for j in r:
        print(string.format(f'{i} * {j}'), end="")
        print(f' = {i * j}')
