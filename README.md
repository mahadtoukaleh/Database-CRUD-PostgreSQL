# Database-CRUD-PostgreSQL

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

2. **Create the `students` Table**: Log into your PostgreSQL client and execute the following SQL commands to create the required table and insert the initial data:

    ```sql
    CREATE TABLE students (
      student_id SERIAL PRIMARY KEY,
      first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      enrollment_date DATE
    );

    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
    ```

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
    ```bash
    python script_name.py
    ```
