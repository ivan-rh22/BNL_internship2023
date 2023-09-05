#!/usr/bin/env python3
"""herons_method.py"""

# important imports
from random import randint
from math import sqrt 
from numpy import mean

def herons_method(value: int) -> float:
    """
    Implements Heron's method to find the square root of a number.
    Iterates over a guess until error is less than 1e-8
    This returns a float value
    """
    # initial values
    x: float = value / 2
    error: float = float('inf')

    while error > pow(10, -8):
        x_revised = float(mean([value / x, x]))
        error = abs(value - x_revised**2)
        x = x_revised
    
    return x_revised

def main() -> None:
    # generates a random number to find the square root of
    num: int = randint(10**6, 2 * 10**6)
    herons_result: float = herons_method(num)

    # Print results from both built in and Heron's method
    print(f"Heron's square roof of {num} is: {round(herons_result,8)}")
    print(f"Built in square roof of {num} is: {round(sqrt(num),8)}")

if __name__ == "__main__":
    main()