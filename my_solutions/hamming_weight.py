#!/usr/bin/env python3
"""hamming_weight.py"""

# The Hamming Weight is the number of 1's in the binary string of a value
def hamming_weight(value: int) -> int:
    """
    returns the count of 1's in the binary string of the value input
    (we use binary shifting)
    """
    count: int = 0 # define and initialize an accumulator 'count'

    # loops through the binary string
    while value:
        # adds 1 to count if lsb is a 1 (& - checks lsb)
        count += value & 1
        # right-shift by 1 bit
        value >>= 1

    return count

def main() -> None:
    testVal: int = 95_601

    # print results to console
    print(f"Our Hamming Weight of {testVal:,} is: {hamming_weight(testVal)}")
    print(f"Python's built in result is: {bin(testVal).count('1')}")

if __name__ == "__main__":
    main()