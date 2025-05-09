#!/usr/bin/env python3

# Created By: Micthelle Michael
# Date: may 09, 2025
# This program calculates the area and perimeter of a rectangle.


def main():
    # this line of code prints out the welcome message
    print("This program calculates the area and perimeter of a rectangle.")
    # this line of code gets the input for length
    length = int(input("Enter the length of the rectangle in cm: "))
    # this line of code gets the input for width
    width = int(input("Enter the width of the rectangle in cm: "))
    # this line of code calculates the area
    area = length * width
    # this line of code calculates the perimeter
    perimeter = 2 * (length + width)
    # this line of code prints out the area and perimeter
    print("Area = {}cm^2".format(area))
    # this line of code prints out the perimeter
    print("Perimeter = {}cm".format(perimeter))


if __name__ == "__main__":
    main()
