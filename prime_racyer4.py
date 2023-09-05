#!/usr/bin/env python3
"""prime_racer3.py"""

from random import randint, seed
from time import process_time

# this program reduced run time but it also consume much more memory

def is_prime(n: int) -> bool:
    """
    Returns True/False if the given number is prime
    using a list of precomputed primes < 1,000 or sqrt(1,000,000)
    """
    # precomputed list of primes (https://www.factors-of.com/prime-numbers-before/Prime-numbers-from-1-to_1000_)
    primes: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
                         59, 61, 67,71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
                         127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 
                         191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
                         257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
                         331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 
                         401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 
                         467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 
                         563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 
                         631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
                         709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
                         797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 
                         877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 
                         967, 971, 977, 983, 991, 997]
    return all(n % factor != 0 for factor in primes)


def main() -> None:
    seed(2016)

    num_samples: int = 10_000
    min_val: int = 100_000
    max_val: int = 1_000_000

    print(
        (
            f"Counting the number of primes in {num_samples:,} random samples\n"
            f"with each sample having a value between {min_val:,} "
            f"and {max_val:,} inclusive . . ."
        )
    )

    samples: list[int] = [randint(min_val, max_val) for _ in range(num_samples)]

    start_time: float = process_time()
    num_primes: int = [is_prime(n) for n in samples].count(True)
    elapsed_time: float = process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
