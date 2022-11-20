# How many words include “berry”?
# What are their indexes (2-number indices)?

goods = [
    ['apple', 'pear', 'peach', 'chery'],
    [
        'salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry',
        'blueberry', 'cloudberry', 'raspberry', 'blackberry'
    ]
]

min_index_outer = 0
min_index_inner = 0

for item in goods:
    for string in item:
        if 'berry' in string:
            min_index_outer = goods.index(item)
            min_index_inner = item.index(string)
            print((string, f"index: {min_index_outer, min_index_inner}"))
