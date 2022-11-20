# Write a function that receives a hyphen-separated sequence of words
# as a parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.

# Sample input : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def sort_sequence(string: str) -> str:
    words = string.split("-")
    words.sort()
    return "-".join(words)


s = "green-red-yellow-black-white"
print(s)

print(sort_sequence(s))