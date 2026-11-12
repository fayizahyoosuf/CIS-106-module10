# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:28:25 2026

@author: shama
"""

def compute_ticket_price(miles):
    if miles >= 30:
        price = 12.0
    elif miles >= 20:
        price = 10.0
    elif miles >= 10:
        price = 8.0
    else:
        price = 5.0

    return price


def main():
    total_tickets = 0.0

    response = input("Do you want to run the program? (Yes or No): ").strip().lower()

    while response in ["yes", "y"]:
        last_name = input("Enter last name: ").strip()
        miles = float(input("Enter miles from downtown Chicago: "))

        ticket_price = compute_ticket_price(miles)
        total_tickets += ticket_price

        print(f"Last Name: {last_name}")
        print(f"Ticket Price: ${ticket_price:,.2f}\n")

        response = input("Do you want to enter another passenger? (Yes or No): ").strip().lower()

    print(f"Total price of all tickets: ${total_tickets:,.2f}")


main()