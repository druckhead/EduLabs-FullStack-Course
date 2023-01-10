from concurrent.futures import ThreadPoolExecutor
from requests import get, exceptions
from time import perf_counter, sleep


def get_tweet() -> None:
    url = "https://api.kanye.rest/"
    response = get(url)
    if response.status_code < 400:
        tweet = response.json()["quote"]
        print(tweet)
    else:
        raise exceptions.RequestException()


def get_tweets(amount=1):
    with ThreadPoolExecutor(amount) as executor:
        futures = []
        for i in range(amount * 10, 0, -1):
            if i % 10 == 0:
                futures.append(executor.submit(get_tweet))
            sleep(0.1)
        print("DONE!")


if __name__ == '__main__':
    s = perf_counter()
    get_tweets(10)
    e = perf_counter()
    print(f"[runtime: {e - s}s]")
