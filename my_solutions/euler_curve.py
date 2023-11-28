#!/usr/bin/env python3
"""euler_curve.py"""

# Code is based on Dr. Biersach's Solution
from __future__ import annotations

import typing

# math tools
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def x(t: float) -> float:
    """returns integral of cos(u^2)"""
    return quad(lambda u: np.cos(u**2), 0, t)[0] # type: ignore

def y(t: float) -> float:
    """returns integral of sin(u^2)"""
    return quad(lambda u: np.sin(u**2), 0, t)[0] # type: ignore

def ds(t: float) -> float:
    return float(np.sqrt(np.cos(t**2) ** 2 + np.sin(t**2) ** 2))

def plot(ax: Axes) -> None:
    tf: float = 12.34
    t: NDArray[np.float_] = np.linspace(0, tf, 1_000)

    # vectorize creates a vector from an array so they have the same dimension
    vx = np.vectorize(x)
    vy = np.vectorize(y)
    ax.plot(vx(t), vy(t))

    arc_length: float = quad(ds, 0, tf)[0] # type: ignore

    # labeling graph
    ax.set_title(rf"Euler's Curve $(0\leq t<{tf:.2f})$ arc length = {arc_length:.2f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")

    # circle center is at the limit of integral of cos(x**2) as x goes to infinity
    c: float = np.sqrt(np.pi / 2) / 2
    ax. scatter(c, c, color = "red")

def main() -> None:
    plt.figure()
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()