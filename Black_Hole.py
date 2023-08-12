# Calculate the radius of the supermassive black hole ton 618 and print it to the console

import math

# Constants
AU = 149597870700 # m
AU_TO_KM = 149597870.700 # km
AU_TO_MILES = 92955807.267 # miles
AU_TO_LIGHT_YEARS = 0.000015812507409 # light years
AU_TO_PARSEC = 0.000004848136811 # parsec

# Variables
distance = 0.0 # m
radius = 0.0 # m

# Calculate the radius of the supermassive black hole ton 618
distance = 2.8 * AU
radius = math.sqrt(distance * distance * distance / 332946.0487)

# Print the radius of the supermassive black hole ton 618
print("The radius of the supermassive black hole ton 618 is " + str(radius) + " meters.")
print("The radius of the supermassive black hole ton 618 is " + str(radius / 1000.0) + " kilometers.")