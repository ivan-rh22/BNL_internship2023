#!/usr/bin/env python3
"""plot3d_cylinder.py"""

# Code is based on that provided by Dr. Biersach

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def plot(ax: Axes) -> None:
    """function to plot a wireframe cylinder with a unit radius"""
    u: NDArray[np.float_] = np.linspace(0, np.pi, 30) # poloidal angle
    v: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30) # toroidal angle

    x: NDArray[np.float_] = np.outer(np.ones_like(u), np.sin(v))
    y: NDArray[np.float_] = np.outer(np.ones_like(u), np.cos(v))
    z: NDArray[np.float_] = np.outer(np.cos(u), np.ones_like(v))

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z") # type: ignore

    ax.plot_wireframe(x, y, z) # type: ignore

def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()

if __name__ == "__main__":
    main()