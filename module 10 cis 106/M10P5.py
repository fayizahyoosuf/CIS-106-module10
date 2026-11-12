# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:35:47 2026

@author: shama
"""

def compute_assessed_value(county, market_value):
    county_clean = county.strip().lower()

    if county_clean == "cook":
        assessed_pct = 0.90
    elif county_clean == "dupage":
        assessed_pct = 0.80
    elif county_clean == "mchenry":
        assessed_pct = 0.75
    elif county_clean == "kane":
        assessed_pct = 0.60
    else:
        assessed_pct = 0.70

    assessed_value = market_value * assessed_pct
    return assessed_value


def main():
    total_market_value = 0.0
    total_assessed_value = 0.0

    response = input("Do you want to run the program? (Yes or No): ").strip().lower()

    while response in ["yes", "y"]:
        county = input("Enter county: ")
        market_value = float(input("Enter market value of the home: "))

        assessed_value = compute_assessed_value(county, market_value)
        total_market_value += market_value
        total_assessed_value += assessed_value

        print(f"Assessed Value: ${assessed_value:,.2f}\n")

        response = input("Do you want to enter another home? (Yes or No): ").strip().lower()

    print(f"Total Market Value of all homes: ${total_market_value:,.2f}")
    print(f"Total Assessed Value of all homes: ${total_assessed_value:,.2f}")


main()