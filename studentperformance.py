
# Simple Machine Learning Project
# Student Performance Prediction

students = [65, 75, 85, 90, 55]

average = sum(students) / len(students)

print("Student Performance Analysis")
print("-----------------------------")
print("Student Marks:", students)
print("Average Marks:", average)

if average >= 75:
    print("Performance: Good")
else:
    print("Performance: Needs Improvement")
