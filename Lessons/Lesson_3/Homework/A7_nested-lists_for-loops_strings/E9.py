# Print all the words that include more than 5 letters

goods = [
    ['apple', 'pear', 'peach', 'chery'],
    [
        'salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry',
        'blueberry', 'cloudberry', 'raspberry', 'blackberry'
    ]
]

for item in goods:
    for i, string in enumerate(item):
        if len(string) > 5:
            print(f"{i}) {string}")
