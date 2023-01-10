import pprint

busses = [
    {
        "delays": ['1h 20m', '25m', '3h', '2h 1m'],
        "status": 'bad',
        "name": "Jacob",
        "route_num": 560
    },
    {
        "delays": ['20m', '5m', '3h'],
        "status": 'great',
        "name": "Moshe",
        "route_num": 769
    },
    {
        "delays": ['2h 3m'],
        "status": 'good',
        "name": "Jack",
        "route_num": 766
    },
    {
        "delays": ['6h'],
        "status": 'great',
        "name": "Mark",
        "route_num": 876
    },
    {
        "delays": ['2h 3m'],
        "status": 'good',
        "name": "Anna",
        "route_num": 456
    },
]


def sort_busses(busses_dict: list[dict[str, list[str] | str | int]]) -> list[dict[str, list[str] | str | int]]:
    def get_total_delay(bus: dict[str, list[str] | str | int]) -> int:
        """

        :param bus:
        :return: total delay in minutes
        """
        total = 0
        for delay in bus["delays"]:
            d = delay.split()
            for t in d:
                if 'h' in t:
                    total += int(t[:t.index("h")]) * 60
                if 'm' in t:
                    total += int(t[:t.index("m")])
                if 's' in t:
                    total += int(t[:t.index("s")]) // 60

        return total

    by_name = sorted(busses_dict, key=lambda bus: bus["name"], reverse=True)
    by_name_status = sorted(by_name, key=lambda bus: get_total_delay(bus))
    by_name_status_delay = sorted(by_name_status, key=lambda bus: bus["status"], reverse=True)

    return by_name_status_delay


def len_s(bus_dict: dict[str, list[str] | str | int]):
    len_delays = 0
    for d in bus_dict["delays"]:
        len_delays += (len(d) + 2)
        len_delays += 1
    len_delays += len(bus_dict["delays"])
    ret_width = len("{'delays': [],") + len_delays
    return ret_width


if __name__ == '__main__':
    s_busses = sort_busses(busses)
    for bus in s_busses:
        width = len_s(bus)
        pprint.pprint(bus, indent=1, width=width)
        print()
