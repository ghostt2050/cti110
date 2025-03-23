# ---------------------------------------------
# Money Change Calculator
# Author: Oguzie Amarachi
# Date: [Current Date]
# 
# Description:
# This program takes a float input representing a dollar amount,
# and calculates the most efficient number of dollars, quarters, dimes, nickels,
# and pennies needed to make that amount. If the amount is 0, it outputs "No change".
# ---------------------------------------------

def main():
    amount = float(input("Enter the amount of money as a float: $"))
    cents = round(amount * 100)  # convert dollars to cents to avoid float precision issues

    if cents == 0:
        print("No change")
        return

    denominations = [
        ("Dollars", 100),
        ("Quarters", 25),
        ("Dimes", 10),
        ("Nickels", 5),
        ("Pennies", 1)
    ]

    for name, value in denominations:
        count = cents // value
        cents %= value
        if count:
            print(f"{int(count)} {name}")

if __name__ == "__main__":
    main()

    
input()
