students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully")

def view_students():
    if not students:
        print("No students found")
    else:
        for s in students:
            print(s)

def search_student():
    roll = input("Enter roll number: ")
    for s in students:
        if s["roll"] == roll:
            print("Student found:", s)
            return
    print("Student not found")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted")
            return
    print("Student not found")