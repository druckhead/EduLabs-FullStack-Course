# Write a function to drop empty or None items from a given Dictionary. For example:
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': “”,}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

def rem_none_items(_dict: dict) -> None:
    empty_items = ([], {}, (), "", None)
    l = list()

    for k, v in _dict.items():
        if v in empty_items:
            l.append(k)
    for i in l:
        _dict.pop(i)


    return


d = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': "", "c6": True}
print(d)
rem_none_items(d)
print(d)
