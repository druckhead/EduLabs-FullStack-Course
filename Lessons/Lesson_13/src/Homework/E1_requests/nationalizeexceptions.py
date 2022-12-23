from requests.exceptions import *


class NameNotFound(RequestException):
    def __init__(self, name: str):
        super().__init__(f"Error Code: {404}, Name:'{name}' Not found")


class CountryIdNotFound(RequestException):
    def __init__(self, response: dict, country_id: str):
        super().__init__(f"Error Code: {response['status']}\nCountry ID:'{country_id}' {response['message']}")
