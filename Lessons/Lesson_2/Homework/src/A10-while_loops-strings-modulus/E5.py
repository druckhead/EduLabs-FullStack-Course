even_count = 0

i = 0
while i < 10:
    string = input(f"{i}) Enter a string: ")
    if len(string) % 2 == 0:
        even_count += 1
    i += 1

print(f"\nThe amount of even strings entered: {even_count}")
