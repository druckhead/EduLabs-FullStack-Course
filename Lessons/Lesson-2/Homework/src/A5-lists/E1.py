"""
slicing operator and nested lists
"""

ls = [['Paris', 'London', 'New York'],
      [45, True, 5.5, 'hello'], -3, [5, ['#', '$', '%', '^', [10, 20, 30, 40]]],
      [['a'], ['b'], 'c', [['d']]]]

# 1
print(ls[2])
# 2
print(ls[1][2])
# 3
print(ls[0][::-1])
# 4
print(ls[1:3])
# 5
print(ls[3][1][3])
# 6
print(ls[4][0][0])
# 7
print(ls[4][1])
# 8
print(ls[4][3][0][0])
# 9
print(ls[3][1][4][1:5:2])
# 10
print(ls[3][1][3::-3])

