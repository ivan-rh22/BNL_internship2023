#!/usr/bin/env python3
"""ladder_problem.py"""

# this is an annotated solution from code provided by Dr. David Biersach's
# program displays the maximum ladder length possible that will fit around the corner depicted in the slides

# IMPORTS
from __future__ import annotations
import typing

# graphing and other math tools
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np
import scipy.optimize # type: ignore

# Optimization
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray
    from scipy.optimize import OptimizeResult # type: ignore

def length(theta: NDArray[np.float_]) -> NDArray[np.float_]:
    """
    This function calculates the length of the ladder
    Args:
        theta: array of float values
    Returns:
        2 / np.sin(theta) +1 / np.cos(theta)
    """
    return 2 / np.sin(theta) + 1 / np.cos(theta)

def plot(ax: Axes) -> None:
    """
    Plot the maximum length of the ladder
    Args:
        ax: Axes
    Returns:
        None
    """
    # defining theta excluding the values '0' and '2pi'
    theta: NDArray[np.float_] = np.linspace(0, np.pi/2, 1_000, dtype=np.float_)[1:-2]
    # inputting theta domain into the function
    ladder: NDArray[np.float_] = length(theta)

    # Plotting
    ax.plot(theta, ladder)

    # using Scipy to find the minimum value of the length function
    res: OptimizeResult = scipy.optimize.minimize(length, np.pi / 4) # type: ignore

    # optimized goes into the x array
    c_theta: float = res.x[0] # type: ignore
    # optimized theta goes into the length function for optimized length
    c_length: float = float(length(np.array(c_theta))) # type: ignore

    # labeling plot
    ax.set_title(f"Max Length = {c_length:4f} m")
    ax.plot(c_theta, c_length, color="green", marker="o")
    ax.set_xlabel(r"$\theta$ (radians)")
    ax.set_ylabel("length (m)")

    # adds a horizontal line with the height above the x-axis of c_length
    ax.axhline(c_length, color="gray", linestyle="--")
    # adds a vertical line from x-axis to c_theta
    ax.vlines(x=c_theta, ymin=0, ymax=c_length, color="red")

    # adding minor tick to x and y-axis
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    # limiting the y-axis to only display from 0 to 25
    ax.set_ylim(0, 25)


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
