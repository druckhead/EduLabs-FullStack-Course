amount = input("Enter a storage amount including unit: ")
ls = amount.split(" ")

storage_size = float(ls[0])
storage_unit = ls[1]

storage_multiplier = 1024
if storage_size > 1:
    if storage_unit == "bytes":
        if storage_size / storage_multiplier >= 1:
            storage_size /= storage_multiplier
            storage_unit = "kb"
    if storage_unit == "kb":
        if storage_size / storage_multiplier >= 1:
            storage_size /= storage_multiplier
            storage_unit = "mb"
    if storage_unit == "mb":
        if storage_size / storage_multiplier >= 1:
            storage_size /= storage_multiplier
            storage_unit = "gb"
    if storage_unit == "gb":
        if storage_size / storage_multiplier >= 1:
            storage_size /= storage_multiplier
            storage_unit = "tb"

    print("{0:.1f} {1}".format(storage_size, storage_unit))
else:
    print("Incompatible value given")