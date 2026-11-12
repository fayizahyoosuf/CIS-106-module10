# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:23:42 2026

@author: shama
"""

def compute_out_the_door(msrp, make, model, ev_code):
    make_clean = make.strip().lower()
    model_clean = model.strip().lower()
    ev_clean = ev_code.strip().upper()

    if ev_clean == "Y":
        discount_pct = 0.30
    elif make_clean == "honda" and model_clean == "accord":
        discount_pct = 0.10
    elif make_clean == "toyota" and model_clean == "rav4":
        discount_pct = 0.15
    else:
        discount_pct = 0.05

    new_msrp = msrp * (1 - discount_pct)
    total_price = new_msrp * 1.07
    return total_price


def main():
    total_msrp = 0.0
    total_sales_price = 0.0

    response = input("Do you want to run the program? (Yes or No): ").strip().lower()

    while response in ["yes", "y"]:
        make = input("Enter vehicle make: ")
        model = input("Enter vehicle model: ")
        ev_code = input("Is this an electric vehicle? (Y or N): ")
        msrp = float(input("Enter MSRP (sticker price): "))

        out_the_door = compute_out_the_door(msrp, make, model, ev_code)
        total_msrp += msrp
        total_sales_price += out_the_door

        print(f"Out the door price: ${out_the_door:,.2f}\n")

        response = input("Do you want to enter another vehicle? (Yes or No): ").strip().lower()

    print(f"Total of all MSRPs: ${total_msrp:,.2f}")
    print(f"Total of all Sales Prices: ${total_sales_price:,.2f}")


main()