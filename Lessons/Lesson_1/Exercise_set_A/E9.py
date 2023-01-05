current_salary = int(input("Current monthly salary: "))
new_salary = int(input("New monthly salary: "))

diff = abs(current_salary - new_salary)

if current_salary - new_salary < 0:
    print(f"If you take the new job, you will earn ${diff} more per year")
elif current_salary - new_salary > 0:
    print(f"If you take the new job, you will earn ${diff} less per year")
else:
    print("You will earn the same salary in both jobs")