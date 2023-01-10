storage_amount = int(input("Enter a storage amount in bytes, kb, mb, gb, tb: "))
storage_unit = input("What storage unit did you input in? ")
convert_to = input("What unit do you want to convert to? ")

converted_unit = None

if storage_unit == "bytes":
    if convert_to == "kb":
        converted_unit = storage_amount / 1024
    elif convert_to == "mb":
        converted_unit = storage_amount / 1024 ** 2
    elif convert_to == "gb":
        converted_unit = storage_amount / 1024 ** 3
    elif convert_to == "tb":
        converted_unit = storage_amount / 1024 ** 4
elif storage_unit == "kb":
    if convert_to == "bytes":
        converted_unit = storage_amount * 1024
    elif convert_to == "mb":
        converted_unit = storage_amount / 1024
    elif convert_to == "gb":
        converted_unit = storage_amount / (1024 ** 2)
    elif convert_to == "tb":
        converted_unit = storage_amount / (1024 ** 3)
elif storage_unit == "mb":
    if convert_to == "bytes":
        converted_unit = storage_amount * 1024 ** 2
    elif convert_to == "kb":
        converted_unit = storage_amount * 1024
    elif convert_to == "gb":
        converted_unit = storage_amount / 1024
    elif convert_to == "tb":
        converted_unit = storage_amount / 1024 ** 2
elif storage_unit == "gb":
    if convert_to == "bytes":
        converted_unit = storage_amount * 1024 ** 3
    elif convert_to == "kb":
        converted_unit = storage_amount * 1024 ** 2
    elif convert_to == "mb":
        converted_unit = storage_amount * 1024
    elif convert_to == "tb":
        converted_unit = storage_amount / 1024
elif storage_unit == "tb":
    if convert_to == "bytes":
        converted_unit = storage_amount * 1024 ** 4
    elif convert_to == "kb":
        converted_unit = storage_amount * 1024 ** 3
    elif convert_to == "mb":
        converted_unit = storage_amount * 1024 ** 2
    elif convert_to == "gb":
        converted_unit = storage_amount * 1024

print(converted_unit)
