# Database-CRUD-PostgreSQL

## Link To Youtube Video
    https://youtu.be/EbtScCIvKvE
    

## Project Overview
This project aims to demonstrate CRUD (Create, Read, Update, Delete) operations on a PostgreSQL database using a Python application. The application interfaces with a students table within a PostgreSQL database, performing operations such as adding new student records, retrieving all student information, updating student emails, and deleting student records.

## Application Functions
- `getAllStudents()`: Retrieves and displays all records from the students table.
- `addStudent(first_name, last_name, email, enrollment_date)`: Inserts a new student record into the students table.
- `updateStudentEmail(student_id, new_email)`: Updates the email address for a student with the specified student_id.
- `deleteStudent(student_id)`: Deletes the record of the student with the specified student_id.
- `resetAndRepopulateTable()`: Resets the students table and repopulates it with the original data.

## Requirements
- Python 3.x
- PostgreSQL
- psycopg2 Python library

## Setup Instructions
1. **Install PostgreSQL**: Ensure PostgreSQL is installed and running on your system. Create a database named `Students`.

2. **Create the `students` Table** by Downloading the `database_creation.sql` file and executing it in your PostgreSQL environment. 

## Application Setup
1. **Install Dependencies**: Open a terminal in the project directory and run the following command to install the required Python library:
    ```bash
    pip install psycopg2
    ```
2. **Configure Database Connection**: Modify the `conn_params` dictionary in the Python script with your PostgreSQL database connection details:
    ```python
    conn_params = {
      "host": "localhost",
      "database": "Students",
      "user": "postgres",
      "password": "postgres"
    }
    ```

## Running the Application
Navigate to the project directory in your terminal and execute the Python script:
    ```
    python database_operations.py
    ```
