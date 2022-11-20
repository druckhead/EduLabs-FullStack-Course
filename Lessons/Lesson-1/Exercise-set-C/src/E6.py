plane_seat = input("Enter your plane seat (For example; 4J or 23C): ")
layout = input("Enter the plane layout (For example: ABC DEF): ")

seat = ""
seat_letter = ""
location = ""

for char in plane_seat:
    if char.isnumeric():
        seat += char
    else:
        seat_letter = char

seat_cols = layout.split()

for col in seat_cols:
    if col.find(seat_letter) != -1:
        col_index = seat_cols.index(col)
        seat_index = seat_cols[col_index].find(seat_letter)
        break

if col_index == 0:
    if seat_index == 0:
        location = "Window"
    elif seat_index < len(seat_cols[col_index]) - 1:
        location = "Middle"
    else:
        location = "Aisle"
elif col_index < len(seat_cols) - 1:
    if seat_index == 0 or seat_index == len(seat_cols[col_index]) - 1:
        location = "Aisle"
    else:
        location = "Middle"
else:
    if seat_index == 0:
        location = "Aisle"
    elif seat_index < len(seat_cols[col_index]) - 1:
        location = "Middle"
    else:
        location = "Window"

print(f"Row number: {seat} Char: {seat_letter} {location}")
