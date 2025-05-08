# Name: Oguzie Amarachi
# Date: 03/15/2025
# Assignment: P2HW2
# Description: This program collects grades for six modules, stores them in a list, and 
# displays the lowest, highest, sum, and average of the grades.

grades = []  # List to store grades

grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / len(grades)

print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<20}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<20}{sum_of_grades:.1f}")
print(f"{'Average:':<20}{average:.2f}")
print("--------------------------------")


input()
