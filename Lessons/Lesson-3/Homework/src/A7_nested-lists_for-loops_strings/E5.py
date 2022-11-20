# Find the shortest words
# Find the exact indexes (2-number indices)

goods = [
    ['apple', 'pear', 'peach', 'chery'],
['salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']
]

min_len = len(goods[0][0])
min_index_outer = 0
min_index_inner = 0

min_indices = []

# find the max string len
for item in goods:
    for string in item:
        if min_len >= len(string):
            min_len = len(string)

# iterate again to find the indices that are equal to max len
for item in goods:
    for string in item:
        if min_len == len(string):

            min_index_outer = goods.index(item)
            min_index_inner = item.index(string)
            print((string, f"index: {min_index_outer, min_index_inner}"))