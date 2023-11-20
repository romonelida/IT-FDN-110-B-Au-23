
# ------------------------------------------------------------------------------------------ #
# Title: Assignment06 - Functions, classes, and using the separation of concerns pattern.
# Desc:
# Change Log: (Who, When, What)
#   Nelly,16/11/2023,Created Script
# ------------------------------------------------------------------------------------------ #

import json
import os

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


# Define Constant
FILE_NAME_JSON: str = "Enrollments.json"


# Define the Data Variables
menu_choice: str = ""
student_data: dict = {}
students: list = []

# Define Classes
class FileProcessor:
    """

     FileProcessor is a class for processing files.

    Provides methods to read, write, and perform other common
    file operations. Designed to handle text and binary file formats
    and provide a user-friendly interface for file manipulation.

    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        import json
        try:
            with open(file_name, "r") as file_obj:
                students = json.load(file_obj)
            # new_student_data = student_data
            # students.append(new_student_data)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return students


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # First, read any existing data from the file
        students = []
        try:
            if os.path.isfile(file_name):
                with open(file_name, "r") as file_obj:
                    students = json.load(file_obj)

            # Next, merge existing data with new data
            # This assumes that existing_data and new_data are both lists
            updated_data = students + student_data

            # Finally, write the merged data back to the file
            with open(file_name, "w") as file_obj:
                json.dump(updated_data, file_obj)
        except Exception as e:
            IO.output_error_messages("An error occurred while writing to the file", e)
        print('Here are all the rows of the data from the file:')
        for data in students:
            print(data)


class IO:
    """
    IO is a class for input and output operations.

    Provides methods to for reading and writing different data streams.
    It's intended to simplify complex I/O operations and
    support various data sources and destinations.

    """


    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        if error:
            print(f"{message}: {str(error)}")
        else:
            print(message)

    @staticmethod
    def output_menu(menu: str):
        print()  # Adding extra space to make it look nicer.
        print(MENU)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice


    @staticmethod
    def output_student_courses(student_data: list):
        print("-" * 50)
        for student in student_data:
            print(student["CourseName"])
            print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            if not student_first_name:
                raise ValueError("First name cannot be empty")  # Raise a custom exception if the input is empty
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            if not student_last_name:
                raise ValueError("Last name cannot be empty")  # Raise a custom exception if the input is empty
            student_course_name = input("What is the course name? ")
            student_data = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": student_course_name}
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        else:
            students.append(student_data)  # Append 'student_data' only if no exception was raised
        return students  # Return the updated 'students' list

# ___________________________________________Main Body__________________________________________________________________


while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)
        continue


    # -------------------------------------Present current data------------------____----------------------------------


    elif menu_choice == "2":
        if 'FirstName' in student_data and student_data['FirstName'] == "":
            print("There is no student data, select option 1 to provide data")
            continue
        else:

            students = FileProcessor.read_data_from_file(file_name=FILE_NAME_JSON, student_data=students)

            # Debugging print statement
            print('Debug - Contents of students:', students)

            print('Here are all the rows of the data from the file:')
            for student_data_2 in students:
                print(student_data_2)



    # ----------------------------------------Save data to file --------------------------------------------------------

    elif menu_choice == "3":
        if 'FirstName' in student_data and student_data['FirstName'] == "":
            print("There is no student data, select option 1 to provide data")
            continue
        else:
            FileProcessor.write_data_to_file(file_name=FILE_NAME_JSON, student_data=students)
        continue


    # --------------------------------------------Stop the loop---------------------------------------------------------

    elif menu_choice == "4":
        break  # Exit the loop when user's input is 4
    else:
        print("Invalid choice please select a valid option (1,2,3,4).")
        continue