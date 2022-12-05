import string
from os import system


class Ebook:
    def __init__(self, f_path: str, w_page_lim: int):
        # page_num to page_content
        self.__pages: dict[int, str] = {}
        # page_num to list[Name_bookmark]
        self.__bookmarks: dict[int, list[str]] = {}
        # page_num to list[Name_bookmark]
        self.__recently_deleted: dict[int, list[str]] = {}

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
            self.__pages[curr_page - 1 if curr_page > 1 and curr_w_page == 0 else curr_page] += curr_w
            curr_w = ""
        self.__pages[curr_page] += curr_w

    def get_total_pages(self) -> int:
        """
        Return the total num of pages in the book
        :return: int
        """
        return len(self.__pages.keys())

    def display_page(self, number: int) -> None:
        """
        Displays the given page\n
        :param number: int
        :return: None
        """
        if number not in self.__pages:
            raise KeyError
        system("clear")
        print(self.__pages[number])

        if __debug__:
            print()
            print(f"Displaying page: {number}")
            print(f"It has {len(self.__pages[number].split())} words in it")

    def bookmark(self, name: str, page_num: int) -> None:
        """
        Save a bookmark according to the page_num and give it a name\n
        :param name: str
        :param page_num: int
        :return: None
        """
        if page_num not in self.__pages:
            raise KeyError
        if page_num not in self.__bookmarks:
            self.__bookmarks[page_num] = []
        self.__bookmarks[page_num].append(name)

    def del_bookmark(self, name: str) -> None:
        """
        Delete a single bookmark according to the given bookmark name\n
        :param name:
        :return: None
        """
        page_num = self._find_pg_num(bookmark_name=name, bookmarks_dict=self.__bookmarks)
        if page_num == -1:
            raise KeyError
        if page_num not in self.__recently_deleted:
            self.__recently_deleted[page_num] = []
        index = self.__bookmarks.get(page_num).index(name)
        deleted_mark = self.__bookmarks.get(page_num).pop(index)
        self.__recently_deleted.get(page_num).append(deleted_mark)

    def del_all_bookmarks_for_page(self, pg_num: int) -> None:
        """
        Delete all the bookmarks on a given page\n
        :param pg_num:
        :return: None
        """
        if pg_num not in self.__bookmarks:
            raise KeyError
        deleted_marks = self.__bookmarks.pop(pg_num)
        if pg_num not in self.__recently_deleted:
            self.__recently_deleted[pg_num] = []
        for mark in deleted_marks:
            self.__recently_deleted.get(pg_num).append(mark)

    def display_all_bookmarks(self) -> None:
        """
        Print all bookmarks\n
        :return: None
        """
        if len(self.__bookmarks) == 0:
            print("No bookmarks to display\n")
            return
        marks = "Book Marks\n" \
                "----------\n"
        for pg_num, bookmarks in self.__bookmarks.items():
            marks += f"Page: {pg_num}\n"
            for ind, bookmark in enumerate(bookmarks):
                marks += f"\tBookmark {ind + 1}, Name: {bookmark}\n"
            marks += "\n"
        print(marks[:-1])

    @staticmethod
    def _find_pg_num(bookmark_name: str, bookmarks_dict: dict[int, list[str]]) -> int:
        """
        Returns the page num of the bookmark according to its name\n
        :param bookmark_name: str
        :param bookmarks_dict: list[str]
        :return: int
        """
        bookmarks: list[str] = [name for list_names in bookmarks_dict.values() for name in list_names]
        if bookmark_name not in bookmarks:
            raise KeyError
        page_num = -1
        flag = False
        for pg_num, name_list in bookmarks_dict.items():
            if flag:
                break
            for curr_name in name_list:
                if curr_name == bookmark_name:
                    page_num = pg_num
                    flag = True
                    break
        return page_num

    # Display bookmarked page by bookmark name
    def display_by_bookmark_name(self, name: str) -> None:
        """
        Displays the page according to the bookmark name given\n
        :param name: str
        :return: None
        """
        page_num = self._find_pg_num(bookmark_name=name, bookmarks_dict=self.__bookmarks)
        if page_num == -1:
            raise KeyError
        self.display_page(page_num)

    def restore_deleted_bookmark(self, name: str) -> None:
        """
        Restore a single bookmark according to the name given\n
        :param name: str
        :return: None
        """
        page_num = self._find_pg_num(bookmark_name=name, bookmarks_dict=self.__recently_deleted)
        if page_num not in self.__recently_deleted:
            raise KeyError
        index = self.__recently_deleted.get(page_num).index(name)
        restored_mark = self.__recently_deleted.get(page_num).pop(index)
        if page_num not in self.__bookmarks:
            self.__bookmarks[page_num] = []
        self.__bookmarks.get(page_num).append(restored_mark)

    def restore_all_book_marks_on(self, page_num: int):
        """
        Restore recently deleted bookmarks from given page to current bookmarks on given page\n
        :param page_num:int
        :return: None
        """
        if page_num not in self.__recently_deleted:
            raise KeyError
        restored_marks = self.__recently_deleted.pop(page_num)
        if page_num not in self.__bookmarks:
            self.__bookmarks[page_num] = []
        for mark in restored_marks:
            self.__bookmarks.get(page_num).append(mark)


    def restore_all_bookmarks(self) -> None:
        """
        Restore all recently deleted bookmarks to current bookmarks\n
        """
        for bookmarks in self.__recently_deleted.values():
            for bookmark in bookmarks:
                self.restore_deleted_bookmark(bookmark)
