# Employee Management System (Terminal Version)

employees = []


def show_menu():
    print("\nEmployee Management System")
    print("1. Add New Employee")
    print("2. View All Employees")
    print("3. Search Employee by Name")
    print("4. Exit")


def add_employee():
    emp_id = input("Enter ID: ")
    name = input("Enter name: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    employees.append({
        "id": emp_id,
        "name": name,
        "salary": salary,
        "department": department
    })

    print("Successfully Added!")


def view_all_employees():
    print("\nID | Name | Salary | Department")
    print("--------------------------------")

    for emp in employees:
        print(f"{emp['id']} | {emp['name']} | {emp['salary']:.2f} | {emp['department']}")


def search_employee():
    search_name = input("Enter name to search: ")

    print("\nSearch Results:")
    print("ID | Name | Salary | Department")
    print("--------------------------------")

    found = False
    for emp in employees:
        if emp["name"].lower() == search_name.lower():
            print(f"{emp['id']} | {emp['name']} | {emp['salary']:.2f} | {emp['department']}")
            found = True

    if not found:
        print("No employee found.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Bye!!!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
