# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:01:37 2026

@author: shama
"""

def compute_forecast(month, sales):
    month = month.strip().capitalize()
    forecast_pct = 0.0

    if month in ["Jan", "Feb", "Mar"]:
        forecast_pct = 0.10
    elif month in ["Apr", "May", "Jun"]:
        forecast_pct = 0.15
    elif month in ["Jul", "Aug", "Sep"]:
        forecast_pct = 0.20
    elif month in ["Oct", "Nov", "Dec"]:
        forecast_pct = 0.25

    next_sales = sales * (1 + forecast_pct)
    return next_sales


def main():
    response = input("Do you want to run the program? (Yes or No): ").strip().lower()

    while response in ["yes", "y"]:
        last_name = input("Enter last name: ").strip()
        month = input("Enter month (e.g., Jan, Feb, Mar): ")
        sales = float(input("Enter sales: "))

        forecast_sales = compute_forecast(month, sales)

        print(f"Last Name: {last_name}")
        print(f"Next Month's Forecast: ${forecast_sales:,.2f}\n")

        response = input("Do you want to run the program again? (Yes or No): ").strip().lower()


main()