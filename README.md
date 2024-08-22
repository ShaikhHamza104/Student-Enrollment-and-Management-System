# Student-Enrollment-and-Management-System
MongoDB with Python 

## Overview

The **Student Enrollment and Management System** is a Python-based application designed to manage student data efficiently using MongoDB. This system allows users to add, delete, find, update, and view student records within a MongoDB database. The application includes features for validating input, ensuring data integrity, and providing a user-friendly interface for managing student information.

## Features

- **Add Student:** Add new student records with validation for ID, name, age, gender, department, and course.
- **Delete Student:** Remove student records by ID or name.
- **Find Student:** Search for students by ID or name, and check the availability of departments and courses.
- **Update Student:** Update student details such as ID, name, course, and department.
- **Print All Student Details:** Display all student records in the database.

## Requirements

- **Python 3.x**
- **pymongo:** For MongoDB interactions
- **MongoDB:** A local instance of MongoDB running on port 27017

## Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/ShaikhHamza104/Student-Enrollment-and-Management-System.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Student-Enrollment-and-Management-System
   ```

3. **Install the required Python packages:**
   ```bash
   pip install pymongo
   ```

4. **Ensure MongoDB is running locally:**  
   ```bash
   mongod
   ```

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Interact with the menu:** 
   - **1:** Add a student
   - **2:** Delete a student
   - **3:** Find a student
   - **4:** Update student information
   - **5:** Print all student details
   - **0:** Exit the program

## Code Overview

- **Error Class:** A custom error class to handle validation errors.
- **StudentManagementSystem Class:** Contains methods for managing student records.
  - **`gender_validate(gender)`**: Validates gender input.
  - **`validate_age(age)`**: Validates age input.
  - **`validate_name(name)`**: Validates student name.
  - **`add_student()`**: Adds a new student to the database.
  - **`delete_student()`**: Deletes a student from the database.
  - **`find_student()`**: Finds student details based on various criteria.
  - **`update_student()`**: Updates student details.
  - **`print_all_student_details()`**: Prints all student records.
  - **`main()`**: Provides the main menu for user interaction.

## Contributing

Feel free to contribute to this project by forking the repository and submitting a pull request. If you have any suggestions or find bugs, please create an issue on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```