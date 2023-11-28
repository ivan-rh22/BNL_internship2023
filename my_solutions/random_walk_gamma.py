#!/usr/bin/env python3
"""random_walk_gamma.py"""

# Code is based on that provided by Dr. Biersach

from __future__ import annotations
import typing

# math imports
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def plot(ax: Axes) -> None:
    """
    plots the expected final distance of a uniform random walk of N steps
    on a unit lattice having dimension d
    """
    nSteps: int = 20_000
    x: NDArray[np.float_] = np.linspace(1,25, 100, dtype=np.float_)

    # Euler's Gamma Function using the number of steps and the origin of dimension
    y: NDArray[np.float_] = np.sqrt(2 * nSteps / x) * np.power(gamma((x + 1.0) / 2) / gamma(x / 2), 2) # type: ignore

    # plotting results
    ax.plot(x, y, linewidth=2)

    # Setting label names
    ax.set_title("Mean Final Distance of a\n Uniform Random Walk on a Unit Lattice")
    ax.set_xlabel("Dimensions")
    ax.set_ylabel("Mean Final Distance")

def main()->None:
    plt.figure(__file__)
    plot((plt.axes()))
    plt.show()

if __name__ == "__main__":
    main()