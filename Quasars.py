# Calculate the energy of a quasar ULAS J1342+0928 and print it to the console

import math

# Constants
AU = 149597870700  # m
AU_TO_KM = 149597870.700  # km
AU_TO_MILES = 92955807.267  # miles
AU_TO_LIGHT_YEARS = 0.000015812507409  # light years
AU_TO_PARSEC = 0.000004848136811  # parsec
SPEED_OF_LIGHT = 299792458  # m/s
SPEED_OF_LIGHT_TO_KM_PER_S = 299792.458  # km/s
SPEED_OF_LIGHT_TO_MILES_PER_S = 186282.397  # miles/s
SPEED_OF_LIGHT_TO_AU_PER_DAY = 173.144632674  # AU/day
SPEED_OF_LIGHT_TO_AU_PER_YEAR = 63239.7263  # AU/year
SPEED_OF_LIGHT_TO_LIGHT_YEARS_PER_YEAR = 0.306601393  # light years/year
SPEED_OF_LIGHT_TO_PARSEC_PER_YEAR = 0.000095945454  # parsec/year
SPEED_OF_LIGHT_TO_KM_PER_YEAR = 9460730472580.8  # km/year
SPEED_OF_LIGHT_TO_MILES_PER_YEAR = 5878625373183.67  # miles/year
SPEED_OF_LIGHT_TO_KM_PER_HOUR = 1079252848.8  # km/hour
SPEED_OF_LIGHT_TO_MILES_PER_HOUR = 670616629.384  # miles/hour
SPEED_OF_LIGHT_TO_KM_PER_DAY = 25902068371.2  # km/day
SPEED_OF_LIGHT_TO_MILES_PER_DAY = 16098759144.4  # miles/day
SPEED_OF_LIGHT_TO_KM_PER_MONTH = 777600000000.0  # km/month
SPEED_OF_LIGHT_TO_MILES_PER_MONTH = 482803200000.0  # miles/month

# Variables
distance = 0.0  # m
radius = 0.0  # m
energy = 0.0  # J
energy_in_kilotons_of_tnt = 0.0  # kilotons of TNT
energy_in_megatons_of_tnt = 0.0  # megatons of TNT
energy_in_gigatons_of_tnt = 0.0  # gigatons of TNT
energy_in_teratons_of_tnt = 0.0  # tera-tons of TNT
energy_in_petatons_of_tnt = 0.0  # peta tons of TNT
energy_in_exatons_of_tnt = 0.0  # exa tons of TNT
energy_in_zettatons_of_tnt = 0.0  # zetta tons of TNT
energy_in_yottatons_of_tnt = 0.0  # yotta-tons of TNT
energy_in_ergs = 0.0  # ergs
energy_in_kilowatt_hours = 0.0  # kilowatt hours
energy_in_watt_hours = 0.0  # watt hours
energy_in_calories = 0.0  # calories
energy_in_kilocalories = 0.0  # kilocalories
energy_in_btu = 0.0  # BTU
energy_in_foot_pounds = 0.0  # foot pounds
energy_in_electron_volts = 0.0  # electron volts
energy_in_joules = 0.0  # joules
energy_in_kilojoules = 0.0  # kilojoules
energy_in_megajoules = 0.0  # megajoules
energy_in_gigajoules = 0.0  # gigajoules
energy_in_terajoules = 0.0  # terajoules
energy_in_petajoules = 0.0  # petajoules
energy_in_exajoules = 0.0  # exajoules
energy_in_zettajoules = 0.0  # zettajoules

# Calculate the energy of a quasar ULAS J1342+0928
distance = 13.1 * AU
radius = math.sqrt(distance * distance * distance / 332946.0487)
energy = 4.0 * math.pi * radius * radius * radius * 5.0 * 10.0 ** 26.0
energy_in_kilotons_of_tnt = energy / 4.184 * 10.0 ** -12.0
energy_in_megatons_of_tnt = energy_in_kilotons_of_tnt * 10.0 ** -3.0
energy_in_gigatons_of_tnt = energy_in_megatons_of_tnt * 10.0 ** -3.0
energy_in_teratons_of_tnt = energy_in_gigatons_of_tnt * 10.0 ** -3.0
energy_in_petatons_of_tnt = energy_in_teratons_of_tnt * 10.0 ** -3.0
energy_in_exatons_of_tnt = energy_in_petatons_of_tnt * 10.0 ** -3.0
energy_in_zettatons_of_tnt = energy_in_exatons_of_tnt * 10.0 ** -3.0
energy_in_yottatons_of_tnt = energy_in_zettatons_of_tnt * 10.0 ** -3.0
energy_in_ergs = energy * 10.0 ** 7.0
energy_in_kilowatt_hours = energy / 3600000.0
energy_in_watt_hours = energy_in_kilowatt_hours * 1000.0
energy_in_calories = energy_in_watt_hours * 859.84522785899
energy_in_kilocalories = energy_in_calories / 1000.0
energy_in_btu = energy_in_calories * 3.965666386
energy_in_foot_pounds = energy_in_btu * 778.16926226596
energy_in_electron_volts = energy * 6241509744500000000.0
energy_in_joules = energy
energy_in_kilojoules = energy_in_joules / 1000.0

# Display the results
print("ULAS J1342+0928 Quasar Energy Output")
print("")
print("Distance From Earth: " + str(distance) + " m")
print("Radius: " + str(radius) + " m")
print("Energy: " + str(energy) + " J")
print("Energy: " + str(energy_in_kilotons_of_tnt) + " kilotons of TNT")
print("Energy: " + str(energy_in_megatons_of_tnt) + " megatons of TNT")
print("Energy: " + str(energy_in_gigatons_of_tnt) + " gigatons of TNT")
print("Energy: " + str(energy_in_teratons_of_tnt) + " teratons of TNT")
print("Energy: " + str(energy_in_petatons_of_tnt) + " petatons of TNT")
print("Energy: " + str(energy_in_exatons_of_tnt) + " exatons of TNT")
print("Energy: " + str(energy_in_zettatons_of_tnt) + " zettatons of TNT")
print("Energy: " + str(energy_in_yottatons_of_tnt) + " yottatons of TNT")
print("Energy: " + str(energy_in_ergs) + " ergs")
print("Energy: " + str(energy_in_kilowatt_hours) + " kilowatt hours")
print("Energy: " + str(energy_in_watt_hours) + " watt hours")
print("Energy: " + str(energy_in_calories) + " calories")
print("Energy: " + str(energy_in_kilocalories) + " kilocalories")
print("Energy: " + str(energy_in_btu) + " BTU")
print("Energy: " + str(energy_in_foot_pounds) + " foot pounds")
print("Energy: " + str(energy_in_electron_volts) + " electron volts")
print("Energy: " + str(energy_in_joules) + " joules")
