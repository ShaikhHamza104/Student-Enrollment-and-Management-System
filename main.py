import re
import pymongo

class Error(Exception):
    """Custom error class to handle validation errors."""
    
    def __init__(self, msg):
        self.ErrorMsg = msg
    
    def __str__(self):
        return self.ErrorMsg

class StudentManagementSystem:
    """A system to manage student data in a MongoDB database."""
    
    def __init__(self):
        self.departments = ["CO", "AI", "CI", "AR", "AIML"]
        self.courses = ["Computer Engineering", "AI", "Civil Engineering", "Architecture", "AIML"]
    
    def gender_validate(self, gender):
        """
        Validate the gender input.
        
        Args:
            gender (str): Gender of the student.
            
        Raises:
            Error: If the gender is not in the allowed list.
        """
        allowed_genders = ["Male", "Female", "Other"]
        if gender not in allowed_genders:
            raise Error("Invalid gender. Please choose from Male, Female, or Other.")
    
    def validate_age(self, age):
        """
        Validate the age input.
        
        Args:
            age (int): Age of the student.
            
        Raises:
            ValueError: If the age is not a valid integer or not within the allowed range.
        """
        if not isinstance(age, int) or age < 0 or age >= 100:
            raise ValueError("Age is invalid. Please enter a valid age between 0 and 99.")
    
    def validate_name(self, name):
        """
        Validate the student's name.
        
        Args:
            name (str): Name of the student.
            
        Raises:
            Error: If the name contains non-alphabetic characters.
        """
        if not re.match("^[a-zA-Z\s]+$", name):
            raise Error(f"{name} should not contain special characters or numbers.")
    
    def add_student(self):
        """Add a new student to the database."""
        college_name = "Anjuman-I-Islam's A. R. Kalsekar Polytechnic"
        try:
            while True:
                _id = int(input("Enter your ID: "))
                name = input("Enter the student's name: ").title()
                self.validate_name(name)
                age = int(input("Enter the student's age: "))
                self.validate_age(age)
                gender = input("Enter the student's gender: ").capitalize()
                self.gender_validate(gender)
                department = input("Enter the student's department: ").upper()
                if department not in self.departments:
                    print(f"{department} is not available in {college_name}")
                    continue
                course = input("Enter the student's course: ").title()
                
                student_data = {
                    '_id': _id,
                    'college_name': college_name,
                    'name': name,
                    'age': age,
                    'gender': gender,
                    'department': department,
                    'course': course,
                }
                collection.insert_one(student_data)
                print(f"Student {name} enrolled in {course}.")
                
                continue_choice = input("Do you want to add another student? (yes/no): ").lower()
                if continue_choice != 'yes':
                    break

        except Error as e:
            print(e)
        except ValueError:
            print("Invalid input. Please check your entries.")
            
    def delete_student(self):
        """Delete a student from the database based on the specified criteria."""
        try:
            choice = int(input('''
1. Delete student by ID
2. Delete student by name
'''))

            if choice == 1:
                student_id = int(input("Enter the student ID: "))
                student = collection.find_one({"_id": student_id})
                if student:
                    collection.delete_one({"_id": student_id})
                    print(f"Student with ID {student_id} was deleted successfully.")
                else:
                    print(f"The ID {student_id} is not in the database.")
            elif choice == 2:
                name = input("Enter the student's name: ").title()
                self.validate_name(name)
                student = collection.find_one({"name": name})
                if student:
                    collection.delete_one({"name": name})
                    print(f"Student named '{name}' was deleted successfully.")
                else:
                    print(f"The name '{name}' is not in the database.")
            else:
                raise ValueError("Invalid choice. Please choose 1 or 2.")
                
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def find_student(self):
        """Find student details based on various criteria."""
        try:
            choice = int(input('''
1. Find student by ID
2. Find student by name
3. Find department availability
4. Find course availability
5. Find course by ID
6. Find course by name
'''))

            if choice == 1:
                _id = int(input("Enter student ID: "))
                student = collection.find_one({"_id": _id}, {'_id': 0})
                if student:
                    print(f"Student found: {student}")
                else:
                    print(f"Student with ID {_id} is not in the database.")
            elif choice == 2:
                name = input("Enter the student's name: ").title()
                student = collection.find_one({"name": name})
                if student:
                    print(f"Student found: {student}")
                else:
                    print(f"Student named {name} is not in the database.")
            elif choice == 3:
                department = input("Enter department name: ").upper()
                department_exists = collection.find_one({"department": department})
                if department_exists:
                    print(f"Department {department} is available in the college.")
                else:
                    print(f"Department {department} is not available in the college.")
            elif choice == 4:
                course = input("Enter course name: ").title()
                course_exists = collection.find_one({"course": course})
                if course_exists:
                    print(f"Course {course} is available in the college.")
                else:
                    print(f"Course {course} is not available in the college.")
            elif choice == 5:
                _id = int(input("Enter student ID: "))
                student = collection.find_one({"_id": _id}, {'course': 1})
                if student:
                    print(f"Student's course: {student['course']}")
                else:
                    print(f"Student with ID {_id} is not in the database.")
            elif choice == 6:
                name = input("Enter the student's name: ").title()
                student = collection.find_one({"name": name}, {'course': 1})
                if student:
                    print(f"Student's course: {student['course']}")
                else:
                    print(f"Student named {name} is not in the database.")
            else:
                raise ValueError("Invalid choice. Please choose a valid option.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        
    def update_student(self):
        """Update student details based on user input."""
        try:
            choice = int(input('''
1. Update student ID
2. Update student name
3. Update student course
4. Update student department
'''))

            if choice == 1:
                old_id = int(input("Enter the old ID: "))
                new_id = int(input("Enter the new ID: "))
                if collection.find_one({"_id": old_id}):
                    collection.update_one({"_id": old_id}, {"$set": {"_id": new_id}})
                    print(f"ID updated from {old_id} to {new_id}.")
                else:
                    print(f"Student with ID {old_id} is not in the database.")
            elif choice == 2:
                _id = int(input("Enter student ID: "))
                new_name = input("Enter the new name: ").title()
                if collection.find_one({"_id": _id}):
                    collection.update_one({"_id": _id}, {"$set": {"name": new_name}})
                    print(f"Student name updated to {new_name}.")
                else:
                    print(f"Student with ID {_id} is not in the database.")
            elif choice == 3:
                _id = int(input("Enter student ID: "))
                course = input("Enter the new course: ").title()
                if collection.find_one({"_id": _id}):
                    collection.update_one({"_id": _id}, {"$set": {"course": course}})
                    print(f"Course updated to {course}.")
                else:
                    print(f"Student with ID {_id} is not in the database.")
            elif choice == 4:
                _id = int(input("Enter student ID: "))
                department = input("Enter the new department: ").upper()
                if collection.find_one({"_id": _id}):
                    collection.update_one({"_id": _id}, {"$set": {"department": department}})
                    print(f"Department updated to {department}.")
                else:
                    print(f"Student with ID {_id} is not in the database.")
            else:
                raise ValueError("Invalid choice. Please choose a valid option.")
                
        except ValueError as e:
            print(f"Invalid input: {e}")
        
    def print_all_student_details(self):
        """Print the details of all students in the database."""
        for student in collection.find({}):
            print(student)

    def main(self):
        """Main menu to interact with the Student Management System."""
        while True:
            print("1. Add student\n2. Delete student\n3. Find student\n4. Update student\n5. Print all student details\n0. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.delete_student()
            elif choice == 3:
                self.find_student()
            elif choice == 4:
                self.update_student()
            elif choice == 5:
                self.print_all_student_details()
            elif choice == 0:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        
if __name__ == "__main__":
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["student_management_system"]
        collection = db["students"]
        sms = StudentManagementSystem()
        sms.main()
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print("Could not connect to MongoDB: ", err)
