# WU Student Management System
students = {}

# 1. Add student
def add_student():
    sid = input("Enter ID: ")
    if sid in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    attendance = int(input("Enter Attendance (0-10): "))
    quiz = int(input("Enter Quiz (0-15): "))
    assignment = int(input("Enter Assignment (0-25): "))
    midterm = int(input("Enter Midterm (0-20): "))
    final = int(input("Enter Final (0-30): "))

    total = attendance + quiz + assignment + midterm + final

    if total >= 90:
        grade = "A"
    elif total >= 80:
        grade = "B"
    elif total >= 70:
        grade = "C"
    elif total >= 60:
        grade = "D"
    else:
        grade = "F"

    students[sid] = {
        "Name": name,
        "Attendance": attendance,
        "Quiz": quiz,
        "Assignment": assignment,
        "Midterm": midterm,
        "Final": final,
        "Total": total,
        "Grade": grade
    }

    print("Student added successfully!")

# 2. View all students
def view_all():
    print("\n--- All Students Information ---")
    if not students:
        print("No students found.")
    else:
        for sid, info in students.items():
            print(f"ID: {sid}, Info: {info}")

# 3. Search student
def search_student():
    sid = input("Enter ID to Search: ")
    if sid in students:
        print("\n--- Student Found ---")
        print(students[sid])
    else:
        print("Student ID not found!")

# 4. Update student
def update_student():
    sid = input("Enter ID to Update: ")
    if sid in students:
        print("\n--- Update Student Information ---")
        students[sid]["Attendance"] = int(input("Enter Attendance (0-10): "))
        students[sid]["Quiz"] = int(input("Enter Quiz (0-15): "))
        students[sid]["Assignment"] = int(input("Enter Assignment (0-25): "))
        students[sid]["Midterm"] = int(input("Enter Midterm (0-20): "))
        students[sid]["Final"] = int(input("Enter Final (0-30): "))

        total = (
            students[sid]["Attendance"] +
            students[sid]["Quiz"] +
            students[sid]["Assignment"] +
            students[sid]["Midterm"] +
            students[sid]["Final"]
        )

        students[sid]["Total"] = total

        if total >= 90:
            students[sid]["Grade"] = "A"
        elif total >= 80:
            students[sid]["Grade"] = "B"
        elif total >= 70:
            students[sid]["Grade"] = "C"
        elif total >= 60:
            students[sid]["Grade"] = "D"
        else:
            students[sid]["Grade"] = "F"

        print("Update Successful!")
    else:
        print("Student ID not found!")

# 5. Delete student
def delete_student():
    sid = input("Enter ID to Delete: ")
    if sid in students:
        del students[sid]
        print("Student deleted successfully.")
    else:
        print("Student ID not found!")


while True:
    print("\n========= WU STUDENT MANAGEMENT MENU =========")
    print("1. Add Student Information")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student by ID")
    print("5. Delete Student by ID")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exit Program. Goodbye!")
        break
    else:
        print("Invalid option! Please choose 1-6.")