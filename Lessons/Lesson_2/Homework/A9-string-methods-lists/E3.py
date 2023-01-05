# Get string as an input, and print out string statistics:
# Amount of words
# Amount of chars
# Amount of non-whitespace chars
# Amount of vowels
# --------------------------------------------------------------------------

str_input = input("Enter a string: ")


# count the number of words
words_list = str_input.split()
word_count = len(words_list)

# count the number of chars
char_count = len(str_input)

# chars without spaces
new_str = str_input.replace(" ", "")
without_spaces = len(new_str)

# count the vowels
vowel_count = 0
# vowel_count += str_input.lower().count('a')
# vowel_count += str_input.lower().count('e')
# vowel_count += str_input.lower().count('i')
# vowel_count += str_input.lower().count('o')
# vowel_count += str_input.lower().count('u')
# vowel_count += str_input.lower().count('y')

# count vowels with loop
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for vowel in vowels:
    vowel_count += str_input.count(vowel)

print(f"Word count: {word_count}\n"
      f"Char count: {char_count}\n"
      f"Char w/o spaces: {without_spaces}\n"
      f"vowel count: {vowel_count}")

