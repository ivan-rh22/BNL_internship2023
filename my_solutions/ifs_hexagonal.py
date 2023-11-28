#!/usr/bin/env python3
"""ifs_hexagonal.py"""

# Code is based on Dr. Biersach's Solution
from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem
from pygame import Color
import numpy as np

ifs = IteratedFunctionSystem()

def plot_ifs(ss: SimpleScreen) -> None:
    iterations = 200_000
    x: float = 0.0
    y: float = 0.0
    clr: Color

    # iterate (no drawing) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)
    
    # now draw each pixel in the stable orbit
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)

def main() -> None:
    ifs.set_base_frame(0, 0, 30, 30)

    h = 5 * np.sqrt(3)
    p: float = 1 / 5

    # COD
    ifs.add_mapping(25, 15, 15, 15, 20, 15 + h, Color("blue"), p)
    # DOE
    ifs.add_mapping(20, 15 + h, 15, 15, 10, 15 + h, Color("blue"), p)
    # EOF
    ifs.add_mapping(10, 15 + h, 15, 15, 5, 15, Color("blue"), p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0,0), (30,30)), 
        screen_size=(900,900), 
        draw_function=plot_ifs,
        title="IFS Hexagonal",
    )

    ss.show()

    if __name__ == "__main__":
        main()