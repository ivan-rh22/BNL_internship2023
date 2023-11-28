#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

# Code is based on that provided by Dr. Biersach
from __future__ import annotations

import typing

# Math tools
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator

if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def f(x: NDArray[np.float_], y: NDArray[np.float_]) -> NDArray[np.complex_]:
    """
    returns array of the given arguments such as the regions 
    the surfaces passes through
    
    Return:
        np.array(abs(np.sin(x+ 1j * y)))
    """
    return np.array(np.abs(np.sin(x + 1j * y)))

def plot(ax: Axes) -> None:
    """plots the image of a complex sin function in 3d"""
    x: NDArray[np.float_] = np.linspace(-2.5, 2.5, 100)
    y: NDArray[np.float_] = np.linspace(-1, 1, 100)

    x, y = np.meshgrid(x, y)

    z: NDArray[np.complex_] = f(x, y)

    surf: Any = ax.plot_surface(x, y, z, cmap =cm.coolwarm, linewidth=0, antialiased=False)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")

    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5) # type: ignore

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z") # type: ignore

def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()

if __name__ == "__main__":
    main()