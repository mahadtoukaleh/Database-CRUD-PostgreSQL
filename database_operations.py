import psycopg2

# Database connection parameters
conn_params = {
    "host": "localhost",
    "database": "Students",
    "user": "postgres",
    "password": "postgres"
}

def getAllStudents():
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    for student in students:
        print(student)
    cur.close()
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))
    conn.commit()
    cur.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id))
    conn.commit()
    cur.close()
    conn.close()

def deleteStudent(student_id):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cur.close()
    conn.close()

def resetAndRepopulateTable():
    """removes everything and resets to original"""
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE students RESTART IDENTITY;")
    cur.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
    """)
    conn.commit()
    cur.close()
    conn.close()

# Main
if __name__ == "__main__":
    resetAndRepopulateTable()
    getAllStudents()
