from time import perf_counter
from nationalizeexceptions import *
from E1 import Nationalize
from concurrent.futures import ThreadPoolExecutor
import nameslist

if __name__ == '__main__':
    start = perf_counter()
    n = Nationalize()
    names = nameslist.names
    countries = []

    with ThreadPoolExecutor(max_workers=1) as pool:
        for name in names:
            future = pool.submit(n.info, name)
            countries.append(future)
        last = countries[-1]
        succeed_count = 0
        for country in countries:
            try:
                print(country.result())
                if last != country:
                    print()
            except ConnectionError:
                print("No Connection")
                break
            except NameNotFound as no_name:
                print(f"{no_name}\n")
            except CountryIdNotFound as no_country:
                print(f"{no_country}\n")
            else:
                succeed_count += 1

        end = perf_counter()
        runtime = end - start

        if succeed_count:
            print(f"\nStats\n"
                  f"requests succeeded: {succeed_count}\n"
                  f"requests failed: {len(countries) - succeed_count}")

        print(f"Total runtime: [{runtime}s]")

        with open('time_log.txt', 'a') as f:
            f.write(f'Single thread elapsed time (100 names): {runtime}\n')
