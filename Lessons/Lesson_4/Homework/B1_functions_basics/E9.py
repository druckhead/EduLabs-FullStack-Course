# Write a Python function that takes a number as a parameter and
# checks if the number is prime or not. A prime number (or a prime)
# is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

from math import sqrt


def is_prime(num: int):
    if num < 2:
        return False

    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True

print(is_prime(19))


# sieve of eratosthenes

def sieve(n: int) -> None:
    ls = []
    for i in range(120):
        ls.append(True)

    for i in range(2, int(sqrt(120))):
        if is_prime(i):
            for j in range(i, 120):
                if i * j >= 120:
                    break
                ls[j * i] = False

    for i in range(2, 120):
        if ls[i] is True:
            print(i, end=" ")
    print()


sieve(120)
