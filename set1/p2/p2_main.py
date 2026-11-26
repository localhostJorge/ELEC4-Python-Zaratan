
# Name: RJ JOSHUA C. ZARATAN
# Section: IV-BSIT B
# Activity: P2 - Custom Module: student_utils
# Date: November 23, 2026

# Import a built-in module
import datetime

# Import the custom module
import student_utils

# Import specific functions from the custom module
from student_utils import calculate_average, determine_status


# Main program
def main():
    grades = []

    print("====== STUDENT GRADE REPORT ======")

    while True:
        try:
            total = int(input("How many grades do you want to enter? "))

            if total <= 0:
                print("Please enter at least one grade.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Accept student grades
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

    # Use the imported functions
    average = calculate_average(grades)
    status = determine_status(grades)

    # Use the module import style
    highest = student_utils.get_highest_grade(grades)
    lowest = student_utils.get_lowest_grade(grades)

    # Get the current date and time
    report_date = datetime.datetime.now()

    # Display results
    print("\n========== GRADE RESULTS ==========")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest Grade: {highest:.2f}")
    print(f"Lowest Grade: {lowest:.2f}")
    print(f"Status: {status}")
    print(f"Report Generated: {report_date}")
    print("===================================")


# Run the main program
if __name__ == "__main__":
    main()
