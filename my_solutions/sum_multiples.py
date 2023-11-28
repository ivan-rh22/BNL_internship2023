#!/usr/bin/env python3
"""sum_multiples.py"""

# Program to display sum of all natural numbers < 1900
    # only add if divisible by both 7 and 11


def is_divisible(numIn: int) -> bool:
    """
    Checks if the number provided (numIn) 
    is divisible by both 7 and 11. Returns bool
    """
    return numIn % 7 == 0 and numIn % 11 == 0

def main() -> None:
    # Stores the sum of all natural number less than 1900 if divisible by 7 and 11
    sum_total: int = sum(num for num in range(1, 1900) if is_divisible(num))

    '''
    *** Different way to write/look at the code above ***
    for num in range(1, 1900):
        if is_divisible(num):
            sum_total += num
    '''

    # Show results
    print(f"Total Sum: {sum_total}")


if __name__ == "__main__":
    main()