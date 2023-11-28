#!/usr/bin/env python3
"""euclid_gcd.py"""


def gcd(a: int, b: int) -> int:
    """Returns the greatest common divisor of a & b"""
    if a < b:
        a, b = b, a
    c: int = a - b
    while c > 0:
        if c > b:
            a = c
        else:
            a = b
            b = c
        c = a - b
    return b


def main() -> None:
    a: int = 182
    b: int = 231
    print(f"The GCD of {a} and {b} = {gcd(a,b)}")


if __name__ == "__main__":
    main()
