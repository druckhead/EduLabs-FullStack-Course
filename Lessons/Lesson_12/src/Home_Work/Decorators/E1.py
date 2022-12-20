from time import perf_counter


def performance_log(other_func):
    def wrapper(*args, **kwargs):
        # get start time
        t_start = perf_counter()

        result = other_func(*args, **kwargs)

        # get end time and calculate total runtime
        t_end = perf_counter()
        t_runtime = t_end - t_start
        print(f"[runtime: {t_runtime}sec]")
        return result

    return wrapper


@performance_log
def long_running_function(num, iters):
    val = 1
    for i in range(iters):
        val *= num
    return val


if __name__ == '__main__':
    print(long_running_function(2, 100000, verbose=True))
