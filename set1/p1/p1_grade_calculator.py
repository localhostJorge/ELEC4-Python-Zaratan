
# Name: RJ JOSHUA C. ZARATAN
# Section: IV-BSIT B
# Activity: P1 - Student Grade Calculator
# Date: November 23, 2026

# Global variable
passing_grade = 75


# Function 1: Accept the grades of student 
def accept_grades():
    grades = []

    while True:
        try:
            total = int(input("How many grades do you want to enter? "))

            if total <= 0:
                print("Please enter at least one grade.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(total):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


# Function 2: Calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function 3: Get highest grade
def get_highest_grade(grades):
    return max(grades)


# Function 4: Get lowest grade
def get_lowest_grade(grades):
    return min(grades)


# Function 5: Determine pass or fail
def determine_status(grades, passing=passing_grade):
    average = calculate_average(grades)

    if average >= passing:
        return "PASSED"
    else:
        return "FAILED"


# Function 6: Display results
def display_results(grades):
    if not grades:
        print("\nNo grades available. Please enter grades first.")
        return

    average = calculate_average(grades)
    highest = get_highest_grade(grades)
    lowest = get_lowest_grade(grades)
    status = determine_status(grades)

    print("\n========== GRADE RESULTS ==========")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest Grade: {highest:.2f}")
    print(f"Lowest Grade: {lowest:.2f}")
    print(f"Status: {status}")
    print("===================================")


# Main program
def main():
    student_grades = []

    while True:
        print("\n====== STUDENT GRADE CALCULATOR ======")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_grades = accept_grades()
            print("\nGrades successfully recorded!")

        elif choice == "2":
            display_results(student_grades)

        elif choice == "3":
            print("\nThank you for using the Student Grade Calculator!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


# Run the main program
if __name__ == "__main__":
    main()


# Explanation:
# A local variable is a variable declared inside a function and can only be
# accessed within that function. For example, student_grades is created inside
# the main() function, so it is local to main(). A global variable is declared
# outside all functions and can be accessed by different functions. In this
# program, passing_grade is a global variable used as the default passing grade
# in the determine_status() function.
