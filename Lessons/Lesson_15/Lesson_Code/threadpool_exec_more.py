from concurrent.futures import Future, ThreadPoolExecutor
from requests import get, exceptions
from time import perf_counter


def get_quote(quote_id: int):
    url = "https://api.kanye.rest"
    res = get(url)
    if res.status_code < 400:
        return {"id": quote_id, "quote": res.json()["quote"]}
    else:
        raise exceptions.RequestException()


def print_result(f: Future):
    if f.done():
        res = f.result()
        print(f"ID: {res['id']}, Quote: {res['quote']}")
    elif f.exception():
        raise f.exception()


def get_quotes(num_quotes: int):
    with ThreadPoolExecutor(max_workers=25) as executor:
        futures = [executor.submit(get_quote, i) for i in range(1, num_quotes + 1)]
        for future in futures:
            future.add_done_callback(print_result)


if __name__ == '__main__':
    s = perf_counter()
    get_quotes(num_quotes=100)
    e = perf_counter()
    print(f"[runtime: {e - s}s]")
