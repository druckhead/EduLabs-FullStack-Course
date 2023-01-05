from pprint import pprint
# Write a function that receives a dictionary of lists and splits it into a list of dictionaries.
# For example:
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

# Split dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78},
# {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]


def split_dict(_d: dict[str, list]) -> list[dict[str]]:
    new_list: list[dict] = list()

    for k, v in _d.items():
        for i, _v in enumerate(v):
            # populate list until it has same len as the len of the k(key) : list(value)
            if len(new_list) != len(v):
                new_list.append({k: _v})
            else:
                # if same len can update dictionary in index i of list accordingly
                new_list[i].update({k: _v})
                # new_list[i][k] = _v

    return new_list


a = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
l = split_dict(a)
print(l)
