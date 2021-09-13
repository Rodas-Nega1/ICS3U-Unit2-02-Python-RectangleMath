#!/usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sep 2021
# This program calculates the area and perimeter of a rectangle
#    with length and width inputted from the user

import math


def main():
    # this function calculates the area and perimeter of a rectangle

    # input
    length = int(input("Enter length of rectangle (mm): "))

    # input
    width = int(input("Enter width of a rectangle (mm): "))

    # process
    area_of_rectangle = length * width
    perimeter_of_rectangle = 2 * (length + width)

    # output
    print("")
    print("Area is {0} mm².".format(area_of_rectangle))
    print("Perimeter is {0} mm.".format(perimeter_of_rectangle))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
