# Find how many words starts with vowels
# Provide their indexes
vowels = ('a', 'e', 'i', 'o', 'u', 'y')

goods = [
    ['apple', 'pear', 'peach', 'chery'],
['salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']
]

index_outer = 0
index_inner = 0

start_with_vowel_list = []

for item in goods:
    for string in item:
        for vowel in vowels:
            if string.startswith(vowel):
                index_outer = goods.index(item)
                index_inner = item.index(string)
                start_with_vowel_list.append((index_outer, index_inner))

print(f"The amount of words that start with a vowel: {len(start_with_vowel_list)}\n"
      f"Their indices: {start_with_vowel_list}")