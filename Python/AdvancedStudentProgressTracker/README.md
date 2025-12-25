# Advanced Student Progress Tracker v2

## Overview
The **Advanced Student Progress Tracker v2** is a Python program designed to manage student records and perform analytics.
It supports robust file handling, error management, and generates performance summaries for students based on marks and attendance.

---

## Features
- **Student Records Management**
  - Add new students with marks and attendance.
  - Update existing student marks.
  - Search students by roll number (recursive search).
  - Keyword search in progress file (e.g., "Outstanding", "Needs Improvement").

- **Analytics**
  - Calculates average marks per student.
  - Categorizes performance:
    - ≥ 90 → Outstanding
    - ≥ 75 → Excellent
    - ≥ 50 → Good
    - Else → Needs Improvement
  - Generates a summary report:
    - Count of students in each category.
    - Top student with highest average.

- **File Handling**
  - Maintains `progress.txt` with student records.
  - Safe updates using **mirror file** (`progress_mirror.txt`) for atomic replacement.
  - Generates `summary.txt` with analytics report.
  - Demonstrates pointer control (`seek()`, `tell()`).

- **Error Handling**
  - Handles `ZeroDivisionError`, `FileNotFoundError`, and `KeyError`.
  - Ensures files are closed properly with `finally`.

---

## Project Structure
    - progress_tracker_v2.py   # Main script
    - progress.txt              # Student records file
    - summary.txt               # Analytics report
---

## Usage
1. Run the script:
   ```bash
   python progress_tracker_v2.py

2. Use the menu options:
    1. Add Student
    2. Update Marks
    3. View All Progress
    4. Search Student by Roll No
    5. Keyword Search in File
    6. Generate Summary Report

3. Files will be updated automatically:
    - progress.txt → student records with subjects, marks, performance, and attendance.
    - summary.txt → summary analytics report.

---

## Example Output:
    - progress.txt
        Alpha ;
            Math (82) : GOOD score
            Physics (95) : OUTSTANDING score
            Chemistry (76) : EXCELLENT score
            English (89) : EXCELLENT score
            Hindi (91) : OUTSTANDING score
            Japanese (75) : EXCELLENT score
        Average: Total -> 508 marks : 600, Average -> 84.67 marks
        Attendance: Present Days: 90, Total Days: 100 => ELIGIBLE

    - summary.txt
        === Summary Report ===
        Performance Categories:
            Outstanding: 1 students
            Excellent: 4 students
            Good: 1 students
            Needs Improvement: 0 students

        Top Student: Echo with average 88.50

---

## Developed by Deepaansh Deepak Sial
## Advanced Student Progress Tracker project (2025)

