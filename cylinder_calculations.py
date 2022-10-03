#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds the cost of a pizza, using user inputted diameter

import math


def main():
    # Finds the cost of a pizza using diameter sent by the user

    radius_of_cylinder = int(input("Enter the radius of a cylinder (cm): "))
    height_of_cylinder = int(input("Enter the height of a cylinder (cm): "))
    volume = math.pi * radius_of_cylinder**2 * height_of_cylinder
    surface_area = (
        2 * math.pi * radius_of_cylinder * height_of_cylinder
        + 2 * math.pi * radius_of_cylinder**2
    )
    print("\nThe volume of this cylinder is {}cm³".format(volume))
    print("The surface area of this cylinder is {}cm²".format(surface_area))

    print("\nDone.")


if __name__ == "__main__":
    main()
