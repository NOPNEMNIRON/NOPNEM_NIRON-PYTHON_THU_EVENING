#Find Grade
print("\n====== Find Grade ======")
def grade(total):
    if total>=90:
        return "A"
    elif total>= 80:
        return "B"
    elif total>=70:
        return "C"
    elif total>=60:
        return "D"
    elif total>=50:
        return "E"
    else: 
        return "F"
total=int(input("Enter total score: "))
print("Grade: ", grade(total))