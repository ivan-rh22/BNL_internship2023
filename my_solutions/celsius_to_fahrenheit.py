#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""

# convert celsius to fahrenheit
    # range: -44 C to 106 C in steps of 4
        # we were asked to include 106 
        # since it does not follow the steps of 4 we will show it separately

def main() -> None:
    # loop to go through each of the values from -44 to 104 in steps of 4
    for celsius in range(-44, 105, 4):
        # formula to calculate is "F = C * (9/5) + 32"
        fahrenheit: float = celsius * 9/5 + 32
        print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")
    # after loop we will show 106 to make it inclusive
    celsius: float = 106.00
    fahrenheit: float = celsius * 9/5 + 32
    print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")

if __name__ == "__main__":
    main()