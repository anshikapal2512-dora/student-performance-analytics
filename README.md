# Student Performance Analytics System

A comprehensive Python-based data analytics system designed to analyze student academic performance and attendance data using **Pandas** and **NumPy**.

---

## 📌 Project Overview

The **Student Performance Analytics System** enables educators and administrators to quickly inspect, evaluate, and extract insights from student academic records. The system computes overall grades, assesses pass/fail standing, provides personalized report cards, and offers an interactive question-and-answer analytics menu for class-wide performance metrics.

---

## 📁 Project Structure

```text
├── main.py              # Main Python script for data processing and analysis
├── students1.csv        # Dataset containing student academic records and attendance
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

---

## 📊 Dataset Description (`students1.csv`)

The dataset contains records for 20 students with the following columns:

| Column | Description | Data Type |
|---|---|---|
| `Student_ID` | Unique identifier for each student (Index) | Integer |
| `Name` | Name of the student | String |
| `Department` | Academic department (e.g., Computer Engineering) | String |
| `English` | Marks obtained in English (out of 100) | Integer |
| `Hindi` | Marks obtained in Hindi (out of 100) | Integer |
| `Maths` | Marks obtained in Mathematics (out of 100) | Integer |
| `Attendance` | Overall attendance percentage | Float |

---

## 🚀 Key Features

1. **Dataset Summary**: Displays the entire dataset and total count of enrolled students.
2. **Individual Student Report Card**:
   - Case-insensitive search by student name.
   - Computes Total Marks, Average Marks, Percentage, Grade, and Pass/Fail status.
   - Displays department and attendance records.
3. **Interactive Analytical Insights**:
   - **Highest Scorer**: Identifies the student with the highest average marks across all subjects.
   - **Best Performing Subject**: Identifies the subject having the highest class average.
   - **Pass Count**: Calculates how many students achieved passing criteria (average $\ge$ 35).
   - **Class Average**: Calculates the overall grade average of the entire batch.
   - **Looping Menu**: Allows users to run multiple analytical queries before exiting.

---

## 🎯 Grading Scale

| Average Marks Range | Grade | Status |
|---|---|---|
| 90% – 100% | **A** | Pass |
| 75% – 89.9% | **B** | Pass |
| 60% – 74.9% | **C** | Pass |
| 35% – 59.9% | **D** | Pass |
| Below 35% | **F** | Fail |

---

## 🛠️ Prerequisites & Installation

### Requirements
- Python 3.8 or higher
- `pandas`
- `numpy`

### Installation Steps

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install pandas numpy
   ```

---

## 💻 How to Run

Execute the main script via terminal or command prompt:

```bash
python main.py
```

### Sample Workflow

1. The program prints the dataset summary and total student count.
2. Enter a student's name (e.g., `Aman`) to view their full report card.
3. Choose options `1` through `4` from the analytics menu to inspect batch statistics, or press `5` to exit.

---

## 👤 Author
- **Course**: Python Internship / EWB Courses
