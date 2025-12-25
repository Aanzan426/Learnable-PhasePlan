# Advanced Student Progress Tracker with Analytics

##  Overview
You are tasked with building an **Advanced Student Progress Tracker** in Python that not only manages student data but also performs analytics, error handling, and file operations in a robust way.

---

##  Requirements

### 1. Core Syntax & Variables
- Create multiple student records (at least 5) stored in a list of dictionaries.
- Each dictionary contains: `name`, `roll_no`, `marks` (list of integers), `attendance`.

### 2. Data Types
- Use a **set** to track unique subjects across all students.
- Demonstrate type coercion by converting marks to strings for file output.
- Use **tuples** to store immutable data like `(roll_no, name)` pairs.

### 3. Control Flow
- For each student, calculate average marks and print performance category:
  - ≥ 90 → **Outstanding**
  - ≥ 75 → **Excellent**
  - ≥ 50 → **Good**
  - Else → **Needs Improvement**
- Loop through all students and print their subject list.

### 4. Functions
- `calculate_average(marks)` → returns average.
- `attendance_status(days_present, total_days)` → returns **Eligible** if ≥ 75%.
- Recursive function `search_student(records, roll_no)` → searches for student by roll number.

### 5. File Handling
- Create a file `progress.txt`.
- Write all student records into it in a structured format.
- Append updates when new marks are added.
- Read and display file contents with pointer control (`tell()`, `seek()`).
- Prepend a header:  *** Student Progress Tracker v2 ***

### 6. Exception Handling
- Handle `ZeroDivisionError` in attendance calculation.
- Handle `FileNotFoundError` if `progress.txt` is missing.
- Handle `KeyError` if a student record is missing a field.
- Use `try/except/finally` to ensure file closure.

---

##  Extended Features
- Add a **menu-driven interface**:
1. Add Student
2. Update Marks
3. View All Progress
4. Search Student by Roll No
5. Keyword Search in File (search for "Outstanding" or "Needs Improvement")

- Generate a **summary report**:
- Count how many students fall into each performance category.
- Find the student with the highest average marks.
- Find the subject most frequently appearing across all students.

- Save the summary report into a separate file `summary.txt`.

---

##  Deliverables
1. `progress_tracker_v2.py` (main script)
2. `progress.txt` (student records)
3. `summary.txt` (analytics report)
