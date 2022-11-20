# Create a single list where all the words are from the “goods” list. For each word in the list:
# Cut last 3 letters
# Add cutted 3 letters to the beginning of the word in the reverse order
# Was ‘apple’ ⇒ ‘ap’ +’ple’ ⇒ ‘ple’ +’ap’ ⇒ ‘elp’ + ‘ap’ ⇒ final result: ‘alpap’

goods = [
    ['apple', 'pear', 'peach', 'chery'],
    [
        'salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry',
        'blueberry', 'cloudberry', 'raspberry', 'blackberry'
    ]
]

# A
new_goods = []
for item in goods:
    for string in item:
        new_string = string[0:-3]
        new_goods.append(new_string)
print(new_goods)

print()

# B
new_goods = []
for item in goods:
    for string in item:
        new_string = string[-1:-4:-1] + string[0:-3]
        new_goods.append(new_string)
print(new_goods)