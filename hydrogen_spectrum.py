#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

# Some of the code is based on what was provided by Dr. Biersach

def main() -> None:
    """ calculating wavelengths using both the bohr and rydberg's formulas"""

    # Important constant variables
    rydberg_constant: float = 1.0967757e7
    e_charge: float = 1.602e-19
    e_mass: float = 9.109e-31
    permittivity: float = 8.854e-12
    h_plank: float = 6.626e-34
    speed_light: float = 2.998e8

    # Bohr's formula for ground state energy
    e_0: float = (pow(e_charge, 4) * e_mass) / (8 * pow(permittivity, 2) * pow(h_plank, 2))

    # High energy series (Pfund and Humphreys)
    for final__orbit in range(5, 7):
        print(f"{'Transition':>16}{'Rydberg':>11}{'Bohr':>11}")
        for init_orbit in range(final__orbit + 1, final__orbit + 6):
            # initial energy level
            e_i: float = -e_0 / pow(init_orbit, 2)
            # final energy level
            e_f: float = -e_0 / pow(final__orbit, 2)

            # using rydberg's formula to calculate wavelengths (nm)
            wave_length_rydberg: float = (1 / (rydberg_constant * (1 / pow(final__orbit, 2) - 1 / pow(init_orbit, 2))) * 1e9)

            # using bohr's formula to calculate wavelengths (nm)
            wave_length_bohr: float = h_plank * speed_light / (e_i - e_f) * 1e9
            # printing the results
            print(
                (
                    f"\t{init_orbit:>2} -> {final__orbit:>2}"
                    f"{wave_length_rydberg:8.0f} nm"
                    f"{wave_length_bohr:8.0f} nm"
                )
            )
        print()



if __name__ == "__main__":
    main()