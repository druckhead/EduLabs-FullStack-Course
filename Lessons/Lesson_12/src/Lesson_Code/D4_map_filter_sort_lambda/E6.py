# Use lambda and filter/map/sort. Given a list of strings,
# filter out those containing less than 2 "a" chars.
# For example, for ["apple", "ananas", "banana", "pear"], your code should return ["ananas", "banana"]

def filter_less_than_two(words: list[str]) -> list[str]:
    return list(
        filter(
            lambda word: word.count('a') >= 2,
            words
        )
    )


if __name__ == '__main__':
    print(filter_less_than_two(["apple", "ananas", "banana", "pear"]))
