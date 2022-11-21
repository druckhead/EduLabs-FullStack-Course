# Lists:
# flowers = ['Rose','Lily','Tulip','Orchid','Carnation', 'Hyacinth', 'Rose']
# color = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
# Create a function that receives 2 lists and returns a dictionary, where
# keys are elements from the list #1 and values are elements from the list #2.

# Assume: number of elements in both lists are equal
# Don’t lose any information

from pprint import pprint

flowers = ['Rose', 'Lily', 'Tulip', 'Orchid', 'Carnation', 'Hyacinth', 'Rose', 'Lily']
color = ['red', 'white', 'blue', 'white', 'pink', 'purple', 'white', 'yellow']


def flower_count(_flower: str, _flower_dict: dict[str | str]) -> int:
    """
    returns the amount of times _flower is in _flower_dict
    :param _flower:
    :param _flower_dict:
    :return:
    """
    count = 0
    for flower in _flower_dict.keys():
        if flower == _flower:
            count += 1
    return count


def create_dict(_flowers: list[str], _color: list[str]) -> dict[str]:
    new_dict = dict()

    for i, flower in enumerate(_flowers):
        add_on = ""
        count = 0
        if flower in new_dict.keys():
            count: int = flower_count(flower, new_dict)
        add_on = " " + str(count + 1) if count > 0 else ""

        new_dict[flower + add_on] = color[i]

    return new_dict

def lists_to_dict(list1: list[str], list2: list[str])->dict:
    my_dict = {}
    for i in range(len(flowers)):
        if flowers[i] not in my_dict:
            my_dict.update({flowers[i]: [color[i]]})
        else:
            my_dict[flowers[i]].append(color[i])
    return(my_dict)


pprint(create_dict(flowers, color))

print()

pprint(lists_to_dict(flowers, color))