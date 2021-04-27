#Author: Mothapo Rampedi Lesley
#27 April 2021
"""Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference
and area. Use the constant value 3.14159 for π.
"""
PIE = 3.14159
radius = int(input("Enter the circle radius:  ")) #read the radius
print("Diameter is: ", radius * 2) #radius times two
print("Circumference is: ", 2 * PIE * radius) # 2 times PIE times radius
print("Area is: ", PIE * radius**2) # PIE times raduis squared