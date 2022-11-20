# Display Fibonacci series up to 10 terms.
# The Fibonacci Sequence is a series of numbers.
# The next number is found by adding up the two numbers before it.
# The first two numbers are 0 and 1.

# a = 0
# b = 1
# preva = a
# for i in range(10):
#     preva = a
#     a = b
#     b = preva + b
#     print(preva, end=' ')

t = 1, 2, 3
print(type(t))
exit(0)

a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    (a, b) = (b, a + b)
