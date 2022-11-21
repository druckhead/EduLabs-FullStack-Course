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


# from pprint import pprint

# Create a function that receives my_cities and returns all the cities I’ve visited without duplications.

def visited_cities(_my_cities: dict[int, dict[str, list[str]]
                                    | dict[str, list[str]]
                                    | dict[str, list[str]]]) -> set[str]:
    city_set = set()

    for year, countries in _my_cities.items():
        for country, cities in countries.items():
            for city in cities:
                city_set.add(city.lower())

    # years = _my_cities.keys()
    # for year in years:
    #     countries = my_cities[year]
    #     for country in countries:
    #         cities = countries[country]
    #         for city in cities:
    #             city_set.add(city.lower())

    return city_set


print()
print(visited_cities(my_cities))
