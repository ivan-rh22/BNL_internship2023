#!/usr/bin/env python3
"""factor_quadratic.py"""

from math import gcd


def factor_quadratic(h: int, i: int, j: int) -> None:
    """Displays factors of the quadratic polynomial Jx^2 + Kx + L"""

    print(f"Given the quadratic:{h}x^2 + {i}x + {j}")

    factored: bool  = False

    for a in range(1, h + 1):
        if h % a == 0:
            c: int = h // a
            for b in range(1, j + 1):
                if j % b == 0:
                    d: int = j // b
                    if a * d + b * c == i:
                        factored = True
                        print(f"The factors are: ({a}x + {b})({c}x + {d})")

    if not factored:
        print(f"The expression {h}x^2 + {i}x + {j} cannot be factored")


def main() -> None:
    # variables
    x: int = 115425
    y: int = 32514121
    z: int = 379020
    
    # we will use the GCD to determine if the quadratic is prime (has no factors but 1)
    if gcd(x, y, z) == 1: # if prime print message below don't factor
        print("Based on the GCD the polynomial is prime, unable to factor")
    else:  # if not prime try to factor 
        factor_quadratic(x, y, z)


if __name__ == "__main__":
    main()
