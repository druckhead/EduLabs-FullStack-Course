# In which sublist are there the maximum number of vowels?
# Print it’s index.
vowels = ('a', 'e', 'i', 'o', 'u', 'y')

goods = [
    ['apple', 'pear', 'peach', 'chery'],
['salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']
]

max_count = 0

index = 0

for item in goods:
    current_count = 0
    for string in item:
        for vowel in vowels:
            if vowel in string:
                current_count += 1

        if current_count > max_count:
            max_count = current_count
            index = goods.index(item)

print(f"Max number of vowels in a sublist is: {max_count}\n"
      f"This sublist is at index: {index}")