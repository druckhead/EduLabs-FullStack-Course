# Create a function that receives 2 lists and returns output
# (choose the right single type) with unique elements from list #1 that are absent in list #2
# Case insensitive

colors_1 = ['orange red', 'blue navy', 'BLUE pure','snow white', 'sky blue',
            'pure purple', 'white cream', 'Eggshell white','Orchid purple',
            'Medium blue', 'Egyptian blue', 'Neon blue'
            ]
colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz','white & Red',
            'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure'
            ]


def unique(l1: list[str], l2: list[str]) -> set[str]:
    s1 = set()
    s2 = set()

    for item in l1:
        s1.add(item.lower())
    for item in l2:
        s2.add(item.lower())

    # return s1.difference(s1.intersection(s2))

    return s1.union(s2).difference(s2)


print(unique(colors_1, colors_2))
