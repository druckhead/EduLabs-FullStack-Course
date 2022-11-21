# Write a function to drop empty or None items from a given Dictionary. For example:
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': “”,}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

def rem_none_items(_dict: dict) -> None:
    items_to_pop = list()

    for k, v in _dict.items():
        if _dict.get(k) is None or len(_dict.get(k)) == 0:
            items_to_pop.append(k)

    for item in items_to_pop:
        if _dict.get(item) is None or len(_dict.get(item)) == 0:
            _dict.pop(item)
    return


d = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': ""}
print(d)
rem_none_items(d)
print(d)
