# In this exercise you will get used to reading code documentation,
# which is an important part of every developer's daily job.
# Use the following official python string documentation and solve the exercises:
# https://docs.python.org/3/library/stdtypes.html#string-methods

# I
# Receive a word from a user, and print out whether the word ends with a vowel (a, e, i, o, u, y)

# II
# Receive a string from a user, and print out whether the string contains only whitespaces.

# III
# Receive a sentence from a user, and return the same sentence while every word in it starts from uppercase.
# For example, for the input "The sun is shining", your program should return: "The Sun Is Shining"

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
