# List:

# color_1 = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
# colors_2 = ['red', 'White', 'BLUE','white & Red', 'sky blue', 'purple', 'orange with white straps']

# Create a function that receives two lists and returns output (choose the right type)
# that includes colors that exist in both lists

# Case insensitive

color_1 = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
colors_2 = ['red', 'White', 'BLUE','white & Red', 'sky blue', 'purple', 'orange with white straps']

def exists_in_both(l1: list[str], l2: list[str]) -> set[str]:
    l1_set = set()
    l2_set = set()

    for l in l1:
        l1_set.add(l.lower())
    for l in l2:
        l2_set.add(l.lower())

    return l1_set.intersection(l2_set)


print(exists_in_both(color_1, colors_2))
