def restoreIpAddresses(s: str):
    all_ips = []
    ip = []
    len_section = 4
    return _restoreIpAddresses(s, all_ips, ip, len_section)


def _restoreIpAddresses(s: str, ip_addresses, ip: list, len_section: int):
    if len(s) == 0:
        ip_addresses.append(".".join(ip))
    if len_section == 0:
        return

    for i in range(1, min(4, len(s) + 1)):
        if is_valid(s[:i]):
            ip.append(s[:i])
            _restoreIpAddresses(s[i:], ip_addresses, ip, len_section - 1)
            ip.remove(s[:i])

    return ip_addresses


def is_valid(ip_sect: str):
    if len(ip_sect) > 3:
        return False
    int_ip_sect = int(ip_sect)
    if not (0 <= int_ip_sect <= 255):
        return False
    return True


if __name__ == "__main__":
    a = restoreIpAddresses("25525511135")
    # a = restoreIpAddresses("0000")
    print(a)
