# Write a program that has 2 modes: insert mode and lookup mode.
# The program asks the user whether he wants to insert a birthday date or to look up a birthday.

# If the user chooses to insert a new date,
# ask for the person's name and then ask for the person's birthday, and store them.

# If the user chooses lookup mode, ask for a name and return the birthday of the person.


def insert(_birthday_dict: dict[str | str]) -> None:
    f"""
        Accepts a dictionary of birthdays (str)\n
        Reads from input a Name
        and birthdate to add to the dictionary.
        
    :param _birthday_dict: dict[str | str]
    :return: None
    """
    _name = input("\n>>> Please enter a name\n\n")
    if _name in _birthday_dict:
        _choice = input(f">>> Name: {_name} exists. Overwrite it? (Y/N)\n\n").lower().strip()
        while _choice != 'y' and _choice != 'n':
            print(f"\n>>> \"{_choice}\" Invalid option. Enter Only Y or N")
            _choice = input(f"\n>>> Name: {_name} exists. Overwrite it? (Y/N)\n\n").lower().strip()

        if _choice == 'n':
            print(f"\n>>> No selected... "
                  f"Going back to main menu...\n\n")

            return

    birthday = input("\n>>> Please enter a birthday date\n\n")
    _birthday_dict[_name] = birthday
    print(f"\n>>> Done!\n"
          f">>> {_name}'s birthday is now set to: {birthday}\n\n")

    return


def has_similar_matches(_birthday_dict: dict[str | str], _name: str) -> bool:
    """
        Returns True if _name partially exists in _birthday_dict

    :param _birthday_dict: dict[str | str]
    :param _name: str
    :return: bool
    """
    _similar_matches = []

    for key in _birthday_dict.keys():
        if _name in key:
            _similar_matches.append(key)

    return len(_similar_matches) > 0


def get_matches(_birthday_dict: dict[str | str], _name: str) -> list[str]:
    """
        Returns a list of _birthday_dict keys which are include _name string in them

    :param _birthday_dict: dict[str | str]
    :param _name: str
    :return: list[str]
    """
    _similar_matches = []

    for key in _birthday_dict.keys():
        if _name in key:
            _similar_matches.append(key)

    return _similar_matches


def get_similar_suggestion(_similar_matches: list[str], _name: str) -> str | None:
    f"""
        Prompts user to see similar names.\n
        If yes show all similar names
        Prompt to insert name from similar list or return to main menu.
    
    :param _similar_matches: 
    :param _name: 
    :return: str | None
    """
    _choice = input(f"\n>>> We couldn't find any exact matches for \"{_name}\". "
                    f"Do you want to see suggestions?\n\n").lower().strip()
    while _choice != 'y' and _choice != 'n':
        print(f"\n>>> \"{_choice}\" Invalid option. Enter Only Y or N")

        _choice = input(f"\n>>> We couldn't find any exact matches for \"{_name}\". "
                        f"Do you want to see suggestions?\n\n").lower().strip()
    if _choice == 'y':
        names = ""
        for _match in _similar_matches:
            names += _match
            if _similar_matches.index(_match) < len(_similar_matches) - 1:
                names += ', '
        print("\n>>> We have:", names)

        _name = input("\n>>> Insert a name from the list above or $$$ to return to the main menu.\n\n")

        if _name == "$$$":
            _name = None
            print("\n>>> Returning to main menu...\n\n")

    return _name


def lookup(_birthday_dict: dict[str | str], _name: str) -> str | None:
    f"""
        Looks for _name in _birthday_dict\n
        If _name exists: return _birthday_dict[_name]\n
        else: return None
        
    :param _birthday_dict: 
    :param _name: 
    :return: str | None
    """
    while _name not in _birthday_dict.keys():
        has_matches = has_similar_matches(_birthday_dict, _name)
        if not has_matches:
            return f"\n>>> We don't have a record for {_name}\n\n" \
                   f">>> Returning to main menu"

        _similar_matches = get_matches(_birthday_dict, _name)
        _name = get_similar_suggestion(_similar_matches, _name)
        if _name is None:
            return None

    birthday = _birthday_dict.get(_name)

    return f"\n>>> {_name}'s birthday is {birthday}\n"


def main() -> None:
    """
        main driver function
    :return: None
    """
    birthday_dict = dict()

    while True:
        choice = input(">>> Welcome to the birthday dictionary."
                       " Do you want to insert a new birthday"
                       " or to lookup one?\n\n").lower().strip()

        match choice:
            case "insert":
                insert(birthday_dict)
            case "lookup":
                name = input("\n>>> Who's birthday do you want to look up?\n\n")
                birthday = lookup(birthday_dict, name)
                if birthday is not None:
                    print(birthday)
            case "quit":
                print("\n>>> Bye-bye\n\n")
                break
            case _:
                print(f"\n{choice} is an invalid choice!\n"
                      f"The options are:\n"
                      f"1. insert\n"
                      f"2. lookup\n"
                      f"3. quit\n")
                continue


if __name__ == "__main__":
    main()
