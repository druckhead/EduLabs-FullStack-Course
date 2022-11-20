# Write a Python function that takes a tuple and returns
# a new tuple with unique elements of the first list.
# Arguments types: tuple
# Return value type: tuple


def unique_items(t: tuple) -> tuple:
    unique_t = []
    for item in t:
        if item not in unique_t:
            unique_t.append(item)
    return tuple(unique_t)


def unique_items2(t: tuple) -> tuple:
    set_items = set(t)
    return tuple(set_items)


items = (1, 2, 6, 3, 6, 10, 12, 1, 10, 12)

print(unique_items(items))

print(unique_items2(items))
