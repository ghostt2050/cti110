# Name: Amarachi Oguzie
# Date: 03/15/2025
# Assignment: P2HW1
# Description: This program calculates and displays travel expenses with well-formatted output.

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
fuel = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

remaining_balance = budget - (fuel + accommodation + food)

print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:>8.2f}")
print(f"{'Fuel:':<20}${fuel:>8.2f}")
print(f"{'Accommodation:':<20}${accommodation:>8.2f}")
print(f"{'Food:':<20}${food:>8.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining_balance:>8.2f}")


input()
