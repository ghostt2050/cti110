# Name: Oguzie Amarachi
# Date 4/22/2025
# Vehicle Fuel Calculator
# This program calculates how many gallons of gas are needed to drive a selected vehicle for a user-defined number of miles.

# Create dictionary of vehicles and their MPG
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()
print(keys)

vehicle = input("Enter a vehicle to see it's mpg: ")

mpg = vehicles[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.\n")

miles = float(input(f"How many miles will you drive the {vehicle}? "))

gallons = round(miles / mpg, 2)
print(f"\n{gallons} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")

