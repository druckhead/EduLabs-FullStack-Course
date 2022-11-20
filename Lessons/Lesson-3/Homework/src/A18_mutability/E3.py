########
# 3
########

countires_and_cities = [['Israel', ['Tel Aviv', 'Haifa', 'Beer Sheva']],
                       ['France', ['Paris', 'Lyon', 'Marseille']],
                       ['UK', ['London', 'Manchester', 'Southhampton']]]

israeli_cities = countires_and_cities[0][1] # ['Tel Aviv', 'Haifa', 'Beer Sheva']

israeli_cities.append('Netanya') # ['Tel Aviv', 'Haifa', 'Beer Sheva', 'Netanta']

new_israeli_cities = israeli_cities # ['Tel Aviv', 'Haifa', 'Beer Sheva', 'Netanta']

new_israeli_cities.append('Karmiel') # ['Tel Aviv', 'Haifa', 'Beer Sheva', 'Netanta', Karmiel]

print(israeli_cities is new_israeli_cities) # true
print(countires_and_cities is new_israeli_cities) # false
print(countires_and_cities is israeli_cities) # false
