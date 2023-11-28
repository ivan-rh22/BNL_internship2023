#!/usr/bin/env python3
"""freq_histogram.py"""

from __future__ import annotations

import sys
import typing
from pathlib import Path
from typing import Counter

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes, data_file: Path) -> None:
    # Determine the length of the file
    with open(data_file, "rb") as f_in:
        f_bytes: bytearray = bytearray(f_in.read())
        file_size: int = f_in.tell()
        f_in.close()

    # Create list of ASCII values which recur > 6% within the file
    ticks: list[float] = []
    char_count: NDArray[np.float_] = np.zeros(256, dtype=np.float_)
    for char, count in Counter(f_bytes).items():
        char_count[char] = count
        if count / file_size > 0.06:
            ticks.append(float(char))

    # Display a histogram of ASCII values and their count in the file
    ax.set_title(f"Frequency Analysis ({data_file.name})")
    ax.set_xlabel("ASCII Value")
    ax.set_ylabel("Count")

    ax.bar([*range(256)], char_count)

    # Show tick marks (the ASCII value) only for those
    # ASCII values which recur > 6% within the file
    ax.xaxis.set_ticks(ticks)
    ax.xaxis.set_tick_params(rotation=90)
    ax.yaxis.set_minor_locator(AutoMinorLocator())


def main(data_file: Path) -> None:
    plt.figure(__file__, figsize=(12, 8))
    plot(plt.axes(), data_file)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You must provide a filename")
    else:
        main(Path(sys.argv[1]))
