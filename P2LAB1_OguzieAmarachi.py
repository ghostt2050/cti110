# Name: Oguzie Amarachi
# Date: 03/08/2025
# Assignment Name: P2LAB1
# A brief description of the project

import math

# Prompt the user to enter the radius as a float
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter, circumference, and area using the given formulas
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display the results with the specified formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")

input()
