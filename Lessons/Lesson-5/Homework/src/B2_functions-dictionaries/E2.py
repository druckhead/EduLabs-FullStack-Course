from pprint import pprint

# Write a function that receives a sequence of key-value pairs and creates a dictionary of lists
# (and returns it). For example:

# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}


def create_dict_list(*args: tuple[str, int]) -> dict[str | list]:
    new_dict: dict[str, list] = dict()

    for arg in args[0]:
        if arg[0] not in new_dict.keys():
            new_dict[arg[0]] = [arg[1]]
        else:
            new_dict[arg[0]].append(arg[1])
    return  new_dict


l = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = create_dict_list(l)
# pprint(l)
pprint(d)