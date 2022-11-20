# Create a new list with the structure of the original list,
# but such that all the words will be replaced with only 3
# first letters of each original word.

goods = [
    ['apple', 'pear', 'peach', 'chery'],
    [
        'salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry',
        'blueberry', 'cloudberry', 'raspberry', 'blackberry'
    ]
]

new_goods = []

for item in goods:
    new_goods.append([])
    list_index = goods.index(item)
    for string in item:
        short_string = string[0:3]
        new_goods[list_index].append(short_string)

print(new_goods)

