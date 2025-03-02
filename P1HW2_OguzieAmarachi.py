# Name: Oguzie Amarachi
# Date: 03/02/2025
# Assignment Name: Travel Expenses Calculator
# Description: This program calculates and displays travel expenses.
#              The user enters their budget, travel destination, 
#              and estimated costs for gas, accommodation, and food.
#              The program then calculates the remaining balance 
#              after deducting expenses.

# Pseudocode:
# 1. Ask user to enter their initial budget and store it.
# 2. Ask user to enter their travel destination.
# 3. Ask user for the amount they will spend on gas.
# 4. Ask user for the amount they will spend on accommodation.
# 5. Ask user for the amount they will spend on food.
# 6. Calculate total expenses by summing gas, accommodation, and food.
# 7. Subtract total expenses from the initial budget.
# 8. Display the results, including the travel destination, 
#    budget, expenses, and remaining balance.

# Collecting user input
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")

# Collect expenses
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

# Calculate total expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display the results
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("\nFuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print("\nRemaining Balance:", remaining_balance)
