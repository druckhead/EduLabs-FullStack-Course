# Implement a code that receives the layout of the seats in the aircraft as letters and returns the layout as numbers.
# For example:
# ABC DEF => 3 3
# AB CDEF GH => 2 4 2
# You can assume that the maximum number of seat “batches” in any aircraft is 3.

layout = input("Enter the plane layout (For example: ABC DEF): ")
seat_sets = layout.split()

for section in seat_sets:
    if seat_sets.index(section) < len(seat_sets) - 1:
        end = " "
    else:
        end = None

    print(len(section), end=end)