# Find all the words that include letter ‘b’
# and store them in a new list.
# Print the list.

goods = [
    ['apple', 'pear', 'peach', 'chery'],
['salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']
]

include_b = []

for item in goods:
    for string in item:
        if 'b' in string:
            include_b.append(string)

print(include_b)
