#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

# code uses built in method from scipy
    # https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide
# used ChatGPT to help format the code

# IMPORTS
import numpy as np
from scipy.stats import maxwell
import matplotlib.pyplot as plt

import typing
from numpy.typing import NDArray

def calculate_pdf(a: int, x: NDArray[np.float_]) -> NDArray[np.float_]:
    """
    Calculates the probability density function (PDF) of the Maxwell-Boltzmann distribution.
    Args:
        a: Scale parameter of the distribution.
        x: Array of values to evaluate the PDF at.
    Returns:
        Array of PDF values corresponding to the given x values.
    """
    return maxwell.pdf(x, scale=a)

def plot_pdf(x: NDArray[np.float_], pdf_values: typing.List[NDArray[np.float_]], labels: typing.List[str]) -> None:
    """
    Plots the probability density function (PDF) values.
    Args:
        x: Array of x values.
        pdf_values: List of PDF values corresponding to different parameters.
        labels: List of labels for the plot.
    """
    fig, ax = plt.subplots(1, 1)
    
    for pdf, label in zip(pdf_values, labels):
        ax.plot(x, pdf, label=label)

    ax.set_xlim(0, 20)
    ax.legend(loc="best", frameon=False)
    plt.show()

def main() -> None:
    """
    Calculates and plots the probability density function (PDF)
    of the Maxwell-Boltzmann distribution using different parameters.
    """
    a1: int = 1
    a2: int = 2
    a3: int = 5

    x: NDArray[np.float_] = np.linspace(0, 20, 1_000)
    pdf_values = [
        calculate_pdf(a1, x),
        calculate_pdf(a2, x),
        calculate_pdf(a3, x)
    ]
    labels = ["a1", "a2", "a3"]
    plot_pdf(x, pdf_values, labels)


if __name__ == "__main__":
    main()
