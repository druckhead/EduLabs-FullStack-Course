import re


# Given a string that represents DNA, check whether a given DNA string contain a TATA-box-like pattern

def contains_tata_pattern(dna_sequence: str):
    return re.search("TATAA[ACTG][ACTG][ACTG]TT", dna_sequence) is not None


if __name__ == '__main__':
    # TRUE
    print(contains_tata_pattern("ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
    # FALSE
    print(contains_tata_pattern("ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
