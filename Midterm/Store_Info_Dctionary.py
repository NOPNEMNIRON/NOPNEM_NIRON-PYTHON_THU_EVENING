#Store information to dictionary
def store(student_id, name, total, grade):
    student = {
        "ID": student_id,
        "Name": name,
        "Total": total,
        "Grade": grade
    }
    return student
id = input("Enter ID: ")
name = input("Enter Name: ")
total = input("Enter total: ")
grade = input("Enter Grade: ")

result = store(id, name, total, grade)
print(result)