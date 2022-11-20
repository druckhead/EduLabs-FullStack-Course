illegal_chars = ('#', '<', '$', '+', '%', '>', '!',
                 '`', '&', '*', "'", '|', '{', '?',
                 '"', '=', '}', '/', ':', '\\', '@')

path = input("Enter a file path: ")
if len(path) == 0:
    exit("Error empty file path")

valid_windows_path = None
valid_mac_os_linux_path = None

contains_illegal_char = None

file_name = None
file_ext = None
file = None

directories = path.split('\\')[1:]

for char in illegal_chars:
    for folder in directories:
        if char in folder:
            contains_illegal_char = True
            break

if len(directories) > 0:
    file = directories[-1].split(".")

if file is not None and len(file) > 1:
    file_name = file[0]
    file_ext = file[1]

valid_windows_path = path[0].isupper() \
                     and path[1] == ':' \
                     and path[2] == '\\' \
                     and len(directories) > 2 \
                     and not contains_illegal_char \
                     and file_ext is not None

if valid_windows_path:
    print(f"Valid Windows path\n"
          f"Depth: {len(directories) - 1}\n"
          f"File Name no extension: {file_name}\n"
          f"Extension: {file_ext}")
else:
    print(f"\nInvalid Windows file path...\n"
          f"Checking if valid Mac or Linux path...\n")

    directories = path.split('/')[1:]

    for char in illegal_chars:
        for folder in directories:
            if char in folder:
                contains_illegal_char = True
                break

    if len(directories) > 0:
        file = directories[-1].split(".")

    if file is not None and len(file) > 1:
        file_name = file[0]
        file_ext = file[1]

    valid_mac_os_linux_path = path[0] == '/' \
        and len(directories) > 2 \
        and not contains_illegal_char \
        and file_ext is not None

    if valid_mac_os_linux_path:
        print(f"Valid Mac or Linux path\n"
              f"Depth: {len(directories) - 1}\n"
              f"File Name no extension: {file_name}\n"
              f"Extension: {file_ext}")
    else:
        print("Invalid mac or linux file path")
