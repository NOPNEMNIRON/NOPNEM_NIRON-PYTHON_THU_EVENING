#Delete students information
students={
    "Ronn420": {
        "Attendence": 8,
        "Quiz": 12,
        "Assignment": 23,
        "Midterm": 18,
        "Total": 28,
        "Final": 89,
        "Grade": "B"
    }
}
def delete(student_id):
    if student_id in students:
        del students[student_id]
        print(" Student deleted successfully. ")
    else:
        print("Student ID not found!")
id=input("Enter ID to Delete: ")
delete(id)