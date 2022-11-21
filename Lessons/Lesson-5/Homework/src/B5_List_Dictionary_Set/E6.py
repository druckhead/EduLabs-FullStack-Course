from pprint import pprint

# Input dictionary for example
my_cities = {
    2008: {'Germany': ['Berlin', 'Munich'],
           'France': ['Paris', 'Leon', 'Bordeaux']},
    2009: {'China': ['Hong Kong', 'Shanghai', 'Beijing'],
           'Japan': ['Nagoya', 'Toyokawa', 'Yatomi'],
           'Mexico': ['Tijuana', 'Ecatepec']},
    2010: {'Germany': ['Berlin', 'Dusseldorf'],
           'France': ['Paris', 'Nice', 'Bordeaux'],
           'Japan': ['Tokyo', 'Toyokawa', 'Yatomi']}
}
# Create a function that receives my_cities and returns dictionary arranged as follows:
# Keys = cities
# Values = all dates when I was visiting the cities
# Example of output:
# my_cities_out = {'Berlin':[2008, 2010],....}


def city_dates(_my_cities: dict[int, dict[str, list[str]]
                                | dict[str, list[str]]
                                | dict[str, list[str]]]) -> dict:
    new_dict = dict()

    for year, countries in _my_cities.items():
        for country, cities in countries.items():
            for city in cities:
                new_dict[city] = []

    for year, countries in _my_cities.items():
        for country, cities in countries.items():
            for city in cities:
                new_dict[city].append(year)

    return new_dict


pprint(city_dates(my_cities))
