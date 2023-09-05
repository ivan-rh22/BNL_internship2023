#!/usr/bin/env python3
"""archimedes_spiral.py"""

# code is annotated version of what was provided by Dr. David Biersach

# IMPORTS
from __future__  import annotations

import typing

# plotting and other math tools
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def f(theta: NDArray(np.float_)) -> NDArray[np.float_]:
    """
    This function calculates the square root of (theta squared + 1)
    
    Args:
        theta: array of float values
    Returns:
        sqrt(theta^2 + 1) as an array of float values
    """
    return np.sqrt(theta**2 + 1)

def plot(ax: Axes) -> None:
    """
    Uses pyplot to graph the calculated arc length of an Archimedes Spiral
    with r = theta that rotates from 0 <= theta and < 8pi
    
    Args:
        ax: Axes
    Returns:
        None
    """
    # setting up function values
    theta: NDArray[np.float_] = np.linspace(0, 8 * np.pi, 1_000)
    x = theta * np.cos(theta)
    y = theta * np.sin(theta)

    # calculating arc length using SciPy
    arc_length = integrate.quad(f, 0, 8 * np.pi)[0]

    # Plotting data
    ax.plot(x,y)

    # labeling graph
    ax.set_title(
        (
            r"Archimedes Spiral $(r = \theta, \;0\leq\theta\leq 8\pi)$"
            f"\nArc Length = {arc_length:.4f}"
        )
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")
    ax.set_aspect("equal")

def main() -> None:
    #plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()