# Implement a decorator @valid_param_types that receives as parameter
# allowed argument types and validates whether the argument passed to a
# function answers this requirement. If the validation fails, the decorator
# should raise an InvalidArgument exception.
from typing import Callable, Any


def valid_param_types(allowed_types: list[type]):
    def wrapper(func):
        def decorator(*args, **kwargs):
            found = None
            invalid_arg = None
            for arg in args:
                found = False
                if type(arg) not in allowed_types:
                    raise TypeError(type(arg), f"is not in allowed types: {allowed_types}")
                for t in allowed_types:
                    if isinstance(arg, t):
                        found = True
                        break
                invalid_arg = arg
            if not found:
                raise TypeError(type(invalid_arg), f"is not in allowed types: {allowed_types}")

            invalid_kwarg = None
            found = None
            for kwarg in kwargs.values():
                found = False
                if type(kwarg) not in allowed_types:
                    raise TypeError(type(kwarg), f"is not in allowed types: {allowed_types}")
            for t in allowed_types:
                if isinstance(kwarg, t):
                    found = True
                    break
            invalid_kwarg = kwarg
            if not found:
                raise TypeError(type(invalid_kwarg), f"is not in allowed types: {allowed_types}")

            result = func(*args, **kwargs)
            return result
        return decorator
    return wrapper


@valid_param_types([str, int, float])
def foo(*args, **kwargs):
    pass


if __name__ == '__main__':
    foo("hello, world", "foo", "bar", 7, 7.7, verbose=True)
