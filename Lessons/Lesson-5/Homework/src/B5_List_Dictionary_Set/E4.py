from pprint import pprint


colors_0 = [
    'red', 'blue', 'Purple','white'
]

colors_1 = [
    'orange red', 'blue navy', 'BLUE pure','snow white', 'sky blue', 'pure purple',
    'white cream', 'Eggshell white','Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue'
]

colors_2 = [
    'red Crimson', 'Liberty blue', 'Purple pizzazz','white & Red', 'sky blue',
    'Pale purple', 'Orchid purple', 'BLUE pure'
]

# Create a function that receives 3 lists and returns output
# (choose the right single type) that will indicate which colors are derived from basic colors.
# Basic colors are ones stored in colors_0. Others are derived colors.

# Case insensitive

# TODO need to do

def derived_colors(l1: list[str], l2:list[str], l3: list[str]) -> set:
    colors_set: set[str] = set()
    colors_set: set[str] = set(l2).union(set(l3))

    derived_colors_set: set[str] = set()

    for basic_color in l1:
        for derived_color in colors_set:
            if basic_color.lower() in derived_color.lower():
                derived_colors_set.add(derived_color)

    return derived_colors_set


if __name__ == "__main__":
    s = derived_colors(colors_0, colors_1, colors_2)
    pprint(s)