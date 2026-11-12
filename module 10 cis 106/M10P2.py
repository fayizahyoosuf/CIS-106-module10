# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:16:07 2026

@author: shama
"""

def compute_wall_sqft(length, width, height):
    wall_area = (2 * length * height) + (2 * width * height)
    return wall_area


def compute_ceiling_floor_area(length, width):
    area = length * width
    return area


def main():
    response = input("Do you want to run the program? (Yes or No): ").strip().lower()

    while response in ["yes", "y"]:
        length = float(input("Enter room length: "))
        width = float(input("Enter room width: "))
        height = float(input("Enter room height: "))

        wall_sqft = compute_wall_sqft(length, width, height)
        wall_gallons = wall_sqft / 50.0

        ceiling_floor_sqft = compute_ceiling_floor_area(length, width)
        ceiling_floor_gallons = ceiling_floor_sqft / 50.0

        print(f"Wall Square Footage: {wall_sqft:.2f} sq ft")
        print(f"Gallons needed for walls: {wall_gallons:.2f}")
        print(f"Ceiling/Floor Square Footage: {ceiling_floor_sqft:.2f} sq ft")
        print(f"Gallons needed for ceiling or floor: {ceiling_floor_gallons:.2f}\n")

        response = input("Do you want to run the program again? (Yes or No): ").strip().lower()


main()