# Add  ‘2’ to every second word in each list (pear ⇒ pear2, chery ⇒chery2)

goods = [
    ['apple', 'pear', 'peach', 'chery'],
    [
        'salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry',
        'blueberry', 'cloudberry', 'raspberry', 'blackberry'
    ]
]

print(goods)
print()
for i in range(len(goods)):
    for j in range(len(goods[i])):
        if j % 2 == 1:
            string = goods[i][j] + '2'
            goods[i][j] = string

print(goods)