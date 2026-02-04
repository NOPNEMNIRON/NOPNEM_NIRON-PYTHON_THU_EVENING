#Update Students Information
students=[]
students={
    "Ronn420": {
        "Name": "Ronn",
        "Attendence": 8,
        "Quiz": 12,
        "Assignment": 23,
        "Midterm": 18,
        "Final": 28
    }
}
def update(student_id):
    if student_id in students:
        print("\n====== Update Student Information ======")

        students[student_id]["Name"] = input("Enter Name: ")
        students[student_id]["Attendance"] = int(input("Enter Attendance (0-10): "))
        students[student_id]["Quiz"] = int(input("Enter Quiz (0-15): "))
        students[student_id]["Assignment"] = int(input("Enter Assignment (0-25): "))
        students[student_id]["Midterm"] = int(input("Enter Midterm (0-20): "))
        students[student_id]["Final"] = int(input("Enter Final exam (0-30): "))

        print("\n====== Update Successful! ======")
    else:
        print("Student ID not found!")
id=input("Enter ID to Update: ")
update(id)
print(students)