# read from file
relative_path = "files/data/alice_in_wonderland.txt"
absolute_path = "/src/Lesson_Code/files/data/alice_in_wonderland.txt"

# don't do this
file = open(relative_path, "r")
print(file)
# do stuff
file.close()

# both are the same

# with automatically closes the file resources opened => (this is the preferred way)
with open(relative_path, "r") as file:
    print(file)
    # do more stuff

    # read file
    # leave param empty for entire file (preferred only for small files)
    # returns a string
    content = file.read()
    # print according to the spliced string
print(content[content.index("CHAPTER I"): content.index("CHAPTER II")])
