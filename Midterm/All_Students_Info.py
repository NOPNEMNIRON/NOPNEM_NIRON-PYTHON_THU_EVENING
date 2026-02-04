#All students information
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
    },
    "Ricky420": {
            "Name": "Ricky",
            "Attendence": 10,
            "Quiz": 20,
            "Assignment": 20,
            "Midterm": 20,
            "Final": 28,
            "Total": 98,
            "Grade": "A"
        }
}
def view_all():
    print("\n====== All Students Information ======")
    if not students:
        print("No students found.")
    else:
        for id, info in students.items():
            print(f"ID: {id}, Info: {info}")
view_all()