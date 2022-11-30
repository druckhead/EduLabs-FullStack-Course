# Reverse every word that includes the letter “p”,
# and store the reverse version in a new list.
# Print the list.

goods = [
    ['apple', 'pear', 'peach', 'chery'],
    [
        'salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry',
        'blueberry', 'cloudberry', 'raspberry', 'blackberry'
    ]
]

new_list = []

for item in goods:
    for string in item:
        if 'p' in string:
            rev_string = string[::-1]
            new_list.append(rev_string)

print(new_list)
