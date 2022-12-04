import string


class Ebook:
    def __init__(self, f_path: str, w_page_lim: int):
        # page_num to page_content
        self.__pages: dict[int, str] = {}

        curr_w_page: int = 0
        curr_page: int = 1
        with open(f_path, 'r') as fh:
            content = fh.read()
        curr_w = ""
        for c in content:
            curr_w += c
            if c not in string.whitespace:
                continue
            else:
                if curr_w not in string.whitespace:
                    curr_w_page += 1
                if curr_w_page == w_page_lim:
                    curr_page += 1
                    curr_w_page = 0
                if curr_page not in self.__pages:
                    self.__pages[curr_page] = ""
                self.__pages[curr_page] += curr_w
                curr_w = ""

    def get_total_pages(self) -> int:
        return len(self.__pages.keys())

    def display_page(self, number: int) -> None:
        if number not in self.__pages:
            raise KeyError
        print(self.__pages[number])


if __name__ == "__main__":
    ebook = Ebook(
        "/Users/danielraz/EduLabs-FullStack-Course"
        "/Lessons/Lesson_9/src/Lesson_Code/files/data"
        "/alice_in_wonderland.txt",
        100)

    ebook.display_page(1)
