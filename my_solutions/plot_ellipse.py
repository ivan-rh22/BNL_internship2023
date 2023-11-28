#!/usr/bin/env python3
"""plot_ellipse.py"""

# Code is based on that provided by Dr. Biersach

from __future__ import annotations
import typing

# math tools
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def plot_ellipse(ax: Axes) -> None:
    """
    Plots an ellipse by converting polar to cartesian coordinates
    major axis: 100 (runs along the x-axis)
    minor axis: 50 (runs along the y-axis)
    """
    # initializing variables
    major_axis: float = 100.0
    minor_axis: float = 50.0
    # theta is an array of floating points between 0 and 2pi evenly distributed
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1_000)

    # finding the radius at each theta by converting cartesian into polar coordinates
    radius: NDArray[np.float_] = (major_axis * minor_axis) / np.sqrt((minor_axis * np.cos(theta))**2 + (major_axis * np.sin(theta))**2)

    # convert plart coordinates to cartesian coordinates
    x: NDArray[np.float_] = radius * np.cos(theta)
    y: NDArray[np.float_] = radius * np.sin(theta)

    # Plot the ellipse
    ax.plot(x, y)
    ax.set_title(rf"$ \frac{{x^2}}{{{int(major_axis)}^2}} + \frac{{y^2}}{{{int(minor_axis)}^2}} = 1$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid()
    ax.axhline(0, color="black") # draws line for x-axis
    ax.axvline(0, color="black") # draws line for y-axis

    # Setting locators
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_major_locator(MultipleLocator(10))
    
    ax.set_aspect("equal")




def main() -> None:
    plt.figure(__file__)
    plot_ellipse(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()