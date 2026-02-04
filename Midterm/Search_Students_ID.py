#Search Students ID
students={
    "Ronn420": {
        "Name": "Ronn",
        "Attendence": 8,
        "Quiz": 12,
        "Assignment": 23,
        "Midterm": 18,
        "Final": 28,
        "Total": 89,
        "Grade": "B"
    }
}
def search(student_id):
    if student_id in students:
        print("\n====== Student Found ======")
        print(students[student_id])
    else:
        print("\n====== Student not found! ======")

id=input("Enter ID to search: ")
search(id)
