def pretty_dict(_d: dict, sep: str) -> str:
    __pretty_str = ""
    __len_keys = len(_d.keys())
    i = 0
    for key, value in _d.items():
        __pretty_str += f"{key}{sep} {value}"
        if i < __len_keys - 1:
            __pretty_str += "\n"
        i += 1

    return __pretty_str


def pretty_layout(_t: tuple) -> str:
    __pretty_layout = ""
    __split_at: int = (len(_t) // 2) - 1

    for letter in _t:
        __pretty_layout += letter
        if _t.index(letter) == __split_at:
            __pretty_layout += " " * 5

    return __pretty_layout


def pretty_underscore_string(__string: str) -> str:
    new_str = __string.split('_')
    for i, word in enumerate(new_str):
        new_str[i] = word.capitalize()

    return ' '.join(new_str)
