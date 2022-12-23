# Implement a decorator @single_str_arg that validates that function received exactly one argument
# and that the argument type is string. If the validation fails, the decorator
# should raise an InvalidArgument exception.

class ArgumentException(Exception):
    pass


class InvalidArgumentError(ArgumentException):
    pass


class TooManyArgumentsError(InvalidArgumentError):
    def __init__(self, num_args: int):
        super().__init__(f"Invalid number of arguments.\nReceived: {num_args}\nExpected: {1}")


class ArgumentTypeError(InvalidArgumentError):
    def __init__(self, arg):
        super().__init__(f"{arg} is of type {type(arg).__name__}. Expected str")


def single_str_arg(func):
    def wrapper(*args, **kwargs):
        num_args = len(args)
        if num_args != 1:
            raise TooManyArgumentsError(num_args)
        if not isinstance(args[0], str):
            raise ArgumentTypeError(args[0])
        result = func(*args, **kwargs)
        return result
    return wrapper


@single_str_arg
def foo(*args):
    for arg in args:
        print(arg)


if __name__ == '__main__':
    foo(6)
