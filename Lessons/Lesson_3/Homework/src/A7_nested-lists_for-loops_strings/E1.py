# Find the longest words
# Find the exact indexes (it should contain 2 numbers - the inner list idx + the string index.)
# For example, the index for ‘durian’ is: (1, 3)

# Find and print how many vowels in this words

goods = [
    ['apple', 'pear', 'peach', 'chery'],
    ['salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry', 'blueberry', 'cloudberry', 'raspberry',
     'blackberry']
]

max_len = 0
max_index_outer = 0
max_index_inner = 0

# find the max string len
for item in goods:
    for string in item:
        if max_len <= len(string):
            max_len = len(string)

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

# iterate again to find the indices that are equal to max len
for item in goods:
    for string in item:
        if max_len == len(string):
            vowel_count = 0

            max_index_outer = goods.index(item)
            max_index_inner = item.index(string)
            print(
                (
                    f"The longest Word: {string}",
                    f"The index: {max_index_outer, max_index_inner}"
                )
            )

            for vowel in vowels:
                vowel_count += string.count(vowel)

            print((string, f"The amount of vowels: {vowel_count}"), end="\n\n")
