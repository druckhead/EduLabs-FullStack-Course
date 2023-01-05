from time import perf_counter, perf_counter_ns


class InvalidUnit(ValueError):
    def __init__(self, time_unit, units):
        super().__init__(f"'{time_unit}' not in available units.\nExpected units: {units}")


def performance_log(time_unit):
    units = ('s', 'ms', 'ns')
    if time_unit not in units:
        raise InvalidUnit(time_unit, units)

    def wrapper(func):
        def decorator(*args, **kwargs):
            time_func = perf_counter if time_unit != 'ns' else perf_counter_ns

            # get start time
            t_start = time_func()

            result = func(*args, **kwargs)

            # get end time and calculate total runtime
            t_end = time_func()
            t_runtime = t_end - t_start
            if time_unit == "ms":
                t_runtime *= 1000

            print(f"[runtime: {t_runtime}{time_unit}]")
            return result

        return decorator

    return wrapper


@performance_log(time_unit="ms")
def long_running_function(num, iters, verbose=False):
    val = 1
    for i in range(iters):
        val *= num
    if verbose:
        print(val)
    return val


@performance_log(time_unit="ns")
def sum_and_diff(num1, num2, verbose=False):
    ret_val = num1 + num2, num1 - num2
    if verbose:
        print(ret_val)
    return ret_val


if __name__ == '__main__':
    try:
        long_running_function(2, 500, verbose=True)
    except InvalidUnit as err:
        print(err)

    print()

    try:
        t = sum_and_diff(12, 20, verbose=True)
    except InvalidUnit as err:
        print(err)
