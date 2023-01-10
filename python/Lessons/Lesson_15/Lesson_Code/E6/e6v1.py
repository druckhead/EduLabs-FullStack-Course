from time import sleep, perf_counter


def point_one_intervals(secs: int):
    for i in range(secs * 10, 0, -1):
        print(i / 10)
        sleep(0.1)
    print("DONE!")
    return


if __name__ == '__main__':
    s = perf_counter()
    point_one_intervals(3)
    e = perf_counter()
    print(f"[runtime: {(e - s):.5f}s]")