# calculate the bohr radius of a hydrogen atom and print it to the console

import math

# Constants
AU = 149597870700  # m
AU_TO_KM = 149597870.700  # km
AU_TO_MILES = 92955807.267  # miles
AU_TO_LIGHT_YEARS = 0.000015812507409  # light years
AU_TO_PARSEC = 0.000004848136811  # parsec
ELECTRON_MASS = 9.10938356e-31  # kg
ELECTRON_CHARGE = 1.60217662e-19  # C
ELECTRON_VOLT = 1.60217662e-19  # J
ELECTRON_VOLT_TO_JOULE = 1.60217662e-19  # J
ELECTRON_VOLT_TO_KILOJOULE = 1.60217662e-16  # kJ
ELECTRON_VOLT_TO_GRAM_CALORIE = 3.826733e-20  # cal
ELECTRON_VOLT_TO_KILOCALORIE = 3.826733e-23  # kcal
ELECTRON_VOLT_TO_WATT_HOUR = 4.4505e-23  # Wh
ELECTRON_VOLT_TO_KILOWATT_HOUR = 4.4505e-26  # kWh
ELECTRON_VOLT_TO_BRITISH_THERMAL_UNIT = 1.518570e-22  # BTU
ELECTRON_VOLT_TO_US_THERM = 1.519e-25  # therm
ELECTRON_VOLT_TO_FOOT_POUND = 1.181705e-19  # ft lb

# Variables
radius = 0.0  # m

# Calculate the bohr radius of a hydrogen atom
radius = 4.0 * math.pi * ELECTRON_CHARGE * ELECTRON_CHARGE * ELECTRON_MASS / (
        4.0 * math.pi * ELECTRON_VOLT * ELECTRON_VOLT * 4.0 * math.pi * 8.854187817e-12 * ELECTRON_CHARGE * ELECTRON_CHARGE)


# Print the bohr radius of a hydrogen atom
def print_bohr_radius(radius):
    print("The bohr radius of a hydrogen atom is " + str(radius) + " meters.")
    print("The bohr radius of a hydrogen atom is " + str(radius / 1000.0) + " kilometers.")


print_bohr_radius(radius)
