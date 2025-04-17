# Oguzie Amarachi
# Date: 04/17/2025
# P5LAB: Self-Checkout Change Dispenser
# This program simulates a self-checkout machine that calculates change 
# and breaks it down into dollars and coins.

import random

def disperse_change(change):
    
    remaining_cents = round(change * 100)

    dollars = remaining_cents // 100
    remaining_cents %= 100

    quarters = remaining_cents // 25
    remaining_cents %= 25

    dimes = remaining_cents // 10
    remaining_cents %= 10

    nickels = remaining_cents // 5
    remaining_cents %= 5

    pennies = remaining_cents

    print(f"\n{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    cash_given = float(input("How much cash will you put in the self-checkout? "))

    if cash_given < amount_owed:
        print("Not enough money. Transaction canceled.")
        return

    change = round(cash_given - amount_owed, 2)
    print(f"Change is: ${change:.2f}")

    disperse_change(change)

main()

input()
