total_digits = 0
total_words = 0
total_chars = 0

digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

word = None
while word != '$':
    if word is not None:
        total_chars += len(word)
        # split if given multiple words in one input
        words = word.split()
        if not word.isnumeric() and word.isalnum():
            total_words += len(words)
        # count digits in input
        for digit in digits:
            total_digits += word.count(digit)
    word = input("Enter a word: ")

print(f"Total words: {total_words}\n"
      f"Total chars: {total_chars}\n"
      f"Total digits: {total_digits}")
