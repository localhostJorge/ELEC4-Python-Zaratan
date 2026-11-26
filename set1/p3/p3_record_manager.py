
# Name: RJ JOSHUA C. ZARATAN
# Section: IV-BSIT B
# Activity: P3 - Student Record Manager
# Date: November 26, 2026

# List to store student names
students = []

# Set to prevent duplicate names
student_names = set()


# Function 1: Add a student
def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    # Convert name to lowercase for duplicate checking
    name_check = name.lower()

    if name_check in student_names:
        print("Student already exists!")
    else:
        students.append(name)
        student_names.add(name_check)
        print(name, "has been added successfully!")


# Function 2: Remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    name_found = False

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            student_names.remove(student.lower())
            print(student, "has been removed successfully!")
            name_found = True
            break

    if not name_found:
        print("Student not found.")


# Function 3: Search for a student
def search_student():
    name = input("Enter name to search: ").strip().lower()

    name_found = False

    for student in students:
        if name in student.lower():
            print("Student found:", student)
            name_found = True

    if not name_found:
        print("No matching student found.")


# Function 4: Display all students
def display_students():
    if len(students) == 0:
        print("No students recorded.")
        return

    print("\n====== STUDENT LIST ======")

    sorted_students = sorted(students)

    for i in range(len(sorted_students)):
        print(str(i + 1) + ".", sorted_students[i])

    print("--------------------------")
    print("Total Students:", len(students))


# Main program
def main():
    while True:
        print("\n====== STUDENT RECORD MANAGER ======")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


# Run the main program
if __name__ == "__main__":
    main()


# Explanation:
# A list can store multiple values and allows items to be added or removed.
# In this program, the students list stores all student names.
# A set stores unique values and automatically prevents duplicate entries.
# I used the student_names set to check if a student name already exists.
# Both are useful for managing student records in this program.
