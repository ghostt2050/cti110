# Oguzie Amarachi
# Date: 04/11/2025
# P4HW2 – Employee Pay Calculator
# This program calculates regular pay, overtime pay, and gross pay for multiple employees.
# It uses a sentinel-controlled loop to keep collecting employee data until the user types "Done".
# At the end, it summarizes total regular, overtime, and gross payments for all employees.

# ---------- Pseudocode ----------
# Initialize counters:
#   - total_employees = 0
#   - total_overtime_pay = 0.0
#   - total_regular_pay = 0.0
#   - total_gross_pay = 0.0
# While True:
#     Ask for employee name (if "Done", break)
#     Ask for hours worked
#     Ask for pay rate
#     If hours > 40:
#         - Calculate overtime hours = hours - 40
#         - Regular hours = 40
#     Else:
#         - Overtime = 0
#         - Regular hours = hours
#     Calculate:
#         - overtime_pay = overtime hours * pay rate * 1.5
#         - regular_pay = regular hours * pay rate
#         - gross_pay = overtime_pay + regular_pay
#     Display formatted results for the employee
#     Add to totals
# After loop ends:
#     Display total employees and total pays (overtime, regular, gross)



total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

while True:
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")
    if employee_name.lower() == "done":
        break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    print(f"\nEmployee name: {employee_name}")
    print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
    print("-" * 70)
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<10.2f}\n")

    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime   : ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular pay: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross       : ${total_gross_pay:.2f}")

input()
