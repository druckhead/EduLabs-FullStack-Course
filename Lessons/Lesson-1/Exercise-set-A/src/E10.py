minutes = int(input("Movie length in minutes: "))

hours = minutes // 60

print(f"The movie length is: {hours}:{minutes - hours * 60}")