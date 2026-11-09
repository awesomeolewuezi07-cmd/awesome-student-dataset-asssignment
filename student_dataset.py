import csv

# Fictional Student Dataset

students = [
    {
        "Student ID": "CAL001",
        "Department": "Computer Science",
        "Level": 300,
        "Attendance Percentage": 85,
        "Average Examination Score": 78
    },
    {
        "Student ID": "CAL002",
        "Department": "Cyber Security",
        "Level": 300,
        "Attendance Percentage": 90,
        "Average Examination Score": 82
    },
    {
        "Student ID": "CAL003",
        "Department": "Software Engineering",
        "Level": 200,
        "Attendance Percentage": 75,
        "Average Examination Score": 69
    },
    {
        "Student ID": "CAL004",
        "Department": "Computer Science",
        "Level": 400,
        "Attendance Percentage": 95,
        "Average Examination Score": 88
    },
    {
        "Student ID": "CAL005",
        "Department": "Information Technology",
        "Level": 300,
        "Attendance Percentage": 80,
        "Average Examination Score": 74
    },
    {
        "Student ID": "CAL006",
        "Department": "Cyber Security",
        "Level": 200,
        "Attendance Percentage": 70,
        "Average Examination Score": 65
    },
    {
        "Student ID": "CAL007",
        "Department": "Computer Science",
        "Level": 100,
        "Attendance Percentage": 92,
        "Average Examination Score": 90
    },
    {
        "Student ID": "CAL008",
        "Department": "Software Engineering",
        "Level": 400,
        "Attendance Percentage": 88,
        "Average Examination Score": 84
    },
    {
        "Student ID": "CAL009",
        "Department": "Information Technology",
        "Level": 200,
        "Attendance Percentage": 78,
        "Average Examination Score": 72
    },
    {
        "Student ID": "CAL010",
        "Department": "Computer Science",
        "Level": 300,
        "Attendance Percentage": 96,
        "Average Examination Score": 93
    }
]

# Create a CSV file
with open("student_dataset.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)

print("Student dataset created successfully!")
