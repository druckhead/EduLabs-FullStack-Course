illegal_chars = ('#', '<', '$', '+', '%', '>', '!',
                 '`', '&', '*', "'", '|', '{', '?',
                 '"', '=', '}', '@')

valid_windows_path = None
valid_mac_os_linux_path = None

path = input("Enter a file path: ")
if len(path) == 0:
    exit("Error: empty file path")

# check that the path doesn't contain any illegal characters
for char in illegal_chars:
    if char in path:
        exit(f"Path contains invalid character")

file = None
file_name = None
file_ext = None

# start checking windows path validity

# get all directories in path
# and make sure directories are separated by double back-slash (\\)
directories = path.split('\\')[1:]
if len(directories) > 0:
    file = directories[-1].split(".")
    # get file name and extension
    if file is not None and len(file) > 1:
        file_name = file[0]
        file_ext = file[1]
    else:
        exit(f"No file specified or file has no extension\n"
             f"Exiting...")

    """
    check:
    1) first character is uppercase letter (Home directory)
    2) path has ':' separator
    3) separator is followed by a double back-slash
    4) file has an extension
    """
    valid_windows_path = path[0].isupper() \
        and path[1] == ':' \
        and path[2] == '\\' \
        and len(directories) > 2 \
        and "/" not in path \
        and file_ext is not None

    if valid_windows_path:
        print(f"Valid Windows path\n"
              f"Depth: {len(directories) - 1}\n"
              f"File Name no extension: {file_name}\n"
              f"File extension: {file_ext}")
        exit(0)

# windows validity failed
# check mac or linux validity
print(f"\nInvalid Windows file path...\n\n"
      f"Checking if valid Mac or Linux path...\n")

# get all directories in path
# and make sure directories are separated by forward-slash (/)
directories = path.split('/')[1:]

# get file name and extension
if len(directories) > 0:
    file = directories[-1].split(".")
    if file is not None and len(file) > 1:
        file_name = file[0]
        file_ext = file[1]
    else:
        exit(f"No file specified or file has no extension\n"
             f"Exiting...")

    """
    check:
    1+2) first directory is /Users
    3) path has at least another directory (username => home directory) 
    4) file has an extension
    """
    valid_mac_os_linux_path = path[0] == '/' \
        and directories[0] == 'Users' \
        and len(directories) > 2 \
        and '\\' not in path \
        and file_ext is not None

    if valid_mac_os_linux_path:
        print(f"Valid Mac or Linux path\n"
              f"Depth: {len(directories) - 1}\n"
              f"File Name no extension: {file_name}\n"
              f"File extension: {file_ext}")
        exit(0)
    else:
        # all validity checks failed => path is not valid
        print("Invalid mac or linux file path")
