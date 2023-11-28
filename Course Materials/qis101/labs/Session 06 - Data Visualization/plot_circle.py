#!/usr/bin/env python3
"""plot_circle.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plot a circle of radius 250"""
    radius: float = 250.0
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000)

    # Polar to Cartesian coordinate conversion using vectorized operations
    x: NDArray[np.float_] = radius * np.cos(theta)
    y: NDArray[np.float_] = radius * np.sin(theta)

    ax.plot(x, y)

    ax.set_title(f"$x^2 + y^2 = {radius}$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid()
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    ax.set_aspect("equal")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
