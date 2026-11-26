
# Name: RJ JOSHUA C. ZARATAN
# Section: IV-BSIT B
# Activity: P4 - Exception Handling: Safe Menu Program
# Date: November 23, 2026


# Function 1: Divide two numbers
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input. Please enter numbers only.")

    except ZeroDivisionError:
        print("Error: Cannot divide a number by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")


# Function 2: Open and read a file
def open_file():
    try:
        filename = input("Enter the filename: ").strip()

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File not found.")

    else:
        print("\n====== FILE CONTENTS ======")
        print(content)
        print("===========================")

    finally:
        print("File operation finished.")


# Main program
def main():
    while True:
        print("\n====== SAFE MENU PROGRAM ======")
        print("1. Divide Two Numbers")
        print("2. Open a File")
        print("3. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# Run the main program
if __name__ == "__main__":
    main()
