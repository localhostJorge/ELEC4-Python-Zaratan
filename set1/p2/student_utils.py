
# Name: RJ JOSHUA C. ZARATAN
# Section: IV-BSIT B
# Activity: P2 - Custom Module: student_utils
# Date: November 26, 2026

# Function 1: Calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function 2: Determine pass or fail
def determine_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function 3: Get highest grade
def get_highest_grade(grades):
    return max(grades)


# Function 4: Get lowest grade
def get_lowest_grade(grades):
    return min(grades)
