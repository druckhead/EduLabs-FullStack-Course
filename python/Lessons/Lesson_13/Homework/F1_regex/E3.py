import re

# Use repeats syntax and rewrite previous TATAA - pattern exercise

def contains_tata_pattern(dna_sequence: str):
    return re.search("TATA{2}[ACTG]{3}T{2}", dna_sequence) is not None


if __name__ == '__main__':
    # TRUE
    print(contains_tata_pattern("ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
    # FALSE
    print(contains_tata_pattern("ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))