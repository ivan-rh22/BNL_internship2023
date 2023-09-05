#!/usr/bin/env python3
"""sum_squares.py"""

def main() -> None:
    series_sum: int = 0 # stores the sum of the natural numbers squared
    num_terms: int = 1_000 # number of terms

    # loops through all natural numbers up to 1000 (inclusive)
    for num in range(1, num_terms+1):
        series_sum += num**2 # adds the sum to the accumulator

    # Calculate sum using Gaussian Summation: (2n^3 + 3n^2 +n)/6 where n is # of terms
    gauss_sum: int = int((2 * pow(num_terms,3) + 3 * pow(num_terms, 2) + num_terms) / 6)
    
    # Print results
    print(f"Loop Sum Solution:\n{series_sum:,}")
    print(f"Functional Equation Solution:\n{gauss_sum:,}")

    # Bool check to see if sums match
    if series_sum == gauss_sum:
        print("\nSum is accurate")
    else:
        print("\nERROR: Sums don't match")


if __name__ == "__main__":
    main()