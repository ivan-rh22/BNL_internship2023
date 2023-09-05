#!/usr/bin/env python3
"""eulers_constant.py"""

# Code is annotated from what Dr. David Biersach provided

# IMPORTS
from __future__ import annotations

import typing
# plotting and other math tools
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate # type: ignore
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def f(x: float) -> float:
    """
    Calculate the log used to superimpose a line graph for the first 50 Harmonic Numbers
    
    Args:
        x: float value
    Returns:
        float(np.log(np.log(1/x))) as a float value
    """
    return float(np.log(np.log(1/x))) # type: ignore

def plot(ax: Axes) -> None:
    """
    plots a line graph of gamma + ln(x) on top of a step plot of the first 50 Harmonic Numbers

    Args:
        ax: Axes
    Return:
        None
    """ 
    euler_constant: float = integrate.quad(f, 0, 1)[0] # type: ignore
    
    # Array to generate the first 50 Harmonic Numbers
    h: NDArray[np.float_] = np.zeros(50)
    h[2] = 1
    for i in range(3, 50):
        h[i] = h[i - 1] + 1 / (i - 1)

    # step plot of first 50 Harmonic Numbers
    ax.step(np.arange(50), h, label=r"$\sum_{k=1}^2{\lfloor x\rfloor}\frac{1}{k}$")

    # x is an array excluding the first element (log(0)) of 500 equally spaced points [0, 50]
    x: NDArray[np.float_] = np.linspace(0, 50, 500)[1:]
    logf: NDArray[np.float_] = euler_constant + np.log(x)

    # plotting the gamma function + ln(x)
    ax.plot(x, logf, label=r"$\gamma+\ln x$")

    # Formatting and Labeling graph
    ax.set_title("Asymptotic Limit of the Harmonic Numbers")
    ax.set_xlabel("x")
    ax.set_ylabel("Harmonic Number")
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    ax.legend(loc="center right")
    ax.set_xlim(0)
    ax.set_ylim(0, 5)

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()
