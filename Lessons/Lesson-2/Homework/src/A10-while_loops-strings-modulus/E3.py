students = []
total_grades = 0

print("To quit the program enter $$$")

name = None
while name != "$$$":
    if name is not None:
        split_input = name.split()
        if len(split_input) > 0:
            students.append(name.split()[0])
        if len(split_input) > 1:
            total_grades += int(name.split()[1])
    name = input(f"Enter a students name and grade "
                 f"(if no grade is entered then grade is 0): ")

print(f"names: {students}\n"
      f"amount of names: {len(students)}\n"
      f"Avg grade: {total_grades / len(students)}")
