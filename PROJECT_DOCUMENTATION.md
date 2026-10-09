# Project Documentation – Assessment Activity

---

## 1. Project Title
- **Project Name:** Student Performance Analytics System
- **Student Name:** Anshika Pal
- **Email:** anshikapal2512@gmail.com
- **GitHub Username:** [anshikapal2512-dora](https://github.com/anshikapal2512-dora)
- **Course / Organization:** Python Internship – EWB Courses

---

## 2. Objective
The primary objective of the **Student Performance Analytics System** is to automate the tracking, evaluation, and reporting of student academic performance. 

### Problems It Solves:
- **Eliminates Manual Errors:** Replaces manual calculation of totals, averages, grades, and pass/fail statuses with fast, automated data operations.
- **Instant Report Card Generation:** Enables faculty and administrators to quickly search and retrieve complete individual student report cards including attendance records.
- **Institutional Performance Insights:** Provides batch-level analytical metrics (such as highest scoring student, best performing subject, overall pass rate, and class average) to help educators identify areas where students excel or need additional academic support.

---

## 3. Technologies Used
- **Python 3:** Core programming language used for script execution, conditional logic, and CLI interactions.
- **Pandas:** Used for tabular data management (DataFrames), CSV ingestion, row filtering, string manipulation, and vectorized statistical operations.
- **NumPy:** Used for numerical processing and array-level computations.
- **OS Module:** Used for dynamic, platform-independent relative path resolution.
- **Git & GitHub:** Used for version control, repository management, and project submission.

---

## 4. Dataset Description
- **Dataset File:** `students1.csv`
- **Total Records:** 20 student entries
- **Index Column:** `Student_ID` (Unique integer from 1 to 20)

### Dataset Schema:
| Column Name | Description | Data Type | Example Value |
|---|---|---|---|
| `Student_ID` | Unique identifier for each student | Integer | `1` |
| `Name` | Full name of the student | String | `Aman` |
| `Department` | Academic department / branch | String | `Computer Engineering` |
| `English` | Marks scored in English (out of 100) | Integer | `78` |
| `Hindi` | Marks scored in Hindi (out of 100) | Integer | `67` |
| `Maths` | Marks scored in Mathematics (out of 100) | Integer | `56` |
| `Attendance` | Overall attendance percentage | Float | `75.0` |

---

## 5. Implementation
The project was implemented in Python using the following step-by-step pipeline:

1. **Portable Path Resolution:**
   Using `os.path.dirname(os.path.abspath(__file__))`, the script dynamically determines the directory of `students1.csv`, ensuring it runs seamlessly across any operating system or execution directory without path errors.

2. **Data Loading:**
   The CSV dataset is read into a Pandas DataFrame using:
   ```python
   student_df = pd.read_csv(csv_path, index_col="Student_ID")
   ```

3. **Overview & Enrollment Summary:**
   The entire dataset is displayed to the console, and the total student enrollment count is computed using `len(student_df)`.

4. **Individual Student Search & Evaluation:**
   - Prompts the user for a student name.
   - Performs a robust case-insensitive and whitespace-stripped lookup:
     ```python
     matching_students = student_df[student_df["Name"].str.strip().str.lower() == name_query.lower()]
     ```
   - For matched records, computes:
     - **Total Marks:** Sum of English, Hindi, and Maths.
     - **Average & Percentage:** `Total / 3` (rounded to 2 decimal places).
     - **Grade Assignment:** Categorized as **A** ($\ge$ 90), **B** ($\ge$ 75), **C** ($\ge$ 60), **D** ($\ge$ 35), or **F** (< 35).
     - **Pass/Fail Standing:** Evaluated with a threshold of 35%.

5. **Interactive Analytical Menu:**
   A continuous `while True` loop provides 5 choices:
   - **Option 1 (Top Student):** Computes row-wise averages across subject columns and uses `.sort_values(by="Average", ascending=False).iloc[0]` to identify the top student.
   - **Option 2 (Best Subject):** Computes column-wise subject averages and determines the highest using `.idxmax()`.
   - **Option 3 (Pass Count):** Uses boolean filtering `(student_df[subjects].mean(axis=1) >= 35).sum()` to count passing students.
   - **Option 4 (Class Average):** Computes the grand mean of all student subject marks using `.values.mean()`.
   - **Option 5 (Exit):** Safely terminates the menu loop.

---

## 6. Key Features
- **Dynamic & Case-Insensitive Search:** Accepts names in any casing (`aman`, `Aman`, `AMAN `) without failing.
- **Automated Grading & Pass/Fail Evaluation:** Instant computation of academic status based on standard academic thresholds.
- **Batch Analytics:** Instant identification of top students, best subjects, and overall class performance.
- **Continuous CLI Menu:** Allows users to query multiple analytical questions in a single session without having to restart the script.
- **Clean, Modular & Portable Code:** Eliminates hardcoded absolute paths and fragile numeric row indexing.

---

## 7. Output / Execution Results

### Sample 1: Dataset Summary & Individual Student Report
```text
_____Student Performance Analytics System_____
              Name            Department  English  Hindi  Maths  Attendance
Student_ID                                                                 
1             Aman  Computer Engineering       78     67     56        75.0
2             Rita  Computer Engineering       65     87     58        73.2
...
20           Jyoti  Computer Engineering       44     90     77        76.4

Total number of students in the dataset: 20

Enter the name of the student to get the report: Aman

_____Student_Report_____
Student_ID: 1
Name: Aman
Department: Computer Engineering
English marks: 78
Hindi marks: 67
Maths marks: 56
Total marks: 201
Average marks: 67.0
Pass/Fail Status: Pass
Grade: C
Percentage: 67.0%
Attendance: 75.0%
```

### Sample 2: Analytical Questions & Answers Output
```text
_____Questions/Answers_____
1. Which student has the highest average marks?
2. Which subject has the best average marks?
3. How many students passed?
4. What is the overall class average?
5. Exit
Enter your choice (1-5): 1
Top student: Kajal with an average of 87.00

Enter your choice (1-5): 2
Subject with best average: Hindi (84.35)

Enter your choice (1-5): 3
Number of students who passed: 20 out of 20

Enter your choice (1-5): 4
Overall class average: 79.70

Enter your choice (1-5): 5
Exiting...
```

---

## 8. Final Outcome
The project successfully delivers an end-to-end command-line analytics application. It provides clean data presentation, reliable student lookups, robust calculation logic, and batch-level academic metrics. The project was fully tested, documented, version-controlled with Git, and published to GitHub.

---

## 9. Challenges & Learnings

### Challenges Faced & Solutions:
1. **Hardcoded File Paths:**
   - *Problem:* Using hardcoded absolute Windows paths broke portability on other environments.
   - *Solution:* Resolved dynamically using `os.path.dirname(os.path.abspath(__file__))`.
2. **Brittle Row Indexing (`iloc`):**
   - *Problem:* Using numerical column indices (`iloc[i, 2]`) made code fragile to changes in dataset columns.
   - *Solution:* Replaced with Pandas column names (`student["English"]`, `student["Attendance"]`).
3. **Case Sensitivity in User Input:**
   - *Problem:* Inputting `"aman"` failed to match `"Aman"` in the dataset.
   - *Solution:* Added `.str.strip().str.lower() == name_query.lower()`.
4. **Single-Run Menu Termination:**
   - *Problem:* The original menu exited immediately after one selection.
   - *Solution:* Wrapped menu options in an interactive `while True` loop with an exit condition.

### Key Learnings:
- Gained hands-on experience using Pandas for real-world data processing, filtering, and aggregation.
- Learned the importance of writing portable, clean, and defensively coded Python programs.
- Mastered Git version control workflows, creating remote repositories, and hosting open-source project documentation on GitHub.

---

## 10. GitHub Repository
- **Repository URL:** [https://github.com/anshikapal2512-dora/student-performance-analytics](https://github.com/anshikapal2512-dora/student-performance-analytics)
