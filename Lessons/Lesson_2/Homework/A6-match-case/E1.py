"""
Match case statements
"""

country = input("Enter a country name: ").lower().strip()

match country:
    case "usa":
        print("US Dollar")
    case "israel":
        print("New Israeli Shekel (NIS)")
    case "uk":
        print("Pound")
    case "germany" | "austria" | "czech" | "france" | "italy" | "spain":
        print("Euro")
    case _:
        print("I don't know...")