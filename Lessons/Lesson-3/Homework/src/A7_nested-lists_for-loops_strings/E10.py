# Create a single list from the nested lists
# How many letters are in the list?

goods = [
    ['apple', 'pear', 'peach', 'chery'],
    [
        'salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry',
        'blueberry', 'cloudberry', 'raspberry', 'blackberry'
    ]
]

new_list = []
letter_count = 0

for item in goods:
    for string in item:
        # basic
        # letter_count += len(string)

        # check every char to ensure is actually a letter
        # and not number or other character
        for char in string:
            if char.isalpha():
                letter_count += 1
        new_list.append(string)

print(f"The new joined list is: {new_list}\n"
      f"The letter count in the new list is: {letter_count}")