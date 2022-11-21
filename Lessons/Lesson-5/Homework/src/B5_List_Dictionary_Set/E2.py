# List:
# colors_2 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 'purple', 'orange with white straps']
# Create a function that receives a list and returns output (choose the right type) with unique elements only

# No duplicated elements
# Case insensitive
# Expected result: red,white, blue, sky blue, purple, orange with white straps.

colors_2 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 'purple', 'orange with white straps']


def unique(arg: list[str]) -> set[str]:
    s = set()
    for item in arg:
        s.add(item.lower())

    return s


print(unique(colors_2))