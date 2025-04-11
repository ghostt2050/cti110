# Oguzie Amarachi
# Date: 04/11/2025
# P4HW1 – Score Analyzer with Grading
# This program allows the user to enter a specified number of test scores.
# It validates input, drops the lowest score, calculates the average of the remaining scores,
# and assigns a letter grade based on the average.

# ---------- Pseudocode ----------
# Ask user for number of scores
# Create an empty list to store valid scores
# Loop until that many valid scores are entered:
#     - Ask for a score
#     - If score is valid (0 <= score <= 100), add it to list
#     - If not, prompt again until valid
# Find the lowest score in the list
# Create a new list without the lowest score
# Calculate the average of the modified list
# Determine grade:
#     A = 90–100
#     B = 80–89
#     C = 70–79
#     D = 60–69
#     F = below 60
# Print lowest score, modified list, average, and grade

# ---------- Program Code ----------

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("\nINVALID Score entered!!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("Please enter a valid number.")

lowest_score = min(scores)
scores.remove(lowest_score)
average = sum(scores) / len(scores)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\n----------Results----------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("---------------------------")

input()
