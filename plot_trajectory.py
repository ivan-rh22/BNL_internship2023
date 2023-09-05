#!/usr/bin/env python3
"""plot_trajectory.py"""

# Code is based on that provided by Dr. Biersach
from __future__ import annotations

import typing

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def fit_linear(x: NDArray[np.float_], y: NDArray[np.float_]) -> tuple[float, float]:
    """
    function calculates the line of best fit
    
    Args:
        x -> array of float values

        y -> array of float values
    Returns:
        tuple [m, b] both m and b are float values
    """
    n: int = len(x)
    m: float = float(n * np.sum(x * y) - np.sum(x) * np.sum(y))
    m /= float(n * np.sum(x**2) - np.sum(x) ** 2)
    b: float = float(np.sum(y) - m * np.sum(x))
    b /= n
    return m, b

def plot(ax: Axes) -> None:
    """
    plots graph demonstrating the line of best fit for secondary particles
    Args: NA
    Return: NA
    """
    data_file: Path = Path(__file__).parent.joinpath("ray.csv")
    data = np.genfromtxt(data_file, delimiter=",")

    x = data[:, 0] # time in nanoseconds
    y = data[:, 1] # height in centimeters

    m: float
    b: float
    m, b = fit_linear(x, y)
    h = (np.abs(m) * 1e9 / 100) * (0.1743 / 1e3) / 1_000
    c = 29.98 # speed of light in cm/ns

    # Printing calculated velocity and height origination
    print(f"Slope = {abs(m):.4f} cm/ns")
    print(f"Velocity = {np.abs(m)/c:,.2f} c")
    print(f"Origination Height = {h:,.2f} km")

    # Creating and Labeling graph
    ax.scatter(x, y)
    ax.plot(x, m * x + b, color="red", linewidth=2)
    ax.set_title("Secondary Cosmic Ray Trajectory")
    ax.set_xlabel("time (ns)")
    ax.set_ylabel("height (cm)")
    ax.grid()

    plt.show()

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()