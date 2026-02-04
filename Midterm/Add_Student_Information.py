# list to store students
students = []

def add_student():
    print("\n====== Add Student Information ======")

    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    attendance = int(input("Enter Attendance (0-10): "))
    quiz = int(input("Enter Quiz (0-15): "))
    assignment = int(input("Enter Assignment (0-25): "))
    midterm = int(input("Enter Midterm (0-20): "))
    final_exam = int(input("Enter Final exam (0-30): "))

    student = {
        "ID": student_id,
        "Name": name,
        "Attendance": attendance,
        "Quiz": quiz,
        "Assignment": assignment,
        "Midterm": midterm,
        "Final": final_exam
    }

    students.append(student)
    print("\nStudent added successfully!")
add_student()