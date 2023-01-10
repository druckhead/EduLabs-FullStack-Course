from math import factorial
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from time import perf_counter


def calc_factorials(nums: list) -> tuple[list[int], list[int]]:
    """

    :param nums: a list of numbers to calculate their factorial
    :return: A tuple of lists, the first list of the factorials, the second list of the original nums
    """

    with ThreadPoolExecutor(len(nums)) as thread_executor:
        # submit the factorial calculation tasks
        tfutures = [thread_executor.submit(factorial, num) for num in nums]

        # get the factorial data
        data = [tfuture.result() for tfuture in tfutures]

        return data, nums


def main(factorials) -> None:
    n_workers = 12
    with ProcessPoolExecutor(n_workers) as process_executor:
        pfutures = []
        # split the operations
        chunksize = round(len(factorials) / n_workers)
        for i in range(0, len(factorials), chunksize):
            # select a chunk of numbers
            facts = factorials[i:(i + chunksize)]
            # submit the chunk calculation task
            pfuture = process_executor.submit(calc_factorials, facts)
            pfutures.append(pfuture)

        # print the factorials
        for future in as_completed(pfutures):
            data, nums = future.result()
            for d, n in zip(data, nums):
                print(f"{n}! = {d}")


if __name__ == '__main__':
    factorial_nums = [1550 for _ in range(100_000)]
    start = perf_counter()
    main(factorial_nums)
    end = perf_counter()
    print("Done")
    print(f"[runtime: {end - start}s]")
