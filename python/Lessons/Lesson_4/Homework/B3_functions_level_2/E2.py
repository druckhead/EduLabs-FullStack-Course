# Write a program that can execute 2 actions (according to user choice): insert and search.

# Insert asks the user to insert a word and stores it.

# Search asks for a letter and a number and from all the
# words that have been stored before it displays only words
# in which the provided letter appeared exactly number times
words = []

# TODO improve code and validations

WELCOME_PROMPT = """
Press 1 to insert and store a word.\__n
Press 2 to search and display a word if a certain letter appears _n times.\__n
Press $ to quit.
"""

def insert_word(word: str) -> None:
    if word in words:
        print("\033[0;31mError: Word already in words!\033[0;m")
    if word not in words:
        words.append(word)
    return


def search(letter: str, num_times: int) -> None:
    results = []

    for word in words:
        if word.count(letter) == num_times:
            if word in results:
                continue
            if word not in results:
                results.append(word)
        print(results)
    return


if __name__ == "__main__":
    print(WELCOME_PROMPT)
    while True:
        x = (input("Input: "))
        if x == "$":
            break
        if x.isnumeric():
            int_x = int(x)
            if not (1 <= int_x <= 2):
                print("Error, invalid input\n")
                continue
        match int_x:
            case 1:
                word = input("Insert a word: ")
                insert_word(word)
            case 2:
                letter = input("Insert a letter: ")
                n = int(input("Enter a number: "))
                search(letter, n)
            case _:
                print("Invalid input\n")
                int_x = int(input())
