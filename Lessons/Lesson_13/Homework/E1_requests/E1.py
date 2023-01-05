from concurrent.futures import ThreadPoolExecutor, wait
import nameslist
from time import perf_counter
import requests
from datetime import datetime
import pytz
from nationalizeexceptions import *
from pytz import timezone


def _request(url: str, params=None) -> (int, requests.Response):
    request = requests.get(url, params)
    return request.status_code, request


def _get_countries_list(response: requests.Response, name: str) -> list[dict[str, str | int]]:
    response_dict: dict[str, list[dict[str, str | int]]] = response.json()
    countries_list = response_dict.get("country")
    if len(countries_list) == 0:
        raise NameNotFound(name)

    return countries_list


def _get_most_probable_country_id(countries_list: list[dict[str, str | int]] | None) -> str:
    countries_list.sort(key=lambda country: country.get("probability"),
                        reverse=True)

    most_probable_country_dict = countries_list[0]
    country_id = most_probable_country_dict.get("country_id")

    return country_id


def _list_as_string(lst: list) -> str:
    string = ""
    last = lst[-1]
    for item in lst:
        string += item
        if item != last:
            string += ", "

    return string


class Nationalize:
    __BASE_NATIONALIZE_URL = "https://api.nationalize.io"
    __BASE_RESTCOUNTRIES_URL = "https://restcountries.com/v3.1/alpha/"

    def __init__(self):
        pass

    def __get_country_json(self, name: str) -> dict | None:
        most_probable_country: dict | None = None
        response_code, nationalize_response = _request(self.__BASE_NATIONALIZE_URL, params={"name": name})
        if response_code == 200:
            countries_list = _get_countries_list(nationalize_response, name)
            country_id = _get_most_probable_country_id(countries_list)

            response_code, restcountries_response = _request(self.__BASE_RESTCOUNTRIES_URL + country_id)
            if response_code >= 400:
                r = restcountries_response.json()
                raise CountryIdNotFound(r, country_id)

            if restcountries_response.status_code == 200:
                most_probable_country = restcountries_response.json()[0]

        return most_probable_country

    @staticmethod
    def _nationalize_by_name(country_dict) -> str:
        return country_dict.get("name").get("official")

    @staticmethod
    def _nationalize_by_continent(country_dict) -> str:
        return country_dict.get("continents")[0]

    @staticmethod
    def _language_spoken(country_dict) -> list[str]:
        languages_list: list = []
        languages_dict: dict = country_dict.get("languages")
        for language in languages_dict.values():
            languages_list.append(language)

        return languages_list

    @staticmethod
    def _time_zones(country_dict) -> list[str]:
        time_format = "%H:%M:%S UTC%z"

        times: list[str] = []
        timezones: list[str] = country_dict.get("timezones")
        for _ in timezones:
            now = datetime.now(timezone('UTC'))
            zones = pytz.country_timezones[country_dict.get("cca2")]
            for zone in zones:
                now_other = now.astimezone(timezone(zone))
                times.append(now_other.strftime(time_format))

        return times

    def info(self, name: str) -> str:
        most_probable_country = self.__get_country_json(name)
        return f"Name: {name}\n" \
               f"Most probable country: {self._nationalize_by_name(most_probable_country)}\n" \
               f"Continent: {self._nationalize_by_continent(most_probable_country)}\n" \
               f"Language(s) spoken: {_list_as_string(self._language_spoken(most_probable_country))}\n" \
               f"Timezones: {_list_as_string(self._time_zones(most_probable_country))}"


if __name__ == '__main__':
    start = perf_counter()
    n = Nationalize()
    names = nameslist.names[:10]
    countries = []

    with ThreadPoolExecutor(max_workers=10) as pool:
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
