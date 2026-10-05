import numpy as np

# Marks of students
marks = np.array([
    [78, 85, 90],
    [65, 70, 75],
    [90, 88, 95],
    [45, 55, 60]
])

students = ["Aman", "Raj", "Simran", "Karan"]

# Calculate total marks
total = np.sum(marks, axis=1)

# Calculate average marks
average = np.mean(marks, axis=1)

print("STUDENT PERFORMANCE ANALYZER")
print("--------------------------------")

for i in range(len(students)):
    print("\nStudent:", students[i])
    print("Marks:", marks[i])
    print("Total:", total[i])
    print("Average:", average[i])

    if average[i] >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

# Highest average
highest = np.max(average)

index = np.argmax(average)

print("\nBest Performing Student:")
print(students[index])
print("Average:", highest)

# Overall highest and lowest marks
print("\nHighest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))
