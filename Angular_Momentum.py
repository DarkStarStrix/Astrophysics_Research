# Calculate the angular momentum of the black hole GRS 1915+105 and print it to the console

import math

# Constants
AU = 149597870700 # m
AU_TO_KM = 149597870.700 # km
AU_TO_MILES = 92955807.267 # miles
AU_TO_LIGHT_YEARS = 0.000015812507409 # light years
AU_TO_PARSEC = 0.000004848136811 # parsec
G = 6.67408e-11 # m^3 kg^-1 s^-2
M_SUN = 1.989e30 # kg
M_BLACK_HOLE = 14.8 * M_SUN # kg
M_TON_618 = 66.0 * M_SUN # kg
M_GRS_1915 = 14.0 * M_SUN # kg
M_SAGITTARIUS_A_STAR = 4.31e6 * M_SUN # kg
M_CYGNUS_X_1 = 14.8 * M_SUN # kg
M_V404_CYGNI = 9.0 * M_SUN # kg
M_4U_1543_47 = 9.0 * M_SUN # kg

# Variables
distance = 0.0 # m
radius = 0.0 # m
mass = 0.0 # kg
velocity = 0.0 # m/s
angular_momentum = 0.0 # kg m^2 s^-1

# Calculate the angular momentum of the black hole GRS 1915+105
distance = 1.33e10 * AU
mass = M_GRS_1915
velocity = 0.92 * 3e8
angular_momentum = mass * distance * velocity

# Print the angular momentum of the black hole GRS 1915+105
print("The angular momentum of the black hole GRS 1915+105 is " + str(angular_momentum) + " kg m^2 s^-1.")
