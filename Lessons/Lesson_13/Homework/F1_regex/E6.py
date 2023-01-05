import re


# Maximum 2 TATA-like patterns

def two_tataa(dna: str):
    return 1 <= len(re.findall("(TATA{2}[ACTG]{3}T{2})", dna)) <= 2


def two_tataa2(dna: str):
    return 1 <= len([*re.finditer("(TATA{2}[ACTG]{3}T{2})", dna)]) <= 2


if __name__ == '__main__':
    # TRUE
    print(two_tataa("ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
    # FALSE
    print(two_tataa("ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
    # TRUE
    print(two_tataa("ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAACGATTTCAGCTGATTCGAA"))
    # TRUE
    print(two_tataa2("ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAACGATTTCAGCTGATTCGAA"))
    # FALSE
    print(two_tataa2("TATAAGGGTTACACGGATATAAGGGTTACGCGCTGTATAACGATTTCAGCTGATTCGAA"))
