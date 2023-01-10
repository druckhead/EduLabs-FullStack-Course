# (Advanced) Write a Python function that takes a list and removes
# all the duplicate elements from the list. Note, you should mutate
# the list you received as an argument, not create a new one!

def remove_dup(_l: list) -> None:
    # _l: list = _l.reverse()

    len_l = len(_l)

    for i in range(len_l - 1, -1, -1):
        if _l.count(_l[i]) > 1:
            _l.pop(i)
    return


ls = ["party", "choc", "doc", 1,  "cat", "bug", "choc", "hello", "hello", "party", 1, 1, 1]
print(ls)
remove_dup(ls)
print(ls)

