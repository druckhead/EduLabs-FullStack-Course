# I
word = input("Enter a word: ")
vowels = ('a', 'e', 'i', 'o', 'u', 'y')

# check if word ends with any character in the vowels tuple
does_end_in_vowel = word.endswith(vowels)

print(does_end_in_vowel)

# II
word = input("Enter a String: ")
contains_only_whitespace = None

# split with no param splits all whitespace
# join concatenates all items in list into string
word = ''.join(word.split())

# if word is not empty string => it had characters other than whitespace
if len(word) > 0:
    print("the word you entered does NOT contain only white spaces")
else:
    print("the word you entered DOES contain only white spaces")

# III
sentence = input("Enter a sentence: ")
print(sentence.title())
