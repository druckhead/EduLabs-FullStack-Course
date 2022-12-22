import requests


def _request(url: str, params):
    request = requests.get(url, params)
    return request.status_code, request


class Nationalize:
    __BASE_NATIONALIZE_URL = "https://api.nationalize.io"
    __BASE_RESTCOUNTRIES_URL = "https://restcountries.com/v3.1/alpha/"

    def __init__(self):
        pass

    def nationalize_by_name(self, name: str) -> str:
        most_probable_country = None
        nationalize_response = requests.get(self.__BASE_NATIONALIZE_URL, params={"name": name})
        if nationalize_response.status_code == 200:
            response_dict: dict[str, list[dict[str, str | int]]] = nationalize_response.json()
            countries_list = response_dict.get("country")
            if len(countries_list) == 0:
                raise Exception(404, f"name: {name} not found")

            countries_list.sort(key=lambda country: country.get("probability"),
                                reverse=True)

            most_probable_country_dict = countries_list[0]
            country_id = most_probable_country_dict.get("country_id")

            restcountries_response = requests.get(self.__BASE_RESTCOUNTRIES_URL + country_id)
            if restcountries_response.status_code >= 400:
                r = restcountries_response.json()
                raise Exception(f"Error Code: {r['status']} {r['message']}")
            if restcountries_response.status_code == 200:
                most_probable_country = restcountries_response.json()[0].get("name").get("official")
        return most_probable_country

    def nationalize_by_continent(self, name: str) -> str:
        pass


if __name__ == '__main__':
    n = Nationalize()
    try:
        country_name = n.nationalize_by_name("Daniel")
        print(country_name)
    except Exception as err:
        print(err)
