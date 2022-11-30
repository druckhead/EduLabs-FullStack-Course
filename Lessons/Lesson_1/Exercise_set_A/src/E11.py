length_in_seconds = int(input("Movie length in seconds: "))

total_minutes_in_seconds = length_in_seconds % 3600
total_minutes = total_minutes_in_seconds // 60
total_hours = length_in_seconds // 3600
total_seconds = total_minutes_in_seconds % 60

if len(str(total_hours)) < 2:
    hours = "0" + str(total_hours)
else:
    hours = str(total_hours)
if len(str(total_minutes)) < 2:
    minutes = "0" + str(total_minutes)
else:
    minutes = str(total_minutes)
if len(str(total_seconds)) > 2:
    seconds = "0" + str(total_seconds)
else:
    seconds = str(total_seconds)

print(f"The movie length is: {hours}:{minutes}:{seconds}")

