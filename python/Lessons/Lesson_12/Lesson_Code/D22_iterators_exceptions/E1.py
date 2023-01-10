import string


class AlphabetIterator:
    def __init__(self, start_letter: str):
        if len(start_letter) == 0:
            raise ValueError("start letter can not be empty")
        if len(start_letter) != 1:
            raise ValueError(f"{start_letter} is not an upper or lower case letter")
        if not start_letter.isalpha():
            raise ValueError(f"{start_letter} is not an upper or lower case letter")
        self._start_letter = start_letter
        if start_letter.isupper():
            self._case = string.ascii_uppercase
        else:
            self._case = string.ascii_lowercase
        self._max_len = len(self._case)

    def __iter__(self):
        self.ind = self._case.index(self._start_letter)
        return self

    def __next__(self):
        if self.ind < self._max_len:
            curr = self.ind
            self.ind += 1
            return self._case[curr]
        else:
            raise StopIteration()


if __name__ == '__main__':
    while True:
        try:
            letter = input("Enter a letter (-1 to quit): ")
            if letter == '-1':
                break
            alphabet = AlphabetIterator(letter)
            for letter in alphabet:
                print(letter)
        except ValueError as err:
            print(err)
            continue
        except KeyboardInterrupt:
            exit(0)
