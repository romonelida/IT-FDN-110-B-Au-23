
# ------------------------------------------------------------------------------------------ #
# Title: Assignment05 - Advanced Collections and Error Handling.
# Desc:
# Change Log: (Who, When, What)
#   Nelly,05/11/2023,Created Script
# ------------------------------------------------------------------------------------------ #


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
'''

# Define the Data Variables
FILE_NAME_JSON = "Enrollments.json"
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
menu_choice: str = ""
student_data: dict = {}
students: list = []

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)

    # -------------------------------------Input user data-----------------------------------------------------------

    # Handling errors with exception for keyboard interruptions for menu_choice

    try:
        menu_choice = input("Enter your choice (1,2,3,4): ")
    except KeyboardInterrupt:
        menu_choice = "default_choice"

    if menu_choice == "1":

        # Handling errors with exceptions for first name and last name

        try:

            student_data = {}

            # Input and Validation for "FirstName"

            student_data['FirstName'] = input("Enter the student's first name: ")
            if not student_data['FirstName']:
                raise ValueError("First name cannot be empty")  # Raise a custom exception if the input is empty
            if not student_data['FirstName'].isalpha():
                raise ValueError("First name must be alphabetic")  # Raise a custom exception if input is not alphabetic

            # Input and Validation for "LastName"

            student_data['LastName'] = input("Enter the student's last name: ")
            if not student_data['LastName']:
                raise ValueError("Last name cannot be empty")  # Raise a custom exception if the input is empty
            if not student_data['LastName'].isalpha():
                raise ValueError("Last name must be alphabetic")  # Raise a custom exception if input is not alphabetic

            # Input for "CourseName"

            student_data['CourseName'] = input("Enter the course name: ")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        students.append(student_data)  # Append the new student data to the list
        continue

    # -------------------------------------Present current data---------------------------------------------------------

    elif menu_choice == "2":
        if 'FirstName' in student_data and student_data['FirstName'] == "":
            print("There is no student data, select option 1 to provide data")
            continue
        else:
            students = []  # Initialize an empty list to store student data

            # Handling errors with exceptions when the JSON file is read into the list of dictionary rows

            try:
                import json
                with open(FILE_NAME_JSON, "r") as file_obj:
                    students = json.load(file_obj)
            except FileNotFoundError:
                print("The file 'enrollments.json' was not found.")
            except Exception as e:
                print(f'An error occurred: {str(e)}')
            print('Here are all the rows of the data from the file:')
            for student_data_2 in students:
                print(student_data_2)

    # ------------------------------------Save data to file ---------------------------------------------------------

    elif menu_choice == "3":
        if 'FirstName' in student_data and student_data['FirstName'] == "":
            print("There is no student data, select option 1 to provide data")
            continue
        else:
            students = []  # Initialize an empty list to store student data
            import json
            with open(FILE_NAME_JSON, "r") as file_obj:
                students = json.load(file_obj)
            new_student_data = student_data
            students.append(new_student_data)

            # Handling errors with exceptions when the dictionary rows are written to the JSON file

            try:
                with open(FILE_NAME_JSON, "w") as file_obj:
                    json.dump(students, file_obj)
                file_obj.close()
            except FileNotFoundError:
                print("The file 'enrollments.json' was not found.")
            except Exception as e:
                print(f'An error occurred: {str(e)}')
            print('Here are all the rows of the data from the file:')
            for student_data in students:
                print(student_data)

    # ------------------------------------------Stop the loop-----------------------------------------------------------

    elif menu_choice == "4":
        break  # Exit the loop when user's input is 4
    else:
        print("Invalid choice please select a valid option (1,2,3,4).")
        continue
