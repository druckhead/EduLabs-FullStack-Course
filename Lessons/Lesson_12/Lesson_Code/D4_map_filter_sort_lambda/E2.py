def filter_vowels(any_string: str) -> str:
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    return ''.join(
        filter(
            lambda letter: letter not in vowels, any_string
        )
    )


if __name__ == '__main__':
    print(filter_vowels("Hello, World!"))
    print(filter_vowels("Magic Mountain is so fun"))
    print(filter_vowels("What is up my amigo?"))
    print(filter_vowels("EduLabs Python Morning November 2022"))
