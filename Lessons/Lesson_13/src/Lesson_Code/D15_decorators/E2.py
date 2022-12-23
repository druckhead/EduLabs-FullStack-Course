class InvalidArgumentError(Exception):
    def __init__(self, arg):
        super().__init__(f"{arg} is of type {type(arg)} not of type int or float")


def numeric_params(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not (type(arg) is int or type(arg) is float):
                raise InvalidArgumentError(arg)

        for kwarg in kwargs:
            if not (type(kwarg) is int or type(kwarg) is float):
                raise InvalidArgumentError(kwarg)

        result = func(*args, **kwargs)
        return result

    return wrapper


@numeric_params
def sum_and_diff(num1, num2):
    return num1 + num2, num1 - num2


if __name__ == '__main__':
    a = sum_and_diff(7, 1)
    print(a)
    b = sum_and_diff("a", "a")