from ebook import Ebook

if __name__ == "__main__":
    ebook = Ebook(
        "/Users/danielraz/EduLabs-FullStack-Course"
        "/Lessons/Lesson_9/src/Lesson_Code/files/data"
        "/alice_in_wonderland.txt",
        100)

    # ebook.display_page(1)

    ebook.bookmark("Expo", 1)
    ebook.bookmark("Mid", 133)
    ebook.bookmark("Alice", 1)
    ebook.bookmark("Ending", 265)

    ebook.display_all_bookmarks()

    ebook.del_bookmark("Expo")
    ebook.del_all_bookmarks_for_page(1)
    ebook.del_all_bookmarks_for_page(265)

    ebook.display_all_bookmarks()

    ebook.display_by_bookmark_name("Mid")
    # ebook.display_by_bookmark_name("Alice")

    print()

    ebook.display_all_bookmarks()

    ebook.restore_deleted_bookmark("Expo")

    ebook.display_all_bookmarks()

    ebook.restore_all_bookmarks()

    ebook.display_all_bookmarks()

    ebook.del_all_bookmarks_for_page(1)
    ebook.del_all_bookmarks_for_page(133)
    ebook.del_all_bookmarks_for_page(265)

    ebook.display_all_bookmarks()

    ebook.restore_all_book_marks_on(1)

    ebook.display_all_bookmarks()

    ebook.restore_all_book_marks_on(133)

    ebook.display_all_bookmarks()

    ebook.restore_all_book_marks_on(265)

    ebook.display_all_bookmarks()