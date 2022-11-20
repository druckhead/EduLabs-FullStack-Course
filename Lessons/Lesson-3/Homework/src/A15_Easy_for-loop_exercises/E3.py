cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']

j = 0
for i in range(len(countries)):
    print(f"{countries[i]} -", end=" ")
    if j < len(cities):
        print(cities[j])
        j += 1
