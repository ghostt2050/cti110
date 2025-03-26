# Oguzie Amarachi
# March 26, 2025
# P3HW2 – Salary Calculation
# This program prompts the user to enter an employee's name, number of hours worked, and pay rate.
# It then calculates regular and overtime pay, and displays a summary of the employee's payment information.

emp_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

gross_pay = regular_pay + overtime_pay

print("--------------------------------------------------------------------------")
print(f"Employee name:\t{emp_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print("-" * 70)
print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}")

input()
