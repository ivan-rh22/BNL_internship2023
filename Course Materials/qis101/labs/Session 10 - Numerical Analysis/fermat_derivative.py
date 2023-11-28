#!/usr/bin/env python3
"""fermat_derivative.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def f(x: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.cos(x)


def f_prime_actual(x: NDArray[np.float_]) -> NDArray[np.float_]:
    return -np.sin(x)


def f_prime_fermat(x: NDArray[np.float_], h: float) -> NDArray[np.float_]:
    return (f(x + h) - f(x)) / h


def f_prime_centered(x: NDArray[np.float_], h: float) -> NDArray[np.float_]:
    return (f(x + h) - f(x - h)) / (2 * h)


def plot(ax: Axes) -> None:
    a: float = -4 * np.pi
    b: float = 4 * np.pi
    n: int = 500

    x: NDArray[np.float_] = np.linspace(a, b, n, dtype=float)
    y: NDArray[np.float_] = f(x)

    y_prime_actual: NDArray[np.float_] = f_prime_actual(x)
    y_prime_fermat: NDArray[np.float_] = f_prime_fermat(x, (b - a) / n)
    y_prime_centered: NDArray[np.float_] = f_prime_centered(x, (b - a) / n)

    print(f"Fermat Error   : {sum((y_prime_actual-y_prime_fermat)**2):.14%}")
    print(f"Centered Error : {sum((y_prime_actual-y_prime_centered)**2):.14%}")    

    ax.plot(x, y, label=r"$y=\cos{x}$")
    ax.plot(x, y_prime_centered, label=r"$\frac{dy}{dx}=-\sin{x}$")

    ax.set_title("Fermat's Difference Quotient")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    ax.legend(loc="upper right")

    ax.axhline(0, color="black", linestyle="-")
    ax.axvline(0, color="black", linestyle="-")




def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
