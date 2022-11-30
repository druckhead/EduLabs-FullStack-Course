# You have a list of names.
# Using a for loop append each item with a Dr. prefix, and insert the new strings in a new list.
# Print the result list.
# For example, given the list:
# names = ['Moshe', 'Orly', 'David', 'Jack', 'Ofer', 'James']
# The expected output is:
# ['Dr. Moshe', 'Dr. Orly', 'Dr. David', 'Dr. Jack', 'Dr. Ofer', 'Dr. James']

names = ['Moshe', 'Orly', 'David', 'Jack', 'Ofer', 'James']
print(names)

new_names = []

for name in names:
    appended_name = "Dr. " + name
    new_names.append(appended_name)

print(new_names)