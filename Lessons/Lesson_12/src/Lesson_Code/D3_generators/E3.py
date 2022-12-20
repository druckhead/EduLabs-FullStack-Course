def fib():
    a, b = 1, 1
    while True:
        pa, pb = a, b
        a, b = b, a + b
        yield pa


if __name__ == '__main__':
    for i in fib():
        print(f"{i} ", end="")
        # quit so it doesn't go on forever
        if i > 1_000_000:
            break
