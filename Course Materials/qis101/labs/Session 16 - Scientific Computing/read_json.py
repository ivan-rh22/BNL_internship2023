#!/usr/bin/env python3
"""read_json.py"""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    # Create a Python dictionary from the JSON file
    with open(
        Path(__file__).parent.joinpath("uranium_isotopes.json"), "r", encoding="ascii"
    ) as infile:
        uranium_isotopes: dict[str, dict[str, str | float]] = json.load(infile)

    # Find the two isotopes with the maximum difference in half-life
    iso_pair: tuple[str, str] = ("", "")
    max_diff: float = 0.0
    for k1, v1 in uranium_isotopes.items():
        for k2, v2 in uranium_isotopes.items():
            h1 = float(v1["half-life"])
            h2 = float(v2["half-life"])
            diff: float = abs(h1 - h2)
            if diff > max_diff:
                iso_pair = (k1, k2)
                max_diff = diff

    # Convert maximum half-life difference from seconds to years
    max_diff /= 60 * 60 * 24 * 365.25

    # Determine difference in neutrons between the two isotopes
    iso1: str
    iso2: str
    iso1, iso2 = iso_pair
    neutrons1: int = int(uranium_isotopes[iso1]["neutrons"])
    neutrons2: int = int(uranium_isotopes[iso2]["neutrons"])
    neutron_delta: int = abs(neutrons1 - neutrons2)

    print(
        (
            f"{iso1} and {iso2}:\n"
            f"Half-life difference: {max_diff:,.0f} years\n"
            f"Neutron difference:   {neutron_delta}"
        )
    )


if __name__ == "__main__":
    main()
