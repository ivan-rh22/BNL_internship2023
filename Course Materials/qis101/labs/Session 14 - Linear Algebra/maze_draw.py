#!/usr/bin/env python3
"""maze_draw.py"""

from __future__ import annotations

import os
import pickle
import sys
import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection, PatchCollection
from matplotlib.patches import Rectangle

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def load_maze(file_name: str) -> NDArray[np.int_]:
    maze: NDArray[np.int_] = np.genfromtxt(file_name, delimiter=",", dtype=int)
    print(maze)
    return maze


def validate_maze(maze: NDArray[np.int_]) -> bool:
    for y in range(10):
        for x in range(10):
            cell: int = maze[y, x]
            # Check CSV has a value in every cell
            if cell == -1:
                print(f"Cell {y, x} has no value")
                return False
            # Check for any holes in border walls of maze
            if y == 0 and cell & 1 != 1:
                print(f"Cell {y, x} is missing the NORTH wall")
                return False
            if x == 9 and cell & 2 != 2:
                print(f"Cell {y, x} is missing the EAST wall")
                return False
            if y == 9 and cell & 4 != 4:
                print(f"Cell {y, x} is missing the SOUTH wall")
                return False
            if x == 0 and cell & 8 != 8:
                print(f"Cell {y, x} is missing the WEST wall")
                return False
            # Check every cell agrees with its NORTH cell
            if y > 0:
                cell2: int = maze[y - 1, x]
                if (cell & 1 == 1 and cell2 & 4 != 4) or (
                    cell & 1 != 1 and cell2 & 4 == 4
                ):
                    print(
                        (
                            f"Cell {y, x} and cell {y - 1, x}"
                            " do not agree between NORTH/SOUTH"
                        )
                    )
                    return False
            # Check every cell agrees with its SOUTH cell
            if y < 9:
                cell2 = maze[y + 1, x]
                if (cell & 4 == 4 and cell2 & 1 != 1) or (
                    cell & 4 != 4 and cell2 & 1 == 1
                ):
                    print(
                        (
                            f"Cell {y, x} and cell {y + 1, x}"
                            " do not agree between NORTH/SOUTH"
                        )
                    )
                    return False
            # Check every cell agrees with its EAST cell
            if x < 9:
                cell2 = maze[y, x + 1]
                if (cell & 2 == 2 and cell2 & 8 != 8) or (
                    cell & 2 != 2 and cell2 & 8 == 8
                ):
                    print(
                        (
                            f"Cell {y, x} and cell {y, x + 1}"
                            " do not agree between EAST/WEST"
                        )
                    )
                    return False
            # Check every cell agrees with its WEST cell
            if x > 0:
                cell2 = maze[y, x - 1]
                if (cell & 8 == 8 and cell2 & 2 != 2) or (
                    cell & 8 != 8 and cell2 & 2 == 2
                ):
                    print(
                        (
                            f"Cell {y, x} and cell {y, x - 1}"
                            " do not agree between EAST/WEST"
                        )
                    )
                    return False
    return True


def plot_cell_walls(ax: Axes, maze: NDArray[np.int_]) -> None:
    for y in range(10):
        bottom: int = (9 - y) * 10
        top: int = bottom + 10
        for x in range(10):
            left: int = x * 10
            right: int = left + 10
            cell: int = maze[y, x]
            if cell & 1 == 1:
                lc = LineCollection(
                    [[(left, top), (right, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)  # type: ignore
            if cell & 2 == 2:
                lc = LineCollection(
                    [[(right, bottom), (right, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)  # type: ignore
            if cell & 4 == 4:
                lc = LineCollection(
                    [[(left, bottom), (right, bottom)]], color="black", linewidth=3
                )
                ax.add_collection(lc)  # type: ignore
            if cell & 8 == 8:
                lc = LineCollection(
                    [[(left, bottom), (left, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)  # type: ignore


def plot_maze(ax: Axes, maze: NDArray[np.int_]) -> None:
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_xlim(-5, 105)
    ax.set_ylim(-5, 105)

    # Plot enter and exit cells
    entrance = Rectangle((0, 90), 10, 10)
    ax.add_collection(PatchCollection([entrance], facecolor="tan"))  # type: ignore
    exit = Rectangle((90, 0), 10, 10)
    ax.add_collection(PatchCollection([exit], facecolor="orange"))  # type: ignore

    # Plot cell corner circles
    for x in range(0, 110, 10):
        for y in range(0, 110, 10):
            ax.scatter(x, y, color="black")

    plot_cell_walls(ax, maze)


def main(file_name: str) -> None:
    maze: NDArray[np.int_] = load_maze(file_name)

    if not validate_maze(maze):
        return

    with open(file_name + ".pickle", "wb") as file_out:
        pickle.dump(maze, file_out, pickle.HIGHEST_PROTOCOL)

    plt.figure(file_name)
    plot_maze(plt.axes(), maze)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        file_name: str = os.path.dirname(sys.argv[0]) + "/maze.csv"
    else:
        file_name = sys.argv[1]
    main(file_name)
