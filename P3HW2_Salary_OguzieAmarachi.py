# Oguzie Amarachi
# Date: 03/30/2025
# Assignment: P3HW2 – Gross Pay with Overtime
# This program calculates and displays an employee's gross pay including regular
# and overtime pay based on hours worked and hourly rate.

# ----------- Pseudocode -----------
# 1. Get employee's name
# 2. Get hours worked
# 3. Get pay rate
# 4. If hours worked > 40:
#       - Calculate overtime hours = hours worked - 40
#       - Overtime pay = overtime hours * pay rate * 1.5
#       - Regular pay = 40 * pay rate
#    Else:
#       - Overtime hours = 0
#       - Overtime pay = 0
#       - Regular pay = hours worked * pay rate
# 5. Gross pay = regular pay + overtime pay
# 6. Display results in formatted output


employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

gross_pay = regular_pay + overtime_pay

print("\n---------------------------------")
print(f"Employee name:  {employee_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print("----------------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}")

input()
