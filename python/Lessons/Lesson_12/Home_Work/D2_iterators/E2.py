class EBook:
    def __init__(self, book_path: str, words_num: int):

        self.book_path = book_path
        self.pages: dict[int: str] = {}

        with open(book_path, 'r') as fh:
            content = fh.read()

        all_words: list[str] = content.split()
        page_num = 1
        for i in range(0, len(all_words), words_num):
            page_words = all_words[i: i + words_num]
            self.pages[page_num] = " ".join(page_words)
            page_num += 1

    def __iter__(self):
        self.__page = 1
        return self

    def __next__(self):
        if self.__page not in self.pages.keys():
            raise StopIteration()
        curr_page = self.__page
        self.__page += 1
        return self.get_page_content(curr_page)

    def get_total_pages(self):
        return len(self.pages)

    def get_page_content(self, page_num) -> str | None:
        if page_num not in self.pages:
            return None
        return self.pages[page_num]


if __name__ == '__main__':
    book = EBook('alice_in_wonderland.txt', 1000)
    # print(f"Total pages: {book.get_total_pages()}")
    # print(f"Page 10: {book.get_page_content(27)}")
    for page_num, page_content in enumerate(book):
        print(f"Page: {page_num + 1}\n{page_content}\n")
