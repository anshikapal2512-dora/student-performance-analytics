import os
import pandas as pd
import numpy as np

# Load dataset using a portable relative path
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "students1.csv")

student_df = pd.read_csv(csv_path, index_col="Student_ID")

print("_____Student Performance Analytics System_____")
print(student_df)
print("\nTotal number of students in the dataset:", len(student_df))

# --- Student Report ---
name_query = input("\nEnter the name of the student to get the report: ").strip()
print("\n_____Student_Report_____")

# Case-insensitive lookup using Pandas
matching_students = student_df[student_df["Name"].str.strip().str.lower() == name_query.lower()]

if not matching_students.empty:
    for student_id, student in matching_students.iterrows():
        eng, hindi, maths = student["English"], student["Hindi"], student["Maths"]
        total = eng + hindi + maths
        avg = round(total / 3, 2)
        
        # Grading logic
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 35:
            grade = "D"
        else:
            grade = "F"
            
        status = "Pass" if avg >= 35 else "Fail"

        print(f"Student_ID: {student_id}")
        print(f"Name: {student['Name']}")
        print(f"Department: {student['Department']}")
        print(f"English marks: {eng}")
        print(f"Hindi marks: {hindi}")
        print(f"Maths marks: {maths}")
        print(f"Total marks: {total}")
        print(f"Average marks: {avg}")
        print(f"Pass/Fail Status: {status}")
        print(f"Grade: {grade}")
        print(f"Percentage: {avg}%")
        print(f"Attendance: {student['Attendance']}%")
else:
    print(f"Student '{name_query}' not found in the dataset.")

# Precompute subject list
subjects = ["English", "Hindi", "Maths"]

# --- Performance Analysis Menu Loop ---
while True:
    print("\n_____Questions/Answers_____")
    print("1. Which student has the highest average marks?")
    print("2. Which subject has the best average marks?")
    print("3. How many students passed?")
    print("4. What is the overall class average?")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        student_df["Average"] = student_df[subjects].mean(axis=1)
        top_student = student_df.sort_values(by="Average", ascending=False).iloc[0]
        print(f"\nTop student: {top_student['Name']} with an average of {top_student['Average']:.2f}")

    elif choice == "2":
        subject_avg = student_df[subjects].mean()
        best_subject = subject_avg.idxmax()
        print(f"\nSubject with best average: {best_subject} ({subject_avg[best_subject]:.2f})")

    elif choice == "3":
        passed_count = (student_df[subjects].mean(axis=1) >= 35).sum()
        print(f"\nNumber of students who passed: {passed_count} out of {len(student_df)}")

    elif choice == "4":
        class_avg = student_df[subjects].values.mean()
        print(f"\nOverall class average: {class_avg:.2f}")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")