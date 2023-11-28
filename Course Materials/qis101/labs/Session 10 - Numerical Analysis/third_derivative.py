#!/usr/bin/env python3
"""third_derivative.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def f(x: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.array(np.sin(x**2) / (1 + x**3))


def plot(ax: Axes) -> None:
    a: float = 0
    b: float = 5
    n: int = 500

    x = np.linspace(a, b, n, dtype=np.float_)
    h: float = 2 * (b - a) / n

    y = f(x)

    y_prime = np.zeros_like(y)
    for i in range(1, len(y) - 1):
        y_prime[i] = (y[i + 1] - y[i - 1]) / h

    y_prime2 = np.zeros_like(y)
    for i in range(2, len(y_prime2) - 2):
        y_prime2[i] = (y_prime[i + 1] - y_prime[i - 1]) / h

    y_prime3 = np.zeros_like(y)
    for i in range(3, len(y_prime3) - 3):
        y_prime3[i] = (y_prime2[i + 1] - y_prime2[i - 1]) / h

    ax.plot(x, 20 * y, label=r"$20\times\frac{\sin{x^2}}{1+x^3}$")
    ax.plot(x[1:-2], 10 * y_prime[1:-2],
        label=r"$10\times\frac{\partial}{\partial x}\frac{\sin{x^2}}{1+x^3}$")
    ax.plot(x[2:-3], y_prime2[2:-3],
        label=r"$\frac{\partial ^2}{\partial x^2}\frac{\sin{x^2}}{1+x^3}$")
    ax.plot(x[3:-4], y_prime3[3:-4],
        label=r"$\frac{\partial ^3}{\partial x^3}\frac{\sin{x^2}}{1+x^3}$")

    ax.set_title(r"Higher Order Numerical Derivatives of $\frac{\sin{x^2}}{1+x^3}$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.set_ylim(-10, 10)
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_major_locator(MultipleLocator(1.0))

    ax.legend(loc="upper right", fontsize="16")

    ax.axhline(0, color="black", linestyle="-")
    ax.axvline(0, color="black", linestyle="-")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
