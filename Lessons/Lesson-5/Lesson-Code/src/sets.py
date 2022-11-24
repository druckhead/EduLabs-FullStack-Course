def change(s: set, to_remove: str, to_add: str):
    s.remove(to_remove)
    s.add(to_add)


abc = {'Sun', 'Mon', 'Tues'}
print(abc)
change(abc, 'Sun', 'Wed')
print(abc)

