#!/usr/bin/env python3
"""lcm_gcd.py"""

from math import gcd

def lcm(val1: int, val2: int) -> int:
    """
    This function takes in two numbers and 
    calculates its least common multiple (LCM). returns int
    """
    # using method explained by Dr. Biersach using GCD
        # LCM = product of two values divided by their (GCD)
    return int((val1 * val2) / gcd(val1, val2))

def main() -> None:
    # Test values
    test_val1: int = 447618
    test_val2: int = 2011835
    # Store our result
    least_comm_mul: int = lcm(test_val1, test_val2)
    # Show our results
    print(f"The LCM for {test_val1} and {test_val2} is:\n{least_comm_mul}")

if __name__ == "__main__":
    main()