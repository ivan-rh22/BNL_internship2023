#!/usr/bin/env python3
"""spectrum_bohr.py"""


def main() -> None:
    e_charge: float = 1.602e-19
    e_mass: float = 9.109e-31
    permittivity: float = 8.854e-12
    h_plank: float = 6.626e-34
    speed_light: float = 2.998e8

    # Bohr's formula for ground state energy
    e_0: float = (pow(e_charge, 4) * e_mass) / (
        8 * pow(permittivity, 2) * pow(h_plank, 2)
    )

    print("Bohr Model for Hydrogen Spectral Lines")

    for final_orbit in range(1, 5):
        for init_orbit in range(final_orbit + 1, final_orbit + 6):
            # Initial energy level
            e_i: float = -e_0 / pow(init_orbit, 2)
            # Final energy level
            e_f: float = -e_0 / pow(final_orbit, 2)
            # Formula for waveLength in nanometers
            wave_length: float = h_plank * speed_light / (e_i - e_f) * 1e9
            print(f"\t{init_orbit:>2} -> {final_orbit:>2}{wave_length:8.0f} nm")
        print()


if __name__ == "__main__":
    main()
