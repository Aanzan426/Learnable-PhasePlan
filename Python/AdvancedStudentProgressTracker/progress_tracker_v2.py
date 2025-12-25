from collections import Counter
import os

# Each dictionary contains: name, roll_no, marks (list of integers), attendance.
data_list = [
    {'name': 'Alpha', 'roll_no': 10, 'marks': [82, 95, 76, 89, 91, 75], 'attendance': 90},
    {'name': 'Bravo', 'roll_no': 11, 'marks': [67, 88, 92, 74, 81, 83], 'attendance': 78},
    {'name': 'Charlie', 'roll_no': 12, 'marks': [90, 85, 77, 93, 88, 67], 'attendance': 95},
    {'name': 'Delta', 'roll_no': 13, 'marks': [72, 80, 85, 91, 69, 95], 'attendance': 82},
    {'name': 'Echo', 'roll_no': 14, 'marks': [88, 92, 79, 84, 90, 78], 'attendance': 97},
    {'name': 'Foxtrot', 'roll_no': 15, 'marks': [65, 70, 89, 78, 83, 84], 'attendance': 75}
]

subjects = {"Math", "Physics", "Chemistry", "English", "Hindi", "Japanese"}

records = ( (10, "Alpha"), (11, "Bravo"), (12, "Charlie"), (13, "Delta"), (14, "Echo"), (15, "Foxtrot") )


def initial(file):
    try:
        with open(file, "w+") as f:
            if f.tell() == 0:
                f.write("*** Student Progress Tracker V2 ***\n")
    except FileNotFoundError:
        print("Error: progress.txt file is missing.")


def mark_performance(file_name):
    try:
        with open(file_name, "a") as b:   
            for dictionary in data_list:
                total = 0
                b.write(f"{dictionary['name']} ;\n")
                b.write("\tSubjects and Marks:\n")

                for m, i in zip(dictionary['marks'], sorted(subjects)):  # sorted for stable order
                    if m >= 90:
                        b.write(f"\t{i} ({m}) : OUTSTANDING score\n")
                    elif m >= 75:
                        b.write(f"\t{i} ({m}) : EXCELLENT score\n")
                    elif m >= 50:
                        b.write(f"\t{i} ({m}) : GOOD score\n")
                    else:
                        b.write(f"\t{i} ({m}) : Needs improvement\n")
                    total += m

                b.write(f"Average: {calculate_average(total)}\n")
                b.write(f"Attendance: {attendance_status(dictionary['attendance'])}\n\n")

    except KeyError as e:
        print(f"Error: Missing field in student record → {e}")
    finally:
        print("File handling complete (file closed if it was opened).")
    

def calculate_average(total_marks):
    avg = total_marks / len(subjects)
    return(f"Total -> {total_marks} marks : 600, Average -> {avg} marks")    


def attendance_status(attendance):
    try:
        if attendance >= 75:
            return(f"Present Days: {attendance}, Total Days: 100 => ELLIGIBLE")
        else:
            return("NOT ELLIGIBLE.")
    except ZeroDivisionError:
        print("Error: Attendance or marks list is empty, cannot divide by zero.")


def search_student(records, search, index=0):
    if index >= len(records):
        return "Student Not Found."
    if records[index][0] == search:
        return f"Found! Student Name: {records[index][1]}"

    return search_student(records, search, index + 1)


def mirror_update(file, mirror_file = "progress_mirror.txt"):
    try:
        with open(mirror_file, "w+") as b:
            b.write("*** Student Progress Tracker V2 ***\n")
            for dictionary in data_list:
                total = 0
                b.write(f"{dictionary['name']} ;\n")
                b.write("\tSubjects and Marks:\n")

                for m, i in zip(dictionary['marks'], sorted(subjects)):  
                    if m >= 90:
                        b.write(f"\t{i} ({m}) : OUTSTANDING score\n")
                    elif m >= 75:
                        b.write(f"\t{i} ({m}) : EXCELLENT score\n")
                    elif m >= 50:
                        b.write(f"\t{i} ({m}) : GOOD score\n")
                    else:
                        b.write(f"\t{i} ({m}) : Needs improvement\n")
                    total += m

                b.write(f"Average: {calculate_average(total)}\n")
                b.write(f"Attendance: {attendance_status(dictionary['attendance'])}\n\n")
        os.replace(mirror_file, file)
        
    except FileNotFoundError:
        print("Error: progress.txt file is missing.") 
        
        
# Generate Summary Report
def generate_summary(data_list, subjects):
    categories = {"Outstanding": 0, "Excellent": 0, "Good": 0, "Needs Improvement": 0}
    highest_avg = -1
    top_student = None

    for student in data_list:
        try:
            avg = sum(student["marks"]) / len(student["marks"])
            if avg >= 90:
                categories["Outstanding"] += 1
            elif avg >= 75:
                categories["Excellent"] += 1
            elif avg >= 50:
                categories["Good"] += 1
            else:
                categories["Needs Improvement"] += 1

            if avg > highest_avg:
                highest_avg = avg
                top_student = student["name"]

        except KeyError as e:
            print(f"Missing field in student record: {e}")

    report = []
    report.append("=== Summary Report ===")
    report.append("Performance Categories:")
    for shaw, hobbs in categories.items():
        report.append(f"  {shaw}: {hobbs} students")
        
    #.2f is essentially f -> float, 2 -> 2 num after decimal, you stop
    report.append(f"\nTop Student: {top_student} with average {highest_avg:.2f}") 
    
    try:
        with open("summary.txt", "w") as f:
            # .join() is used because f.write() needs string but not list, .join() creates list into a one big string, with "\n" to put breaks
            f.write("\n".join(report))
            
    finally:
        print("Summary report saved to summary.txt")


# MAIN LOOP
def main():
    global records
    initial("progress.txt")
    while True:
        with open("progress.txt", "r+") as k:
            print("""Menu:
              1. Add Student 
              2. Update Marks
              3. View All Progress
              4. Search Student by Roll No
              5. Keyword Search in File (search for "Outstanding" or "Needs Improvement")
              6. Generate Summary Report
            """)
            n = int(input("\n Enter Choice => "))
            
            if n == 1:
                name = input("Enter new Student Name => ")
                roll = int(input("Enter New Student Roll_No => "))
                marks = []
                for i in range(6):
                    mark = int(input("Enter marks =>"))
                    marks.append(mark)
                attend = int(input("Enter attendance => "))
                
                records = records + ((roll, name),)
                sorted_records = tuple(sorted(records, key = lambda x: x[0]))
                records = sorted_records
                
                data_list.append({
                    'name': name, 
                    'roll_no': roll, 
                    'marks': marks, 
                    'attendance': attend
                })
                initial("progress.txt")
                mark_performance("progress.txt")
                
            elif n == 2:
                roll = int(input("Enter Roll_No to update marks => "))
                new_marks = []
                for i in range(6):
                    new_mark = int(input("Enter marks =>"))
                    new_marks.append(new_mark)
                for student in data_list:
                    if student['roll_no'] == roll:
                        student['marks'] = new_marks
                mirror_update("progress.txt")
                    
            elif n == 3:
                k.seek(0)
                print(k.read())
                
            elif n == 4:
                roll = int(input("Enter Roll_No to search => "))
                print(search_student(records, roll))
                
            elif n == 5:
                keyword = input("Enter Keyword to search => ")    
                k.seek(0)
                for i, line in enumerate(k, start=1):
                    if keyword in line:
                        print(f"Word found in line {i} : {line.strip()}")
            
            elif n == 6:
                generate_summary(data_list, subjects)
            
            else:
                print("Exiting the program...")
                break



if __name__ == "__main__":
    main()
