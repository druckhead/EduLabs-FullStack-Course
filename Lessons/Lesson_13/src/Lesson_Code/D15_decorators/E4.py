class InvalidArgumentError(Exception):
    def __init__(self, arg, min: int, max: int):
        super().__init__(f"{arg} is not in range ({min}, {max})")


def numeric_in_range(min: int, max: int):
    def wrapper(func):
        def decorated(*args, **kwargs):
            for arg in args:
                if not (min <= arg <= max):
                    raise InvalidArgumentError(arg, min, max)

            result = func(*args, **kwargs)
            return result

        return decorated

    return wrapper


@numeric_in_range(7, 12)
def foo(*args):
    print(*args)


if __name__ == '__main__':
    foo(7, 7, 7, 8, 9, 10, 11, 12)
    foo(1, 7, 7, 7, 8, 9, 10, 11, 12)
