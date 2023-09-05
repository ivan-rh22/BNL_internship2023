#!/usr/bin/env python3
"""benfords_law.py"""

# This code demonstrates the Law of Anomalous Numbers by calculating
#  the probability of each digit (1 to 9) appearing as the most significant
#  digit in 100,000 very large random numbers

# Code is aided and annotated from that given by Dr. David Biersach

# IMPORT
    # aids for return types and type hints
from __future__ import annotations
import typing
    # plotting tools and other math tools
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import random

# using the typing library to allow
    # use Axes as a variable
    # use NDArrays
if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def p_MSD() -> NDArray[np.float_]:
    """
    calculates the most significant digit in accordance with Benford's Law
    for 100,000 numbers ranging from (1, 1,000,000) inclusive
    """
    # array of probabilities initialized with all 0's (zeros)
    p: NDArray[np.float_] = np.zeros (10, dtype=np.float_)

    # Repeat the process 100,000
    for _ in range (100_000):
        # produce random int from range of (1, 1,000,000) and raising it to power of 100
        n: int = random.randint(1, 1_000_000)**100
        # convert to string and get the element at the first index
        p[int(str(n)[0])] += 1

    # remove first element of p because Benford's Law does not include 0
    p = p[1:]
    # Calculate probability by dividing by total num of nums
    p = p/100_000
    # MSD returns p array
    return p

def plot(ax:Axes) -> None:
    """create and plot a histogram"""
    # creates bar plot with range of 1-9 with higher bars on top of lower value bars
    plt.bar(range(1,10), p_MSD(), zorder=2.5)
    # show grid lines
    plt.grid()

    # title and labels for histogram
    ax.set_title("Benford's Law")
    ax.set_xlabel("Most Significant Digit (MSD)")
    ax.set_ylabel("Probability of MSD")
    ax.xaxis.set_major_locator(MultipleLocator(1))

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()